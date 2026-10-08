---
url: https://docs.copilotkit.ai/ms-agent-harness-dotnet/whats-new/a2a-mcp-handshake/
title: A2A and MCP Handshake
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:21:18.535512+00:00
---

# A2A and MCP Handshake

> Source: https://docs.copilotkit.ai/ms-agent-harness-dotnet/whats-new/a2a-mcp-handshake/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMS Agent Harness (.NET)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ms-agent-harness-dotnet)[Quickstart](https://docs.copilotkit.ai/ms-agent-harness-dotnet/quickstart)[Build with agents](https://docs.copilotkit.ai/ms-agent-harness-dotnet/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ms-agent-harness-dotnet/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ms-agent-harness-dotnet/webmcp)

Agent capabilities

MS Agent Harness (.NET)

[Sub-agents](https://docs.copilotkit.ai/ms-agent-harness-dotnet/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ms-agent-harness-dotnet/learning)

[User Memories](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/ms-agent-harness-dotnet/telemetry)[Community frameworks](https://docs.copilotkit.ai/ms-agent-harness-dotnet/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[MS Agent Harness (.NET)](https://docs.copilotkit.ai/ms-agent-harness-dotnet)[What's New](https://docs.copilotkit.ai/ms-agent-harness-dotnet/whats-new)

# A2A and MCP Handshake

AG-UI handshakes enable seamless protocol interoperability

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

# A2A and MCP Handshake

AG-UI now includes **handshakes** with both **MCP** and **A2A** protocols, ensuring smooth interoperability across the full agentic stack.

## What Are Protocol Handshakes?#

Protocol handshakes allow AG-UI to seamlessly communicate with agents using different interaction protocols. This means you can connect your frontend to agents that internally use MCP or A2A without any additional configuration.

## Benefits#

### Full Interoperability#

If your host agent connects to subagents using **MCP** or **A2A** , their UI properties can be propagated all the way through to the user-facing application.

### Security and Control#

Handshakes preserve **full security, policy, and observability controls** throughout the communication chain.

### Simplified Architecture#

No need to choose between protocols—use them all together in a single application.

## How It Works#

  1. **Frontend connects via AG-UI** \- Your application uses AG-UI to connect to the host agent
  2. **Host agent uses MCP/A2A** \- The host agent can communicate with subagents using MCP or A2A
  3. **UI properties propagate** \- Generative UI and other properties flow back to your frontend automatically



## Learn More#

  * [AG-UI Protocol](https://docs.copilotkit.ai/ag-ui-protocol)
  * [MCP Integration](https://docs.copilotkit.ai/connect-mcp-servers)
  * [A2A Protocol](https://docs.copilotkit.ai/a2a-protocol)
  * [Agentic Protocols](https://docs.copilotkit.ai/ms-agent-harness-dotnet/agentic-protocols)


