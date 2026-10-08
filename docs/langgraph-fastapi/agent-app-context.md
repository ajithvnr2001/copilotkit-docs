---
url: https://docs.copilotkit.ai/langgraph-fastapi/agent-app-context/
title: Readables
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:04:13.191964+00:00
---

# Readables

> Source: https://docs.copilotkit.ai/langgraph-fastapi/agent-app-context/

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

[Readables](https://docs.copilotkit.ai/langgraph-fastapi/agent-app-context)[Configurable](https://docs.copilotkit.ai/langgraph-fastapi/configurable)[Subgraphs](https://docs.copilotkit.ai/langgraph-fastapi/subgraphs)[Guardrails & DLP](https://docs.copilotkit.ai/langgraph-fastapi/guardrails)[AWS AgentCore](https://docs.copilotkit.ai/langgraph-fastapi/deploy-agentcore)[LangSmith Platform](https://docs.copilotkit.ai/langgraph-fastapi/deploy-langsmith)

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

Agent capabilitiesLangGraph (FastAPI)

# Readables

Share app specific context with your agent.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

One of the most common use cases for CopilotKit is to register app state and context using `useAgentContext`. This way, you can notify CopilotKit of what is going on in your app in real time. Some examples might be: the current user, the current page, etc.

This context can then be shared with your LangGraph agent.

## Implementation#

Check out the [Frontend Data documentation](https://docs.copilotkit.ai/langgraph-python/agent-app-context) to understand what this is and how to use it.

Context values arrive as JSON strings

The AG-UI protocol defines a context value as a string. Therefore `useAgentContext` calls `JSON.stringify` on any `value` that is not already a string, and your agent receives the JSON text instead of the object or the array.

Parse the value before you read a field from it. Use `json.loads(item["value"])` in Python, or `JSON.parse(item.value)` in TypeScript. If you skip the parse step, an index such as `colleagues[0]` returns a single character, and a shape check such as `isinstance(value, list)` can never pass.

Do not stringify the value again, because that produces double encoding. A `value` that is already a string is sent unchanged, so no parse step is needed for it.
