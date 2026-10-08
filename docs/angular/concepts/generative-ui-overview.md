---
url: https://docs.copilotkit.ai/angular/concepts/generative-ui-overview/
title: Generative UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:49:01.460900+00:00
---

# Generative UI

> Source: https://docs.copilotkit.ai/angular/concepts/generative-ui-overview/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendAngularAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/angular)[Build with agents](https://docs.copilotkit.ai/angular/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/intelligence/overview)

Basics

Generative UI

Interactivity

[WebMCP](https://docs.copilotkit.ai/angular/webmcp)

Agent capabilities

Built-in Agent

[Sub-agents](https://docs.copilotkit.ai/angular/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/angular/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/angular/learning)

[User Memories](https://docs.copilotkit.ai/angular/intelligence/memories)[Standalone collector](https://docs.copilotkit.ai/angular/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/angular/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/angular/intelligence/analytics)[Channels](https://docs.copilotkit.ai/angular/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

Concepts

[Architecture](https://docs.copilotkit.ai/angular/concepts/architecture)[Generative UI](https://docs.copilotkit.ai/angular/concepts/generative-ui-overview)[Open source vs Intelligence](https://docs.copilotkit.ai/angular/concepts/oss-vs-enterprise)

[Agentic Protocols](https://docs.copilotkit.ai/angular/agentic-protocols)

Angular guides

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/angular/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Generative UI

LearnConcepts

# Generative UI

How CopilotKit lets agents drive UI — the primitives it ships, what each one is for, and how to pick the right one.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Generative UI in CopilotKit is the set of primitives that let an agent decide what appears on the screen — from rendering a specific application component you've built, to composing layouts from a catalog, to embedding sandboxed UI shipped by an MCP server.

## What CopilotKit ships#

Six primitives. Each one solves a different problem.

Primitive| What it does  
---|---  
**[Components as Tools](https://docs.copilotkit.ai/angular/guides/frontend-tools-generative-ui)**|  Register an application component as a frontend tool; the agent calls it and CopilotKit renders it inline with typed inputs.  
**[Tool Call Rendering](https://docs.copilotkit.ai/angular/guides/frontend-tools-generative-ui)**|  Map your agent's existing backend tool calls to custom UI cards showing live status, arguments, and results.  
**[State Rendering](https://docs.copilotkit.ai/angular/guides/frontend-tools-generative-ui)**|  Subscribe to the agent's streamed state and re-render UI as values arrive.  
**[Reasoning](https://docs.copilotkit.ai/angular/guides/frontend-tools-generative-ui)**|  Render the model's reasoning tokens inline as a first-class message type (default card, or fully custom).  
**[A2UI](https://docs.copilotkit.ai/angular/guides/a2ui)**|  Render UI from a declarative schema the agent emits, composed against a catalog you register. Two flavors: [Dynamic Schema](https://docs.copilotkit.ai/angular/guides/a2ui) (LLM generates the schema) and [Fixed Schema](https://docs.copilotkit.ai/angular/guides/a2ui) (you author the schema, agent supplies data).  
**[MCP Apps](https://docs.copilotkit.ai/angular/guides/frontend-tools-generative-ui)**|  Embed UI that an MCP server ships alongside its tools, rendered in a sandboxed iframe. No frontend renderer required.  
  
### Angular API#

Pass a standalone Angular component to `registerFrontendTool` when the tool runs in the browser. Use `registerRenderToolCall` when the tool runs on the backend and Angular only controls how the call appears.

**Prefer to learn by building?** Follow [Frontend tools and generative UI](https://docs.copilotkit.ai/angular/guides/frontend-tools-generative-ui) for a complete Angular example with typed tools, standalone renderer components, A2UI, Open Generative UI, and MCP Apps.

## Pick one#

Match the row that sounds like your situation:

You want to…| Use  
---|---  
Let the agent render a specific application component you've already built| **[Components as Tools](https://docs.copilotkit.ai/angular/guides/frontend-tools-generative-ui)**  
Brand the cards CopilotKit draws for your agent's existing backend tools| **[Tool Call Rendering](https://docs.copilotkit.ai/angular/guides/frontend-tools-generative-ui)**  
Update UI as the agent's state changes (progress, drafts, dashboards)| **[State Rendering](https://docs.copilotkit.ai/angular/guides/frontend-tools-generative-ui)**  
Surface the model's thinking chain in the chat| **[Reasoning](https://docs.copilotkit.ai/angular/guides/frontend-tools-generative-ui)**  
Let the agent compose layouts from a catalog you define| **[A2UI](https://docs.copilotkit.ai/angular/guides/a2ui)** — [Fixed Schema](https://docs.copilotkit.ai/angular/guides/a2ui) if the surface is known, [Dynamic Schema](https://docs.copilotkit.ai/angular/guides/a2ui) if it isn't  
Embed someone else's MCP-hosted UI in the chat| **[MCP Apps](https://docs.copilotkit.ai/angular/guides/frontend-tools-generative-ui)**  
  
## How the primitives compare#

These primitives sit along a spectrum from author-controlled to agent-invented. Same frontend application, same runtime, same AG-UI protocol — the choice is per-feature, not per-product.

  * **Controlled** — you wrote the component; the agent only picks _which_ one to render and _what data_ to pass. Highest predictability, highest engineering cost per capability. _Components as Tools, Tool Call Rendering, State Rendering, Reasoning._
  * **Declarative** — the agent emits a structured spec; the frontend composes from a catalog you registered. Creativity inside a guardrail. _A2UI (Dynamic and Fixed Schema)._
  * **Open-Ended** — the UI is invented elsewhere (an MCP server) and you sandbox it. Highest expressive range, hardest to guarantee accessibility / brand / security. _MCP Apps._



## Where to go next#

### [Components as ToolsRegister an application component as a tool the agent can call.](https://docs.copilotkit.ai/angular/guides/frontend-tools-generative-ui)### [Tool Call RenderingCustom UI for your agent's backend tool calls.](https://docs.copilotkit.ai/angular/guides/frontend-tools-generative-ui)### [State RenderingUI that re-renders as the agent's state streams in.](https://docs.copilotkit.ai/angular/guides/frontend-tools-generative-ui)### [ReasoningRender the model's reasoning tokens inline.](https://docs.copilotkit.ai/angular/guides/frontend-tools-generative-ui)### [A2UIDeclarative UI from an agent-emitted schema.](https://docs.copilotkit.ai/angular/guides/a2ui)### [MCP AppsEmbed MCP-hosted UI in a sandboxed iframe.](https://docs.copilotkit.ai/angular/guides/frontend-tools-generative-ui)

### On this page

What CopilotKit shipsAngular APIPick oneHow the primitives compareWhere to go next
