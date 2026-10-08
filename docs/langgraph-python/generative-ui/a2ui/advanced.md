---
url: https://docs.copilotkit.ai/langgraph-python/generative-ui/a2ui/advanced/
title: Advanced
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:07:55.772100+00:00
---

# Advanced

> Source: https://docs.copilotkit.ai/langgraph-python/generative-ui/a2ui/advanced/

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

On this page

[LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python)[Build Generative UI](https://docs.copilotkit.ai/langgraph-python/generative-ui)[A2UI](https://docs.copilotkit.ai/langgraph-python/generative-ui/a2ui)

# Advanced

Custom progress rendering, frontend action handlers, and advanced A2UI configuration.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Custom A2UI Progress Renderer#

When using [Dynamic Schema A2UI](https://docs.copilotkit.ai/langgraph-python/generative-ui/a2ui/advanced/dynamic-schema), a secondary LLM generates the UI schema and data. This takes a few seconds — during which CopilotKit shows a built-in progress indicator.

You can replace the built-in indicator with your own component using `useRenderTool`.

### How it works#

The dynamic schema flow calls a tool named `render_a2ui` under the hood. While the tool call is in progress (`status === "inProgress"`), your custom renderer is shown. Once the A2UI surface starts rendering (`status === "complete"`), your component is hidden and the actual surface takes over.

### Implementation#

### Create a progress component#

src/components/a2ui-progress.tsx
    
    
    "use client";
    
    import { memo } from "react";
    
    interface A2UIProgressProps {
      parameters: Record<string, unknown>;
    }
    
    export const A2UIProgress = memo(function A2UIProgress({
      parameters,
    }: A2UIProgressProps) {
      // You can inspect `parameters` to show partial progress.
      // As the LLM streams, `parameters.components` and `parameters.items`
      // will progressively populate.
      const componentCount = Array.isArray(parameters?.components)
        ? parameters.components.length
        : 0;
      const itemCount = Array.isArray(parameters?.items)
        ? parameters.items.length
        : 0;
    
      return (
        <div className="rounded-lg border border-gray-200 bg-gray-50 p-4">
          <div className="flex items-center gap-2 text-sm text-gray-600">
            <div className="h-4 w-4 animate-spin rounded-full border-2 border-gray-300 border-t-gray-600" />
            <span>Building interface...</span>
          </div>
          {componentCount > 0 && (
            <p className="mt-2 text-xs text-gray-500">
              {componentCount} components, {itemCount} items
            </p>
          )}
        </div>
      );
    });

### Register the renderer#

Use `useRenderTool` to intercept the `render_a2ui` tool call and show your component while it's in progress:

src/hooks/use-a2ui-progress.tsx
    
    
    "use client";
    
    import { useRenderTool } from "@copilotkit/react-core/v2";
    import { z } from "zod";
    import { A2UIProgress } from "@/components/a2ui-progress";
    
    export function useA2UIProgress() {
      useRenderTool(
        {
          name: "render_a2ui",
          parameters: z.any(),
          render: ({ status, parameters }) => {
            // Hide when complete — the A2UI surface renderer takes over
            if (status === "complete") return <></>;
            return <A2UIProgress parameters={parameters ?? {}} />;
          },
        },
        [],
      );
    }

### Call the hook in your page#

src/app/page.tsx
    
    
    "use client";
    
    import { useA2UIProgress } from "@/hooks/use-a2ui-progress";
    
    function Chat() {
      useA2UIProgress();
    
      return <CopilotChat className="flex-1" />;
    }

The `parameters` object updates progressively as the LLM streams the `render_a2ui` tool call. You can use this to show a skeleton that fills in as components and data arrive.

### What's in `parameters`?#

As the secondary LLM generates the A2UI surface, the `parameters` object accumulates:

Field| Type| Description  
---|---|---  
`surfaceId`| `string`| Unique ID for this surface  
`components`| `array`| The component tree (schema) — arrives first  
`root`| `string`| Root component ID  
`items`| `array`| Data items — arrive after the schema  
  
A common pattern is to show a skeleton layout once `components` has data, then show item count as `items` streams in.

## Action Handlers#

Action handling in this section is client-side. The current Python SDK's `a2ui.render` does not support the `action_handlers=` keyword; the fixed-schema guide preserves the button schema and documents that server-side handlers are not supported. The current React API exposes `createA2UIMessageRenderer` with an `onAction` interceptor.

This section covers the current frontend interceptor and the v0.9 schema button format.

### Schema button with action context#

The v0.9 A2UI schema defines buttons with an event and data-bound context fields. Components inside a repeating list use relative paths, so the context values resolve from the clicked item:
    
    
    {
      "id": "book-button",
      "component": "Button",
      "child": "book-label",
      "variant": "primary",
      "action": {
        "event": {
          "name": "book_flight",
          "context": {
            "flightNumber": { "path": "flightNumber" },
            "price": { "path": "price" }
          }
        }
      }
    }

The resulting `A2UIUserAction` will include the resolved context:
    
    
    {
      name: "book_flight",
      surfaceId: "flight-search-results",
      sourceComponentId: "book-button",
      timestamp: "2025-01-01T00:00:00.000Z",
      context: { flightNumber: "AA100", price: "$350" },
    }

### `onAction` interceptor#

Pass `onAction` to the exported renderer factory to handle an action in the browser. Return `null` after handling the action locally; return `undefined` to forward it unchanged to the agent:
    
    
    import {
      createA2UIMessageRenderer,
      type A2UIUserAction,
    } from "@copilotkit/react-core/v2";
    import { theme } from "./theme";
    
    const A2UIMessageRenderer = createA2UIMessageRenderer({
      theme,
      onAction: (action: A2UIUserAction) => {
        if (action.name === "book_flight") {
          console.info("Booking requested", action.context);
          return null;
        }
        return undefined;
      },
    });

Pass the returned renderer through the provider's `renderActivityMessages` prop when you need this custom `onAction` behavior. User-provided renderers take precedence over the provider's built-in A2UI renderer.

### Forward a modified action#

An interceptor can return a modified exported `A2UIUserAction`; the renderer forwards that action to the agent:
    
    
    const A2UIMessageRenderer = createA2UIMessageRenderer({
      theme,
      onAction: (action) => {
        if (action.name !== "book_flight") return;
    
        return {
          ...action,
          context: {
            ...(action.context ?? {}),
            source: "a2ui",
          },
        };
      },
    });

### Current action flow#

The current renderer applies `onAction` before forwarding an action:

  1. Returning `null` handles the action in the browser and skips the agent.
  2. Returning an `A2UIUserAction` forwards that modified action.
  3. Returning `undefined` forwards the original action.



The current Python SDK does not create server-side action handlers from an `action_handlers=` argument. The frontend interceptor is the supported custom-handling path in this documentation. The current React bridge does not include `dataContextPath` in the action passed to `onAction`; use `context` for values needed by the callback.

### Types reference#

Type| Description  
---|---  
`A2UIUserAction`| Dispatched action: `{ name, surfaceId, sourceComponentId, timestamp, context? }`  
`A2UIActionInterceptor`| `(action, forward) => A2UIUserAction | null | void | Promise<void | A2UIUserAction | null>` — exported interceptor type  
`createA2UIMessageRenderer`| Exported factory that accepts `theme` and optional `onAction`  
  
### On this page

Custom A2UI Progress RendererHow it worksImplementationCreate a progress componentRegister the rendererCall the hook in your pageWhat's in parameters?Action HandlersSchema button with action contextonAction interceptorForward a modified actionCurrent action flowTypes reference
