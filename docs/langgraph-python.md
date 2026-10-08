---
url: https://docs.copilotkit.ai/langgraph-python/
title: Introduction
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:06:55.016342+00:00
---

# Introduction

> Source: https://docs.copilotkit.ai/langgraph-python/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-python)[Quickstart](https://docs.copilotkit.ai/langgraph-python/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/langgraph-python/webmcp)

Agent capabilities

LangGraph (Python)

[Sub-agents](https://docs.copilotkit.ai/langgraph-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/langgraph-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/langgraph-python/learning)

[User Memories](https://docs.copilotkit.ai/langgraph-python/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/langgraph-python/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/langgraph-python/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/langgraph-python/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/langgraph-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/langgraph-python/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/langgraph-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/langgraph-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

CopilotKit + LangGraph

# Bring your LangGraph agents  
into any app

CopilotKit is an open-source framework that connects your app to LangGraph agents. Give your agents chat, generative UI, human-in-the-loop, AG-UI Streams, Automatic Learning and more.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

[Quickstart](https://docs.copilotkit.ai/langgraph-python/quickstart)

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

Your nodes return state updates and tool calls as they run. CopilotKit streams both to the browser by default and renders them as React components your users watch update while the graph works.

[Read the docs ](https://docs.copilotkit.ai/langgraph-python/generative-ui)

### Human-in-the-loop

A node calls interrupt() and stops mid-execution. CopilotKit catches that event, renders your own UI for the decision, and resumes the graph with the answer.

[Read the docs ](https://docs.copilotkit.ai/langgraph-python/human-in-the-loop/interrupt-flow)

### Shared state

Your graph carries one state object from node to node. CopilotKit mirrors it into your app and back, so a user edit and a node write land in the same place.

[Read the docs ](https://docs.copilotkit.ai/langgraph-python/shared-state)

Chat surfaces, headless UI, frontend tools and subagent flows work with LangGraph too. [And more](https://docs.copilotkit.ai/langgraph-python/build-with-agents)

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

Existing projectAdd a LangGraph (Python) agent to your appExisting agentConnect your LangGraph (Python) agent to your appNew projectBuild an app and agent from scratch

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
    

[Read the setup guide ](https://docs.copilotkit.ai/langgraph-python/quickstart)

## Already have LangGraph conversations?

When you add a user-facing app to an existing LangGraph agent, your users may need to open and continue conversations they already started. [CopilotKit Intelligence](https://docs.copilotkit.ai/intelligence/overview) can import supported LangGraph history as threads so your app does not start with an empty thread list.

The importer reads LangGraph Server, LangGraph Platform, or LangSmith Deployment thread and run APIs. It does not import standalone LangChain message stores, LangSmith traces, or embedded checkpointers that are not exposed through those APIs.

Import history once; future CopilotKit-mediated runs synchronize with Intelligence and continue through LangGraph's native persistence path when your durable checkpointer or Platform deployment remains configured. This is not a continuous mirror of runs made outside CopilotKit.

[Import and synchronize LangGraph threads](https://docs.copilotkit.ai/langgraph-python/threads-import) for source setup, agent mapping, and thread continuity.

[View on GitHub](https://github.com/CopilotKit/CopilotKit)Start building 
