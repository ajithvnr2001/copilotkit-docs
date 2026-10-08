---
url: https://docs.copilotkit.ai/langgraph-fastapi/advanced/emit-messages/
title: Manually emitting messages
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:04:09.499573+00:00
---

# Manually emitting messages

> Source: https://docs.copilotkit.ai/langgraph-fastapi/advanced/emit-messages/

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

[LangGraph (FastAPI)](https://docs.copilotkit.ai/langgraph-fastapi)Advanced

# Manually emitting messages

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

While most agent interactions happen automatically through shared state updates as the agent runs, you can also **manually send messages from within your agent code** to provide immediate feedback to users.

This video shows the result of `npx copilotkit@latest init` with the implementation section applied to it!

## What is this?#

In LangGraph, messages are only emitted when a node is completed. CopilotKit allows you to manually emit messages in the middle of a node's execution to provide immediate feedback to the user.

## When should I use this?#

Manually emitted messages are great for **when you don't want to wait for the node** to complete **and you** :

  * Have a long running task that you want to provide feedback on
  * Want to provide a status update to the user
  * Want to provide a warning or error message



## Implementation#

### Run and connect your agent#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/langgraph/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point as this guide uses it as a starting point.

### Install the CopilotKit SDK#

Any LangGraph agent can be used with CopilotKit. However, creating deep agentic experiences with CopilotKit requires our LangGraph SDK.

PythonTypeScript

uvpoetrypipconda
    
    
    uv add copilotkit
    
    
    poetry add copilotkit
    
    
    pip install copilotkit --extra-index-url https://copilotkit.gateway.scarf.sh/simple/
    
    
    conda install copilotkit -c copilotkit-channel

`npm npm install @copilotkit/sdk-js `

### Manually emit a message#

The `copilotkit_emit_message` method allows you to emit messages early in a node's execution to communicate status updates to the user. This is particularly useful for long running tasks.

PythonTypeScript
    
    
    from langchain_core.messages import SystemMessage, AIMessage
    from langchain_openai import ChatOpenAI
    from langchain_core.runnables import RunnableConfig
    from copilotkit.langgraph import copilotkit_emit_message 
    # ...
    
    async def chat_node(state: AgentState, config: RunnableConfig):
        model = ChatOpenAI(model="gpt-5.4")
    
        intermediate_message = "Thinking really hard..."
        await copilotkit_emit_message(config, intermediate_message)
    
        # simulate a long running task
        await asyncio.sleep(2)
    
        response = await model.ainvoke([
            SystemMessage(content="You are a helpful assistant."),
            *state["messages"]
        ], config)
    
        return Command(
            goto=END,
            update={
                # Make sure to include the emitted message in the messages history 
                "messages": [AIMessage(content=intermediate_message), response]
            }
        )
    
    
    // ...
    
    async function chat_node(state: AgentState, config: RunnableConfig) {
        const model = new ChatOpenAI({ model: "gpt-5.4" });
    
        const intermediateMessage = "Thinking really hard...";
        await copilotkitEmitMessage(config, intermediateMessage);
    
        // simulate a long-running task
        await new Promise(resolve => setTimeout(resolve, 2000));
    
        const response = await model.invoke([
            new SystemMessage({content: "You are a helpful assistant."}),
            ...state.messages
        ], config);
    
        return {
            // Make sure to include the emitted message in the messages history
            messages: [new AIMessage(intermediateMessage), response],
        };
    }

### Give it a try!#

Now when you talk to your agent you'll notice that it immediately responds with the message "Thinking really hard..." before giving you a response 2 seconds later.

### On this page

What is this?When should I use this?Implementation
