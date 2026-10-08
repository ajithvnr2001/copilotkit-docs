---
url: https://docs.copilotkit.ai/angular/agno/
title: Introduction
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:48:17.869336+00:00
---

# Introduction

> Source: https://docs.copilotkit.ai/angular/agno/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendAngularAgent backendAgno

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/angular/agno)[Quickstart](https://docs.copilotkit.ai/angular/agno/quickstart)[Build with agents](https://docs.copilotkit.ai/angular/agno/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/agno/intelligence/overview)

Basics

Generative UI

Interactivity

[WebMCP](https://docs.copilotkit.ai/angular/agno/webmcp)

Agent capabilities

Angular Guides

[Sub-agents](https://docs.copilotkit.ai/angular/agno/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/angular/agno/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/angular/agno/learning)

[User Memories](https://docs.copilotkit.ai/angular/agno/intelligence/memories)[Standalone collector](https://docs.copilotkit.ai/angular/agno/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/angular/agno/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/angular/agno/intelligence/analytics)[Channels](https://docs.copilotkit.ai/angular/agno/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

Angular guides

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/angular/agno/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/agno/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

CopilotKit + Agno

# Bring your Agno agents  
into any app

CopilotKit is an open-source framework that connects your app to Agno agents. Give your agents chat, generative UI, human-in-the-loop, AG-UI Streams, Automatic Learning and more.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

[Quickstart](https://docs.copilotkit.ai/angular/agno/quickstart)

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

Agno and CopilotKit running together, in the React frontend. Every demo below is the same integration with one capability turned on.

## Build with Agno

Agno gives you the agent: a model, tools, memory and a server that runs them. What it does not give you is the surface. Somewhere for the conversation to happen, a way to show the run while it is running, and a moment for a person to step in. Each capability below builds on something your agent already does.

### Generative UI

Your agent calls tools and reports progress as it works. CopilotKit streams that to the browser and renders each step as a an Angular component your users watch update while the agent works.

[Read the docs ](https://docs.copilotkit.ai/angular/agno/guides/frontend-tools-generative-ui)[Live demo ](https://showcase.copilotkit.ai/angular/agno/gen-ui-tool-based)

### Human-in-the-loop

A frontend tool registered with useHumanInTheLoop renders your own UI, waits for the user's answer, and hands it back to the agent as the tool result.

[Read the docs ](https://docs.copilotkit.ai/angular/agno/guides/human-in-the-loop)[Live demo ](https://showcase.copilotkit.ai/angular/agno/hitl-in-chat)

### Shared state

Your agent keeps state between turns on the server. CopilotKit mirrors it into your app and back, so a user edit and an agent write land in the same place.

[Read the docs ](https://docs.copilotkit.ai/angular/agno/guides/shared-state)[Live demo ](https://showcase.copilotkit.ai/angular/agno/shared-state-read-write)

Chat surfaces, headless UI, frontend tools and multi-agent flows work with Agno too. [And more](https://docs.copilotkit.ai/angular/agno/build-with-agents)

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

Existing projectAdd a Agno agent to your appExisting agentConnect your Agno agent to your appNew projectBuild an app and agent from scratch

Step 1 of 4Setup

## Connect your agent

Your agent keeps running as its own Agno service. The AgnoAgent bridge points CopilotKit at its AG-UI endpoint, so nothing inside the agent changes.

app/api/copilotkit/route.ts
    
    
    import {
      CopilotRuntime,
      createCopilotRuntimeHandler,
    } from "@copilotkit/runtime/v2";
    import { AgnoAgent } from "@ag-ui/agno";
    
    const runtime = new CopilotRuntime({
      agents: {
        my_agent: new AgnoAgent({ url: "http://localhost:8000/agui" }),
      },
    });
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
    });
    
    export const GET = handler;
    export const POST = handler;

[Read the setup guide ](https://docs.copilotkit.ai/angular/agno/quickstart)[View on GitHub](https://github.com/CopilotKit/CopilotKit)Start building 
