---
url: https://docs.copilotkit.ai/langgraph-fastapi/generative-ui/interactive/
title: Interactive components
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:05:10.983591+00:00
---

# Interactive components

> Source: https://docs.copilotkit.ai/langgraph-fastapi/generative-ui/interactive/

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

[LangGraph (FastAPI)](https://docs.copilotkit.ai/langgraph-fastapi)[Build Generative UI](https://docs.copilotkit.ai/langgraph-fastapi/generative-ui)

# Interactive components

Create approval flows where the agent pauses and waits for human input.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Not supported on LangGraph (FastAPI)

LangGraph (FastAPI) doesn't support Human in the Loop: Interrupts. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.

## What is this?#

Interactive generative UI creates flows where the agent pauses execution and waits for user input before continuing. This enables approval workflows, confirmation dialogs, and any scenario where human judgment is needed mid-execution.

## When should I use this?#

Use interactive generative UI when you need:

  * Approval/rejection flows (e.g. "Run this command?")
  * User decisions that the agent should know about
  * Confirmation dialogs with structured responses
  * Any flow where the agent pauses for human judgment



## How it works in code#

### Install the LangGraph Python SDK

uvpoetrypipconda
    
    
    uv add copilotkit
    
    
    poetry add copilotkit
    
    
    pip install copilotkit --extra-index-url https://copilotkit.gateway.scarf.sh/simple/
    
    
    conda install copilotkit -c copilotkit-channel

### Wire CopilotKit middleware into your graph

For `useHumanInTheLoop` tool-based HITL, the tool is defined entirely on the frontend and forwarded to the agent. `CopilotKitMiddleware` is what forwards it — drop it into your `create_agent` call.

frontend_tools.py
    
    
    from langchain.agents import create_agent
    from langchain_openai import ChatOpenAI
    from copilotkit import CopilotKitMiddleware
    
    graph = create_agent(
        model=ChatOpenAI(model="gpt-5.4"),
        tools=[],
        middleware=[CopilotKitMiddleware()],
        system_prompt="You are a helpful, concise assistant.",
    )

For the `useInterrupt` graph-paused pattern, you'll also use LangGraph's native `interrupt(...)` primitive inside a graph node — no extra CopilotKit setup beyond the middleware above.

On the frontend, register an interrupt renderer with `useInterrupt`. When the agent pauses, your component mounts inline in the chat, captures the user's choice, and resumes the run with that input.

Not supported on LangGraph (FastAPI)

LangGraph (FastAPI) doesn't support Human in the Loop: Interrupts. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.

On the backend, the agent calls into the interrupt primitive and waits for the resumed response before continuing the graph.

Not supported on LangGraph (FastAPI)

LangGraph (FastAPI) doesn't support Human in the Loop: Interrupts. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.
