---
url: https://docs.copilotkit.ai/strands-typescript/concepts/architecture/
title: Architecture
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:29:17.891819+00:00
---

# Architecture

> Source: https://docs.copilotkit.ai/strands-typescript/concepts/architecture/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAWS Strands (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/strands-typescript)[Quickstart](https://docs.copilotkit.ai/strands-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/strands-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/strands-typescript/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/strands-typescript/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/strands-typescript/webmcp)

Agent capabilities

AWS Strands (TypeScript)

[Sub-agents](https://docs.copilotkit.ai/strands-typescript/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/strands-typescript/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/strands-typescript/learning)

[User Memories](https://docs.copilotkit.ai/strands-typescript/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/strands-typescript/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/strands-typescript/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/strands-typescript/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/strands-typescript/intelligence/analytics)[Channels](https://docs.copilotkit.ai/strands-typescript/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

Learn

Concepts

[Architecture](https://docs.copilotkit.ai/strands-typescript/concepts/architecture)[Generative UI](https://docs.copilotkit.ai/strands-typescript/concepts/generative-ui-overview)[Which Hook for Which Job](https://docs.copilotkit.ai/strands-typescript/concepts/which-hook)[Open source vs Intelligence](https://docs.copilotkit.ai/strands-typescript/concepts/oss-vs-enterprise)

[Agentic Protocols](https://docs.copilotkit.ai/strands-typescript/agentic-protocols)

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/strands-typescript/telemetry)[Community frameworks](https://docs.copilotkit.ai/strands-typescript/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Architecture

LearnConcepts

# Architecture

How CopilotKit's pieces fit together

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

CopilotKit is a three-layer stack — **frontend, runtime, agent** — connected by the open **[AG-UI](https://docs.copilotkit.ai/strands-typescript/agentic-protocols/ag-ui)** event protocol. The runtime lives in your own application server, so the only thing between your UI and your agent is a wire format you can inspect.

## The 30-second version#

  * **Frontend.** A framework-native SDK and prebuilt chat components that connect your UI to a running agent.
  * **Runtime.** A request handler mounted in your app server (Next.js, Express, Hono, Bun, Deno, Workers). Brokers auth, tool calls, and the AG-UI stream.
  * **Agent.** Any AG-UI-compatible backend — Built-in, LangGraph, Mastra, CrewAI, Pydantic AI, MAF, or your own.
  * **AG-UI** is the wire format: 16 event types, transport-agnostic, framework-agnostic. Swap any layer without rewriting the others.



## The three layers#

![](https://cdn.copilotkit.ai/docs/copilotkit/images/architecture-diagram.png)

### 1\. Frontend#

The application your users interact with. CopilotKit ships framework-native state and tool APIs plus prebuilt components such as `CopilotChat`, `CopilotSidebar`, and `CopilotPopup`. Use a prebuilt chat surface, build a fully custom UI with the headless APIs, or mix the two.

### 2\. Runtime#

A request handler that mounts inside your application server (Next.js App Router, Express, Hono, Bun, Deno, Cloudflare Workers). The runtime accepts requests from the frontend, mediates auth and tool calls, and forwards work to your agent over AG-UI. For the framework-agnostic path you can instantiate a `BuiltInAgent` in-process and skip an external agent process entirely.

### 3\. Agent#

The agent backend you choose: LangGraph, Mastra, CrewAI, Pydantic AI, Microsoft Agent Framework, the Built-in Agent, or any custom AG-UI-compatible implementation. The agent runs your prompt, calls tools, emits state, and streams events back to the runtime.

## AG-UI: the protocol bridge#

CopilotKit doesn't lock you into one agent framework. The runtime talks to your agent over **[AG-UI](https://docs.copilotkit.ai/strands-typescript/agentic-protocols/ag-ui)** , an open, event-driven protocol that standardizes how agents communicate with applications:

  * **Event-driven** — 16 standardized event types (text deltas, tool calls, state snapshots and deltas, run lifecycle) stream from the agent through the runtime to the frontend.
  * **Bidirectional** — users send input, agents respond, agents pause for human-in-the-loop input, frontends expose frontend tools the agent can invoke.
  * **Transport-agnostic** — SSE, WebSockets, webhooks, whatever your stack prefers.
  * **Framework-agnostic** — every supported integration ships a thin AG-UI adapter. Switch backends with one line of runtime configuration.



> _"The future of agents isn't one company or one platform — it's an agentic ecosystem connected by protocols."_

Because the contract is a protocol — not an SDK lock-in — you can swap the agent layer without rewriting the frontend, run multiple agent backends side by side, and integrate with anything AG-UI-compatible: MCP servers, A2UI components, Oracle / Google / AWS agent platforms.

## Request flow at a glance#

  1. A user sends a message in your frontend application.
  2. The frontend agent API posts to your runtime endpoint.
  3. Runtime opens an AG-UI session with the configured agent.
  4. Agent emits text, tool calls, and state updates as AG-UI events.
  5. Runtime streams the events back; the frontend renders them in real time.
  6. If the agent calls a frontend tool, the runtime relays the request, your browser handler runs, and the result flows back to the agent.
  7. Threads, persistence, and realtime sync (when configured) are mediated by [CopilotKit Intelligence](https://docs.copilotkit.ai/strands-typescript/intelligence/overview) — the platform backend that sits beside the runtime.



## Where to go next#

  * **Practical setup** — [Quickstart](https://docs.copilotkit.ai/strands-typescript/quickstart) wires all three layers in ~10 minutes against the Built-in Agent.
  * **Protocol depth** — [AG-UI documentation](https://docs.copilotkit.ai/strands-typescript/agentic-protocols/ag-ui) covers every event type, transport option, and middleware hook.
  * **Backend choices** — [Agents & Backends](https://docs.copilotkit.ai/strands-typescript) explains the runtime, custom agents, and the trade-offs between Built-in, external frameworks, and bring-your-own.
  * **CopilotKit Intelligence overview** — [CopilotKit Intelligence](https://docs.copilotkit.ai/strands-typescript/intelligence/overview) covers Threads, persistence, inspection, and the cloud-hosted or self-hosted decision.



### On this page

The 30-second versionThe three layers1\. Frontend2\. Runtime3\. AgentAG-UI: the protocol bridgeRequest flow at a glanceWhere to go next
