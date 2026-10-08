---
url: https://docs.copilotkit.ai/reference/v1/hooks/useAgent/
title: useAgent
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:58.144476+00:00
---

# useAgent

> Source: https://docs.copilotkit.ai/reference/v1/hooks/useAgent/

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

# useAgent

React hook for accessing AG-UI agent instances

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

`useAgent` is a v2 API, exported from `@copilotkit/react-core/v2`. See the [v2 `useAgent` reference](https://docs.copilotkit.ai/reference/v2/hooks/useAgent) for the full, up-to-date documentation.

## Overview

`useAgent` is a React hook that returns an [AG-UI AbstractAgent](https://docs.ag-ui.com/sdk/js/client/abstract-agent) instance. The hook subscribes to agent state changes and triggers re-renders when the agent's state, messages, or execution status changes.

**Throws error** if no agent is configured with the specified `agentId`.

## Signature
    
    
    function useAgent(options?: UseAgentProps): { agent: AbstractAgent }

## Parameters

Prop

Type

`options?`UseAgentProps

## Return Value

Prop

Type

`object?`{ agent: AbstractAgent }

## Usage

### Basic Usage
    
    
    import { useAgent } from "@copilotkit/react-core/v2";
    
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

### Accessing State
    
    
    function StateDisplay() {
      const { agent } = useAgent();
    
      return <pre>{JSON.stringify(agent.state, null, 2)}</pre>;
    }

### Updating State
    
    
    function StateController() {
      const { agent } = useAgent();
    
      return (
        <button onClick={() => agent.setState({ ...agent.state, count: 1 })}>
          Increment
        </button>
      );
    }

### Event Subscription
    
    
    import { useEffect } from "react";
    import { useAgent } from "@copilotkit/react-core/v2";
    import type { AgentSubscriber } from "@ag-ui/client";
    
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
    
    
    function MultiAgentView() {
      const { agent: primary } = useAgent({ agentId: "primary" });
      const { agent: support } = useAgent({ agentId: "support" });
    
      return (
        <div>
          <div>Primary: {primary.messages.length}</div>
          <div>Support: {support.messages.length}</div>
        </div>
      );
    }

### Optimizing Re-renders

Control when your component re-renders using the `updates` parameter:
    
    
    import { useAgent, UseAgentUpdate } from "@copilotkit/react-core/v2";
    
    // Only re-render when messages change
    function MessageCount() {
      const { agent } = useAgent({
        updates: [UseAgentUpdate.OnMessagesChanged]
      });
    
      return <div>Messages: {agent.messages.length}</div>;
    }
    
    // Manually manage subscriptions (no automatic re-renders)
    function ManualSubscription() {
      const { agent } = useAgent({ updates: [] });
    
      useEffect(() => {
        const { unsubscribe } = agent.subscribe({
          onMessagesChanged: () => {
            // Handle changes manually
          }
        });
        return unsubscribe;
      }, [agent]);
    
      return <div>Manual mode</div>;
    }

## Behavior

  * **Automatic Re-renders** : Component re-renders when agent state, messages, or execution status changes (configurable via `updates` parameter)
  * **Error Handling** : Throws error if no agent exists with specified `agentId`
  * **State Synchronization** : State updates via `setState()` are immediately available to both app and agent
  * **Event Subscriptions** : Subscribe/unsubscribe pattern for lifecycle and custom events



## Related

  * [AG-UI AbstractAgent](https://docs.ag-ui.com/sdk/js/client/abstract-agent) \- Full agent interface documentation


