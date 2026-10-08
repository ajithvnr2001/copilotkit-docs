---
url: https://docs.copilotkit.ai/reference/vue/hooks/useAgent/
title: useAgent
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:20.915289+00:00
---

# useAgent

> Source: https://docs.copilotkit.ai/reference/vue/hooks/useAgent/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁VueSDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Components

[CopilotChat](https://docs.copilotkit.ai/reference/vue/components/CopilotChat)[CopilotChatAssistantMessage](https://docs.copilotkit.ai/reference/vue/components/CopilotChatAssistantMessage)[CopilotChatInput](https://docs.copilotkit.ai/reference/vue/components/CopilotChatInput)[CopilotChatMessageView](https://docs.copilotkit.ai/reference/vue/components/CopilotChatMessageView)[CopilotChatUserMessage](https://docs.copilotkit.ai/reference/vue/components/CopilotChatUserMessage)[CopilotChatView](https://docs.copilotkit.ai/reference/vue/components/CopilotChatView)[CopilotKitProvider](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider)[CopilotPopup](https://docs.copilotkit.ai/reference/vue/components/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/vue/components/CopilotSidebar)

Hooks

[useAgent](https://docs.copilotkit.ai/reference/vue/hooks/useAgent)[useAgentContext](https://docs.copilotkit.ai/reference/vue/hooks/useAgentContext)[useCapabilities](https://docs.copilotkit.ai/reference/vue/hooks/useCapabilities)[useComponent](https://docs.copilotkit.ai/reference/vue/hooks/useComponent)[useConfigureSuggestions](https://docs.copilotkit.ai/reference/vue/hooks/useConfigureSuggestions)[useCopilotChatConfiguration](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotChatConfiguration)[useCopilotKit](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotKit)[useDefaultRenderTool](https://docs.copilotkit.ai/reference/vue/hooks/useDefaultRenderTool)[useFrontendTool](https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool)[useHumanInTheLoop](https://docs.copilotkit.ai/reference/vue/hooks/useHumanInTheLoop)[useInterrupt](https://docs.copilotkit.ai/reference/vue/hooks/useInterrupt)[useRenderTool](https://docs.copilotkit.ai/reference/vue/hooks/useRenderTool)[useSuggestions](https://docs.copilotkit.ai/reference/vue/hooks/useSuggestions)[useThreads](https://docs.copilotkit.ai/reference/vue/hooks/useThreads)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[vue](https://docs.copilotkit.ai/reference/vue)Hooks

# useAgent

Vue 3 composable for accessing AG-UI agent instances

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useAgent` is a Vue 3 composable that returns a reactive reference to an [AG-UI AbstractAgent](https://docs.ag-ui.com/sdk/js/client/abstract-agent) instance. The composable subscribes to agent changes and triggers reactive updates when the agent's state, messages, or execution status changes.

The composable returns `{ agent }`, where `agent` is a Vue `shallowRef<AbstractAgent | null>` — it is `null` until an agent resolves. (If the agent cannot be resolved for the given `agentId` after the runtime syncs, the composable throws rather than leaving `agent` as `null`.) Access the underlying instance with `agent.value` in `<script setup>`, or rely on auto-unwrapping in `<template>`, and guard with `agent?.` / `agent.value?.` for the unresolved case.

Throws an error if no agent can be resolved for the given `agentId` after the runtime has synced (for example, when the id does not match any agent reported by your runtime `/info` or registered via `agents__unsafe_dev_only`).

## Signature
    
    
    import { useAgent } from "@copilotkit/vue/v2";
    import type { ShallowRef } from "vue";
    import type { AbstractAgent } from "@ag-ui/client";
    
    function useAgent(props?: UseAgentProps): {
      agent: ShallowRef<AbstractAgent | null>;
    };

## Parameters

All reactive inputs accept `MaybeRefOrGetter`, so you can pass a plain value, a `ref`, or a getter function and the composable will re-resolve when it changes.

Prop

Type

`props?`UseAgentProps

## Return Value

Prop

Type

`object?`{ agent: ShallowRef<AbstractAgent | null> }

## Usage

### Basic Usage
    
    
    <script setup lang="ts">
    import { useAgent } from "@copilotkit/vue/v2";
    
    const { agent } = useAgent();
    </script>
    
    <template>
      <div v-if="agent">
        <div>Agent: {{ agent.agentId }}</div>
        <div>Messages: {{ agent.messages.length }}</div>
        <div>Running: {{ agent.isRunning ? "Yes" : "No" }}</div>
      </div>
    </template>

### Accessing and Updating State
    
    
    <script setup lang="ts">
    import { useAgent } from "@copilotkit/vue/v2";
    
    const { agent } = useAgent();
    
    function updateState() {
      if (!agent.value) return;
      agent.value.setState({ ...agent.value.state, count: 1 });
    }
    </script>
    
    <template>
      <div>
        <pre>{{ JSON.stringify(agent?.state, null, 2) }}</pre>
        <button @click="updateState">Update State</button>
      </div>
    </template>

### Event Subscription
    
    
    <script setup lang="ts">
    import { watchEffect } from "vue";
    import { useAgent } from "@copilotkit/vue/v2";
    
    const { agent } = useAgent();
    
    watchEffect((onCleanup) => {
      if (!agent.value) return;
      const { unsubscribe } = agent.value.subscribe({
        onRunStartedEvent: () => console.log("Started"),
        onRunFinalized: () => console.log("Finished"),
      });
    
      onCleanup(unsubscribe);
    });
    </script>
    
    <template>
      <div />
    </template>

### Multiple Agents
    
    
    <script setup lang="ts">
    import { useAgent } from "@copilotkit/vue/v2";
    
    const { agent: primary } = useAgent({ agentId: "primary" });
    const { agent: support } = useAgent({ agentId: "support" });
    </script>
    
    <template>
      <div>
        <div>Primary: {{ primary?.messages?.length ?? 0 }} messages</div>
        <div>Support: {{ support?.messages?.length ?? 0 }} messages</div>
      </div>
    </template>

### Per-Thread Agents
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { useAgent } from "@copilotkit/vue/v2";
    
    const threadId = ref("thread-1");
    
    // Each thread id resolves an independent agent clone with its own
    // messages and state.
    const { agent } = useAgent({ agentId: "default", threadId });
    </script>
    
    <template>
      <div v-if="agent">Thread: {{ agent.threadId }} ({{ agent.messages.length }} messages)</div>
    </template>

### Optimizing Reactive Updates
    
    
    <script setup lang="ts">
    import { useAgent, UseAgentUpdate } from "@copilotkit/vue/v2";
    
    // Only update when messages change.
    const { agent } = useAgent({
      updates: [UseAgentUpdate.OnMessagesChanged],
    });
    </script>
    
    <template>
      <div>Messages: {{ agent?.messages?.length ?? 0 }}</div>
    </template>

### Throttling High-Frequency Updates
    
    
    import { useAgent } from "@copilotkit/vue/v2";
    
    // Coalesce streaming message and state updates into at most one update
    // per 100ms. Run lifecycle callbacks still fire immediately.
    const { agent } = useAgent({ throttleMs: 100 });

## Behavior

  * **Reactive updates** : The `agent` ref triggers reactivity when state, messages, or execution status changes (configurable via the `updates` parameter).
  * **Reactive inputs** : `agentId`, `threadId`, and `throttleMs` accept `MaybeRefOrGetter`. The composable re-resolves and re-subscribes when they change, and also re-resolves when the runtime connection status or available agents change.
  * **Per-thread clones** : When `threadId` is set, the composable resolves a per-thread clone of the agent so each thread keeps independent messages and state.
  * **Throttling** : Message and state updates can be throttled via `throttleMs`, resolved as `throttleMs ?? provider defaultThrottleMs ?? 0`. Run lifecycle callbacks always fire immediately.
  * **Error handling** : Throws an error if no agent can be resolved for the specified `agentId` after the runtime has synced.
  * **State synchronization** : State updates via `setState()` are immediately available to both app and agent.



## Related

  * [AG-UI AbstractAgent](https://docs.ag-ui.com/sdk/js/client/abstract-agent) \- full agent interface documentation


