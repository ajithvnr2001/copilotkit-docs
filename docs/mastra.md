---
url: https://docs.copilotkit.ai/mastra/
title: Introduction
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:15:46.485435+00:00
---

# Introduction

> Source: https://docs.copilotkit.ai/mastra/

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

CopilotKit + Mastra

# Bring your Mastra agents  
into any app

CopilotKit is an open-source framework that connects your app to Mastra agents. Give your agents chat, generative UI, human-in-the-loop, AG-UI Streams, Automatic Learning and more.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

[Quickstart](https://docs.copilotkit.ai/mastra/quickstart)

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

**Loading Chat…**

Previous slide

Chat

AG-UI Streams

Automatic Learning

Generative UI

Declarative UI

Human-in-the-loop

Frontend tools

Shared state

Headless UI

Sub-agents

Next slide

Mastra and CopilotKit running together, in the React frontend. Every demo below is the same integration with one capability turned on.

## Build with Mastra

Mastra gives you agents, tools, workflows and working memory in TypeScript, and a server that runs them. What it does not give you is the surface. Somewhere for the conversation to happen, a way to show what the agent is doing while it works, and a moment for a person to step in. Each capability below builds on something Mastra already does.

### Generative UI

Your agent keeps working memory across the session. CopilotKit renders that state as your own React components, so users watch the draft take shape instead of waiting for a final answer.

[Read the docs ](https://docs.copilotkit.ai/mastra/generative-ui/state-rendering)

### Human-in-the-loop

Mastra's own suspend() stays inside Mastra's execution model. A frontend tool registered with useHumanInTheLoop renders UI, waits for the user's answer, and hands it back to the agent as the tool result.

[Read the docs ](https://docs.copilotkit.ai/mastra/human-in-the-loop/tool-based)

### Shared state

Working memory lives on the server, scoped by resourceId. The useAgent hook mirrors it into your app and back, so a user edit and an agent write land in the same place.

[Read the docs ](https://docs.copilotkit.ai/mastra/shared-state)

Chat surfaces, headless UI, frontend tools and background tasks work with Mastra too. [And more](https://docs.copilotkit.ai/mastra/build-with-agents)

## Start building

Connect an existing agent or build a new one. Get a tailored setup prompt.

Your setup

  1. 1Setup
  2. 2Frontend
  3. 3Features
  4. 4Prompt



Step 1 of 4

Step 1 of 4Setup

### What are you building?

Tell us what you already have. We’ll tailor your setup.

Existing projectAdd a Mastra agent to your appExisting agentConnect your Mastra agent to your appNew projectBuild an app and agent from scratch

Step 1 of 4Setup

## Connect your agent

Your Mastra service stays where it runs today. CopilotKit reaches it over HTTP through AG-UI and leaves it exactly where it is, so nothing inside Mastra changes.

app/api/copilotkit/[[...slug]]/route.ts
    
    
    import { CopilotRuntime, createCopilotRuntimeHandler, InMemoryAgentRunner } from "@copilotkit/runtime/v2";
    import { MastraAgent } from "@ag-ui/mastra";
    import { MastraClient } from "@mastra/client-js";
    
    const mastraClient = new MastraClient({
      baseUrl: process.env.MASTRA_BASE_URL ?? "http://127.0.0.1:4111",
    });
    
    const runtime = new CopilotRuntime({
      agents: () =>
        MastraAgent.getRemoteAgents({
          mastraClient,
          // Local demo only. Use your authenticated user ID in a multi-user app.
          resourceId: "local-demo-user",
        }),
      runner: new InMemoryAgentRunner(),
    });
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
    });
    
    export const GET = handler;
    export const POST = handler;
    export const PATCH = handler;
    export const DELETE = handler;

[Read the setup guide ](https://docs.copilotkit.ai/mastra/quickstart)[View on GitHub](https://github.com/CopilotKit/CopilotKit)Start building 
