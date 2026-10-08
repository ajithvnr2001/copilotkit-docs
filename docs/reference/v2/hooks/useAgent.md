---
url: https://docs.copilotkit.ai/reference/v2/hooks/useAgent/
title: useAgent
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:34:41.249724+00:00
---

# useAgent

> Source: https://docs.copilotkit.ai/reference/v2/hooks/useAgent/

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

# useAgent

React hook for accessing AG-UI agent instances

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useAgent` is a React hook that returns an [AG-UI AbstractAgent](https://docs.ag-ui.com/sdk/js/client/abstract-agent) instance. The hook subscribes to agent state changes and triggers re-renders when the agent's state, messages, or execution status changes.

**Throws an error** if no agent is configured with the specified `agentId`, or if only part of the thread-scoped option set is provided.

## Signature
    
    
    import { useAgent } from "@copilotkit/react-core/v2";
    
    function useAgent(options?: UseAgentProps): {
      agent: AbstractAgent;
      isReady: boolean;
    };

For fully headless UI that does not import the built-in chat rendering stack, import the hook from the headless entry:
    
    
    import { useAgent } from "@copilotkit/react-core/v2/headless";

## Two valid shapes

The options object admits exactly two shapes, and the type rejects everything in between:
    
    
    // Bind to an agent — the shared instance from the registry. The thread comes
    // from the surrounding chat configuration.
    const { agent } = useAgent();
    const { agent } = useAgent({ agentId: "default" });
    
    // Bind a private agent to a thread — all three properties are required.
    const { agent } = useAgent({
      agentId: "chat-1",          // local id to register the private agent under
      runtimeAgentId: "default",  // the runtime agent it routes to
      threadId: "thread-abc",     // the thread to pin it to
    });

Partial combinations do not compile. `useAgent({ agentId, threadId })`, `useAgent({ agentId, runtimeAgentId })` and `useAgent({ runtimeAgentId, threadId })` are all type errors.

A runtime agent registered under a given id is a singleton. Writing a per-hook `threadId` straight onto it would let two `useAgent` calls that share an `agentId` clobber each other's thread, so scoping a thread requires a private agent to pin it to.

Use the second shape when several frontend agents — one per open thread, for instance — have to mount against a single runtime agent. `runtimeAgentId` registers a proxied agent through `CopilotKitCore.registerProxiedAgent`, so each hook gets its own instance instead of a shared one.

## Parameters

Prop

Type

`options?`UseAgentProps

## Return Value

Prop

Type

`object?`{ agent: AbstractAgent; isReady: boolean }

## Usage

### Basic Usage
    
    
    function AgentStatus() {
      const { agent } = useAgent();
    
      return (
        <div>
          <div>Agent: {agent.agentId}</div>
          <div>Messages: {agent.messages.length}</div>
          <div>Running: {agent.isRunning ? "Yes" : "No"}</div>
        </div>
      );
    }

### Accessing and Updating State
    
    
    function StateController() {
      const { agent } = useAgent();
    
      return (
        <div>
          <pre>{JSON.stringify(agent.state, null, 2)}</pre>
          <button onClick={() => agent.setState({ ...agent.state, count: 1 })}>
            Update State
          </button>
        </div>
      );
    }

### Event Subscription
    
    
    function EventListener() {
      const { agent, isReady } = useAgent();
    
      useEffect(() => {
        // Guard on `isReady` so the subscription lands on the real agent rather
        // than the provisional one shown while the runtime is still connecting.
        // Depending on `agent` re-subscribes automatically once the real agent
        // is bound.
        if (!isReady) return;
    
        const { unsubscribe } = agent.subscribe({
          onRunStartedEvent: () => console.log("Started"),
          onRunFinalized: () => console.log("Finished"),
        });
    
        return unsubscribe;
      }, [agent, isReady]);
    
      return null;
    }

### Multiple Agents
    
    
    function MultiAgentView() {
      const { agent: primary } = useAgent({ agentId: "primary" });
      const { agent: support } = useAgent({ agentId: "support" });
    
      return (
        <div>
          <div>Primary: {primary.messages.length} messages</div>
          <div>Support: {support.messages.length} messages</div>
        </div>
      );
    }

### Thread-scoped Agent

Use the thread-scoped form when one runtime agent needs multiple independent frontend instances, for example one per open conversation. The local `agentId` must be unique in the current provider.
    
    
    function ThreadPreview({ threadId }: { threadId: string }) {
      const { agent, isReady } = useAgent({
        agentId: `preview-${threadId}`,
        runtimeAgentId: "support",
        threadId,
        throttleMs: 100,
      });
    
      if (!isReady) return <div>Loading...</div>;
    
      return <div>{agent.messages.length} messages</div>;
    }

### Optimizing Re-renders
    
    
    // Only re-render when messages change
    function MessageCount() {
      const { agent } = useAgent({
        updates: [UseAgentUpdate.OnMessagesChanged],
      });
    
      return <div>Messages: {agent.messages.length}</div>;
    }

## Behavior

  * **Automatic Re-renders** : Component re-renders when agent state, messages, or execution status changes (configurable via `updates` parameter)
  * **Readiness** : While the runtime is connecting, `agent` is a fully-constructed provisional stand-in and `isReady` is `false`; once the runtime syncs, `agent` swaps to the real instance and `isReady` becomes `true`. Guard on `isReady` for work that must target the real agent (e.g. one-time subscriptions)
  * **Error Handling** : Throws error if no agent exists with specified `agentId`
  * **State Synchronization** : State updates via `setState()` are immediately available to both app and agent
  * **Event Subscriptions** : Subscribe/unsubscribe pattern for lifecycle and custom events



## Related

  * [AG-UI AbstractAgent](https://docs.ag-ui.com/sdk/js/client/abstract-agent) \- Full agent interface documentation


