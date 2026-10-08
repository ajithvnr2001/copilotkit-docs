---
url: https://docs.copilotkit.ai/reference/react-native/hooks/useAgent/
title: useAgent
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:47.983179+00:00
---

# useAgent

> Source: https://docs.copilotkit.ai/reference/react-native/hooks/useAgent/

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

# useAgent

React hook for accessing AG-UI agent instances in React Native

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useAgent` is a React hook that returns an [AG-UI AbstractAgent](https://docs.ag-ui.com/sdk/js/client/abstract-agent) instance. The hook subscribes to agent state changes and triggers re-renders when the agent's state, messages, or execution status changes.

Re-exported from `@copilotkit/react-core/v2`. It is identical to the [React (V2) `useAgent`](https://docs.copilotkit.ai/reference/v2/hooks/useAgent); only the import path differs.

By default it binds to a shared agent from the CopilotKit registry. It can also register a private proxied agent for one thread, which is useful for custom thread switchers and multi-conversation UIs.

**Throws an error** if no agent is configured with the specified `agentId`, or if only part of the thread-scoped option set is provided.

## Signature
    
    
    import { useAgent } from "@copilotkit/react-native";
    
    function useAgent(options?: UseAgentProps): {
      agent: AbstractAgent;
      isReady: boolean;
    };

For fully headless UI that does not import the built-in chat rendering stack, import the hook from the headless entry:
    
    
    import { useAgent } from "@copilotkit/react-native/headless";

## Parameters

Prop

Type

`options?`UseAgentProps

There are two valid option shapes:

  * `useAgent()` or `useAgent({ agentId })`: bind to a shared agent. The thread comes from chat configuration or the agent itself.
  * `useAgent({ agentId, runtimeAgentId, threadId })`: register a private local agent under `agentId`, route it to the runtime agent named by `runtimeAgentId`, and pin it to `threadId`.



## Return Value

Prop

Type

`object?`{ agent: AbstractAgent; isReady: boolean }

## Usage

### Basic Usage
    
    
    import { Text, View } from "react-native";
    import { useAgent } from "@copilotkit/react-native";
    
    function AgentStatus() {
      const { agent } = useAgent();
    
      return (
        <View>
          <Text>Agent: {agent.agentId}</Text>
          <Text>Messages: {agent.messages.length}</Text>
          <Text>Running: {agent.isRunning ? "Yes" : "No"}</Text>
        </View>
      );
    }

### Accessing and Updating State
    
    
    import { Text, TouchableOpacity, View } from "react-native";
    import { useAgent } from "@copilotkit/react-native";
    
    function StateController() {
      const { agent } = useAgent();
    
      return (
        <View>
          <Text>{JSON.stringify(agent.state, null, 2)}</Text>
          <TouchableOpacity
            onPress={() => agent.setState({ ...agent.state, count: 1 })}
          >
            <Text>Update State</Text>
          </TouchableOpacity>
        </View>
      );
    }

### Event Subscription
    
    
    import { useEffect } from "react";
    import { useAgent } from "@copilotkit/react-native";
    
    function EventListener() {
      const { agent } = useAgent();
    
      useEffect(() => {
        const { unsubscribe } = agent.subscribe({
          onRunStartedEvent: () => console.log("Started"),
          onRunFinalized: () => console.log("Finished"),
        });
    
        return unsubscribe;
      }, []);
    
      return null;
    }

### Multiple Agents
    
    
    import { Text, View } from "react-native";
    import { useAgent } from "@copilotkit/react-native";
    
    function MultiAgentView() {
      const { agent: primary } = useAgent({ agentId: "primary" });
      const { agent: support } = useAgent({ agentId: "support" });
    
      return (
        <View>
          <Text>Primary: {primary.messages.length} messages</Text>
          <Text>Support: {support.messages.length} messages</Text>
        </View>
      );
    }

### Thread-scoped Agent

Use the thread-scoped form when one runtime agent needs multiple independent frontend instances, for example one per open conversation. The local `agentId` must be unique in the current provider.
    
    
    import { Text } from "react-native";
    import { useAgent } from "@copilotkit/react-native";
    
    function ThreadPreview({ threadId }: { threadId: string }) {
      const { agent, isReady } = useAgent({
        agentId: `preview-${threadId}`,
        runtimeAgentId: "support",
        threadId,
        throttleMs: 100,
      });
    
      if (!isReady) return <Text>Loading...</Text>;
    
      return <Text>{agent.messages.length} messages</Text>;
    }

### Optimizing Re-renders
    
    
    import { Text } from "react-native";
    import { useAgent, UseAgentUpdate } from "@copilotkit/react-native";
    
    // Only re-render when messages change
    function MessageCount() {
      const { agent } = useAgent({
        updates: [UseAgentUpdate.OnMessagesChanged],
      });
    
      return <Text>Messages: {agent.messages.length}</Text>;
    }

## Behavior

  * **Automatic Re-renders** : Component re-renders when agent state, messages, or execution status changes (configurable via `updates` parameter)
  * **Optional Throttling** : Message and state update re-renders can be throttled with `throttleMs` or the provider's `defaultThrottleMs`.
  * **Readiness** : While the runtime is connecting, `agent` is a fully-constructed provisional stand-in and `isReady` is `false`; once the runtime syncs, `agent` swaps to the real instance and `isReady` becomes `true`. Guard on `isReady` for work that must target the real agent (e.g. one-time subscriptions)
  * **Error Handling** : Throws error if no agent exists with specified `agentId`
  * **Thread Scoping** : `threadId` and `runtimeAgentId` must be passed together with an explicit local `agentId`; partial combinations throw at runtime and are rejected by the TypeScript type.
  * **State Synchronization** : State updates via `setState()` are immediately available to both app and agent
  * **Event Subscriptions** : Subscribe/unsubscribe pattern for lifecycle and custom events



## Related

  * [AG-UI AbstractAgent](https://docs.ag-ui.com/sdk/js/client/abstract-agent) \- Full agent interface documentation
  * [`useCopilotKit`](https://docs.copilotkit.ai/reference/react-native/hooks/useCopilotKit) \- Low-level hook for accessing the CopilotKit core instance
  * [React (V2) reference](https://docs.copilotkit.ai/reference/v2/hooks/useAgent) \- The web equivalent this page mirrors


