---
url: https://docs.copilotkit.ai/angular/pydantic-ai/
title: Introduction
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:50:59.417797+00:00
---

# Introduction

> Source: https://docs.copilotkit.ai/angular/pydantic-ai/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendAngularAgent backendPydanticAI

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/angular/pydantic-ai)[Quickstart](https://docs.copilotkit.ai/angular/pydantic-ai/quickstart)[Build with agents](https://docs.copilotkit.ai/angular/pydantic-ai/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/pydantic-ai/intelligence/overview)

Basics

Generative UI

Interactivity

[WebMCP](https://docs.copilotkit.ai/angular/pydantic-ai/webmcp)

Agent capabilities

Pydantic AI

[Sub-agents](https://docs.copilotkit.ai/angular/pydantic-ai/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/angular/pydantic-ai/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/angular/pydantic-ai/learning)

[User Memories](https://docs.copilotkit.ai/angular/pydantic-ai/intelligence/memories)[Standalone collector](https://docs.copilotkit.ai/angular/pydantic-ai/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/angular/pydantic-ai/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/angular/pydantic-ai/intelligence/analytics)[Channels](https://docs.copilotkit.ai/angular/pydantic-ai/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/angular/pydantic-ai/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/pydantic-ai/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

CopilotKit + Pydantic AI

# Bring your Pydantic AI agents  
into any app

CopilotKit is an open-source framework that connects your app to Pydantic AI agents. Give your agents chat, generative UI, human-in-the-loop, AG-UI Streams, Automatic Learning and more.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

[Quickstart](https://docs.copilotkit.ai/angular/pydantic-ai/quickstart)

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

Pydantic AI and CopilotKit running together, in the React frontend. Every demo below is the same integration with one capability turned on.

## Build with Pydantic AI

Pydantic AI gives you the agent and the types around it: validated tools, typed results and the dependencies you hand in. What it does not give you is the surface. Somewhere for the conversation to happen, a way to show the run while it is running, and a moment for a person to step in. Each capability below builds on something your agent already does.

### Generative UI

Your agent calls typed tools as it runs. CopilotKit streams those calls to the browser and renders each one as a an Angular component, instead of leaving the user with a spinner.

[Read the docs ](https://docs.copilotkit.ai/angular/pydantic-ai/guides/frontend-tools-generative-ui)[Live demo ](https://showcase.copilotkit.ai/angular/pydantic-ai/gen-ui-tool-based)

### Human-in-the-loop

A frontend tool registered with useHumanInTheLoop renders your own UI, waits for the user's answer, and hands it back to the agent as the tool result.

[Read the docs ](https://docs.copilotkit.ai/angular/pydantic-ai/guides/human-in-the-loop)[Live demo ](https://showcase.copilotkit.ai/angular/pydantic-ai/hitl-in-chat)

### Shared state

Your agent carries state between turns. CopilotKit mirrors it into your app and back, so a user edit and an agent write land in the same place.

[Read the docs ](https://docs.copilotkit.ai/angular/pydantic-ai/guides/shared-state)[Live demo ](https://showcase.copilotkit.ai/angular/pydantic-ai/shared-state-read-write)

Chat surfaces, headless UI, frontend tools and multi-agent flows work with Pydantic AI too. [And more](https://docs.copilotkit.ai/angular/pydantic-ai/build-with-agents)

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

Existing projectAdd a PydanticAI agent to your appExisting agentConnect your PydanticAI agent to your appNew projectBuild an app and agent from scratch

Step 1 of 4Setup

## Connect your agent

Your agent keeps running as its own Python service, with the AGUIAdapter from pydantic_ai.ui.ag_ui in front of it. CopilotKit reaches that service over HTTP, so nothing inside the agent changes.

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

[Read the setup guide ](https://docs.copilotkit.ai/angular/pydantic-ai/quickstart)[View on GitHub](https://github.com/CopilotKit/CopilotKit)Start building 
