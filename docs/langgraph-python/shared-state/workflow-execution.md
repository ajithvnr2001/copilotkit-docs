---
url: https://docs.copilotkit.ai/langgraph-python/shared-state/workflow-execution/
title: Workflow Execution
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:08:52.481450+00:00
---

# Workflow Execution

> Source: https://docs.copilotkit.ai/langgraph-python/shared-state/workflow-execution/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-python)[Quickstart](https://docs.copilotkit.ai/langgraph-python/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/langgraph-python/webmcp)

Agent capabilities

LangGraph (Python)

[Sub-agents](https://docs.copilotkit.ai/langgraph-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/langgraph-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/langgraph-python/learning)

[User Memories](https://docs.copilotkit.ai/langgraph-python/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/langgraph-python/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/langgraph-python/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/langgraph-python/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/langgraph-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/langgraph-python/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/langgraph-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/langgraph-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python)[Shared State](https://docs.copilotkit.ai/langgraph-python/shared-state)

# Workflow Execution

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
    
    
    import { StateSchema } from "@langchain/langgraph";
    import { CopilotKitStateSchema } from "@copilotkit/sdk-js/langgraph";
    import { z } from "zod";
    
    const AgentState = new StateSchema({
      ...CopilotKitStateSchema.fields,
      question: z.string(),
      answer: z.string(),
      resources: z.array(z.string()).default(() => []),
    })

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
    
    
    import { StateSchema } from "@langchain/langgraph";
    import { CopilotKitStateSchema } from "@copilotkit/sdk-js/langgraph";
    import { z } from "zod";
    
    // Divide the state to 3 parts
    
    // An input schema for inputs you are willing to accept from the frontend
    const InputSchema = new StateSchema({
      ...CopilotKitStateSchema.fields,
      question: z.string(),
    });
    
    // Output schema for output you are willing to pass to the frontend
    const OutputSchema = new StateSchema({
      ...CopilotKitStateSchema.fields,
      answer: z.string(),
    });
    
    // The full schema, including the inputs, outputs and internal state ("resources" in our case)
    export const AgentStateSchema = new StateSchema({
      ...CopilotKitStateSchema.fields,
      ...OutputSchema.fields,
      ...InputSchema.fields,
      resources: z.array(z.string()).default(() => []),
    });
    
    // Define a typed state that supports the entire
    export type AgentState = typeof AgentStateSchema.State;
    
    async function answerNode(state: AgentState, config: RunnableConfig) {
      const model = new ChatOpenAI()
    
      const systemMessage = new SystemMessage({
        content: `You are a helpful assistant. Answer the question: ${state.question}.`,
      });
    
      const response = await modelWithTools.invoke(
        [systemMessage, ...state.messages],
        config
      );
    
      // ...add the rest of the agent implementation
      // extract the answer, which will be assigned to the state soon
      const answer = response.content
    
      return {
        messages: response,
        // include the answer in the returned state
        answer,
      }
    }
    
    // finally, before compiling the graph, we define the 3 state components
    const workflow = new StateGraph({
      input: InputSchema,
      output: OutputSchema,
      stateSchema: AgentStateSchema,
    })
      .addNode("answer_node", answerNode) // add all the different nodes and edges and compile the graph
      .addEdge(START, "answer_node")
      .addEdge("answer_node", END)
    export const graph = workflow.compile()

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

### On this page

What is this?When should I use this?Implementation
