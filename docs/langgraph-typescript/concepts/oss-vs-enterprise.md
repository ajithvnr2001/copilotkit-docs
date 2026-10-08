---
url: https://docs.copilotkit.ai/langgraph-typescript/concepts/oss-vs-enterprise/
title: Open source vs Intelligence
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:10:30.186339+00:00
---

# Open source vs Intelligence

> Source: https://docs.copilotkit.ai/langgraph-typescript/concepts/oss-vs-enterprise/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-typescript)[Quickstart](https://docs.copilotkit.ai/langgraph-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-typescript/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-typescript/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/langgraph-typescript/webmcp)

Agent capabilities

LangGraph (TypeScript)

[Sub-agents](https://docs.copilotkit.ai/langgraph-typescript/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/langgraph-typescript/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/langgraph-typescript/learning)

[User Memories](https://docs.copilotkit.ai/langgraph-typescript/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/langgraph-typescript/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/langgraph-typescript/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/langgraph-typescript/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/langgraph-typescript/intelligence/analytics)[Channels](https://docs.copilotkit.ai/langgraph-typescript/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

Learn

Concepts

[Architecture](https://docs.copilotkit.ai/langgraph-typescript/concepts/architecture)[Generative UI](https://docs.copilotkit.ai/langgraph-typescript/concepts/generative-ui-overview)[Which Hook for Which Job](https://docs.copilotkit.ai/langgraph-typescript/concepts/which-hook)[Open source vs Intelligence](https://docs.copilotkit.ai/langgraph-typescript/concepts/oss-vs-enterprise)

[Agentic Protocols](https://docs.copilotkit.ai/langgraph-typescript/agentic-protocols)

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/langgraph-typescript/telemetry)[Community frameworks](https://docs.copilotkit.ai/langgraph-typescript/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Open source vs Intelligence

LearnConcepts

# Open source vs Intelligence

Compare CopilotKit's open-source SDKs and runtime with Intelligence services for AG-UI Streams, User Memories, Automatic Learning, Product Analytics, and Channels.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

CopilotKit's **open-source SDKs and TypeScript runtime** connect your frontend to your agent without requiring a CopilotKit service. **CopilotKit Intelligence** adds AG-UI Streams, User Memories, Automatic Learning, Product Analytics, and Channels to that application. Choose the services your application needs while keeping your frontend and agent framework.

The TypeScript runtime is the default, most fully featured implementation and the only runtime that works without Intelligence. Python, Go, Ruby, and C#/.NET runtimes require cloud-hosted or self-hosted Intelligence. Their source is also open source; the distinction is the service they require. See [Runtime languages](https://docs.copilotkit.ai/langgraph-typescript/backend/copilot-runtime#runtime-languages) to choose a server implementation.

## The 30-second version#

  * **The open-source packages are enough for** building a working agentic application with framework-native APIs, prebuilt chat, frontend tools, gen-UI, and any AG-UI integration. The license is MIT. The packages run anywhere.
  * **Your own persistence remains an option.** LangGraph checkpointers, ADK session services, and application-owned storage can retain history without Intelligence. You own the storage and UI integration.
  * **CopilotKit Intelligence adds** conversation replay and continuity across devices, memory beyond one conversation, reviewed skills from real usage, usage data, and channel connections.
  * **CopilotKit Intelligence runs two ways** — [cloud-hosted](https://docs.copilotkit.ai/langgraph-typescript/intelligence/managed-intelligence-platform), or self-hosted on [Kubernetes](https://docs.copilotkit.ai/langgraph-typescript/intelligence/self-hosting) or [AWS ECS](https://docs.copilotkit.ai/langgraph-typescript/intelligence/self-hosting-ecs). Both deployments use the same app APIs.

| Open source only| Needs CopilotKit Intelligence  
---|---|---  
Agent chat, frontend tools, agent state, gen-UI| Yes|   
Any AG-UI integration (LangGraph, Mastra, Built-in, custom)| Yes|   
Framework-native or application-owned persistence| You operate and integrate it|   
Local Inspector for live events, tools, state, and connection debugging| Yes|   
AG-UI Streams with saved UI, resumable runs, and realtime sync| | Yes  
User Memories and Automatic Learning| | Yes  
Product Analytics and cloud-hosted channel connections| | Yes  
Inspector's saved Rich Threads and Automatic Learning panes| | Yes  
Intelligence project administration and API keys| | Yes  
  
## What's in the open-source core#

Everything you need to build a working agentic app, with no external service from CopilotKit:

  * **Frontend SDK** — `@copilotkit/react-core`, exporting hooks and prebuilt components for chat, tools, state, threads, and generative UI.


  * **Runtime** — `@copilotkit/runtime`, the request handler that mounts in your application server. Framework-agnostic core plus thin adapters for Express, Hono, Bun, Deno, Cloudflare Workers.
  * **AG-UI protocol** — open standard for agent ↔ frontend communication. 16 standardized event types, transport-agnostic.
  * **Built-in Agent** — `BuiltInAgent` runs an in-process agent loop (OpenAI / Anthropic / Google / any AI-SDK model) without requiring an external framework.
  * **Integrations** — first-party adapters for LangGraph (Python / TypeScript / FastAPI), Mastra, CrewAI, Pydantic AI, Microsoft Agent Framework, AWS Strands, Google ADK, and others.
  * **Generative UI primitives** — tool rendering, state rendering, headless APIs, and framework-native theming.



MIT licensed. Run it on any host, in any cloud, with any LLM provider.

## What's in CopilotKit Intelligence#

A **backend service** beside your runtime, with capabilities you can add as needed:

  * **[AG-UI Streams](https://docs.copilotkit.ai/langgraph-typescript/threads)** — save conversations, UI, and inputs; reopen them across devices and reconnect to active runs.
  * **[User Memories](https://docs.copilotkit.ai/langgraph-typescript/intelligence/memories)** — retain facts beyond a single conversation, with user and project scopes.
  * **[Automatic Learning](https://docs.copilotkit.ai/langgraph-typescript/learning)** — turn real usage into skills you review and publish; use [Skill delivery](https://docs.copilotkit.ai/langgraph-typescript/intelligence/learned-skills) to make published skills available to your agent.
  * **[Product Analytics](https://docs.copilotkit.ai/langgraph-typescript/intelligence/analytics)** — understand how people use your agent and its tools.
  * **[Channels](https://docs.copilotkit.ai/langgraph-typescript/intelligence/channels)** — connect your existing agent to Slack or Microsoft Teams through cloud-hosted Intelligence. Both are generally available. The open-source Channels SDK also lets you operate your own channel runner.
  * **Project administration** — manage organizations, projects, API keys, and plans in the [cloud-hosted web app](https://docs.copilotkit.ai/langgraph-typescript/intelligence/managed-intelligence-platform).



### Inspector with and without Intelligence#

[Inspector](https://docs.copilotkit.ai/langgraph-typescript/inspector) is available by default in development builds of React, Vue, and Angular browser apps. Use its local panes to debug your connection, live AG-UI events, tools, and state without Intelligence. Its **Rich Threads** and **Automatic Learning** panes require the corresponding Intelligence services to show saved conversations and learning data.

### Cloud-Hosted vs Self-Hosted#

Same CopilotKit Intelligence — you pick where it runs:

  * **[Cloud-hosted CopilotKit Intelligence](https://docs.copilotkit.ai/langgraph-typescript/intelligence/managed-intelligence-platform)** is the service CopilotKit operates. Sign up, get an API key, and point your runtime at it. Pick this when you want zero ops on the platform side.
  * **Self-hosted** runs in your infrastructure. Follow the [Kubernetes guide](https://docs.copilotkit.ai/langgraph-typescript/intelligence/self-hosting) for the Helm chart or the [AWS ECS guide](https://docs.copilotkit.ai/langgraph-typescript/intelligence/self-hosting-ecs) for the ECS bundle. You operate the services and their dependencies; use the deployment guide for the required infrastructure and credentials.



Application code doesn't change between cloud-hosted and self-hosted — same frontend SDK and runtime APIs. Only the platform endpoint and credential set change.

## Licenses#

The open-source SDKs and runtime use MIT. CopilotKit Intelligence and Showcase have separate terms.

## Where to go next#

  * **Existing agent framework** — start with your framework's overview and quickstart in the docs framework selector.
  * **Built-in Agent** — [Quickstart](https://docs.copilotkit.ai/langgraph-typescript/quickstart) starts an app when you want CopilotKit's built-in agent. No Intelligence credentials needed.
  * **CopilotKit Intelligence overview** — [CopilotKit Intelligence](https://docs.copilotkit.ai/langgraph-typescript/intelligence/overview) lists every platform capability and the per-feature setup.
  * **Cloud-hosted setup** — [Cloud-hosted CopilotKit Intelligence](https://docs.copilotkit.ai/langgraph-typescript/intelligence/managed-intelligence-platform) when CopilotKit operates the service.
  * **Self-hosted deployment** — [Kubernetes](https://docs.copilotkit.ai/langgraph-typescript/intelligence/self-hosting) or [AWS ECS](https://docs.copilotkit.ai/langgraph-typescript/intelligence/self-hosting-ecs) for your own infrastructure.
  * **Architecture deep-dive** — [CopilotKit Intelligence architecture](https://docs.copilotkit.ai/langgraph-typescript/intelligence/intelligence-platform) covers runtime/platform roles, project boundaries, threads, and realtime sync.



### On this page

The 30-second versionWhat's in the open-source coreWhat's in CopilotKit IntelligenceInspector with and without IntelligenceCloud-Hosted vs Self-HostedLicensesWhere to go next
