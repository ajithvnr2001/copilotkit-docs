---
url: https://docs.copilotkit.ai/angular/strands/
title: Introduction
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:51:13.808768+00:00
---

# Introduction

> Source: https://docs.copilotkit.ai/angular/strands/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendAngularAgent backendAWS Strands (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/angular/strands)[Quickstart](https://docs.copilotkit.ai/angular/strands/quickstart)[Build with agents](https://docs.copilotkit.ai/angular/strands/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/strands/intelligence/overview)

Basics

Generative UI

Interactivity

[WebMCP](https://docs.copilotkit.ai/angular/strands/webmcp)

Agent capabilities

AWS Strands (Python)

[Sub-agents](https://docs.copilotkit.ai/angular/strands/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/angular/strands/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/angular/strands/learning)

[User Memories](https://docs.copilotkit.ai/angular/strands/intelligence/memories)[Standalone collector](https://docs.copilotkit.ai/angular/strands/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/angular/strands/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/angular/strands/intelligence/analytics)[Channels](https://docs.copilotkit.ai/angular/strands/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

Concepts

Angular guides

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/angular/strands/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/strands/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

CopilotKit + AWS Strands

# Bring your AWS Strands agents  
into any app

CopilotKit is an open-source framework that connects your app to AWS Strands agents. Give your agents chat, generative UI, human-in-the-loop, AG-UI Streams, Automatic Learning and more.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

[Quickstart](https://docs.copilotkit.ai/angular/strands/quickstart)

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

Strands and CopilotKit running together, in the React frontend. Every demo below is the same integration with one capability turned on.

## Build with AWS Strands

Strands gives you the agent: a model, a tool loop and the state it carries between turns. What it does not give you is the surface. Somewhere for the conversation to happen, a way to show the run while it is running, and a moment for a person to step in. Each capability below builds on something your agent already does.

### Generative UI

Your agent calls tools and reports progress as it works. CopilotKit streams that to the browser and renders each step as a an Angular component, instead of leaving the user with a spinner.

[Read the docs ](https://docs.copilotkit.ai/angular/strands/guides/frontend-tools-generative-ui)[Live demo ](https://showcase.copilotkit.ai/angular/strands/gen-ui-tool-based)

### Human-in-the-loop

A frontend tool registered with useHumanInTheLoop renders your own UI, waits for the user's answer, and hands it back to the agent as the tool result.

[Read the docs ](https://docs.copilotkit.ai/angular/strands/guides/human-in-the-loop)[Live demo ](https://showcase.copilotkit.ai/angular/strands/hitl-in-chat)

### Shared state

Your agent keeps state on the server between turns. CopilotKit mirrors it into your app and back, so a user edit and an agent write land in the same place.

[Read the docs ](https://docs.copilotkit.ai/angular/strands/guides/shared-state)[Live demo ](https://showcase.copilotkit.ai/angular/strands/shared-state-read-write)

Chat surfaces, headless UI, frontend tools and multi-agent flows work with Strands too. [And more](https://docs.copilotkit.ai/aws-strands/build-with-agents)

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

Existing projectAdd a AWS Strands (Python) agent to your appExisting agentConnect your AWS Strands (Python) agent to your appNew projectBuild an app and agent from scratch

Step 1 of 4Setup

## Connect your agent

Your agent keeps running as its own Python service, with the AG-UI bridge from ag_ui_strands in front of it. CopilotKit reaches that service over HTTP, so nothing inside the agent changes.
    
    
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

[Read the setup guide ](https://docs.copilotkit.ai/aws-strands/quickstart)[View on GitHub](https://github.com/CopilotKit/CopilotKit)Start building 
