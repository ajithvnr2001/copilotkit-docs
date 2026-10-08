---
url: https://docs.copilotkit.ai/langgraph-python/generative-ui/json-render/
title: JSON Render
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:08:05.948830+00:00
---

# JSON Render

> Source: https://docs.copilotkit.ai/langgraph-python/generative-ui/json-render/

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

[A2UI](https://docs.copilotkit.ai/langgraph-python/generative-ui/a2ui)

[JSON Render](https://docs.copilotkit.ai/langgraph-python/generative-ui/json-render)[Hashbrown](https://docs.copilotkit.ai/langgraph-python/generative-ui/hashbrown)

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

JSON Render

Generative UIDeclarative

# JSON Render

Bring your own component library. Have the agent emit a JSON spec and let json-render render it against a Zod-validated catalog of React components.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

byoc_json_render_agent.py

page.tsx

json-render-renderer.tsx

registry.tsx

catalog.ts

metric-card.tsx

bar-chart.tsx

pie-chart.tsx

types.ts

suggestions.ts

route.ts
    
    
    """LangGraph agent backing the BYOC json-render demo.Emits a single JSON object shaped like `@json-render/react`'s flat specformat (`{ root, elements }`) so the frontend can feed it directly into`<Renderer />` against a Zod-validated catalog of three components —MetricCard, BarChart, PieChart.The scenario mirrors the declarative-hashbrown demo so the two BYOC rows on thedashboard are directly comparable. The only difference is the renderingtechnology; the catalog shape and suggestion prompts are identical."""from langchain.agents import create_agentfrom langchain_openai import ChatOpenAIfrom copilotkit import CopilotKitMiddlewareSYSTEM_PROMPT = """You are a sales-dashboard UI generator for a BYOC json-render demo.When the user asks for a UI, respond with **exactly one JSON object** andnothing else — no prose, no markdown fences, no leading explanation. Theobject must match this schema (the "flat element map" format consumed by`@json-render/react`):{  "root": "<id of the root element>",  "elements": {    "<id>": {      "type": "<component name>",      "props": { ... component-specific props ... },      "children": [ "<id>", ... ]    },    ...  }}Available components (use each name verbatim as "type"):- MetricCard  props: { "label": string, "value": string, "trend": string | null }  Example trend strings: "+12% vs last quarter", "-3% vs last month", null.- BarChart  props: {    "title": string,    "description": string | null,    "data": [ { "label": string, "value": number }, ... ]  }- PieChart  props: {    "title": string,    "description": string | null,    "data": [ { "label": string, "value": number }, ... ]  }Rules:1. Output **only** valid JSON. No markdown code fences. No text outside   the object.2. Every id referenced in `root` or any `children` array must be a key   in `elements`.3. For a multi-component dashboard, use a root MetricCard and list the   charts in its `children` array, OR pick any element as root and list   the others as its children. Do not emit orphan elements.4. Use realistic sales-domain values (revenue, pipeline, conversion,   categories, months) — the demo is a sales dashboard.5. `children` is optional but when present must be an array of strings.6. Never invent component types outside the three listed above.### Worked example — "Show me the sales dashboard with metrics and a revenue chart"{  "root": "revenue-metric",  "elements": {    "revenue-metric": {      "type": "MetricCard",      "props": {        "label": "Revenue (Q3)",        "value": "$1.24M",        "trend": "+18% vs Q2"      },      "children": ["revenue-bar"]    },    "revenue-bar": {      "type": "BarChart",      "props": {        "title": "Monthly revenue",        "description": "Revenue by month across Q3",        "data": [          { "label": "Jul", "value": 380000 },          { "label": "Aug", "value": 410000 },          { "label": "Sep", "value": 450000 }        ]      }    }  }}### Worked example — "Break down revenue by category as a pie chart"{  "root": "category-pie",  "elements": {    "category-pie": {      "type": "PieChart",      "props": {        "title": "Revenue by category",        "description": "Share of total revenue by product category",        "data": [          { "label": "Enterprise", "value": 540000 },          { "label": "SMB", "value": 310000 },          { "label": "Self-serve", "value": 220000 },          { "label": "Partner", "value": 170000 }        ]      }    }  }}### Worked example — "Show me monthly expenses as a bar chart"{  "root": "expense-bar",  "elements": {    "expense-bar": {      "type": "BarChart",      "props": {        "title": "Monthly expenses",        "description": "Operating expenses by month",        "data": [          { "label": "Jul", "value": 210000 },          { "label": "Aug", "value": 225000 },          { "label": "Sep", "value": 240000 }        ]      }    }  }}Respond with the JSON object only."""# Force JSON-object output mode. The frontend's `parseSpec` already# tolerates code fences and prose preamble via `extractJsonObject`, but# locking the model to JSON at the API layer removes the ambiguity# entirely — the only thing the LLM can emit is a single JSON object,# which is exactly what `<Renderer />` needs.graph = create_agent(    model=ChatOpenAI(        model="gpt-5.4",        temperature=0.2,        model_kwargs={"response_format": {"type": "json_object"}},    ),    tools=[],    middleware=[CopilotKitMiddleware()],    system_prompt=SYSTEM_PROMPT.strip(),)

You have a chat surface and you want the agent to draw a dashboard from a typed JSON spec. By the end of this guide, the agent will emit a `{ root, elements }` object, [`@json-render/react`](https://www.npmjs.com/package/@json-render/react) will validate it against a Zod-described catalog, and the user sees the dashboard render as a single React tree.

## When to use this#

  * **Structured UI with a typed contract** where the agent's output is validated against a known schema before it touches the DOM.
  * **Tolerance for prose preamble + code fences** in the agent's output (json-render's parser handles them).
  * **Cases where you already use json-render** elsewhere or prefer Zod-validated catalogs.



If you'd rather have a streaming progressive render rather than a one-shot validated render, see the sibling page [Hashbrown](https://docs.copilotkit.ai/langgraph-python/generative-ui/hashbrown) for the same scenario with `@hashbrownai/react`.

## Frontend#

The integration point is `<CopilotChat>`'s `messageView.assistantMessage` slot. Swap the default renderer for a json-render-backed one:

frontend/src/app/page.tsx
    
    
    import {
      CopilotKit,
      CopilotChat,
      useConfigureSuggestions,
    } from "@copilotkit/react-core/v2";
    import { JsonRenderAssistantMessage } from "./json-render-renderer";
    
    export default function ByocJsonRenderDemo() {
      useConfigureSuggestions({
        suggestions: [
          { title: "Sales dashboard", message: "Show me a sales dashboard." },
          { title: "Region breakdown", message: "Break down sales by region." },
        ],
        available: "always",
      });
    
      return (
        <CopilotKit runtimeUrl="/api/copilotkit-byoc-json-render" agent="byoc_json_render">
          <CopilotChat
            messageView={{ assistantMessage: JsonRenderAssistantMessage }}
          />
        </CopilotKit>
      );
    }

The custom renderer parses the streaming assistant content (tolerating partial tokens, code fences, and prose preamble), validates each element against a Zod-typed catalog, and feeds the resulting spec into `<Renderer />`:

frontend/src/app/json-render-renderer.tsx
    
    
    import { Renderer } from "@json-render/react";
    import { catalog } from "./registry";
    
    export function JsonRenderAssistantMessage({ message }: { message: AssistantMessage }) {
      const spec = parseSpec(message.content ?? "");
      if (!spec) return null;
      return <Renderer spec={spec} catalog={catalog} />;
    }
    
    function parseSpec(content: string) {
      const cleaned = stripCodeFencesAndPrelude(content);
      const partial = tolerantJsonParse(cleaned);
      return validateAgainstCatalog(partial);
    }

The catalog lives next to the renderer and pairs each component with a Zod schema describing its props:

frontend/src/app/registry.tsx
    
    
    import { z } from "zod";
    import { MetricCard } from "./metric-card";
    import { BarChart } from "./charts/bar-chart";
    import { PieChart } from "./charts/pie-chart";
    
    export const catalog = {
      MetricCard: {
        component: MetricCard,
        propsSchema: z.object({
          title: z.string(),
          value: z.number(),
          delta: z.number().optional(),
        }),
      },
      BarChart: {
        component: BarChart,
        propsSchema: z.object({
          data: z.array(z.object({ label: z.string(), value: z.number() })),
        }),
      },
      PieChart: {
        component: PieChart,
        propsSchema: z.object({
          data: z.array(z.object({ label: z.string(), value: z.number() })),
        }),
      },
    };

Validation is the safety net: anything the agent emits that doesn't match a registered schema is rejected before it hits React, so the chat can't render arbitrary garbage.

## Backend#

The agent emits a `{ root, elements }` JSON object as the assistant message content. `root` references a top-level element id; `elements` maps each id to a `{ type, props, children }` triple matching the catalog.

example agent output
    
    
    {
      "root": "dashboard",
      "elements": {
        "dashboard": {
          "type": "Stack",
          "children": ["revenue-card", "by-region"]
        },
        "revenue-card": {
          "type": "MetricCard",
          "props": { "title": "Total revenue", "value": 184302 }
        },
        "by-region": {
          "type": "BarChart",
          "props": { "data": [...] }
        }
      }
    }

Anything else (free-form text, code fences around the JSON, a "Here's your dashboard:" preamble) is stripped by the renderer's tolerant parser before validation. The agent doesn't need to be perfectly clean.

## Comparing the two patterns#

Both `byoc-json-render` and [`byoc-hashbrown`](https://docs.copilotkit.ai/langgraph-python/generative-ui/hashbrown) solve the same problem with two different rendering libraries. The agent contract is similar; the React glue, validation strategy, and rendering behaviour differ.

### On this page

When to use thisFrontendBackendComparing the two patterns
