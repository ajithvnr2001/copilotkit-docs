---
url: https://docs.copilotkit.ai/deepagents/shared-state/state-inputs-outputs/
title: Input/Output Schemas
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:01:01.023648+00:00
---

# Input/Output Schemas

> Source: https://docs.copilotkit.ai/deepagents/shared-state/state-inputs-outputs/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendDeep Agents

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/deepagents)[Quickstart](https://docs.copilotkit.ai/deepagents/quickstart)[Build with agents](https://docs.copilotkit.ai/deepagents/build-with-agents)[Intelligence](https://docs.copilotkit.ai/deepagents/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/deepagents/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

[Reading agent state](https://docs.copilotkit.ai/deepagents/shared-state/in-app-agent-read)[Writing agent state](https://docs.copilotkit.ai/deepagents/shared-state/in-app-agent-write)[State streaming](https://docs.copilotkit.ai/deepagents/shared-state/predictive-state-updates)[Input/Output Schemas](https://docs.copilotkit.ai/deepagents/shared-state/state-inputs-outputs)[Workflow Execution](https://docs.copilotkit.ai/deepagents/shared-state/workflow-execution)

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/deepagents/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/deepagents/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/deepagents/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/deepagents/learning)

[User Memories](https://docs.copilotkit.ai/deepagents/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/deepagents/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/deepagents/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/deepagents/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/deepagents/intelligence/analytics)[Channels](https://docs.copilotkit.ai/deepagents/intelligence/channels)

Hosting

Backend

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

[Open-source telemetry](https://docs.copilotkit.ai/deepagents/telemetry)[Community frameworks](https://docs.copilotkit.ai/deepagents/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Input/Output Schemas

InteractivityShared state

# Input/Output Schemas

Decide which state properties are received and returned to the frontend

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

Not all state properties are relevant for frontend-backend sharing. This guide shows how to ensure only the right portion of state is communicated back and forth.

This guide is based on [LangGraph's Input/Output Schema feature](https://docs.langchain.com/oss/python/langgraph/use-graph-api#define-input-and-output-schemas)

This pattern uses **LangGraph's input/output schema split** , which applies when you're building a custom LangGraph graph. `createDeepAgent` uses middleware with a single state schema and doesn't expose separate input/output schemas. The Python example below shows the LangGraph custom-graph approach. For the Deep Agents TypeScript equivalent of "shared state between agent and frontend", see the [shared state guides](https://docs.copilotkit.ai/deepagents/shared-state/in-app-agent-read).

## When should I use this?#

Depending on your implementation, some properties are meant to be processed internally, while some others are the way for the UI to communicate user input. In addition, some state properties contain a lot of information. Syncing them back and forth between the agent and UI can be costly, while it might not have any practical benefit.

## Implementation#

### Examine our old state#

LangGraph is stateful. As you transition between nodes, that state is updated and passed to the next node. For this example, let's assume that the state our agent should be using, can be described like this:

agent.py
    
    
    from copilotkit import CopilotKitState
    
    class AgentState(CopilotKitState):
        question: str
        answer: str
        resources: list[str]

### Divide state to Input and Output#

Our example case lists several state properties, which with its own purpose:

  * The question is being asked by the user, expecting the llm to answer
  * The answer is what the LLM returns
  * The resources list will be used by the LLM to answer the question, and should not be communicated to the user, or set by them.



agent.py
    
    
    from copilotkit import CopilotKitState
    
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
