---
url: https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/a2ui/
title: A2UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:20:28.731993+00:00
---

# A2UI

> Source: https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/a2ui/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMS Agent Harness (.NET)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ms-agent-harness-dotnet)[Quickstart](https://docs.copilotkit.ai/ms-agent-harness-dotnet/quickstart)[Build with agents](https://docs.copilotkit.ai/ms-agent-harness-dotnet/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ms-agent-harness-dotnet/frontend-tools)

Generative UI

Controlled

Declarative

[A2UI](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/a2ui)

[Dynamic Schema A2UI](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/a2ui/dynamic-schema)[Fixed Schema A2UI](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/a2ui/fixed-schema)

[JSON Render](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/json-render)[Hashbrown](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/hashbrown)

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ms-agent-harness-dotnet/webmcp)

Agent capabilities

MS Agent Harness (.NET)

[Sub-agents](https://docs.copilotkit.ai/ms-agent-harness-dotnet/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ms-agent-harness-dotnet/learning)

[User Memories](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/ms-agent-harness-dotnet/telemetry)[Community frameworks](https://docs.copilotkit.ai/ms-agent-harness-dotnet/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

A2UI

Generative UIDeclarativeA2UI

# A2UI

Render rich, declarative UI surfaces from your agent using the A2UI protocol.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

[A2UI](https://a2ui.org) (Agent-to-UI) is a declarative Generative UI specification, led by Google with CopilotKit as a launch and design partner. It lets your agent render structured UI components through a JSON-based schema instead of plain text: cards, rows, columns, badges, and price tags, all composed from a catalog of components you (or the platform) define.

You can design and preview A2UI schemas visually using the [A2UI Composer](https://a2ui-composer.ag-ui.com/).

**Free course:** See this pattern built end-to-end in [Build Interactive Agents with Generative UI](https://www.deeplearning.ai/short-courses/build-interactive-agents-with-generative-ui/), a free DeepLearning.AI short course taught by CopilotKit's CEO covering the full Generative UI spectrum (Controlled, Declarative, and Open-Ended).

## The two approaches#

CopilotKit ships two complementary A2UI approaches:

  * **[Dynamic Schema](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/a2ui/a2ui/dynamic-schema)** : a secondary LLM generates both the schema _and_ the data. Maximum flexibility, so the agent can produce any UI for any prompt.

  * **[Fixed Schema](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/a2ui/a2ui/fixed-schema)** : the component tree is authored ahead of time as JSON. The agent only streams _data_ into the data model at runtime. Fastest, with no LLM schema generation.




Both approaches share the same A2UI wire protocol and the same frontend renderer. The difference is _where the schema comes from_ and _how data reaches the client_.

## How it works#

Every A2UI surface is assembled from three operations emitted by the agent and consumed by the frontend renderer:

  1. **`createSurface`** initializes the surface with its catalog and must come first.
  2. **`updateComponents`** defines the component tree (the schema) for the surface.
  3. **`updateDataModel`** supplies the data that populates the components via JSON Pointer paths.



The CopilotKit Python SDK provides helpers for each:
    
    
    from copilotkit import a2ui
    
    a2ui.create_surface(surface_id, catalog_id=...)
    a2ui.update_components(surface_id, components)
    a2ui.update_data_model(surface_id, {"items": data})
    a2ui.render(operations=[...])  # wraps in a2ui_operations and serializes

## Setup#

A2UI turns on in one of two ways. Most apps use the first.

### Pass a catalog on the provider (recommended)#

Pass an A2UI catalog to the `<CopilotKit>` provider. The catalog tells the renderer which components your agent can draw, and it does two things for you automatically: it enables A2UI and it injects the A2UI tool into your agent. No `a2ui` block on the runtime is required.

app/page.tsx
    
    
    import { CopilotKit } from "@copilotkit/react-core/v2";
    
    <CopilotKit runtimeUrl="/api/copilotkit" a2ui={{ catalog: myCatalog }}>
      {children}
    </CopilotKit>;

### Enable on the runtime without a catalog#

If you do not pass a catalog, enable A2UI on the runtime instead. `a2ui: true` applies the middleware so the surfaces your agent emits are rendered; add `injectA2UITool: true` to also inject the render tool so the agent can generate surfaces dynamically:

app/api/copilotkit/[[...slug]]/route.ts
    
    
    import { CopilotRuntime, InMemoryAgentRunner } from "@copilotkit/runtime/v2";
    
    const runtime = new CopilotRuntime({
      agents: { default: myAgent },
      a2ui: { injectA2UITool: true },
      runner: new InMemoryAgentRunner(),
    });

The middleware handles the wire protocol automatically, intercepting tool results that contain A2UI operations and rendering them as rich surfaces in the chat.

With neither a catalog on the provider nor `a2ui` on the runtime, A2UI surfaces will not render. The operations fall through as plain tool results.

### What gets injected#

When injection is on, the runtime adds a tool named `generate_a2ui` to your agent. Calling it runs a secondary LLM, a subagent, that designs the full A2UI surface (components, layout, and data) from your catalog, then streams it into the chat. You do not write this tool yourself. See [Dynamic Schema](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/a2ui/a2ui/dynamic-schema) for the full flow.

### Customize or opt out#

To take control instead of relying on auto-inject, set `injectA2UITool: false` and provide the tool yourself with the AG-UI factory (`get_a2ui_tools()` in Python, `getA2UITools()` in TypeScript), where you set the model, default catalog id, and more. An explicit `injectA2UITool: false` always wins, even when a catalog is present. This is also how the [Fixed Schema](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/a2ui/a2ui/fixed-schema) approach works: your agent owns a data-only tool and no subagent is injected.

## Choose your approach#

### [Dynamic SchemaA secondary LLM generates both the schema and data. Any UI from any prompt.](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/a2ui/a2ui/dynamic-schema)### [Fixed SchemaPre-authored JSON schema, agent streams data. Fastest path to production-quality UI.](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/a2ui/a2ui/fixed-schema)

### On this page

What is this?The two approachesHow it worksSetupPass a catalog on the provider (recommended)Enable on the runtime without a catalogWhat gets injectedCustomize or opt outChoose your approach
