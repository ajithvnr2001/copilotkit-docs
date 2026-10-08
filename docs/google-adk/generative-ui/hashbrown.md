---
url: https://docs.copilotkit.ai/google-adk/generative-ui/hashbrown/
title: Hashbrown
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:03:01.419753+00:00
---

# Hashbrown

> Source: https://docs.copilotkit.ai/google-adk/generative-ui/hashbrown/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendGoogle ADK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/google-adk)[Quickstart](https://docs.copilotkit.ai/google-adk/quickstart)[Build with agents](https://docs.copilotkit.ai/google-adk/build-with-agents)[Intelligence](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/google-adk/frontend-tools)

Generative UI

Controlled

Declarative

[A2UI](https://docs.copilotkit.ai/google-adk/generative-ui/a2ui)

[JSON Render](https://docs.copilotkit.ai/google-adk/generative-ui/json-render)[Hashbrown](https://docs.copilotkit.ai/google-adk/generative-ui/hashbrown)

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/google-adk/webmcp)

Agent capabilities

Google ADK

[Sub-agents](https://docs.copilotkit.ai/google-adk/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/google-adk/learning)

[User Memories](https://docs.copilotkit.ai/google-adk/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/google-adk/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/google-adk/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/google-adk/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/google-adk/intelligence/analytics)[Channels](https://docs.copilotkit.ai/google-adk/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/google-adk/telemetry)[Community frameworks](https://docs.copilotkit.ai/google-adk/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Hashbrown

Generative UIDeclarative

# Hashbrown

Bring your own component library. Have the agent stream structured output and let Hashbrown's progressive JSON parser render it as React components in real time.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

byoc_agents.py

page.tsx

route.ts
    
    
    """Agents backing the BYOC (Bring Your Own Component-renderer) demos.
    
    Both byoc-hashbrown and byoc-json-render share one ADK `byoc_agent`. The
    registry pins both to the same instance (see `registry.py`):
    
        "byoc_hashbrown": AgentSpec(byoc_agent),
        "byoc_json_render": AgentSpec(byoc_agent),
    
    The LP sibling splits the two into separate graphs with distinct system
    prompts (see `showcase/integrations/langgraph-python/src/agents/`):
    
      - `byoc_hashbrown_agent.py` + `byoc_hashbrown_prompt.py` — emits
        hashbrown-shaped `{ "ui": [{"componentName": {"props": {...}}}, ...] }`
        that `@hashbrownai/react`'s `useJsonParser` streams progressively into
        the catalog kit.
      - `byoc_json_render_agent.py` — emits json-render's flat spec
        `{ "root": "<id>", "elements": { "<id>": { "type": "...", "props": {...} } } }`
        that `@json-render/react`'s `<Renderer />` paints once the JSON parses.
    
    Because the ADK registry routes both demo names to the same `byoc_agent`
    instance, the unified prompt below instructs the model to emit a single
    JSON object that contains BOTH structures (a `ui` array AND a flat
    `root`/`elements` map describing the same dashboard). Each frontend
    renderer extracts only the keys it cares about:
    
      - hashbrown's `useJsonParser` reads `ui[]`
      - json-render's `parseSpec` reads `root` + `elements{}`
    
    Extra top-level keys are tolerated by both parsers, so a single response
    drives both demos without per-route divergence. This sidesteps the
    registry split that LP uses while keeping the agent's wire output
    LP-equivalent on each frontend.
    
    For future maintainers who do want to split into two LlmAgents matching
    LP, additional agent modules can be added and `registry.py` updated to
    reference them per route — the existing exports below keep this option
    open.
    """
    
    from __future__ import annotations
    
    from google.adk.agents import LlmAgent
    from google.genai import types
    
    from agents.shared_chat import get_model, stop_on_terminal_text
    
    
    # ─── System prompt ────────────────────────────────────────────────────────────
    # Mirrors LP's `byoc_hashbrown_prompt.BYOC_HASHBROWN_SYSTEM_PROMPT` and
    # `byoc_json_render_agent.SYSTEM_PROMPT`, fused into a single instruction that
    # emits both wire formats in one JSON envelope.
    #
    # Why fused: the ADK registry pins both byoc-hashbrown and byoc-json-render
    # demo routes to the same `byoc_agent` instance. A single agent cannot
    # selectively emit one of two mutually-exclusive top-level shapes without
    # knowing which route it serves. Producing both keys at the top level of one
    # JSON response is the cleanest LP-aligned way to make BOTH frontends work:
    #
    #   - `@hashbrownai/react`'s `useJsonParser` only reads `ui[]` — extra
    #     sibling keys are ignored.
    #   - `@json-render/react`'s `parseSpec` only reads `root` + `elements{}` —
    #     extra sibling keys are ignored.
    #
    # Both arrays/maps must describe the SAME dashboard so the rendered output
    # is visually equivalent across the two demo pages.
    _BYOC_SYSTEM_PROMPT = """\
    You are a sales analytics assistant that replies by emitting a single JSON
    object consumed by two streaming UI parsers on the frontend.
    
    ALWAYS respond with a single JSON object containing BOTH of the following
    top-level keys describing the SAME dashboard:
    
    1. A "ui" array (hashbrown wire format):
    
       {
         "ui": [
           { <componentName>: { "props": { ... } } },
           ...
         ]
       }
    
    2. A flat element map ("root" + "elements"; json-render wire format):
    
       {
         "root": "<id of the root element>",
         "elements": {
           "<id>": {
             "type": "<component name>",
             "props": { ... component-specific props ... },
             "children": [ "<id>", ... ]
           },
           ...
         }
       }
    
    The full response is exactly one JSON object with `ui`, `root`, and
    `elements` all at the top level — no code fences, no preface, no
    explanation outside the JSON. The response MUST be valid JSON.
    
    Available components for the `ui` array (hashbrown names + prop schemas):
    
    - "metric": { "props": { "label": string, "value": string } }
        A KPI card. `value` is a pre-formatted string like "$1.2M" or "248".
    
    - "pieChart": { "props": { "title": string, "data": string } }
        A donut chart. `data` is a JSON-encoded STRING (embedded JSON) of an
        array of {label, value} objects with at least 3 segments, e.g.
        "data": "[{\\"label\\":\\"Enterprise\\",\\"value\\":600000}]".
    
    - "barChart": { "props": { "title": string, "data": string } }
        A vertical bar chart. `data` is a JSON-encoded STRING of an array of
        {label, value} objects with at least 3 bars, typically time-ordered.
    
    - "dealCard": { "props": { "title": string, "stage": string, "value": number } }
        A single sales deal. `stage` MUST be one of: "prospect", "qualified",
        "proposal", "negotiation", "closed-won", "closed-lost". `value` is a
        raw number (no currency symbol or comma).
    
    - "Markdown": { "props": { "children": string } }
        Short explanatory text. Use for section headings and brief summaries.
        Standard markdown is supported in `children`.
    
    Available components for `elements` (json-render PascalCase types):
    
    - MetricCard
      props: { "label": string, "value": string, "trend": string | null }
      Example trend strings: "+12% vs last quarter", "-3% vs last month", null.
    
    - BarChart
      props: {
        "title": string,
        "description": string | null,
        "data": [ { "label": string, "value": number }, ... ]
      }
      Note: `data` is a real JSON array (NOT a JSON-encoded string).
    
    - PieChart
      props: {
        "title": string,
        "description": string | null,
        "data": [ { "label": string, "value": number }, ... ]
      }
    
    Rules:
    - Always produce plausible sample data when the user asks for a dashboard or
      chart — do not refuse for lack of data.
    - Prefer 3-6 rows of data in charts; keep labels short.
    - Use "Markdown" in `ui[]` for short headings between visual components.
      Do not emit long prose. The `elements` map does not need a Markdown twin.
    - Do not emit components that are not listed above.
    - `data` props on hashbrown's `pieChart`/`barChart` MUST be a JSON STRING.
      `data` props on json-render's `BarChart`/`PieChart` MUST be a real JSON
      array of objects.
    - The `ui[]` and `elements{}` representations MUST describe the same
      dashboard (same metric values, same chart titles, same segment labels).
      Use realistic sales-domain values (revenue, pipeline, conversion,
      categories, months) — the demo is a sales dashboard.
    - Every id referenced by `root` or any `children` array must exist as a
      key in `elements`. For multi-component dashboards, pick any element as
      `root` and list the others as its `children`.
    
    Example response (sales dashboard, both wire formats describing the same
    two-tile + chart layout):
    
    {
      "ui": [
        { "Markdown": { "props": { "children": "## Q4 Sales Summary" } } },
        { "metric": { "props": { "label": "Total Revenue", "value": "$1.2M" } } },
        { "metric": { "props": { "label": "New Customers", "value": "248" } } },
        { "pieChart": { "props": { "title": "Revenue by Segment", "data": "[{\\"label\\":\\"Enterprise\\",\\"value\\":600000},{\\"label\\":\\"SMB\\",\\"value\\":400000},{\\"label\\":\\"Startup\\",\\"value\\":200000}]" } } },
        { "barChart": { "props": { "title": "Monthly Revenue", "data": "[{\\"label\\":\\"Oct\\",\\"value\\":350000},{\\"label\\":\\"Nov\\",\\"value\\":400000},{\\"label\\":\\"Dec\\",\\"value\\":450000}]" } } }
      ],
      "root": "revenue-metric",
      "elements": {
        "revenue-metric": {
          "type": "MetricCard",
          "props": {
            "label": "Total Revenue",
            "value": "$1.2M",
            "trend": "+18% vs Q3"
          },
          "children": ["revenue-pie", "revenue-bar"]
        },
        "revenue-pie": {
          "type": "PieChart",
          "props": {
            "title": "Revenue by Segment",
            "description": "Share by customer segment",
            "data": [
              { "label": "Enterprise", "value": 600000 },
              { "label": "SMB", "value": 400000 },
              { "label": "Startup", "value": 200000 }
            ]
          }
        },
        "revenue-bar": {
          "type": "BarChart",
          "props": {
            "title": "Monthly Revenue",
            "description": "Revenue by month across Q4",
            "data": [
              { "label": "Oct", "value": 350000 },
              { "label": "Nov", "value": 400000 },
              { "label": "Dec", "value": 450000 }
            ]
          }
        }
      }
    }
    
    If the user asks something off-topic ("tell me a joke", "what is 2+2"),
    you may reply with a single JSON object whose `ui` array contains a
    single Markdown component answering the question, and an `elements` map
    that mirrors that Markdown as a MetricCard with `label` = "Reply" and
    `value` = your answer. The renderers will display these as appropriate.
    """
    
    
    # ─── Agents ───────────────────────────────────────────────────────────────────
    # `byoc_agent` is the registry-bound instance (both demo routes pin to it).
    # `byoc_hashbrown_agent` / `byoc_json_render_agent` are LP-parity aliases
    # for future split, but registry.py currently uses only `byoc_agent`.
    _BYOC_INSTRUCTION = _BYOC_SYSTEM_PROMPT
    
    
    byoc_agent = LlmAgent(
        name="ByocAgent",
        model=get_model(),
        instruction=_BYOC_INSTRUCTION,
        # No backend tools — the prompt produces all dashboard data inline so
        # the streaming JSON parsers on the frontend can rebuild the UI
        # progressively. LP's sibling agents (byoc_hashbrown_agent,
        # byoc_json_render_agent) follow the same `tools=[]` pattern.
        tools=[],
        # Force Gemini's JSON-object output mode. LP's sibling agents pass
        # `response_format={"type": "json_object"}` to OpenAI for the same
        # reason: the streaming frontend parsers (`@hashbrownai/react`'s
        # `useJsonParser` and `@json-render/react`'s `parseSpec`) bail to
        # `null` on any non-JSON prefix (code fences, prose preamble, etc.),
        # so leaving the model free to wander out of JSON leaves the renderer
        # empty in practice. `response_mime_type="application/json"` is
        # Gemini's equivalent — it constrains output to a single JSON value.
        # `temperature=0.2` matches LP's `byoc_json_render_agent` and keeps
        # the schema-adherence tight while still allowing some variation in
        # sample data.
        generate_content_config=types.GenerateContentConfig(
            response_mime_type="application/json",
            temperature=0.2,
        ),
        after_model_callback=stop_on_terminal_text,
    )
    
    
    # LP-parity exports. These mirror the split in
    # `showcase/integrations/langgraph-python/src/agents/` so that future ADK
    # registry updates can wire each demo route to its own LlmAgent.
    byoc_hashbrown_agent = byoc_agent
    byoc_json_render_agent = byoc_agent
    

You have a chat surface and you want the agent to draw a dashboard, not just describe one in prose. By the end of this guide, the agent will stream a structured output object, [`@hashbrownai/react`](https://www.npmjs.com/package/@hashbrownai/react)'s progressive JSON parser will hand each finished slice to your renderer as it arrives, and the user sees the dashboard fill in live.

## When to use this#

  * **Streaming dashboards** where partial state should render before the full payload arrives.
  * **Agents authoring structured UI** where the output is JSON-shaped, not free text.
  * **Cases where you already use Hashbrown** for UI generation elsewhere in your stack.



If you'd rather work with an explicit catalog of registered components rather than streaming a JSON tree, see the sibling page [JSON Render](https://docs.copilotkit.ai/google-adk/generative-ui/json-render) for the same scenario implemented with `@json-render/react`.

## Frontend#

The integration point is `<CopilotChat>`'s `messageView.assistantMessage` slot. Replace the default assistant-message renderer with a Hashbrown-backed one, and the chat takes care of everything else:

frontend/src/app/page.tsx
    
    
    import {
      CopilotKit,
      CopilotChat,
      useConfigureSuggestions,
    } from "@copilotkit/react-core/v2";
    import { HashBrownAssistantMessage } from "./hashbrown-renderer";
    
    export default function ByocHashbrownDemo() {
      useConfigureSuggestions({
        suggestions: [
          { title: "Sales overview", message: "Show me a sales dashboard." },
          { title: "Region split", message: "Break down sales by region." },
        ],
        available: "always",
      });
    
      return (
        <CopilotKit runtimeUrl="/api/copilotkit-byoc-hashbrown" agent="byoc_hashbrown">
          <CopilotChat
            messageView={{ assistantMessage: HashBrownAssistantMessage }}
          />
        </CopilotKit>
      );
    }

The custom renderer is where Hashbrown earns its keep. `useJsonParser` consumes the streaming text content of an assistant message and emits typed JSON values as they parse; `useUiKit` resolves component names against your catalog and renders them with their props:

frontend/src/app/hashbrown-renderer.tsx
    
    
    import { useJsonParser, useUiKit } from "@hashbrownai/react";
    import { MetricCard } from "./metric-card";
    import { PieChart, BarChart } from "./charts";
    
    const catalog = {
      MetricCard,
      PieChart,
      BarChart,
    };
    
    export function HashBrownAssistantMessage({ message }: { message: AssistantMessage }) {
      const parsed = useJsonParser(message.content ?? "");
      const ui = useUiKit({ catalog, value: parsed });
      return <div className="space-y-3">{ui}</div>;
    }

Each component in the catalog is just a regular React component. The catalog acts as a typed allowlist: anything the agent emits that isn't in the catalog won't render, so the agent can't draw arbitrary HTML into the page.

## Backend#

The agent's job is to stream structured output, not text. How you do that depends on your framework, but the shape is always the same: emit a JSON object at the top level of the assistant message, where each child references a component name and props matching the catalog.

example agent output (streaming)
    
    
    {
      "type": "MetricCard",
      "title": "Total revenue",
      "value": 184302,
      "delta": 0.07
    }

Or a tree:
    
    
    {
      "type": "Stack",
      "children": [
        { "type": "MetricCard", "title": "Total revenue", "value": 184302 },
        { "type": "BarChart",   "data": [...] }
      ]
    }

Hashbrown's parser tolerates partial JSON, so the user sees `MetricCard` resolve before `BarChart` even starts streaming.

## Comparing the two patterns#

Both `byoc-hashbrown` and [`byoc-json-render`](https://docs.copilotkit.ai/google-adk/generative-ui/json-render) solve the same problem (agent-authored structured UI, rendered through a typed catalog), with two different rendering libraries. Pick whichever you already use elsewhere — the agent contract is the same shape; the React glue is what changes.

### On this page

When to use thisFrontendBackendComparing the two patterns
