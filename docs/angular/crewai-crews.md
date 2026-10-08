---
url: https://docs.copilotkit.ai/angular/crewai-crews/
title: Introduction
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:49:04.890743+00:00
---

# Introduction

> Source: https://docs.copilotkit.ai/angular/crewai-crews/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendAngularAgent backendCrewAI Flows

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/angular/crewai-crews)[Quickstart](https://docs.copilotkit.ai/angular/crewai-crews/quickstart)[Build with agents](https://docs.copilotkit.ai/angular/crewai-crews/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/crewai-crews/intelligence/overview)

Basics

Generative UI

Interactivity

[WebMCP](https://docs.copilotkit.ai/angular/crewai-crews/webmcp)

Agent capabilities

CrewAI Flows

[Sub-agents](https://docs.copilotkit.ai/angular/crewai-crews/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/angular/crewai-crews/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/angular/crewai-crews/learning)

[User Memories](https://docs.copilotkit.ai/angular/crewai-crews/intelligence/memories)[Standalone collector](https://docs.copilotkit.ai/angular/crewai-crews/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/angular/crewai-crews/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/angular/crewai-crews/intelligence/analytics)[Channels](https://docs.copilotkit.ai/angular/crewai-crews/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/angular/crewai-crews/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/crewai-crews/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

CopilotKit + CrewAI Flows

# Bring your CrewAI Flows agents  
into any app

CopilotKit is an open-source framework that connects your app to CrewAI Flows agents. Give your agents chat, generative UI, human-in-the-loop, AG-UI Streams, Automatic Learning and more.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

[Quickstart](https://docs.copilotkit.ai/angular/crewai-crews/quickstart)

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

CrewAI and CopilotKit running together, in the React frontend. Every demo below is the same integration with one capability turned on.

## Build with CrewAI Flows

CrewAI gives you the flow: steps, state and the crew that works through them. What it does not give you is the surface. Somewhere for the conversation to happen, a way to show the flow while it runs, and a moment for a person to step in. Each capability below builds on something your flow already does.

### Generative UI

Your flow emits state and tool calls as each step completes. CopilotKit streams those to the browser and renders them as Angular components your users watch update while the flow runs.

[Read the docs ](https://docs.copilotkit.ai/angular/crewai-crews/guides/frontend-tools-generative-ui)[Live demo ](https://showcase.copilotkit.ai/angular/crewai-crews/gen-ui-tool-based)

### Human-in-the-loop

A flow can stop and wait for a person. CopilotKit renders your own UI for that decision and resumes the flow with the answer.

[Read the docs ](https://docs.copilotkit.ai/angular/crewai-crews/human-in-the-loop/flow)[Live demo ](https://showcase.copilotkit.ai/angular/crewai-crews/hitl-in-chat)

### Shared state

Flow state is the one object every step reads and writes. CopilotKit mirrors it into your app and back, so a user edit and a step write land in the same place.

[Read the docs ](https://docs.copilotkit.ai/angular/crewai-crews/guides/shared-state)[Live demo ](https://showcase.copilotkit.ai/angular/crewai-crews/shared-state-read-write)

Chat surfaces, headless UI, frontend tools and multi-agent flows work with CrewAI too. [And more](https://docs.copilotkit.ai/crewai-flows/build-with-agents)

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

Existing projectAdd a CrewAI Flows agent to your appExisting agentConnect your CrewAI Flows agent to your appNew projectBuild an app and agent from scratch

Step 1 of 4Setup

## Connect your agent

Your flow keeps running as its own Python service, with the AG-UI bridge from ag_ui_crewai in front of it. CopilotKit reaches that service over HTTP, so nothing inside the flow changes.

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

[Read the setup guide ](https://docs.copilotkit.ai/crewai-flows/quickstart)[View on GitHub](https://github.com/CopilotKit/CopilotKit)Start building 
