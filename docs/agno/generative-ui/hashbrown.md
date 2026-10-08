---
url: https://docs.copilotkit.ai/agno/generative-ui/hashbrown/
title: Hashbrown
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:47:00.570876+00:00
---

# Hashbrown

> Source: https://docs.copilotkit.ai/agno/generative-ui/hashbrown/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAgno

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/agno)[Quickstart](https://docs.copilotkit.ai/agno/quickstart)[Build with agents](https://docs.copilotkit.ai/agno/build-with-agents)[Intelligence](https://docs.copilotkit.ai/agno/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/agno/frontend-tools)

Generative UI

Controlled

Declarative

[A2UI](https://docs.copilotkit.ai/agno/generative-ui/a2ui)

[JSON Render](https://docs.copilotkit.ai/agno/generative-ui/json-render)[Hashbrown](https://docs.copilotkit.ai/agno/generative-ui/hashbrown)

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/agno/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/agno/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/agno/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/agno/learning)

[User Memories](https://docs.copilotkit.ai/agno/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/agno/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/agno/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/agno/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/agno/intelligence/analytics)[Channels](https://docs.copilotkit.ai/agno/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/agno/telemetry)[Community frameworks](https://docs.copilotkit.ai/agno/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Hashbrown

Generative UIDeclarative

# Hashbrown

Bring your own component library. Have the agent stream structured output and let Hashbrown's progressive JSON parser render it as React components in real time.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Not available for Agno yet

This feature (`declarative-hashbrown`) hasn't been tagged in any Agno cell yet. Try [CopilotKit's Built-in Agent](https://docs.copilotkit.ai/built-in-agent/generative-ui/hashbrown), [LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python/generative-ui/hashbrown), [LangGraph (TypeScript)](https://docs.copilotkit.ai/langgraph-typescript/generative-ui/hashbrown).

DemoCode

Missing demo source

No demo found for `agno::declarative-hashbrown`. Check the integration slug and demo id (matches manifest `slug` / `demos[i].id`).

You have a chat surface and you want the agent to draw a dashboard, not just describe one in prose. By the end of this guide, the agent will stream a structured output object, [`@hashbrownai/react`](https://www.npmjs.com/package/@hashbrownai/react)'s progressive JSON parser will hand each finished slice to your renderer as it arrives, and the user sees the dashboard fill in live.

## When to use this#

  * **Streaming dashboards** where partial state should render before the full payload arrives.
  * **Agents authoring structured UI** where the output is JSON-shaped, not free text.
  * **Cases where you already use Hashbrown** for UI generation elsewhere in your stack.



If you'd rather work with an explicit catalog of registered components rather than streaming a JSON tree, see the sibling page [JSON Render](https://docs.copilotkit.ai/agno/generative-ui/json-render) for the same scenario implemented with `@json-render/react`.

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

Both `byoc-hashbrown` and [`byoc-json-render`](https://docs.copilotkit.ai/agno/generative-ui/json-render) solve the same problem (agent-authored structured UI, rendered through a typed catalog), with two different rendering libraries. Pick whichever you already use elsewhere — the agent contract is the same shape; the React glue is what changes.

### On this page

When to use thisFrontendBackendComparing the two patterns
