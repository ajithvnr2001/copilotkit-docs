---
url: https://docs.copilotkit.ai/claude-sdk-typescript/
title: Claude Agent SDK (TypeScript)
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:54:12.615421+00:00
---

# Claude Agent SDK (TypeScript)

> Source: https://docs.copilotkit.ai/claude-sdk-typescript/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendClaude Agent SDK (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/claude-sdk-typescript)[Quickstart](https://docs.copilotkit.ai/claude-sdk-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/claude-sdk-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/claude-sdk-typescript/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/claude-sdk-typescript/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/claude-sdk-typescript/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/claude-sdk-typescript/learning)

[User Memories](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/analytics)[Channels](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/claude-sdk-typescript/telemetry)[Community frameworks](https://docs.copilotkit.ai/claude-sdk-typescript/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

CopilotKit + Claude Agent SDK (TypeScript)

# Bring your Claude Agent SDK (TypeScript) agents  
into any app

CopilotKit is an open-source framework that connects your app to Claude Agent SDK (TypeScript) agents. Give your agents chat, generative UI, human-in-the-loop, AG-UI Streams, Automatic Learning and more.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

[Quickstart](https://docs.copilotkit.ai/claude-sdk-typescript/quickstart)

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

The Claude Agent SDK and CopilotKit running together, in the React frontend. Every demo below is the same integration with one capability turned on.

## Build with Claude Agent SDK (TypeScript)

The Claude Agent SDK gives you the agent loop: tools, context handling, and a session that keeps its history. What it does not give you is the surface. Somewhere for the conversation to happen, a way to show the run while it is running, and a moment for a person to step in. Each capability below builds on something your agent already does.

### Generative UI

Your agent calls tools and reports progress as it works. CopilotKit streams those calls to the browser and renders each one as a React component, instead of leaving the user with a spinner.

[Read the docs ](https://docs.copilotkit.ai/claude-sdk-typescript/generative-ui)

### Human-in-the-loop

The agent calls an approval tool and waits for its result. CopilotKit resolves that tool from the browser once the user decides, and the same Claude run continues with the answer.

[Read the docs ](https://docs.copilotkit.ai/claude-sdk-typescript/human-in-the-loop)

### Shared state

Your session carries state across turns on the server. CopilotKit mirrors it into your app and back, so a user edit and an agent write land in the same place.

[Read the docs ](https://docs.copilotkit.ai/claude-sdk-typescript/shared-state)

Chat surfaces, headless UI, frontend tools and multi-agent flows work with the Claude Agent SDK too. [And more](https://docs.copilotkit.ai/claude-sdk-typescript/build-with-agents)

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

Existing projectAdd a Claude Agent SDK (TypeScript) agent to your appExisting agentConnect your Claude Agent SDK (TypeScript) agent to your appNew projectBuild an app and agent from scratch

Step 1 of 4Setup

## Connect your agent

Your agent keeps running as its own service, with the AG-UI adapter from @ag-ui/claude-agent-sdk in front of it. CopilotKit reaches that service over HTTP, so nothing inside the agent changes.
    
    
    import {
      CopilotRuntime,
      createCopilotRuntimeHandler,
    } from "@copilotkit/runtime/v2";
    import { HttpAgent } from "@ag-ui/client";
    
    const runtime = new CopilotRuntime({
      agents: {
        my_agent: new HttpAgent({ url: process.env.AGENT_URL! }),
      },
    });
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
    });
    
    export const GET = handler;
    export const POST = handler;

[Read the setup guide ](https://docs.copilotkit.ai/claude-sdk-typescript/quickstart)[View on GitHub](https://github.com/CopilotKit/CopilotKit)Start building 
