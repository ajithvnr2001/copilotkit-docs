---
url: https://docs.copilotkit.ai/angular/llamaindex/
title: Introduction
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:50:36.053638+00:00
---

# Introduction

> Source: https://docs.copilotkit.ai/angular/llamaindex/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendAngularAgent backendLlamaIndex

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/angular/llamaindex)[Quickstart](https://docs.copilotkit.ai/angular/llamaindex/quickstart)[Build with agents](https://docs.copilotkit.ai/angular/llamaindex/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/llamaindex/intelligence/overview)

Basics

Generative UI

Interactivity

Shared state

[WebMCP](https://docs.copilotkit.ai/angular/llamaindex/webmcp)

Agent capabilities

LlamaIndex

[Sub-agents](https://docs.copilotkit.ai/angular/llamaindex/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/angular/llamaindex/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/angular/llamaindex/learning)

[User Memories](https://docs.copilotkit.ai/angular/llamaindex/intelligence/memories)[Standalone collector](https://docs.copilotkit.ai/angular/llamaindex/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/angular/llamaindex/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/angular/llamaindex/intelligence/analytics)[Channels](https://docs.copilotkit.ai/angular/llamaindex/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/angular/llamaindex/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/llamaindex/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

CopilotKit + LlamaIndex

# Bring your LlamaIndex agents  
into any app

CopilotKit is an open-source framework that connects your app to LlamaIndex agents. Give your agents chat, generative UI, human-in-the-loop, AG-UI Streams, Automatic Learning and more.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

[Quickstart](https://docs.copilotkit.ai/angular/llamaindex/quickstart)

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

LlamaIndex and CopilotKit running together, in the React frontend. Every demo below is the same integration with one capability turned on.

## Build with LlamaIndex

LlamaIndex gives you the agent and everything it reads: indexes, retrievers and the workflow around them. What it does not give you is the surface. Somewhere for the conversation to happen, a way to show the run while it is running, and a moment for a person to step in. Each capability below builds on something your agent already does.

### Generative UI

Your workflow emits events and tool calls as it runs. CopilotKit streams them to the browser and renders each one as a an Angular component, so retrieval and reasoning are visible instead of hidden behind a spinner.

[Read the docs ](https://docs.copilotkit.ai/angular/llamaindex/guides/frontend-tools-generative-ui)[Live demo ](https://showcase.copilotkit.ai/angular/llamaindex/gen-ui-tool-based)

### Human-in-the-loop

A frontend tool registered with useHumanInTheLoop renders your own UI, waits for the user's answer, and hands it back to the agent as the tool result.

[Read the docs ](https://docs.copilotkit.ai/angular/llamaindex/guides/human-in-the-loop)[Live demo ](https://showcase.copilotkit.ai/angular/llamaindex/hitl-in-chat)

### Shared state

Your workflow carries state between steps. CopilotKit mirrors it into your app and back, so a user edit and an agent write land in the same place.

[Read the docs ](https://docs.copilotkit.ai/angular/llamaindex/guides/shared-state)[Live demo ](https://showcase.copilotkit.ai/angular/llamaindex/shared-state-read-write)

Chat surfaces, headless UI, frontend tools and multi-agent flows work with LlamaIndex too. [And more](https://docs.copilotkit.ai/angular/llamaindex/build-with-agents)

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

Existing projectAdd a LlamaIndex agent to your appExisting agentConnect your LlamaIndex agent to your appNew projectBuild an app and agent from scratch

Step 1 of 4Setup

## Connect your agent

Your agent keeps running as its own LlamaIndex service. The LlamaIndexAgent bridge points CopilotKit at its AG-UI endpoint, so nothing inside the agent changes.

app/api/copilotkit/route.ts
    
    
    import {
      CopilotRuntime,
      createCopilotRuntimeHandler,
    } from "@copilotkit/runtime/v2";
    import { LlamaIndexAgent } from "@ag-ui/llamaindex";
    
    const runtime = new CopilotRuntime({
      agents: {
        my_agent: new LlamaIndexAgent({ url: "http://localhost:8000/run" }),
      },
    });
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
    });
    
    export const GET = handler;
    export const POST = handler;

[Read the setup guide ](https://docs.copilotkit.ai/angular/llamaindex/quickstart)[View on GitHub](https://github.com/CopilotKit/CopilotKit)Start building 
