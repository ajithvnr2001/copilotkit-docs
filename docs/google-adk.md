---
url: https://docs.copilotkit.ai/google-adk/
title: ADK
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:02:12.294721+00:00
---

# ADK

> Source: https://docs.copilotkit.ai/google-adk/

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

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/google-adk/telemetry)[Community frameworks](https://docs.copilotkit.ai/google-adk/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

CopilotKit + ADK

# Bring your ADK agents  
into any app

CopilotKit is an open-source framework that connects your app to ADK agents. Give your agents chat, generative UI, human-in-the-loop, AG-UI Streams, Automatic Learning and more.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

[Quickstart](https://docs.copilotkit.ai/google-adk/quickstart)

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

ADK and CopilotKit running together, in the React frontend. Every demo below is the same integration with one capability turned on.

## Build with ADK

ADK gives you the agent: tools, sessions and a runner that serves them. What it does not give you is the surface. Somewhere for the conversation to happen, a way to show the run while it is running, and a moment for a person to step in. Each capability below builds on something your agent already does.

### Generative UI

Your agent calls tools and updates session state as it runs. CopilotKit streams both to the browser and renders them as React components your users watch update while the agent works.

[Read the docs ](https://docs.copilotkit.ai/google-adk/generative-ui)

### Human-in-the-loop

AGUIToolset() puts frontend tools in reach of your agent. CopilotKit renders the one that asks for a decision, waits for the user's answer, and hands it back as the tool result.

[Read the docs ](https://docs.copilotkit.ai/google-adk/human-in-the-loop)

### Shared state

ADK sessions keep state between turns on the server. CopilotKit mirrors it into your app and back, so a user edit and an agent write land in the same place.

[Read the docs ](https://docs.copilotkit.ai/google-adk/shared-state)

Chat surfaces, headless UI, frontend tools and multi-agent flows work with ADK too. [And more](https://docs.copilotkit.ai/google-adk/build-with-agents)

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

Existing projectAdd a Google ADK agent to your appExisting agentConnect your Google ADK agent to your appNew projectBuild an app and agent from scratch

Step 1 of 4Setup

## Connect your agent

Your agent keeps running as its own Python service, with the AG-UI bridge from ag_ui_adk in front of it. CopilotKit reaches that service over HTTP, so nothing inside the agent changes.
    
    
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

[Read the setup guide ](https://docs.copilotkit.ai/google-adk/quickstart)

## Already have Google ADK sessions?

When you add a user-facing app to an existing ADK agent, your users may need to open and continue sessions they started elsewhere. [CopilotKit Intelligence](https://docs.copilotkit.ai/intelligence/overview) can import persisted ADK sessions as threads, bringing that history into your CopilotKit app.

The importer supports ADK database session stores and Vertex/Agent Engine session history. In-memory sessions cannot be exported; legacy pickle stores need migration first.

Import history once; future CopilotKit-mediated runs synchronize with Intelligence and continue through ADK's native persistence path when your agent uses a durable session service with appropriate retention. This is not a continuous mirror of runs made outside CopilotKit.

[Import and synchronize Google ADK sessions](https://docs.copilotkit.ai/google-adk/threads-import) for source setup, agent mapping, and thread continuity.

[View on GitHub](https://github.com/CopilotKit/CopilotKit)Start building 
