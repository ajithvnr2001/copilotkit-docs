---
url: https://docs.copilotkit.ai/deepagents/
title: Introduction
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:58:35.135338+00:00
---

# Introduction

> Source: https://docs.copilotkit.ai/deepagents/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendDeep Agents

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/deepagents)[Quickstart](https://docs.copilotkit.ai/deepagents/quickstart)[Build with agents](https://docs.copilotkit.ai/deepagents/build-with-agents)[Intelligence](https://docs.copilotkit.ai/deepagents/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/deepagents/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/deepagents/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/deepagents/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/deepagents/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/deepagents/learning)

[User Memories](https://docs.copilotkit.ai/deepagents/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/deepagents/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/deepagents/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/deepagents/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/deepagents/intelligence/analytics)[Channels](https://docs.copilotkit.ai/deepagents/intelligence/channels)

Hosting

Backend

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

[Open-source telemetry](https://docs.copilotkit.ai/deepagents/telemetry)[Community frameworks](https://docs.copilotkit.ai/deepagents/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

CopilotKit + Deep Agents

# Bring your Deep Agents agents  
into any app

CopilotKit is an open-source framework that connects your app to Deep Agents agents. Give your agents chat, generative UI, human-in-the-loop, AG-UI Streams, Automatic Learning and more.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

[Quickstart](https://docs.copilotkit.ai/deepagents/quickstart)

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

**Loading AG-UI Streams…**

Previous slide

AG-UI Streams

Automatic Learning

Next slide

## Build with Deep Agents

Deep Agents gives you a planning agent on LangGraph: subagents, a task list and the state they share. What it does not give you is the surface. Somewhere for the conversation to happen, a way to show the plan while it is worked through, and a moment for a person to step in. Each capability below builds on something your agent already does.

### Generative UI

Your agent updates its plan and calls tools as it works. CopilotKit streams both to the browser and renders them as React components, so the user watches the task list fill in.

[Read the docs ](https://docs.copilotkit.ai/deepagents/generative-ui)

### Human-in-the-loop

A node can interrupt and wait for a person. CopilotKit renders your own UI for that decision and resumes the run with the answer.

[Read the docs ](https://docs.copilotkit.ai/deepagents/human-in-the-loop)

### Shared state

The graph carries one state object between subagents. CopilotKit mirrors it into your app and back, so a user edit and an agent write land in the same place.

[Read the docs ](https://docs.copilotkit.ai/deepagents/shared-state)

Chat surfaces, headless UI, frontend tools and subagent flows work with Deep Agents too. [And more](https://docs.copilotkit.ai/deepagents/build-with-agents)

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

Existing projectAdd a Deep Agents agent to your appExisting agentConnect your Deep Agents agent to your appNew projectBuild an app and agent from scratch

Step 1 of 4Setup

## Connect your agent

Your agent stays where it runs today, on LangGraph Platform or your own service. CopilotKit reaches it over AG-UI, so nothing inside the agent changes.

app/api/copilotkit/[[...slug]]/route.ts
    
    
    import { CopilotRuntime, createCopilotRuntimeHandler } from "@copilotkit/runtime/v2";
    import { LangGraphAgent } from "@copilotkit/runtime/langgraph";
    
    const runtime = new CopilotRuntime({
      agents: {
        sample_agent: new LangGraphAgent({
          deploymentUrl: process.env.LANGGRAPH_DEPLOYMENT_URL!,
          graphId: "sample_agent",
          langsmithApiKey: process.env.LANGSMITH_API_KEY!,
        }),
      },
    });
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
    });
    
    export const GET = handler;
    export const POST = handler;
    export const PATCH = handler;
    export const DELETE = handler;

[Read the setup guide ](https://docs.copilotkit.ai/deepagents/quickstart)[View on GitHub](https://github.com/CopilotKit/CopilotKit)Start building 
