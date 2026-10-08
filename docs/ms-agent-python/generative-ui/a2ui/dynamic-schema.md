---
url: https://docs.copilotkit.ai/ms-agent-python/generative-ui/a2ui/dynamic-schema/
title: Dynamic Schema A2UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:22:06.569235+00:00
---

# Dynamic Schema A2UI

> Source: https://docs.copilotkit.ai/ms-agent-python/generative-ui/a2ui/dynamic-schema/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMS Agent Framework (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ms-agent-python)[Quickstart](https://docs.copilotkit.ai/ms-agent-python/quickstart)[Build with agents](https://docs.copilotkit.ai/ms-agent-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ms-agent-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ms-agent-python/frontend-tools)

Generative UI

Controlled

Declarative

[A2UI](https://docs.copilotkit.ai/ms-agent-python/generative-ui/a2ui)

[Dynamic Schema A2UI](https://docs.copilotkit.ai/ms-agent-python/generative-ui/a2ui/dynamic-schema)[Fixed Schema A2UI](https://docs.copilotkit.ai/ms-agent-python/generative-ui/a2ui/fixed-schema)

[JSON Render](https://docs.copilotkit.ai/ms-agent-python/generative-ui/json-render)[Hashbrown](https://docs.copilotkit.ai/ms-agent-python/generative-ui/hashbrown)

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ms-agent-python/webmcp)

Agent capabilities

Microsoft Agent Framework

[Sub-agents](https://docs.copilotkit.ai/ms-agent-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ms-agent-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ms-agent-python/learning)

[User Memories](https://docs.copilotkit.ai/ms-agent-python/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ms-agent-python/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ms-agent-python/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ms-agent-python/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ms-agent-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ms-agent-python/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ms-agent-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/ms-agent-python/community-frameworks)

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
  3. The tool call arguments stream through the agent as `TOOL_CALL_ARGS` events
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

## Backend — auto-injected tool#

The agent binds no A2UI tool of its own. When `injectA2UITool` is on, the `agent-framework-ag-ui` adapter auto-injects `generate_a2ui` (built from your agent's own model) and executes it:

src/agents/a2ui_dynamic.py
    
    
    from agent_framework import Agent
    from agent_framework_ag_ui import AgentFrameworkAgent
    
    base_agent = Agent(
        client=chat_client,
        name="declarative_gen_ui_agent",
        instructions=(
            "Whenever a response would benefit from a rich visual — a dashboard, "
            "KPI summary, card layout, or chart — call `generate_a2ui` to draw it. "
            "Keep chat replies to one short sentence and let the UI do the talking."
        ),
    )
    
    # No A2UI tool here — the adapter auto-injects `generate_a2ui` when
    # `injectA2UITool` is on. Binding one yourself would suppress auto-injection.
    agent = AgentFrameworkAgent(agent=base_agent)

The system prompt can be used to tell the model _when_ to draw; the adapter supplies and runs the tool.

## Backend — recovery and other policy#

The auto-inject path takes an optional `a2ui_config` on the endpoint — a backend policy dict the adapter reads when it injects the tool. This is where the error-recovery demo pins the validate→retry loop's attempt cap (and where MAF's upstream recovery example puts its config). The agent stays a plain agent; only the endpoint config changes:

src/agents/agent_server.py
    
    
    add_agent_framework_fastapi_endpoint(
        app=app,
        agent=a2ui_recovery_agent,
        path="/a2ui_recovery",
        a2ui_config={
            "recovery": {"maxAttempts": 3},
            "default_catalog_id": "declarative-gen-ui-catalog",
        },
    )

`a2ui_config` accepts the same params the adapter uses under the hood:

  * **`recovery`** — the validate→retry loop config, e.g. `{"maxAttempts": 3}`. When every attempt is invalid the tool returns a graceful `a2ui_recovery_exhausted` fallback.
  * **`default_catalog_id`** — binds generated surfaces to your catalog (BYOC). Catalog ownership stays with the host; the model never picks it.
  * **`guidelines`** — optional prompt knobs for the render sub-agent (which components exist and how to compose them).



## Progressive streaming#

The secondary LLM's `render_a2ui` tool call streams through the agent as `TOOL_CALL_ARGS` events. The A2UI middleware:

  1. Extracts the `components` array as it streams — waits for the full schema before rendering
  2. Extracts `surfaceId` and `root` from the partial JSON
  3. Once the schema is complete, emits `createSurface` \+ `updateComponents`
  4. Extracts complete `items` objects progressively and emits `updateDataModel` for each
  5. Cards appear one by one as data streams in



## Built-in progress indicator#

CopilotKit includes a built-in progress indicator that shows while the schema is being generated. It appears automatically and hides once data items start streaming.

To replace it with a custom component, see the [Advanced — Custom A2UI Progress Renderer](https://docs.copilotkit.ai/ms-agent-python/generative-ui/a2ui/dynamic-schema/advanced#custom-a2ui-progress-renderer) guide.

### On this page

How it worksFrontend / runtimeBackend — auto-injected toolBackend — recovery and other policyProgressive streamingBuilt-in progress indicator
