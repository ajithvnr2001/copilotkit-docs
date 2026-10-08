---
url: https://docs.copilotkit.ai/reference/hooks/useRenderTool/
title: useRenderTool
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:41.216113+00:00
---

# useRenderTool

> Source: https://docs.copilotkit.ai/reference/hooks/useRenderTool/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁React (V2)SDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Components

[CopilotChat](https://docs.copilotkit.ai/reference/v2/components/CopilotChat)[CopilotChatAssistantMessage](https://docs.copilotkit.ai/reference/v2/components/CopilotChatAssistantMessage)[CopilotChatInput](https://docs.copilotkit.ai/reference/v2/components/CopilotChatInput)[CopilotChatMessageView](https://docs.copilotkit.ai/reference/v2/components/CopilotChatMessageView)[CopilotChatUserMessage](https://docs.copilotkit.ai/reference/v2/components/CopilotChatUserMessage)[CopilotChatView](https://docs.copilotkit.ai/reference/v2/components/CopilotChatView)[CopilotKit](https://docs.copilotkit.ai/reference/v2/components/CopilotKit)[CopilotPopup](https://docs.copilotkit.ai/reference/v2/components/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/v2/components/CopilotSidebar)[CopilotThreadsDrawer](https://docs.copilotkit.ai/reference/v2/components/CopilotThreadsDrawer)

Hooks

[useAgent](https://docs.copilotkit.ai/reference/v2/hooks/useAgent)[useAgentContext](https://docs.copilotkit.ai/reference/v2/hooks/useAgentContext)[useCapabilities](https://docs.copilotkit.ai/reference/v2/hooks/useCapabilities)[useComponent](https://docs.copilotkit.ai/reference/v2/hooks/useComponent)[useConfigureSuggestions](https://docs.copilotkit.ai/reference/v2/hooks/useConfigureSuggestions)[useCopilotChatConfiguration](https://docs.copilotkit.ai/reference/v2/hooks/useCopilotChatConfiguration)[useCopilotKit](https://docs.copilotkit.ai/reference/v2/hooks/useCopilotKit)[useDefaultRenderTool](https://docs.copilotkit.ai/reference/v2/hooks/useDefaultRenderTool)[useFrontendTool](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTool)[useFrontendTools](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTools)[useHumanInTheLoop](https://docs.copilotkit.ai/reference/v2/hooks/useHumanInTheLoop)[useInterrupt](https://docs.copilotkit.ai/reference/v2/hooks/useInterrupt)[useRenderTool](https://docs.copilotkit.ai/reference/v2/hooks/useRenderTool)[useRenderToolCall](https://docs.copilotkit.ai/reference/v2/hooks/useRenderToolCall)[useSuggestions](https://docs.copilotkit.ai/reference/v2/hooks/useSuggestions)[useThreads](https://docs.copilotkit.ai/reference/v2/hooks/useThreads)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[v2](https://docs.copilotkit.ai/reference/v2)Hooks

# useRenderTool

Register typed renderers for tool calls, by tool name or wildcard

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useRenderTool` registers a chat renderer for tool calls. You can target a specific tool name (with a typed Zod `parameters` schema) or use a wildcard (`"*"`) fallback renderer.

This is part of the v2 tool rendering hook set with [`useComponent`](https://docs.copilotkit.ai/reference/hooks/useComponent), [`useDefaultRenderTool`](https://docs.copilotkit.ai/reference/hooks/useDefaultRenderTool), and [`useRenderToolCall`](https://docs.copilotkit.ai/reference/hooks/useRenderToolCall).

This hook only handles rendering. It does not register a frontend handler.

## Signature

### Wildcard overload
    
    
    import { useRenderTool } from "@copilotkit/react-core/v2";
    
    useRenderTool(
      {
        name: "*",
        render: (props) => React.ReactElement | null,
        agentId?: string,
      },
      deps?: ReadonlyArray<unknown>,
    );

### Named overload
    
    
    import { z } from "zod";
    import { useRenderTool } from "@copilotkit/react-core/v2";
    
    useRenderTool(
      {
        name: string,
        parameters: z.ZodTypeAny,
        render: (props) => React.ReactElement | null,
        agentId?: string,
      },
      deps?: ReadonlyArray<unknown>,
    );

## Render Props

`render` receives one of these states:

  * `{ status: "inProgress", parameters: Partial<T>, result: undefined }`
  * `{ status: "executing", parameters: T, result: undefined }`
  * `{ status: "complete", parameters: T, result: string }`



`name` is always present in all states.

## Behavior

  * `render` may return `null` to draw nothing for a tool call. `null` was always legal where a renderer is _invoked_ — `ReactToolCallRenderer.render` is a `React.ComponentType`, a function component returns `ReactNode`, and `null` is a member of `ReactNode` — so only the build-side signature forbade it.
  * Builds a renderer entry with `defineToolCallRenderer`.
  * Deduplicates by `agentId:name` key (latest registration wins).
  * Intentionally does not remove the renderer on cleanup so previous chat history can still render.
  * Tracks updates by `config.name` plus values in `deps` (include changing captures in `deps`).



## Usage

### Named tool renderer
    
    
    function App() {
      useRenderTool(
        {
          name: "searchDocs",
          parameters: z.object({ query: z.string() }),
          render: ({ name, parameters, status, result }) => {
            if (status === "inProgress") return <div>Preparing {name}…</div>;
            if (status === "executing")
              return <div>Searching for: {parameters.query}</div>;
            return <div>Done: {result}</div>;
          },
        },
        [],
      );
    
      return null;
    }

### Wildcard fallback renderer
    
    
    function App() {
      useRenderTool(
        {
          name: "*",
          render: ({ name, status }) => (
            <div>
              {status === "complete" ? "✓" : "⏳"} {name}
            </div>
          ),
        },
        [],
      );
    
      return null;
    }

### Disable rendering for a tool

Return `null` to suppress the default UI. The wildcard (`"*"`) needs no schema; a named tool takes a pass-through schema (`z.any()`).
    
    
    import { z } from "zod";
    
    function App() {
      // One specific tool…
      useRenderTool(
        { name: "searchDocs", parameters: z.any(), render: () => null },
        [],
      );
      // …or everything without its own renderer.
      useRenderTool({ name: "*", render: () => null }, []);
    
      return null;
    }

## Related

  * [`useDefaultRenderTool`](https://docs.copilotkit.ai/reference/hooks/useDefaultRenderTool)
  * [`useRenderToolCall`](https://docs.copilotkit.ai/reference/hooks/useRenderToolCall)
  * [`useFrontendTool`](https://docs.copilotkit.ai/reference/hooks/useFrontendTool)


