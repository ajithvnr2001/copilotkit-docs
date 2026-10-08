---
url: https://docs.copilotkit.ai/reference/react-native/hooks/useCopilotKit/
title: useCopilotKit
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:51.986935+00:00
---

# useCopilotKit

> Source: https://docs.copilotkit.ai/reference/react-native/hooks/useCopilotKit/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁React NativeSDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Components

[AssistantMessage](https://docs.copilotkit.ai/reference/react-native/components/AssistantMessage)[CopilotChat](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat)[CopilotKitProvider](https://docs.copilotkit.ai/reference/react-native/components/CopilotKitProvider)[CopilotMarkdown](https://docs.copilotkit.ai/reference/react-native/components/CopilotMarkdown)[CopilotModal](https://docs.copilotkit.ai/reference/react-native/components/CopilotModal)[CopilotPopup](https://docs.copilotkit.ai/reference/react-native/components/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/react-native/components/CopilotSidebar)[UserMessage](https://docs.copilotkit.ai/reference/react-native/components/UserMessage)

Hooks

[useAgent](https://docs.copilotkit.ai/reference/react-native/hooks/useAgent)[useAgentContext](https://docs.copilotkit.ai/reference/react-native/hooks/useAgentContext)[useAttachments](https://docs.copilotkit.ai/reference/react-native/hooks/useAttachments)[useCapabilities](https://docs.copilotkit.ai/reference/react-native/hooks/useCapabilities)[useComponent](https://docs.copilotkit.ai/reference/react-native/hooks/useComponent)[useConfigureSuggestions](https://docs.copilotkit.ai/reference/react-native/hooks/useConfigureSuggestions)[useCopilotKit](https://docs.copilotkit.ai/reference/react-native/hooks/useCopilotKit)[useFrontendTool](https://docs.copilotkit.ai/reference/react-native/hooks/useFrontendTool)[useHumanInTheLoop](https://docs.copilotkit.ai/reference/react-native/hooks/useHumanInTheLoop)[useInterrupt](https://docs.copilotkit.ai/reference/react-native/hooks/useInterrupt)[useRenderTool](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool)[useSuggestions](https://docs.copilotkit.ai/reference/react-native/hooks/useSuggestions)[useThreads](https://docs.copilotkit.ai/reference/react-native/hooks/useThreads)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[react-native](https://docs.copilotkit.ai/reference/react-native)Hooks

# useCopilotKit

Low-level React hook for accessing the CopilotKit context in React Native

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useCopilotKit` is a low-level React hook that returns the CopilotKit context value, providing direct access to the core instance and provider-level state. It subscribes to runtime connection status changes and triggers re-renders when the connection status updates.

Re-exported from `@copilotkit/react-core/v2`, identical to the [React (V2) `useCopilotKit`](https://docs.copilotkit.ai/reference/v2/hooks/useCopilotKit). The only difference is the import path.

`useCopilotKit` is a low-level hook. Most applications should use higher-level hooks like `useAgent` or `useFrontendTool` instead.

**Throws an error** if used outside of a `CopilotKitProvider`.

## Signature
    
    
    import { useCopilotKit } from "@copilotkit/react-native";
    
    function useCopilotKit(): CopilotKitContextValue;

## Parameters

This hook takes no parameters.

## Return Value

Prop

Type

`context?`CopilotKitContextValue

## Usage

### Accessing the Core Instance
    
    
    import { Text, View } from "react-native";
    import { useCopilotKit } from "@copilotkit/react-native";
    
    function DebugPanel() {
      const { copilotkit } = useCopilotKit();
    
      const agents = Object.keys(copilotkit.agents ?? {});
    
      return (
        <View>
          <Text>Registered Agents</Text>
          {agents.map((id) => (
            <Text key={id}>{id}</Text>
          ))}
        </View>
      );
    }

### Running an Agent

`copilotkit.runAgent()` triggers an agent run directly from code. This is the validated React Native pattern: add a message to the agent, then run it.
    
    
    import { useCallback, useState } from "react";
    import { Text, TextInput, TouchableOpacity, View } from "react-native";
    import { useAgent, useCopilotKit } from "@copilotkit/react-native";
    
    function Composer() {
      const [inputText, setInputText] = useState("");
      const { copilotkit } = useCopilotKit();
      const { agent } = useAgent({ agentId: "default" });
    
      const handleSend = useCallback(async () => {
        const text = inputText.trim();
        if (!text || !agent) return;
        setInputText("");
        agent.addMessage({
          id: `user-${Date.now()}`,
          role: "user",
          content: text,
        });
        try {
          await copilotkit.runAgent({ agent });
        } catch (error) {
          console.error("CopilotKit runAgent failed:", error);
        }
      }, [inputText, agent, copilotkit]);
    
      return (
        <View>
          <TextInput
            value={inputText}
            onChangeText={setInputText}
            placeholder="Type a message..."
            onSubmitEditing={handleSend}
          />
          <TouchableOpacity onPress={handleSend}>
            <Text>Send</Text>
          </TouchableOpacity>
        </View>
      );
    }

### Subscribing to Core Events
    
    
    import { useEffect } from "react";
    import { useCopilotKit } from "@copilotkit/react-native";
    
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

`copilotkit.runTool()` lets you execute a registered frontend tool directly from code, with no LLM turn required. The tool's handler runs, render components appear in the UI, and both the tool call and result are added to the agent's message history.
    
    
    import { Text, TouchableOpacity } from "react-native";
    import { useCopilotKit, useFrontendTool } from "@copilotkit/react-native";
    import { z } from "zod";
    
    function ExportButton() {
      const { copilotkit } = useCopilotKit();
    
      // Register the tool
      useFrontendTool({
        name: "exportData",
        description: "Export data as CSV",
        parameters: z.object({ format: z.string() }),
        handler: async ({ format }) => {
          const csv = await generateCsv(format);
          await saveFile(csv);
          return `Exported as ${format}`;
        },
      });
    
      // Trigger it from a button, no LLM needed
      const handleExport = async () => {
        const { result, error } = await copilotkit.runTool({
          name: "exportData",
          parameters: { format: "csv" },
        });
        if (error) console.error(error);
      };
    
      return (
        <TouchableOpacity onPress={handleExport}>
          <Text>Export CSV</Text>
        </TouchableOpacity>
      );
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
    
    
    import { Text } from "react-native";
    import { useCopilotKit } from "@copilotkit/react-native";
    
    function ToolExecutionIndicator() {
      const { executingToolCallIds } = useCopilotKit();
    
      if (executingToolCallIds.size === 0) {
        return null;
      }
    
      return <Text>Executing {executingToolCallIds.size} tool call(s)...</Text>;
    }

## Behavior

  * **Error on Missing Provider** : Throws an error if the hook is used outside of `CopilotKitProvider`.
  * **Runtime Status Subscription** : The hook subscribes to `onRuntimeConnectionStatusChanged` events, so components re-render when the runtime connection completes or fails.
  * **Stable Core Reference** : The `copilotkit` instance is created once per provider and remains stable across re-renders. Only the `executingToolCallIds` set changes as tool calls begin and complete.
  * **Provider-Level Tool Tracking** : `executingToolCallIds` is tracked at the provider level rather than in individual components. This ensures that tool execution start events fired before child components mount are not lost.



## Related

  * [`useAgent`](https://docs.copilotkit.ai/reference/react-native/hooks/useAgent): High-level hook for accessing agent instances
  * [`useFrontendTool`](https://docs.copilotkit.ai/reference/react-native/hooks/useFrontendTool): Register frontend tools that `runTool()` can execute
  * [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/react-native/components/CopilotKitProvider): The provider component that creates the context
  * [React (V2) reference](https://docs.copilotkit.ai/reference/v2/hooks/useCopilotKit): The web equivalent this page mirrors


