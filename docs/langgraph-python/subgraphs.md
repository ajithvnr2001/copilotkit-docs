---
url: https://docs.copilotkit.ai/langgraph-python/subgraphs/
title: Subgraphs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:08:55.635383+00:00
---

# Subgraphs

> Source: https://docs.copilotkit.ai/langgraph-python/subgraphs/

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

[Readables](https://docs.copilotkit.ai/langgraph-python/agent-app-context)[Configurable](https://docs.copilotkit.ai/langgraph-python/configurable)[Subgraphs](https://docs.copilotkit.ai/langgraph-python/subgraphs)[Guardrails & DLP](https://docs.copilotkit.ai/langgraph-python/guardrails)[AWS AgentCore](https://docs.copilotkit.ai/langgraph-python/deploy-agentcore)[LangSmith Platform](https://docs.copilotkit.ai/langgraph-python/deploy-langsmith)

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

Subgraphs

Agent capabilitiesLangGraph (Python)

# Subgraphs

Use multiple agents as subgraphs in your application.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

This example demonstrates subgraphs in the [CopilotKit Feature Viewer](https://feature-viewer.copilotkit.ai/langgraph/feature/subgraphs).

## What are Subgraphs?#

A subgraph is simply a graph used as a node inside another graph. Think of it as encapsulation for LangGraph: each subgraph is a self-contained unit that can be combined to build larger, more complex systems.

## When should I use this?#

Subgraphs are useful when you need to structure a graph into smaller, reusable pieces. They let you build multi-agent systems, reuse node sets across multiple graphs, and let different teams develop separate parts of a graph independently.

## How does CopilotKit support this?#

CopilotKit supports streaming directly from subgraphs, so nested graphs can emit events in real time just like a single graph.

Using this feature requires no extra steps on the agent side. All you need to do is subscribe to the agent state in your frontend:
    
    
    const { agent } = useAgent({
      agentId: "sample_agent",
    });
    
    // Access agent state as usual - subgraph streaming is handled automatically
    const state = agent.state;

The subgraph nodes will stream as usual, and you can also use `interrupt()` directly from a subgraph.

### On this page

What are Subgraphs?When should I use this?How does CopilotKit support this?
