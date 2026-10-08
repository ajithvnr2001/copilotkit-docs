---
url: https://docs.copilotkit.ai/agent-spec/
title: Open Agent Spec
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:45:35.654115+00:00
---

# Open Agent Spec

> Source: https://docs.copilotkit.ai/agent-spec/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/agent-spec)[Quickstart](https://docs.copilotkit.ai/agent-spec/quickstart)[Build with agents](https://docs.copilotkit.ai/agent-spec/build-with-agents)[Intelligence](https://docs.copilotkit.ai/agent-spec/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/agent-spec/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/agent-spec/webmcp)

Agent capabilities

Open Agent Spec

[Sub-agents](https://docs.copilotkit.ai/agent-spec/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/agent-spec/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/agent-spec/learning)

[User Memories](https://docs.copilotkit.ai/agent-spec/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/agent-spec/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/agent-spec/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/agent-spec/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/agent-spec/intelligence/analytics)[Channels](https://docs.copilotkit.ai/agent-spec/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/agent-spec/telemetry)[Community frameworks](https://docs.copilotkit.ai/agent-spec/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

CopilotKit + Open Agent Spec

# Bring your Open Agent Spec agents  
into any app

CopilotKit is an open-source framework that connects your app to Open Agent Spec agents. Give your agents chat, generative UI, human-in-the-loop, AG-UI Streams, Automatic Learning and more.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

[Quickstart](https://docs.copilotkit.ai/agent-spec/quickstart)

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

**Loading AG-UI Streams…**

Previous slide

AG-UI Streams

Automatic Learning

Next slide

## Build with Open Agent Spec

Open Agent Spec describes an agent in a form other tools can run. What it does not describe is the surface your users work in. Each capability below builds on what a running spec already emits.

### Generative UI

Your agent's tool calls arrive as they happen. CopilotKit renders each one as a React component in your own app, instead of leaving the user with a spinner.

[Read the docs ](https://docs.copilotkit.ai/agent-spec/generative-ui)

### Human-in-the-loop

A frontend tool registered with useHumanInTheLoop renders your own UI, waits for the user's answer, and hands it back to the agent as the tool result.

[Read the docs ](https://docs.copilotkit.ai/agent-spec/human-in-the-loop)

### Shared state

Your agent carries state between turns. CopilotKit mirrors it into your app and back, so a user edit and an agent write land in the same place.

[Read the docs ](https://docs.copilotkit.ai/agent-spec/shared-state)

Chat surfaces, headless UI, frontend tools and multi-agent flows work with Open Agent Spec too. [And more](https://docs.copilotkit.ai/agent-spec/build-with-agents)

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

Existing projectAdd a Agent Spec agent to your appExisting agentConnect your Agent Spec agent to your appNew projectBuild an app and agent from scratch

Step 1 of 4Setup

## Connect your agent

Your agent keeps running where it runs today, behind an AG-UI endpoint. CopilotKit reaches it over HTTP, so nothing inside the agent changes.
    
    
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

[Read the setup guide ](https://docs.copilotkit.ai/agent-spec/quickstart)[View on GitHub](https://github.com/CopilotKit/CopilotKit)Start building 
