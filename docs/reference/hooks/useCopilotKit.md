---
url: https://docs.copilotkit.ai/reference/hooks/useCopilotKit/
title: useCopilotKit
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:38.771702+00:00
---

# useCopilotKit

> Source: https://docs.copilotkit.ai/reference/hooks/useCopilotKit/

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

# useCopilotKit

Low-level React hook for accessing the CopilotKit context

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useCopilotKit` is a low-level React hook that returns the CopilotKit context value, providing direct access to the core instance and provider-level state. It subscribes to runtime connection status changes and triggers re-renders when the connection status updates.

`useCopilotKit` is a low-level hook. Most applications should use higher-level hooks like `useAgent` or `useFrontendTool` instead.

**Throws an error** if used outside of a `CopilotKit` (or the `<CopilotKit>` wrapper component).

## Signature
    
    
    import { useCopilotKit } from "@copilotkit/react-core/v2";
    
    function useCopilotKit(): CopilotKitContextValue;

## Parameters

This hook takes no parameters.

## Return Value

Prop

Type

`context?`CopilotKitContextValue

## Usage

### Accessing the Core Instance
    
    
    function DebugPanel() {
      const { copilotkit } = useCopilotKit();
    
      const agents = Object.keys(copilotkit.agents ?? {});
    
      return (
        <div>
          <h3>Registered Agents</h3>
          <ul>
            {agents.map((id) => (
              <li key={id}>{id}</li>
            ))}
          </ul>
        </div>
      );
    }

### Subscribing to Core Events
    
    
    function ConnectionMonitor() {
      const { copilotkit } = useCopilotKit();
    
      useEffect(() => {
        const subscription = copilotkit.subscribe({
          onRuntimeConnectionStatusChanged: () => {
            console.log("Runtime connection status changed");
          },
        });
    
        return () => {
          subscription.unsubscribe();
        };
      }, [copilotkit]);
    
      return null;
    }

### Running a Tool Programmatically

`copilotkit.runTool()` lets you execute a registered frontend tool directly from code — no LLM turn required. The tool's handler runs, render components appear in the UI, and both the tool call and result are added to the agent's message history.
    
    
    function ExportButton() {
      const { copilotkit } = useCopilotKit();
    
      // Register the tool
      useFrontendTool({
        name: "exportData",
        description: "Export data as CSV",
        parameters: [{ name: "format", type: "string" }],
        handler: async ({ format }) => {
          const csv = await generateCsv(format);
          downloadFile(csv);
          return `Exported as ${format}`;
        },
      });
    
      // Trigger it from a button — no LLM needed
      const handleExport = async () => {
        const { result, error } = await copilotkit.runTool({
          name: "exportData",
          parameters: { format: "csv" },
        });
        if (error) console.error(error);
      };
    
      return <button onClick={handleExport}>Export CSV</button>;
    }

#### `runTool` Parameters

Prop

Type

`params?`CopilotKitCoreRunToolParams

#### `runTool` Return Value

Prop

Type

`result?`CopilotKitCoreRunToolResult

### Checking Tool Execution State
    
    
    function ToolExecutionIndicator() {
      const { executingToolCallIds } = useCopilotKit();
    
      if (executingToolCallIds.size === 0) {
        return null;
      }
    
      return <div>Executing {executingToolCallIds.size} tool call(s)...</div>;
    }

## Behavior

  * **Error on Missing Provider** : Throws an error if the hook is used outside of `CopilotKit` or the `<CopilotKit>` wrapper component.
  * **Runtime Status Subscription** : The hook subscribes to `onRuntimeConnectionStatusChanged` events, so components re-render when the runtime connection completes or fails.
  * **Stable Core Reference** : The `copilotkit` instance is created once per provider and remains stable across re-renders. Only the `executingToolCallIds` set changes as tool calls begin and complete.
  * **Provider-Level Tool Tracking** : `executingToolCallIds` is tracked at the provider level rather than in individual components. This ensures that tool execution start events fired before child components mount are not lost.



## Related

  * [`useAgent`](https://docs.copilotkit.ai/reference/hooks/useAgent) \-- High-level hook for accessing agent instances
  * [`useFrontendTool`](https://docs.copilotkit.ai/reference/hooks/useFrontendTool) \-- Register frontend tools that `runTool()` can execute
  * [`CopilotKit`](https://docs.copilotkit.ai/reference/v2) \-- The provider component that creates the context


