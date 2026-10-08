---
url: https://docs.copilotkit.ai/angular/ag2/
title: Introduction
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:48:11.524721+00:00
---

# Introduction

> Source: https://docs.copilotkit.ai/angular/ag2/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendAngularAgent backendAG2

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/angular/ag2)[Quickstart](https://docs.copilotkit.ai/angular/ag2/quickstart)[Build with agents](https://docs.copilotkit.ai/angular/ag2/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/ag2/intelligence/overview)

Basics

Generative UI

Interactivity

[WebMCP](https://docs.copilotkit.ai/angular/ag2/webmcp)

Agent capabilities

AG2

[Sub-agents](https://docs.copilotkit.ai/angular/ag2/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/angular/ag2/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/angular/ag2/learning)

[User Memories](https://docs.copilotkit.ai/angular/ag2/intelligence/memories)[Standalone collector](https://docs.copilotkit.ai/angular/ag2/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/angular/ag2/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/angular/ag2/intelligence/analytics)[Channels](https://docs.copilotkit.ai/angular/ag2/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/angular/ag2/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/ag2/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

CopilotKit + AG2

# Bring your AG2 agents  
into any app

CopilotKit is an open-source framework that connects your app to AG2 agents. Give your agents chat, generative UI, human-in-the-loop, AG-UI Streams, Automatic Learning and more.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

[Quickstart](https://docs.copilotkit.ai/angular/ag2/quickstart)

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

AG2 and CopilotKit running together, in the React frontend. Every demo below is the same integration with one capability turned on.

## Build with AG2

AG2 gives you the conversation between your agents: roles, turns and the tools they call. What it does not give you is the surface a person joins it through. Each capability below builds on something your agents already do.

### Generative UI

Your agents call tools as the conversation runs. CopilotKit streams those calls to the browser and renders each one as a an Angular component, instead of leaving the user with a spinner.

[Read the docs ](https://docs.copilotkit.ai/angular/ag2/guides/frontend-tools-generative-ui)[Live demo ](https://showcase.copilotkit.ai/angular/ag2/gen-ui-tool-based)

### Human-in-the-loop

A frontend tool registered with useHumanInTheLoop renders your own UI, waits for the user's answer, and hands it back to the agent as the tool result.

[Read the docs ](https://docs.copilotkit.ai/angular/ag2/guides/human-in-the-loop)[Live demo ](https://showcase.copilotkit.ai/angular/ag2/hitl-in-chat)

### Shared state

Your agents carry state across turns. CopilotKit mirrors it into your app and back, so a user edit and an agent write land in the same place.

[Read the docs ](https://docs.copilotkit.ai/angular/ag2/guides/shared-state)[Live demo ](https://showcase.copilotkit.ai/angular/ag2/shared-state-read-write)

Chat surfaces, headless UI, frontend tools and multi-agent flows work with AG2 too. [And more](https://docs.copilotkit.ai/angular/ag2/build-with-agents)

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

Existing projectAdd a AG2 agent to your appExisting agentConnect your AG2 agent to your appNew projectBuild an app and agent from scratch

Step 1 of 4Setup

## Connect your agent

Your agents keep running as their own Python service, with AGUIStream from ag2.ag_ui in front of them. CopilotKit reaches that service over HTTP, so nothing inside AG2 changes.

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

[Read the setup guide ](https://docs.copilotkit.ai/angular/ag2/quickstart)[View on GitHub](https://github.com/CopilotKit/CopilotKit)Start building 
