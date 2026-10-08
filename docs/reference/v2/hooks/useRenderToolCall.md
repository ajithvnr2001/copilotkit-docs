---
url: https://docs.copilotkit.ai/reference/v2/hooks/useRenderToolCall/
title: useRenderToolCall
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:34:49.009732+00:00
---

# useRenderToolCall

> Source: https://docs.copilotkit.ai/reference/v2/hooks/useRenderToolCall/

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

# useRenderToolCall

React hook that returns a renderer function for tool calls in the chat interface

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

Same name, different API than v1

The v2 `useRenderToolCall` (this page, from `@copilotkit/react-core/v2`) is a **no-argument hook** that _returns_ a renderer function for consuming tool calls. It is **not** the v1 [`useRenderToolCall`](https://docs.copilotkit.ai/reference/v1/hooks/useRenderToolCall), which takes a `{ name, parameters, render }` config object to _register_ a renderer. To register renderers for existing backend tools in v2, use [`useRenderTool`](https://docs.copilotkit.ai/reference/hooks/useRenderTool).

`useRenderToolCall` returns a renderer function that maps tool calls to React elements. The returned function looks up the matching render configuration by tool name (preferring a renderer scoped to the active `agentId`, then an unscoped one, then a wildcard `"*"` renderer if no exact match is found), partially parses the JSON arguments, determines the current `ToolCallStatus`, and returns the appropriate React element. When neither a per-tool nor a wildcard renderer is registered, it falls back to the framework's built-in `DefaultToolCallRenderer`, so the returned element is effectively always non-null (the signature keeps `ReactElement | null` for type compatibility).

This hook is primarily used by chat UI components to display visual feedback for tool calls. In most applications you will not call it directly; instead, you register render components for existing backend tools via `useRenderTool`, and the chat components use `useRenderToolCall` internally to resolve them.

## Signature
    
    
    import { useRenderToolCall } from "@copilotkit/react-core/v2";
    
    function useRenderToolCall(): (
      props: UseRenderToolCallProps,
    ) => React.ReactElement | null;

## Return Value

Prop

Type

`renderer?`(props: UseRenderToolCallProps) => React.ReactElement | null

## Status Resolution

The renderer determines the `ToolCallStatus` based on the inputs:

Condition| Status| `result`  
---|---|---  
No `toolMessage`, tool call id **not** in the executing set| `ToolCallStatus.InProgress`| `undefined`  
No `toolMessage`, tool call id **is** in the provider executing set| `ToolCallStatus.Executing`| `undefined`  
A `toolMessage` is present| `ToolCallStatus.Complete`| The result string from the tool message  
  
## ToolCallStatus

The `ToolCallStatus` enum is exported from `@copilotkit/react-core/v2`:

Value| Description  
---|---  
`ToolCallStatus.InProgress`| The tool call's arguments are still being streamed.  
`ToolCallStatus.Executing`| Arguments are fully resolved; the tool is executing.  
`ToolCallStatus.Complete`| Execution is finished and a result is available.  
  
## Usage

### Using the Renderer in a Custom Chat Component
    
    
    function CustomChatMessage({ message }) {
      const renderToolCall = useRenderToolCall();
    
      if (message.type === "tool_call") {
        // Always returns an element: your registered renderer, the wildcard
        // ("*") renderer, or the framework's built-in DefaultToolCallRenderer.
        const element = renderToolCall({
          toolCall: message.toolCall,
          toolMessage: message.toolMessage,
        });
    
        return <div className="tool-call-container">{element}</div>;
      }
    
      return <div>{message.content}</div>;
    }

### Registering Renderers with useRenderTool

Tool call renderers for existing backend tools are registered through `useRenderTool` or directly via the `renderToolCalls` prop on the provider. The `useRenderToolCall` hook resolves these registrations at render time.
    
    
    import { useRenderTool } from "@copilotkit/react-core/v2";
    import { z } from "zod";
    
    function App() {
      useRenderTool(
        {
          name: "searchDatabase",
          parameters: z.object({
            query: z.string().describe("Search query"),
          }),
          render: ({ parameters, status, result }) => {
            if (status === "inProgress") {
              return <div>Preparing search...</div>;
            }
            if (status === "executing") {
              return <div>Searching for "{parameters.query}"...</div>;
            }
            if (status === "complete" && result) {
              return <div>Search complete: {result}</div>;
            }
            return null;
          },
        },
        [],
      );
    
      return <ChatInterface />;
    }

### Wildcard Renderer

If no exact name match is found, the hook falls back to a wildcard `"*"` renderer. This is useful for providing a generic UI for all unhandled tool calls.
    
    
    function App() {
      return (
        <CopilotKit
          runtimeUrl="/api/copilotkit"
          renderToolCalls={[
            {
              name: "*",
              render: ({ name, args, status, result }) => {
                if (status === ToolCallStatus.InProgress) {
                  return (
                    <div className="text-gray-500 text-sm">Running {name}...</div>
                  );
                }
                if (status === ToolCallStatus.Complete) {
                  return (
                    <div className="text-green-600 text-sm">{name} completed.</div>
                  );
                }
                return null;
              },
            },
          ]}
        >
          <YourApp />
        </CopilotKit>
      );
    }

## Behavior

  * **Name-based lookup with agent scoping** : The renderer searches registered render configurations for an exact tool name match first. When multiple match the same name, it prefers the one scoped to the active `agentId`, then an unscoped renderer, then the first match. If no exact match exists, it falls back to a wildcard (`"*"`) renderer, and finally to the framework's built-in `DefaultToolCallRenderer`.
  * **Partial JSON parsing** : The tool call's `arguments` string is parsed with `partialJSONParse` before being passed to the render component, so partially-streamed arguments can render incrementally while the tool call is still `InProgress`.
  * **Status inference** : Status is determined from the presence of the `toolMessage` prop and whether the tool call id is in the provider's executing set. The render component always receives a consistent shape with `name`, `toolCallId`, `args`, `status`, and `result`.
  * **Default renderer for unmatched tools** : If no renderer is registered for the tool name and no wildcard renderer exists, the function falls back to the built-in `DefaultToolCallRenderer` rather than returning `null`, so unhandled tool calls still paint out-of-the-box.
  * **Used internally by chat components** : The built-in `CopilotChat`, `CopilotPopup`, and `CopilotSidebar` components use this hook to render tool calls. You only need to call it directly when building custom chat UIs.



### Disable default tool rendering

Because the hook falls back to the built-in `DefaultToolCallRenderer` when no renderer matches, tool calls paint UI out-of-the-box. To turn that off, register a renderer that produces no UI (an empty fragment, `() => <></>`). A registered renderer takes priority over the default, so no fallback UI is shown.

Register a wildcard (`"*"`) renderer with [`useRenderTool`](https://docs.copilotkit.ai/reference/hooks/useRenderTool) to disable the default for **all** tool calls. The wildcard overload takes no `parameters` schema, so no Zod is required. Any tool with its own named renderer still paints.
    
    
    function App() {
      // Suppress the built-in DefaultToolCallRenderer for every tool call
      // without its own named renderer.
      useRenderTool({ name: "*", render: () => <></> }, []);
    
      return <YourApp />;
    }

#### For specific tools

To disable rendering for a single tool, register a renderer under that tool's name. Named renderers take a `parameters` schema; when you only want to suppress UI, pass a pass-through schema (`z.any()`):
    
    
    import { z } from "zod";
    
    function App() {
      useRenderTool(
        { name: "specificTool", parameters: z.any(), render: () => <></> },
        [],
      );
    
      return <YourApp />;
    }

You can also opt out conditionally — render nothing for some statuses and real UI for others (for example, hide while `InProgress` but show a result on `Complete`), since the `render` function receives the current `status`.

## Related

  * [`useRenderTool`](https://docs.copilotkit.ai/reference/hooks/useRenderTool) \-- register a renderer by tool name or wildcard (no schema needed for `"*"`)
  * [`useFrontendTool`](https://docs.copilotkit.ai/reference/hooks/useFrontendTool) \-- register tools with render components
  * [`useHumanInTheLoop`](https://docs.copilotkit.ai/reference/hooks/useHumanInTheLoop) \-- register interactive tools with render components
  * [`CopilotKit`](https://docs.copilotkit.ai/reference/v2) \-- configure static render tool calls at the provider level


