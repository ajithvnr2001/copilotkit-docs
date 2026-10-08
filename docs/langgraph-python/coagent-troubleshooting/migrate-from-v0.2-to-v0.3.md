---
url: https://docs.copilotkit.ai/langgraph-python/coagent-troubleshooting/migrate-from-v0.2-to-v0.3
title: Migrate from v0.2 to v0.3
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:07:31.141923+00:00
---

# Migrate from v0.2 to v0.3

> Source: https://docs.copilotkit.ai/langgraph-python/coagent-troubleshooting/migrate-from-v0.2-to-v0.3

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

[LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python)Coagent Troubleshooting

# Migrate from v0.2 to v0.3

How to migrate from v0.2 to v0.3.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What's new in v0.3?#

Starting with `v0.3`, we changed how messages are synced between the agent (LangGraph) and CopilotKit. Essentially, both will now share exactly the same message history.

This means that you need to return the messages you want to appear in CopilotKit chat from your LangGraph nodes, for example:
    
    
    from langchain_core.runnables import RunnableConfig
    
    def my_node(state: State, config: RunnableConfig) -> State:
        response = # ... llm call ...
        return {
            "messages": response,
        }

All tool messages are now emitted by default, so you don't need to manually call `copilotkit_customize_config` to configure tool call emissions.

![](https://cdn.copilotkit.ai/docs/copilotkit/images/coagents-v-0-3-migration-image.png)

## How do I migrate?#

  1. Make sure to return any messages (tool calls or text messages) you want to be part of the message history from your LangGraph nodes.

  2. Optionally, remove manual `copilotkit_customize_config` calls when you want to emit tool calls.

  3. If you want to hide tool calls or messages from the chat, use `copilotkit_customize_config` and set `emit_tool_calls` or `emit_messages` to `False`. Make sure to not return these messages in your nodes so they don't become part of the message history.




### On this page

What's new in v0.3?How do I migrate?
