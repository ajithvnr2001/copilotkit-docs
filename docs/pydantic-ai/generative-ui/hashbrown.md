---
url: https://docs.copilotkit.ai/pydantic-ai/generative-ui/hashbrown/
title: Hashbrown
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:23:59.991480+00:00
---

# Hashbrown

> Source: https://docs.copilotkit.ai/pydantic-ai/generative-ui/hashbrown/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendPydanticAI

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/pydantic-ai)[Quickstart](https://docs.copilotkit.ai/pydantic-ai/quickstart)[Build with agents](https://docs.copilotkit.ai/pydantic-ai/build-with-agents)[Intelligence](https://docs.copilotkit.ai/pydantic-ai/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/pydantic-ai/frontend-tools)

Generative UI

Controlled

Declarative

[A2UI](https://docs.copilotkit.ai/pydantic-ai/generative-ui/a2ui)

[JSON Render](https://docs.copilotkit.ai/pydantic-ai/generative-ui/json-render)[Hashbrown](https://docs.copilotkit.ai/pydantic-ai/generative-ui/hashbrown)

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/pydantic-ai/webmcp)

Agent capabilities

Pydantic AI

[Sub-agents](https://docs.copilotkit.ai/pydantic-ai/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/pydantic-ai/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/pydantic-ai/learning)

[User Memories](https://docs.copilotkit.ai/pydantic-ai/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/pydantic-ai/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/pydantic-ai/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/pydantic-ai/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/pydantic-ai/intelligence/analytics)[Channels](https://docs.copilotkit.ai/pydantic-ai/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/pydantic-ai/telemetry)[Community frameworks](https://docs.copilotkit.ai/pydantic-ai/community-frameworks)

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

byoc_hashbrown_agent.py

page.tsx

hashbrown-renderer.tsx

suggestions.ts

route.ts
    
    
    """PydanticAI agent backing the byoc-hashbrown demo.Mirrors showcase/integrations/langgraph-python/src/agents/byoc_hashbrown_agent.py.Emits hashbrown-shaped structured output that the ported HashBrownDashboardrenderer (`src/app/demos/byoc-hashbrown/hashbrown-renderer.tsx`)progressively parses via `@hashbrownai/react`'s `useJsonParser` +`useUiKit`.Wire format-----------`@hashbrownai/react`'s `useJsonParser(content, kit.schema)` expects theagent to stream a JSON object literal matching `kit.schema`. The promptbelow mirrors the post-PR #4271 langgraph-python prompt verbatim so thestreaming envelope produced by this PydanticAI agent is byte-compatiblewith the frontend kit:    {      "ui": [        { "metric":   { "props": { "label": "...", "value": "..." } } },        { "pieChart": { "props": { "title": "...", "data": "[{...}]" } } },        { "barChart": { "props": { "title": "...", "data": "[{...}]" } } },        { "dealCard": { "props": { "title": "...", "stage": "prospect", "value": 100000 } } },        { "Markdown": { "props": { "children": "## heading\\nbody" } } }      ]    }"""from __future__ import annotationsfrom pydantic_ai import Agentfrom pydantic_ai.models.openai import OpenAIResponsesModelBYOC_HASHBROWN_SYSTEM_PROMPT = """\You are a sales analytics assistant that replies by emitting a single JSONobject consumed by a streaming JSON parser on the frontend.ALWAYS respond with a single JSON object of the form:{  "ui": [    { <componentName>: { "props": { ... } } },    ...  ]}Do NOT wrap the response in code fences. Do NOT include any preface orexplanation outside the JSON object. The response MUST be valid JSON.Available components and their prop schemas:- "metric": { "props": { "label": string, "value": string } }    A KPI card. `value` is a pre-formatted string like "$1.2M" or "248".- "pieChart": { "props": { "title": string, "data": string } }    A donut chart. `data` is a JSON-encoded STRING (embedded JSON) of an    array of {label, value} objects with at least 3 segments, e.g.    "data": "[{\\"label\\":\\"Enterprise\\",\\"value\\":600000}]".- "barChart": { "props": { "title": string, "data": string } }    A vertical bar chart. `data` is a JSON-encoded STRING of an array of    {label, value} objects with at least 3 bars, typically time-ordered.- "dealCard": { "props": { "title": string, "stage": string, "value": number } }    A single sales deal. `stage` MUST be one of: "prospect", "qualified",    "proposal", "negotiation", "closed-won", "closed-lost". `value` is a    raw number (no currency symbol or comma).- "Markdown": { "props": { "children": string } }    Short explanatory text. Use for section headings and brief summaries.    Standard markdown is supported in `children`.Rules:- Always produce plausible sample data when the user asks for a dashboard or  chart — do not refuse for lack of data.- Prefer 3-6 rows of data in charts; keep labels short.- Use "Markdown" for short headings or linking sentences between visual  components. Do not emit long prose.- Do not emit components that are not listed above.- `data` props on charts MUST be a JSON STRING — escape inner quotes.Example response (sales dashboard):{"ui":[{"Markdown":{"props":{"children":"## Q4 Sales Summary"}}},{"metric":{"props":{"label":"Total Revenue","value":"$1.2M"}}},{"metric":{"props":{"label":"New Customers","value":"248"}}},{"pieChart":{"props":{"title":"Revenue by Segment","data":"[{\\"label\\":\\"Enterprise\\",\\"value\\":600000},{\\"label\\":\\"SMB\\",\\"value\\":400000},{\\"label\\":\\"Startup\\",\\"value\\":200000}]"}}},{"barChart":{"props":{"title":"Monthly Revenue","data":"[{\\"label\\":\\"Oct\\",\\"value\\":350000},{\\"label\\":\\"Nov\\",\\"value\\":400000},{\\"label\\":\\"Dec\\",\\"value\\":450000}]"}}}]}"""agent = Agent(    model=OpenAIResponsesModel("gpt-5-mini"),    system_prompt=BYOC_HASHBROWN_SYSTEM_PROMPT,)

You have a chat surface and you want the agent to draw a dashboard, not just describe one in prose. By the end of this guide, the agent will stream a structured output object, [`@hashbrownai/react`](https://www.npmjs.com/package/@hashbrownai/react)'s progressive JSON parser will hand each finished slice to your renderer as it arrives, and the user sees the dashboard fill in live.

## When to use this#

  * **Streaming dashboards** where partial state should render before the full payload arrives.
  * **Agents authoring structured UI** where the output is JSON-shaped, not free text.
  * **Cases where you already use Hashbrown** for UI generation elsewhere in your stack.



If you'd rather work with an explicit catalog of registered components rather than streaming a JSON tree, see the sibling page [JSON Render](https://docs.copilotkit.ai/pydantic-ai/generative-ui/json-render) for the same scenario implemented with `@json-render/react`.

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

Both `byoc-hashbrown` and [`byoc-json-render`](https://docs.copilotkit.ai/pydantic-ai/generative-ui/json-render) solve the same problem (agent-authored structured UI, rendered through a typed catalog), with two different rendering libraries. Pick whichever you already use elsewhere — the agent contract is the same shape; the React glue is what changes.

### On this page

When to use thisFrontendBackendComparing the two patterns
