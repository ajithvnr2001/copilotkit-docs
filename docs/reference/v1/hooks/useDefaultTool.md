---
url: https://docs.copilotkit.ai/reference/v1/hooks/useDefaultTool/
title: useDefaultTool
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:01.921003+00:00
---

# useDefaultTool

> Source: https://docs.copilotkit.ai/reference/v1/hooks/useDefaultTool/

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

# useDefaultTool

The useDefaultTool hook enables rendering of a default UI which catches any tool that does not have a specific renderer.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

`useDefaultTool` is still supported, but we recommend migrating to [`useFrontendTool`](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTool) from the v2 API.

`useDefaultTool` is a React hook that allows you to render custom UI for any tool call that doesn't have a specific renderer

## Usage
    
    
    import { useDefaultTool } from "@copilotkit/react-core";
    
    useDefaultTool({
      render: ({ name, args, status, result }) => {
        return (
          <div className="p-4 border rounded my-2">
            <div className="flex items-center justify-between mb-2">
              <h4 className="font-semibold">{name}</h4>
              <span className="text-sm text-gray-500">
                {status === "inProgress" && "Running..."}
                {status === "executing" && "Executing..."}
                {status === "complete" && "Complete"}
              </span>
            </div>
    
            {Object.keys(args).length > 0 && (
              <div className="mb-2">
                <p className="text-sm font-medium text-gray-600">Parameters:</p>
                <pre className="text-xs bg-gray-100 p-2 rounded mt-1">
                  {JSON.stringify(args, null, 2)}
                </pre>
              </div>
            )}
    
            {status === "complete" && result && (
              <div>
                <p className="text-sm font-medium text-gray-600">Result:</p>
                <pre className="text-xs bg-gray-100 p-2 rounded mt-1">
                  {JSON.stringify(result, null, 2)}
                </pre>
              </div>
            )}
          </div>
        );
      },
    });

### Rendering Model Context Protocol (MCP) Tools
    
    
    import { useDefaultTool } from "@copilotkit/react-core";
    
    // Render any MCP tool call with a custom UI
    useDefaultTool({
      render: ({ name, args, status, result }) => {
        // Custom rendering for MCP tools
        if (name.startsWith("mcp_")) {
          return <MCPToolRenderer name={name} args={args} status={status} result={result} />;
        }
    
        // Default rendering for other tools
        return <DefaultToolRenderer name={name} args={args} status={status} result={result} />;
      },
    });

## Parameters

Prop

Type

`tool`ReactRenderToolCall<T>

Prop

Type

`dependencies?`any[]

## Common Use Cases

  1. **Backend Tool Visualization** : Display progress and results of long-running backend operations
  2. **Generic Tool Rendering** : Provide a fallback UI for any tool without specific rendering
  3. **MCP Tool Integration** : Render Model Context Protocol tools from various sources
  4. **Debugging** : Display all tool calls during development
  5. **Analytics** : Track and display tool usage



## Migration from useCopilotAction

If you're migrating from `useCopilotAction` with only a `render` function:
    
    
    // Before with useCopilotAction
    useCopilotAction({
      render: ({ name, args, status, result }) => (
        <GenericToolCall name={name} args={args} status={status} result={result} />
      ),
    });
    
    // After with useDefaultTool
    useDefaultTool({
      render: ({ name, args, status, result }) => (
        <GenericToolCall name={name} args={args} status={status} result={result} />
      ),
    });

The migration is straightforward - just change the hook name. The render props remain the same.
