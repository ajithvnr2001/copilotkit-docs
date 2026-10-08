---
url: https://docs.copilotkit.ai/angular/langgraph-typescript/
title: Introduction
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:50:25.198878+00:00
---

# Introduction

> Source: https://docs.copilotkit.ai/angular/langgraph-typescript/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendAngularAgent backendLangGraph (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/angular/langgraph-typescript)[Quickstart](https://docs.copilotkit.ai/angular/langgraph-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/angular/langgraph-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/langgraph-typescript/intelligence/overview)

Basics

Generative UI

Interactivity

[WebMCP](https://docs.copilotkit.ai/angular/langgraph-typescript/webmcp)

Agent capabilities

LangGraph (TypeScript)

[Sub-agents](https://docs.copilotkit.ai/angular/langgraph-typescript/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/angular/langgraph-typescript/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/angular/langgraph-typescript/learning)

[User Memories](https://docs.copilotkit.ai/angular/langgraph-typescript/intelligence/memories)[Standalone collector](https://docs.copilotkit.ai/angular/langgraph-typescript/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/angular/langgraph-typescript/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/angular/langgraph-typescript/intelligence/analytics)[Channels](https://docs.copilotkit.ai/angular/langgraph-typescript/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/angular/langgraph-typescript/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/langgraph-typescript/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

CopilotKit + LangGraph

# Bring your LangGraph agents  
into any app

CopilotKit is an open-source framework that connects your app to LangGraph agents. Give your agents chat, generative UI, human-in-the-loop, AG-UI Streams, Automatic Learning and more.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

[Quickstart](https://docs.copilotkit.ai/angular/langgraph-typescript/quickstart)

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

LangGraph and CopilotKit running together, in the React frontend. Every demo below is the same integration with one capability turned on.

## Build with LangGraph

LangGraph gives you the graph: nodes, edges, one state object, and interrupts that stop a run mid-node. What it does not give you is the surface. Somewhere for the conversation to happen, a way to show the run while it is running, and a moment for a person to step in. Each capability below builds on something your graph already does.

### Generative UI

Your nodes return state updates and tool calls as they run. CopilotKit streams both to the browser by default and renders them as Angular components your users watch update while the graph works.

[Read the docs ](https://docs.copilotkit.ai/angular/langgraph-typescript/guides/frontend-tools-generative-ui)[Live demo ](https://showcase.copilotkit.ai/angular/langgraph-typescript/gen-ui-tool-based)

### Human-in-the-loop

A node calls interrupt() and stops mid-execution. CopilotKit catches that event, renders your own UI for the decision, and resumes the graph with the answer.

[Read the docs ](https://docs.copilotkit.ai/angular/langgraph-typescript/guides/human-in-the-loop)[Live demo ](https://showcase.copilotkit.ai/angular/langgraph-typescript/hitl-in-chat)

### Shared state

Your graph carries one state object from node to node. CopilotKit mirrors it into your app and back, so a user edit and a node write land in the same place.

[Read the docs ](https://docs.copilotkit.ai/angular/langgraph-typescript/guides/shared-state)[Live demo ](https://showcase.copilotkit.ai/angular/langgraph-typescript/shared-state-read-write)

Chat surfaces, headless UI, frontend tools and subagent flows work with LangGraph too. [And more](https://docs.copilotkit.ai/langgraph/build-with-agents)

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

Existing projectAdd a LangGraph (TypeScript) agent to your appExisting agentConnect your LangGraph (TypeScript) agent to your appNew projectBuild an app and agent from scratch

Step 1 of 4Setup

## Connect your agent

Your graph stays where it runs today: LangGraph Platform, LangSmith, or your own FastAPI service. CopilotKit reaches it over AG-UI, so nothing inside the graph changes.
    
    
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
    

[Read the setup guide ](https://docs.copilotkit.ai/langgraph/quickstart)[Bring your LangGraph agents to productionAdd persistent threads, observability, and the inspector with CopilotKit Intelligence.Create a free account](https://ssr-placeholder.invalid/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_langgraph_overview&utm_frontend=angular&utm_backend=langgraph-typescript)[View on GitHub](https://github.com/CopilotKit/CopilotKit)Start building 
