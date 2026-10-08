---
url: https://docs.copilotkit.ai/langgraph-fastapi/shared-state/state-inputs-outputs/
title: Input/Output Schemas
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:05:55.176527+00:00
---

# Input/Output Schemas

> Source: https://docs.copilotkit.ai/langgraph-fastapi/shared-state/state-inputs-outputs/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (FastAPI)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-fastapi)[Quickstart](https://docs.copilotkit.ai/langgraph-fastapi/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-fastapi/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-fastapi/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/langgraph-fastapi/webmcp)

Agent capabilities

LangGraph (FastAPI)

[Sub-agents](https://docs.copilotkit.ai/langgraph-fastapi/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/langgraph-fastapi/learning)

[User Memories](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/analytics)[Channels](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

Learn

Concepts

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/langgraph-fastapi/telemetry)[Community frameworks](https://docs.copilotkit.ai/langgraph-fastapi/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[LangGraph (FastAPI)](https://docs.copilotkit.ai/langgraph-fastapi)[Shared State](https://docs.copilotkit.ai/langgraph-fastapi/shared-state)

# Input/Output Schemas

Decide which state properties are received and returned to the frontend

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

Not all state properties are relevant for frontend-backend sharing. This guide shows how to ensure only the right portion of state is communicated back and forth.

This guide is based on [LangGraph's Input/Output Schema feature](https://docs.langchain.com/oss/python/langgraph/use-graph-api#define-input-and-output-schemas)

## When should I use this?#

Depending on your implementation, some properties are meant to be processed internally, while some others are the way for the UI to communicate user input. In addition, some state properties contain a lot of information. Syncing them back and forth between the agent and UI can be costly, while it might not have any practical benefit.

## Implementation#

### Examine our old state#

LangGraph is stateful. As you transition between nodes, that state is updated and passed to the next node. For this example, let's assume that the state our agent should be using, can be described like this:

PythonTypeScript

agent.py
    
    
    from copilotkit import CopilotKitState
    from typing import Literal
    
    class AgentState(CopilotKitState):
        question: str
        answer: str
        resources: List[str]

agent-js/sample_agent/agent.ts
    
    
    import { Annotation } from "@langchain/langgraph";
    import { CopilotKitStateAnnotation } from "@copilotkit/sdk-js/langgraph";
    import { z } from "zod";
    
    const AgentStateAnnotation = Annotation.Root({
      ...CopilotKitStateAnnotation.spec,
      question: Annotation<string>,
      answer: Annotation<string>,
      resources: Annotation<string[]>,
    });
    
    export type AgentState = typeof AgentStateAnnotation.State;

### Divide state to Input and Output#

Our example case lists several state properties, which with its own purpose:

  * The question is being asked by the user, expecting the llm to answer
  * The answer is what the LLM returns
  * The resources list will be used by the LLM to answer the question, and should not be communicated to the user, or set by them.



PythonTypeScript

agent.py
    
    
    from langchain_core.runnables import RunnableConfig
    from copilotkit import CopilotKitState
    from typing import Literal
    
    # Divide the state to 3 parts
    
    # Input schema for inputs you are willing to accept from the frontend
    class InputState(CopilotKitState):
      question: str
    
    # Output schema for output you are willing to pass to the frontend
    class OutputState(CopilotKitState):
      answer: str
    
    # The full schema, including the inputs, outputs and internal state ("resources" in our case)
    class OverallState(InputState, OutputState):
      resources: List[str]
    
    async def answer_node(state: OverallState, config: RunnableConfig):
      """
      Standard chat node, meant to answer general questions.
      """
    
      model = ChatOpenAI()
    
      # add the input question in the system prompt so it's passed to the LLM
      system_message = SystemMessage(
        content=f"You are a helpful assistant. Answer the question: {state.get('question')}"
      )
    
      response = await model.ainvoke([
        system_message,
        *state["messages"],
      ], config)
    
      # ...add the rest of the agent implementation
    
      # extract the answer, which will be assigned to the state soon
      answer = response.content
    
      return {
         "messages": response,
          # include the answer in the returned state
         "answer": answer
      }
    
    
    # finally, before compiling the graph, we define the 3 state components
    builder = StateGraph(OverallState, input=InputState, output=OutputState)
    
    # add all the different nodes and edges and compile the graph
    builder.add_node("answer_node", answer_node)
    builder.add_edge(START, "answer_node")
    builder.add_edge("answer_node", END)
    graph = builder.compile()

agent-js/sample_agent/agent.ts
    
    
    import { Annotation, StateGraph, START, END } from "@langchain/langgraph";
    import { CopilotKitStateAnnotation } from "@copilotkit/sdk-js/langgraph";
    import { ChatOpenAI } from "@langchain/openai";
    import { SystemMessage } from "@langchain/core/messages";
    import type { RunnableConfig } from "@langchain/core/runnables";
    
    // Divide the state to 3 parts
    
    // An input annotation for inputs you are willing to accept from the frontend
    const InputAnnotation = Annotation.Root({
      ...CopilotKitStateAnnotation.spec,
      question: Annotation<string>,
    });
    
    // Output annotation for output you are willing to pass to the frontend
    const OutputAnnotation = Annotation.Root({
      ...CopilotKitStateAnnotation.spec,
      answer: Annotation<string>,
    });
    
    // The full annotation, including the inputs, outputs and internal state ("resources" in our case)
    const AgentStateAnnotation = Annotation.Root({
      ...CopilotKitStateAnnotation.spec,
      question: Annotation<string>,
      answer: Annotation<string>,
      resources: Annotation<string[]>,
    });
    
    export type AgentState = typeof AgentStateAnnotation.State;
    
    async function answerNode(state: AgentState, config: RunnableConfig) {
      const model = new ChatOpenAI();
    
      const systemMessage = new SystemMessage({
        content: `You are a helpful assistant. Answer the question: ${state.question}.`,
      });
    
      const response = await model.invoke(
        [systemMessage, ...state.messages],
        config
      );
    
      // ...add the rest of the agent implementation
      // extract the answer, which will be assigned to the state soon
      const answer = typeof response.content === 'string' 
        ? response.content 
        : JSON.stringify(response.content);
    
      return {
        messages: [response],
        // include the answer in the returned state
        answer,
      }
    }
    
    // finally, before compiling the graph, we define the 3 state components
    // StateGraph accepts the full state annotation as the first parameter,
    // with optional input/output annotations to filter what's communicated with the frontend
    const workflow = new StateGraph(AgentStateAnnotation, {
      input: InputAnnotation,
      output: OutputAnnotation,
    })
      .addNode("answer_node", answerNode)
      .addEdge(START, "answer_node")
      .addEdge("answer_node", END);
    
    export const graph = workflow.compile();

### Give it a try!#

Now that we know which state properties our agent emits, we can inspect the state and expect the following to happen:

  * While we are able to provide a question, we will not receive it back from the agent. If we are using it in our UI, we need to remember the UI is the source of truth for it
  * Answer will change once it's returned back from the agent
  * The UI has no access to resources.


    
    
    import { useAgent } from "@copilotkit/react-core/v2"; 
    
    const { agent } = useAgent({
      agentId: "sample_agent",
    });
    
    const answer = agent.state.answer as string;
    
    console.log(answer) // You can expect seeing "answer" change, while the others are not returned from the agent

## Emitting a state key outside the output schema#

The filtering above is driven by the graph's output schema. If you compile the graph with an output schema that is narrower than its state, for example `StateGraph(State, output_schema=Output)`, state keys outside `Output` never reach the frontend.

In Python, list the keys that the frontend needs under `schema_keys` in the agent's `config`. They are emitted alongside the schema-derived ones, and the graph's own output schema does not change:

agent.py
    
    
    from copilotkit import LangGraphAGUIAgent
    
    agent = LangGraphAGUIAgent(
        name="sample_agent",
        graph=graph,
        config={"schema_keys": {"output": ["steps"]}},
    )

This adds to what the output schema already exposes, it does not replace it. If you can add the key to the output schema instead, do that. A malformed `schema_keys` value is logged as a warning and ignored.

### On this page

What is this?When should I use this?ImplementationEmitting a state key outside the output schema
