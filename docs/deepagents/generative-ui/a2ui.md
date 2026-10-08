---
url: https://docs.copilotkit.ai/deepagents/generative-ui/a2ui/
title: Overview
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:59:59.022165+00:00
---

# Overview

> Source: https://docs.copilotkit.ai/deepagents/generative-ui/a2ui/

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

[A2UI](https://docs.copilotkit.ai/deepagents/generative-ui/a2ui)

[Dynamic Schema A2UI](https://docs.copilotkit.ai/deepagents/generative-ui/a2ui/dynamic-schema)[Fixed Schema A2UI](https://docs.copilotkit.ai/deepagents/generative-ui/a2ui/fixed-schema)

[JSON Render](https://docs.copilotkit.ai/deepagents/generative-ui/json-render)[Hashbrown](https://docs.copilotkit.ai/deepagents/generative-ui/hashbrown)

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

A2UI

Generative UIDeclarativeA2UI

# Overview

Render rich, declarative UI surfaces from your LangGraph agent using the A2UI protocol.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

[A2UI](https://a2ui.org) (Agent-to-UI) is a Declarative Generative UI specification led by Google, with CopilotKit as a launch and design partner. It lets your agent render structured UI components using a JSON-based schema. Instead of sending plain text, the agent produces surfaces — cards, lists, buttons, images — that render natively in the chat.

You can design and preview A2UI schemas visually using the [A2UI Composer](https://a2ui-composer.ag-ui.com/).

## Setup#

Enable A2UI in your CopilotRuntime by adding `a2ui: true`, or pass an object to customise:

app/api/copilotkit/[[...slug]]/route.ts
    
    
    import { CopilotRuntime, InMemoryAgentRunner } from "@copilotkit/runtime/v2";
    
    // Simple — enable with defaults
    const runtime = new CopilotRuntime({
      agents: { default: myAgent },
      a2ui: true,
      runner: new InMemoryAgentRunner(),
    });
    
    // Or customise — e.g. inject a render tool into the agent
    const runtime = new CopilotRuntime({
      agents: { default: myAgent },
      a2ui: {
        injectA2UITool: true,
      },
      runner: new InMemoryAgentRunner(),
    });

This tells the runtime to apply the A2UI middleware to your agents. The middleware intercepts tool results containing A2UI operations and renders them as rich UI surfaces in the chat.

Without `a2ui` configured in your CopilotRuntime, A2UI surfaces will not render — tool results will appear as plain text.

## Approaches#

CopilotKit supports three approaches to A2UI, each with different tradeoffs:

  * **[Fixed Schema](https://docs.copilotkit.ai/deepagents/generative-ui/a2ui/fixed-schema)** — Pre-defined schema loaded from JSON. Agent provides data only. Fastest — no LLM schema generation.
  * **[Fixed Schema (Streaming)](https://docs.copilotkit.ai/deepagents/generative-ui/a2ui/fixed-schema)** — Same pre-defined schema, but cards appear one-by-one as the LLM streams data. Great for lists.
  * **[Dynamic Schema](https://docs.copilotkit.ai/deepagents/generative-ui/a2ui/dynamic-schema)** — A secondary LLM generates both the schema and data. Fully flexible — any UI from any prompt.



## When to use which?#

Approach| Schema source| Rendering| Best for  
---|---|---|---  
**Fixed Schema**|  JSON file| Instant (all at once)| Known UI patterns (flight cards, product lists)  
**Fixed Schema Streaming**|  JSON file| Progressive (card by card)| Long lists where you want immediate feedback  
**Dynamic Schema**|  LLM-generated| Progressive (card by card)| Unknown/varied UI — the agent decides what to show  
  
All three approaches use the same A2UI protocol and renderer. The difference is where the schema comes from and how data reaches the client.

## How it works#

Every A2UI v0.9 surface is built from three operations:

  1. **`createSurface`** — initializes the surface with its catalog (must come first)
  2. **`updateComponents`** — defines the component tree (the schema)
  3. **`updateDataModel`** — provides the data that populates the components



The CopilotKit Python SDK provides helpers to build these operations:
    
    
    from copilotkit import a2ui
    
    a2ui.create_surface(surface_id)
    a2ui.update_components(surface_id, components)
    a2ui.update_data_model(surface_id, {"items": data})
    a2ui.render(operations)  # wraps in a2ui_operations and serializes

Continue to one of the approach guides above to see the full implementation.

### On this page

SetupApproachesWhen to use which?How it works
