---
url: https://docs.copilotkit.ai/reference/v1/hooks/useRenderToolCall/
title: useRenderToolCall
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:03.513515+00:00
---

# useRenderToolCall

> Source: https://docs.copilotkit.ai/reference/v1/hooks/useRenderToolCall/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁React (V1)SDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Components

[CopilotKit](https://docs.copilotkit.ai/reference/v1/components/CopilotKit)[CopilotTextarea](https://docs.copilotkit.ai/reference/v1/components/CopilotTextarea)[CopilotChat](https://docs.copilotkit.ai/reference/v1/components/chat/CopilotChat)[CopilotPopup](https://docs.copilotkit.ai/reference/v1/components/chat/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/v1/components/chat/CopilotSidebar)[All Chat Components](https://docs.copilotkit.ai/reference/v1/components/chat)

Hooks

[useAgent](https://docs.copilotkit.ai/reference/v1/hooks/useAgent)[useCoAgent](https://docs.copilotkit.ai/reference/v1/hooks/useCoAgent)[useCoAgentStateRender](https://docs.copilotkit.ai/reference/v1/hooks/useCoAgentStateRender)[useCopilotAction](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotAction)[useCopilotAdditionalInstructions](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotAdditionalInstructions)[useCopilotChat](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotChat)[useCopilotChatHeadless_c](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotChatHeadless_c)[useCopilotChatSuggestions](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotChatSuggestions)[useCopilotReadable](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotReadable)[useDefaultTool](https://docs.copilotkit.ai/reference/v1/hooks/useDefaultTool)[useFrontendTool](https://docs.copilotkit.ai/reference/v1/hooks/useFrontendTool)[useHumanInTheLoop](https://docs.copilotkit.ai/reference/v1/hooks/useHumanInTheLoop)[useLangGraphInterrupt](https://docs.copilotkit.ai/reference/v1/hooks/useLangGraphInterrupt)[useRenderToolCall](https://docs.copilotkit.ai/reference/v1/hooks/useRenderToolCall)

Classes

[CopilotRuntime](https://docs.copilotkit.ai/reference/v1/classes/CopilotRuntime)[CopilotTask](https://docs.copilotkit.ai/reference/v1/classes/CopilotTask)[AnthropicAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/AnthropicAdapter)[GoogleGenerativeAIAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/GoogleGenerativeAIAdapter)[GroqAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/GroqAdapter)[LangChainAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/LangChainAdapter)[OpenAIAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/OpenAIAdapter)[OpenAIAssistantAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/OpenAIAssistantAdapter)

SDKs

[LangGraph SDK](https://docs.copilotkit.ai/reference/v1/sdk/js/LangGraph)[CrewAI SDK](https://docs.copilotkit.ai/reference/v1/sdk/python/CrewAI)[CrewAIAgent](https://docs.copilotkit.ai/reference/v1/sdk/python/CrewAIAgent)[LangGraph SDK](https://docs.copilotkit.ai/reference/v1/sdk/python/LangGraph)[LangGraphAGUIAgent](https://docs.copilotkit.ai/reference/v1/sdk/python/LangGraphAGUIAgent)[Remote Endpoints](https://docs.copilotkit.ai/reference/v1/sdk/python/RemoteEndpoints)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[v1](https://docs.copilotkit.ai/reference/v1)Hooks

# useRenderToolCall

The useRenderToolCall hook enables rendering of backend tool calls in the frontend.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

This v1 `useRenderToolCall` takes a `{ name, parameters, render }` config object to **register** a renderer for an existing backend tool. In v2, use [`useRenderTool`](https://docs.copilotkit.ai/reference/v2/hooks/useRenderTool) for that job. The v2 hook named [`useRenderToolCall`](https://docs.copilotkit.ai/reference/v2/hooks/useRenderToolCall) is a different, low-level API that returns a renderer function for consuming tool calls.
    
    
    import { useRenderTool } from "@copilotkit/react-core/v2";
    import { z } from "zod";
    
    function StatusTool() {
      useRenderTool({
        name: "showStatus",
        parameters: z.object({}),
        render: ({ status, result }) => (
          <div>{status === "complete" ? result : "Running..."}</div>
        ),
      });
      return null;
    }

`useRenderToolCall` is purely a rendering hook. It displays custom UI for tool calls without executing any logic. This is typically used to visualize backend tool executions in your chat interface, showing users what the AI is doing behind the scenes.

This hook has no handler function. You only provide a render function that receives information about the tool call (arguments, status, results) and displays it however you want. You can target specific tool names or use an asterisk (`"*"`) to catch and render all tool calls.

## Usage

### Rendering a Specific Backend Tool
    
    
    import { useRenderToolCall } from "@copilotkit/react-core";
    
    useRenderToolCall({
      name: "analyzeData",
      description: "Display results of data analysis",
      parameters: [
        {
          name: "datasetName",
          type: "string",
          description: "Name of the dataset being analyzed",
          required: true,
        },
        {
          name: "metrics",
          type: "string[]",
          description: "Metrics being calculated",
          required: true,
        },
      ],
      render: ({ args, status, result }) => {
        if (status === "inProgress") {
          return (
            <div className="p-4 border rounded animate-pulse">
              <h3>Analyzing {args.datasetName}...</h3>
              <p>Calculating: {args.metrics?.join(", ")}</p>
            </div>
          );
        }
    
        if (status === "complete" && result) {
          return (
            <div className="p-4 border rounded bg-green-50">
              <h3>Analysis Complete: {args.datasetName}</h3>
              <pre className="mt-2 p-2 bg-gray-100 rounded">
                {JSON.stringify(result, null, 2)}
              </pre>
            </div>
          );
        }
    
        return null;
      },
    });

## Migration from useCopilotAction

If you're migrating from `useCopilotAction` with only a `render` function:
    
    
    // Before with useCopilotAction
    useCopilotAction({
      name: "showResult",
      render: ({ args }) => <ResultCard {...args} />,
    });
    
    // After with useRenderToolCall
    useRenderToolCall({
      name: "showResult",
      render: ({ args }) => <ResultCard {...args} />,
    });

The migration is straightforward - just change the hook name. The render props remain the same.

## Parameters

Prop

Type

`name`string

Prop

Type

`description?`string

Prop

Type

`parameters?`T

Prop

Type

`render?`FrontendAction<T>['render']

Prop

Type

`available?`'disabled' | 'enabled'
