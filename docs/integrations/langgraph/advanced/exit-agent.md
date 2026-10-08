---
url: https://docs.copilotkit.ai/integrations/langgraph/advanced/exit-agent/
title: Exiting the agent loop
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:37:32.540075+00:00
---

# Exiting the agent loop

> Source: https://docs.copilotkit.ai/integrations/langgraph/advanced/exit-agent/

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

[LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python)Advanced

# Exiting the agent loop

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

After your agent has finished a workflow, you'll usually want to explicitly end that loop by calling the CopilotKit exit method in your agent code.

Exiting the agent has different effects depending on mode:

  * **Router Mode** : Exiting the agent hands responsibility for handling input back to the router, which can initiate chat, call actions, other agents, etc. The router can return to this agent later (starting a new loop) to satisfy a user request.

  * **Agent Lock Mode** : Exiting the agent restarts the workflow loop for the current agent.




In this example from [our email-sending app](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-qa), the `send_email` node explicitly exits, then manually sends a response back to the user as a `ToolMessage`:

### Install the CopilotKit SDK#

Any LangGraph agent can be used with CopilotKit. However, creating deep agentic experiences with CopilotKit requires our LangGraph SDK.

PythonTypeScript

uvpoetrypipconda
    
    
    uv add copilotkit
    
    
    poetry add copilotkit
    
    
    pip install copilotkit --extra-index-url https://copilotkit.gateway.scarf.sh/simple/
    
    
    conda install copilotkit -c copilotkit-channel

`npm npm install @copilotkit/sdk-js `

### Exit the agent loop#

This will exit the agent session as soon as the current LangGraph run is finished, either by a breakpoint or by reaching the `END` node.

PythonTypeScript
    
    
    from langchain_core.runnables import RunnableConfig
    from copilotkit.langgraph import (copilotkit_exit)
    # ...
    async def send_email_node(state: EmailAgentState, config: RunnableConfig):
        """Send an email."""
    
        await copilotkit_exit(config) 
    
        # get the last message and cast to ToolMessage
        last_message = cast(ToolMessage, state["messages"][-1])
        if last_message.content == "CANCEL":
            return {
                "messages": [AIMessage(content="❌ Cancelled sending email.")],
            }
        else:
            return {
                "messages": [AIMessage(content="✅ Sent email.")],
            }
    
    
    // ...
    
    async function sendEmailNode(state: EmailAgentState, config: RunnableConfig): Promise<{ messages: any[] }> {
        // Send an email.
    
        await copilotkitExit(config); 
    
        // get the last message and cast to ToolMessage
        const lastMessage = state.messages[state.messages.length - 1] as ToolMessage;
        if (lastMessage.content === "CANCEL") {
            return {
                messages: [new AIMessage(content="❌ Cancelled sending email.")],
            }
        } else {
            return {
                messages: [new AIMessage(content="✅ Sent email.")],
            }
        }
    }
