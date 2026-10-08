---
url: https://docs.copilotkit.ai/deepagents/generative-ui/a2ui/dynamic-schema/
title: Dynamic Schema A2UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:59:59.127884+00:00
---

# Dynamic Schema A2UI

> Source: https://docs.copilotkit.ai/deepagents/generative-ui/a2ui/dynamic-schema/

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

Dynamic Schema A2UI

Generative UIDeclarativeA2UI

# Dynamic Schema A2UI

LLM-generated A2UI — a secondary LLM creates both the schema and data from any prompt.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

In the dynamic-schema approach, a secondary LLM generates the entire UI — schema, data, and layout — based on the conversation context. It's the most flexible A2UI flavor: the agent can render any UI for any request without pre-defined schemas.

## How it works#

  1. The primary LLM decides to call `generate_a2ui`
  2. Inside the tool, a secondary LLM generates a `render_a2ui` tool call with components, data, and layout
  3. The tool call arguments stream through LangGraph as `TOOL_CALL_ARGS` events
  4. The A2UI middleware intercepts these events and renders cards progressively as they stream in



## Frontend / runtime#

Enable A2UI on your `CopilotRuntime` with `injectA2UITool: true`:

app/api/copilotkit/route.ts
    
    
    const runtime = new CopilotRuntime({
      agents: { default: myAgent },
      a2ui: {
        injectA2UITool: true,
      },
    });

`injectA2UITool: true` is the single switch: it forwards the decision to the agent so the A2UI tool is injected. Set it to `false` to turn A2UI off entirely — nothing is injected and no surfaces render.

Register your component catalog on the provider so the LLM knows what it can draw (see [Bring Your Own Catalog](https://docs.copilotkit.ai/generative-ui/a2ui/dynamic-schema) for the catalog `definitions` / `renderers` / `createCatalog` split):

frontend/src/app/page.tsx
    
    
    <CopilotKit a2ui={{ catalog: myCatalog }}>
      {/* ... */}
    </CopilotKit>

## Backend#

Just add `CopilotKitMiddleware` — it auto-injects `generate_a2ui` (built from your agent's own model) when `injectA2UITool` is on, and executes it:

agent/a2ui_dynamic.py
    
    
    from copilotkit import CopilotKitMiddleware
    from deepagents import create_deep_agent
    from langchain_openai import ChatOpenAI
    
    graph = create_deep_agent(
        model=ChatOpenAI(model="gpt-5.4"),
        tools=[],
        middleware=[CopilotKitMiddleware()],
        system_prompt=(
            "Whenever a response would benefit from a rich visual — a dashboard, "
            "KPI summary, card layout, or chart — call `generate_a2ui` to draw it. "
            "Keep chat replies to one short sentence and let the UI do the talking."
        ),
    )

The system prompt can be used to tell the model _when_ to draw; the middleware supplies and runs the tool.

## Progressive streaming#

The secondary LLM's `render_a2ui` tool call streams through LangGraph as `TOOL_CALL_ARGS` events. The A2UI middleware:

  1. Extracts the `components` array as it streams — waits for the full schema before rendering
  2. Extracts `surfaceId` and `root` from the partial JSON
  3. Once the schema is complete, emits `createSurface` \+ `updateComponents`
  4. Extracts complete `items` objects progressively and emits `updateDataModel` for each
  5. Cards appear one by one as data streams in



## Built-in progress indicator#

CopilotKit includes a built-in progress indicator that shows while the schema is being generated. It appears automatically and hides once data items start streaming.

To replace it with a custom component, see the [Advanced — Custom A2UI Progress Renderer](https://docs.copilotkit.ai/deepagents/generative-ui/a2ui/dynamic-schema/advanced#custom-a2ui-progress-renderer) guide.

### On this page

How it worksFrontend / runtimeBackendProgressive streamingBuilt-in progress indicator
