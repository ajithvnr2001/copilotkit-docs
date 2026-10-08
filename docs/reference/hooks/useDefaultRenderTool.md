---
url: https://docs.copilotkit.ai/reference/hooks/useDefaultRenderTool/
title: useDefaultRenderTool
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:41.165732+00:00
---

# useDefaultRenderTool

> Source: https://docs.copilotkit.ai/reference/hooks/useDefaultRenderTool/

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

# useDefaultRenderTool

Register a wildcard default renderer for unhandled tool calls

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useDefaultRenderTool` is a convenience wrapper around `useRenderTool` with `name: "*"`.

This is part of the v2 tool rendering hook set with [`useComponent`](https://docs.copilotkit.ai/reference/hooks/useComponent), [`useRenderTool`](https://docs.copilotkit.ai/reference/hooks/useRenderTool), and [`useRenderToolCall`](https://docs.copilotkit.ai/reference/hooks/useRenderToolCall).

  * With no config, it registers CopilotKit's built-in default tool-call UI.
  * With `render`, it replaces that default UI with your own wildcard renderer.



Use this for catch-all rendering of tool calls that do not have a specific named renderer.

## Signature
    
    
    import { useDefaultRenderTool } from "@copilotkit/react-core/v2";
    
    function useDefaultRenderTool(
      config?: {
        render?: (props: {
          name: string;
          parameters: any;
          status: string;
          result: string | undefined;
        }) => React.ReactElement | null;
      },
      deps?: ReadonlyArray<unknown>,
    ): void;

## Behavior

  * Internally calls `useRenderTool({ name: "*", ... })`.
  * If `config.render` is omitted, uses an expandable default card UI that shows status, parameters, and result.
  * If `config.render` is provided, your renderer is used instead.
  * Your renderer can return `null` to draw nothing. Use this to render only the tool calls you care about and suppress the rest.
  * Inherits `useRenderTool` registration behavior and dependency semantics.



## Usage

### Built-in default renderer
    
    
    function App() {
      useDefaultRenderTool();
      return null;
    }

### Custom wildcard renderer
    
    
    function App() {
      useDefaultRenderTool(
        {
          render: ({ name, status, result }) => (
            <div>
              <strong>{name}</strong>: {status}
              {status === "complete" && result ? <pre>{result}</pre> : null}
            </div>
          ),
        },
        [],
      );
    
      return null;
    }

## Related

  * [`useRenderTool`](https://docs.copilotkit.ai/reference/hooks/useRenderTool)
  * [`useRenderToolCall`](https://docs.copilotkit.ai/reference/hooks/useRenderToolCall)


