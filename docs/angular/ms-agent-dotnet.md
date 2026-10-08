---
url: https://docs.copilotkit.ai/angular/ms-agent-dotnet/
title: Introduction
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:50:50.770185+00:00
---

# Introduction

> Source: https://docs.copilotkit.ai/angular/ms-agent-dotnet/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendAngularAgent backendMS Agent Framework (.NET)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/angular/ms-agent-dotnet)[Quickstart](https://docs.copilotkit.ai/angular/ms-agent-dotnet/quickstart)[Build with agents](https://docs.copilotkit.ai/angular/ms-agent-dotnet/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/ms-agent-dotnet/intelligence/overview)

Basics

Generative UI

Interactivity

[WebMCP](https://docs.copilotkit.ai/angular/ms-agent-dotnet/webmcp)

Agent capabilities

Microsoft Agent Framework

[Sub-agents](https://docs.copilotkit.ai/angular/ms-agent-dotnet/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/angular/ms-agent-dotnet/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/angular/ms-agent-dotnet/learning)

[User Memories](https://docs.copilotkit.ai/angular/ms-agent-dotnet/intelligence/memories)[Standalone collector](https://docs.copilotkit.ai/angular/ms-agent-dotnet/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/angular/ms-agent-dotnet/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/angular/ms-agent-dotnet/intelligence/analytics)[Channels](https://docs.copilotkit.ai/angular/ms-agent-dotnet/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/angular/ms-agent-dotnet/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/ms-agent-dotnet/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

CopilotKit + Microsoft Agent Framework

# Bring your Microsoft Agent Framework agents  
into any app

CopilotKit is an open-source framework that connects your app to Microsoft Agent Framework agents. Give your agents chat, generative UI, human-in-the-loop, AG-UI Streams, Automatic Learning and more.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

[Quickstart](https://docs.copilotkit.ai/angular/ms-agent-dotnet/quickstart)

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

The Microsoft Agent Framework and CopilotKit running together, in the React frontend. Every demo below is the same integration with one capability turned on.

## Build with Microsoft Agent Framework

The Microsoft Agent Framework gives you the agent: tools, threads and the host that runs them, in Python or .NET. What it does not give you is the surface. Somewhere for the conversation to happen, a way to show the run while it is running, and a moment for a person to step in. Each capability below builds on something your agent already does.

### Generative UI

Your agent calls tools and updates state as it runs. CopilotKit streams both to the browser and renders them as Angular components your users watch update while the agent works.

[Read the docs ](https://docs.copilotkit.ai/angular/ms-agent-dotnet/guides/frontend-tools-generative-ui)[Live demo ](https://showcase.copilotkit.ai/angular/ms-agent-dotnet/gen-ui-tool-based)

### Human-in-the-loop

Your agent can pause for a decision, or call a tool that lives in the browser. CopilotKit renders your own UI for either and resumes the run with the user's answer.

[Read the docs ](https://docs.copilotkit.ai/angular/ms-agent-dotnet/guides/human-in-the-loop)[Live demo ](https://showcase.copilotkit.ai/angular/ms-agent-dotnet/hitl-in-chat)

### Shared state

Threads carry state between turns on the server. CopilotKit mirrors it into your app and back, so a user edit and an agent write land in the same place.

[Read the docs ](https://docs.copilotkit.ai/angular/ms-agent-dotnet/guides/shared-state)[Live demo ](https://showcase.copilotkit.ai/angular/ms-agent-dotnet/shared-state-read-write)

Chat surfaces, headless UI, frontend tools and multi-agent flows work with the Microsoft Agent Framework too. [And more](https://docs.copilotkit.ai/microsoft-agent-framework/build-with-agents)

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

Existing projectAdd a MS Agent Framework (.NET) agent to your appExisting agentConnect your MS Agent Framework (.NET) agent to your appNew projectBuild an app and agent from scratch

Step 1 of 4Setup

## Connect your agent

Your agent keeps running as its own service, with the AG-UI bridge from agent_framework_ag_ui in front of it. CopilotKit reaches that service over HTTP, so nothing inside the agent changes.

app/api/copilotkit/route.ts
    
    
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

[Read the setup guide ](https://docs.copilotkit.ai/microsoft-agent-framework/quickstart)[View on GitHub](https://github.com/CopilotKit/CopilotKit)Start building 
