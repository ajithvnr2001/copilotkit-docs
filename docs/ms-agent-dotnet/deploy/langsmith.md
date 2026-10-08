---
url: https://docs.copilotkit.ai/ms-agent-dotnet/deploy/langsmith/
title: LangSmith Platform
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:18:27.291757+00:00
---

# LangSmith Platform

> Source: https://docs.copilotkit.ai/ms-agent-dotnet/deploy/langsmith/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMS Agent Framework (.NET)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ms-agent-dotnet)[Quickstart](https://docs.copilotkit.ai/ms-agent-dotnet/quickstart)[Build with agents](https://docs.copilotkit.ai/ms-agent-dotnet/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ms-agent-dotnet/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ms-agent-dotnet/webmcp)

Agent capabilities

Microsoft Agent Framework

[Sub-agents](https://docs.copilotkit.ai/ms-agent-dotnet/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ms-agent-dotnet/learning)

[User Memories](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ms-agent-dotnet/telemetry)[Community frameworks](https://docs.copilotkit.ai/ms-agent-dotnet/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[MS Agent Framework (.NET)](https://docs.copilotkit.ai/ms-agent-dotnet)Deploy

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## CopilotKit + LangSmith Platform

[LangSmith Deployment](https://docs.langchain.com/langsmith/deployment) gives your LangGraph and Google ADK agents a managed runtime (serverless by default) — handling scaling, persistence, and the LangGraph Server API. CopilotKit gives those agents a production-ready frontend.

## How it works

The two connect through **CopilotKit Runtime** , a lightweight server-side layer that sits between your browser and your LangSmith deployment. It's the same runtime you'd use with any CopilotKit-powered agent — it just needs to run server-side so your `LANGSMITH_API_KEY` never reaches the browser.
    
    
    Browser → CopilotKit Runtime → LangSmith deployment → your agent

LangSmith hosts the agent only; there's no frontend-hosting offering. You host the CopilotKit frontend and runtime wherever you already deploy your app (Vercel, your own Node server, etc.) and point the runtime at the LangSmith deployment URL.

## What you get

  * **Chat UI** — prebuilt chat interface, or headless hooks to build your own
  * **Shared state** — bidirectional sync between agent state and your React UI
  * **Generative UI** — render custom components from tool calls in real time
  * **Human-in-the-loop** — let users review, approve, or redirect agent actions
  * **Managed persistence** — thread history and checkpoints live in the LangSmith deployment



## Quickstart

LangSmith authority

These steps reproduce the LangSmith deploy flow inline so you can finish here. For the canonical reference — pricing, deployment types, and self-hosting — see the [LangSmith deployment docs](https://docs.langchain.com/langsmith/deployment).

Prerequisites

You need a [LangSmith account](https://smith.langchain.com) on the **Plus plan or above** and a LangSmith API key (`lsv2_...`). Deploying uses the LangGraph CLI; Docker is optional (only needed for local container builds). **Google ADK** additionally needs **Python 3.11+** , the `deployments-wrap-sdk[google-adk]` package, and a **Google AI API key** if you use Gemini models.

Deployment models

This guide uses **LangSmith Cloud** via the CLI — serverless by default, or `--deployment-type dedicated` for a dedicated deployment. LangSmith also supports self-hosted control plane, hybrid, and standalone-server models; see the [deployment overview](https://docs.langchain.com/langsmith/deployment) to pick one. The CopilotKit wiring below is the same regardless of which model you deploy to.

## Troubleshooting

The runtime can't find my graph / 404 on invoke

Your `graphId` must exactly match a key in the `graphs` object of your deployment's `langgraph.json`. The LangGraph template names it `agent`; an ADK app uses whatever key you set (e.g. `my_agent`). Check the deployment's config in the LangSmith UI if unsure.

401 / authentication errors from the deployment

Confirm `LANGSMITH_API_KEY` is set on the **server** (where CopilotKit Runtime runs), not the browser, and that the key belongs to the same LangSmith workspace as the deployment. The key must start with `lsv2_`.

langgraph deploy fails or hangs

Ensure your LangSmith account is on the **Plus plan or above** and that `LANGSMITH_API_KEY` is present in `.env`. For local container builds, Docker (with the daemon running) is required — on Apple Silicon you also need Docker Buildx.

My ADK agent won't deploy

ADK agents must be wrapped with `wrap()` from `saf_sdk.adk` and use a `LangsmithSessionService`. The wrapped object has to be exported as a module-level variable that `langgraph.json` points at (e.g. `./agent.py:agent`). See the [Deploy Google ADK agents](https://docs.langchain.com/langsmith/deploy-google-adk) guide.

## What's next?

### Generative UI

Render custom React components directly from your agent's tool calls.

### Shared State

Sync structured state between your agent and your React UI bidirectionally.
