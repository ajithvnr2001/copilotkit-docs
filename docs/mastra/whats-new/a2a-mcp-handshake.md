---
url: https://docs.copilotkit.ai/mastra/whats-new/a2a-mcp-handshake/
title: A2A and MCP Handshake
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:17:31.769498+00:00
---

# A2A and MCP Handshake

> Source: https://docs.copilotkit.ai/mastra/whats-new/a2a-mcp-handshake/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMastra

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/mastra)[Quickstart](https://docs.copilotkit.ai/mastra/quickstart)[Build with agents](https://docs.copilotkit.ai/mastra/build-with-agents)[Intelligence](https://docs.copilotkit.ai/mastra/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/mastra/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/mastra/webmcp)

Agent capabilities

Mastra

[Sub-agents](https://docs.copilotkit.ai/mastra/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/mastra/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/mastra/learning)

[User Memories](https://docs.copilotkit.ai/mastra/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/mastra/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/mastra/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/mastra/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/mastra/intelligence/analytics)[Channels](https://docs.copilotkit.ai/mastra/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/mastra/telemetry)[Community frameworks](https://docs.copilotkit.ai/mastra/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Mastra](https://docs.copilotkit.ai/mastra)[What's New](https://docs.copilotkit.ai/mastra/whats-new)

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
  * [Agentic Protocols](https://docs.copilotkit.ai/mastra/agentic-protocols)


