---
url: https://docs.copilotkit.ai/google-adk/agentic-protocols/
title: Overview
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:02:15.953379+00:00
---

# Overview

> Source: https://docs.copilotkit.ai/google-adk/agentic-protocols/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendGoogle ADK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/google-adk)[Quickstart](https://docs.copilotkit.ai/google-adk/quickstart)[Build with agents](https://docs.copilotkit.ai/google-adk/build-with-agents)[Intelligence](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/google-adk/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/google-adk/webmcp)

Agent capabilities

Google ADK

[Sub-agents](https://docs.copilotkit.ai/google-adk/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/google-adk/learning)

[User Memories](https://docs.copilotkit.ai/google-adk/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/google-adk/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/google-adk/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/google-adk/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/google-adk/intelligence/analytics)[Channels](https://docs.copilotkit.ai/google-adk/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

Learn

Concepts

[Architecture](https://docs.copilotkit.ai/google-adk/concepts/architecture)[Generative UI](https://docs.copilotkit.ai/google-adk/concepts/generative-ui-overview)[Which Hook for Which Job](https://docs.copilotkit.ai/google-adk/concepts/which-hook)[Open source vs Intelligence](https://docs.copilotkit.ai/google-adk/concepts/oss-vs-enterprise)

[Agentic Protocols](https://docs.copilotkit.ai/google-adk/agentic-protocols)

[AG-UI](https://docs.copilotkit.ai/google-adk/agentic-protocols/ag-ui)[AG-UI Middleware](https://docs.copilotkit.ai/google-adk/agentic-protocols/ag-ui-middleware)[MCP](https://docs.copilotkit.ai/google-adk/agentic-protocols/mcp)[A2A](https://docs.copilotkit.ai/google-adk/agentic-protocols/a2a)

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/google-adk/telemetry)[Community frameworks](https://docs.copilotkit.ai/google-adk/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Overview

LearnConceptsAgentic Protocols

# Overview

CopilotKit connects to your agents through the Agentic Protocol of your choice

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

CopilotKit is fully compatible with three major agentic protocols: AG-UI, MCP, and A2A.  
Learn about these protocols and how to connect your app to agents which support them using CopilotKit.

![Agentic Protocols - Venn Diagram](https://docs.copilotkit.ai/images/venn-agentic-light.svg)![Agentic Protocols - Venn Diagram](https://docs.copilotkit.ai/images/venn-agentic-dark.svg)Connection| Protocol| Purpose  
---|---|---  
**Agent ↔ User Interaction**| [**AG-UI**](https://docs.copilotkit.ai/agentic-protocols/ag-ui)  
(Agent–User Interaction Protocol)| The open, event-based standard that connects agents to user-facing applications — enabling real-time, multimodal, interactive experiences.  
**Agent ↔ Tools & Data**| [**MCP**](https://docs.copilotkit.ai/agentic-protocols/mcp)  
(Model Context Protocol)| Open standard that lets agents securely connect to external systems — tools, workflows, and data sources.  
**Agent ↔ Agent**| [**A2A**](https://docs.copilotkit.ai/agentic-protocols/a2a)  
(Agent to Agent)| Defines how agents coordinate and share work across distributed agentic systems.  
**Agent ↔ Generative UI**| **[A2UI](https://docs.copilotkit.ai/google-adk/generative-ui/a2ui)** (Google)  
**[MCP Apps](https://docs.copilotkit.ai/google-adk/generative-ui/mcp-apps)** (MCP Ecosystem)  
**Open-JSON-UI** (OpenAI)| Declarative, LLM-friendly [generative UI specs](https://docs.copilotkit.ai/generative-ui) that define _what_ to render and how to structure agent responses visually. CopilotKit fully supports all of these.  
  
## **Mixing and Matching Protocols**#

CopilotKit lets developers connect to any of these protocols **directly or in combination.** CopilotKit can connect through any of the Interaction Protocols to your agentic backend.

![Any Agentic Backend](https://docs.copilotkit.ai/images/any-agentic-backend-light.png)![Any Agentic Backend](https://docs.copilotkit.ai/images/any-agentic-backend-dark.png)

Or, since AG-UI also includes **handshakes** with both **MCP** and **A2A** , CopilotKit can connect to MCP or A2A supporting agents through AG-UI.

This means that if your host agent connects to subagents using **MCP** or **A2A** , their UI properties can be propagated all the way through to the user-facing application — while preserving **full security, policy, and observability controls.**

![MCP and A2A through AG-UI](https://docs.copilotkit.ai/images/mcp-and-a2a-through-agui-light.png)![MCP and A2A through AG-UI](https://docs.copilotkit.ai/images/mcp-and-a2a-through-agui-dark.png)

### On this page

Mixing and Matching Protocols
