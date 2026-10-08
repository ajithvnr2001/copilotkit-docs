---
url: https://docs.copilotkit.ai/crewai-crews/generative-ui/json-render/
title: JSON Render
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:57:02.344048+00:00
---

# JSON Render

> Source: https://docs.copilotkit.ai/crewai-crews/generative-ui/json-render/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendCrewAI Flows

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/crewai-crews)[Quickstart](https://docs.copilotkit.ai/crewai-crews/quickstart)[Build with agents](https://docs.copilotkit.ai/crewai-crews/build-with-agents)[Intelligence](https://docs.copilotkit.ai/crewai-crews/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/crewai-crews/frontend-tools)

Generative UI

Controlled

Declarative

[A2UI](https://docs.copilotkit.ai/crewai-crews/generative-ui/a2ui)

[JSON Render](https://docs.copilotkit.ai/crewai-crews/generative-ui/json-render)[Hashbrown](https://docs.copilotkit.ai/crewai-crews/generative-ui/hashbrown)

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/crewai-crews/webmcp)

Agent capabilities

CrewAI Flows

[Sub-agents](https://docs.copilotkit.ai/crewai-crews/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/crewai-crews/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/crewai-crews/learning)

[User Memories](https://docs.copilotkit.ai/crewai-crews/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/crewai-crews/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/crewai-crews/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/crewai-crews/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/crewai-crews/intelligence/analytics)[Channels](https://docs.copilotkit.ai/crewai-crews/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/crewai-crews/telemetry)[Community frameworks](https://docs.copilotkit.ai/crewai-crews/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

JSON Render

Generative UIDeclarative

# JSON Render

Bring your own component library. Have the agent emit a JSON spec and let json-render render it against a Zod-validated catalog of React components.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Not available for CrewAI Flows yet

This feature (`declarative-json-render`) hasn't been tagged in any CrewAI Flows cell yet. Try [CopilotKit's Built-in Agent](https://docs.copilotkit.ai/built-in-agent/generative-ui/json-render), [LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python/generative-ui/json-render), [LangGraph (TypeScript)](https://docs.copilotkit.ai/langgraph-typescript/generative-ui/json-render).

DemoCode

Missing demo source

No demo found for `crewai-crews::declarative-json-render`. Check the integration slug and demo id (matches manifest `slug` / `demos[i].id`).

You have a chat surface and you want the agent to draw a dashboard from a typed JSON spec. By the end of this guide, the agent will emit a `{ root, elements }` object, [`@json-render/react`](https://www.npmjs.com/package/@json-render/react) will validate it against a Zod-described catalog, and the user sees the dashboard render as a single React tree.

## When to use this#

  * **Structured UI with a typed contract** where the agent's output is validated against a known schema before it touches the DOM.
  * **Tolerance for prose preamble + code fences** in the agent's output (json-render's parser handles them).
  * **Cases where you already use json-render** elsewhere or prefer Zod-validated catalogs.



If you'd rather have a streaming progressive render rather than a one-shot validated render, see the sibling page [Hashbrown](https://docs.copilotkit.ai/crewai-crews/generative-ui/hashbrown) for the same scenario with `@hashbrownai/react`.

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

Both `byoc-json-render` and [`byoc-hashbrown`](https://docs.copilotkit.ai/crewai-crews/generative-ui/hashbrown) solve the same problem with two different rendering libraries. The agent contract is similar; the React glue, validation strategy, and rendering behaviour differ.

### On this page

When to use thisFrontendBackendComparing the two patterns
