---
url: https://docs.copilotkit.ai/reference/vue/hooks/useCapabilities/
title: useCapabilities
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:20.050066+00:00
---

# useCapabilities

> Source: https://docs.copilotkit.ai/reference/vue/hooks/useCapabilities/

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

# useCapabilities

Vue composable for reading an agent's declared capabilities

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useCapabilities` returns the [AG-UI `AgentCapabilities`](https://docs.ag-ui.com/concepts/capabilities) declared by an agent. Capabilities describe what an agent supports: tool calling, streaming, multi-agent coordination, human-in-the-loop, and more.

Capabilities are populated from the runtime `/info` response at connection time. The value is `undefined` until the runtime handshake completes or if the agent doesn't declare capabilities.

This composable returns a Vue `ComputedRef`. Read it with `.value` in `<script setup>`, or unwrapped directly in a `<template>`. The ref stays reactive, so it updates automatically once the runtime handshake populates capabilities.

## Signature
    
    
    import { useCapabilities } from "@copilotkit/vue/v2";
    
    function useCapabilities(agentId?: string): ComputedRef<AgentCapabilities | undefined>

## Parameters

Prop

Type

`agentId?`string

## Return Value

Prop

Type

`capabilities?`ComputedRef<AgentCapabilities | undefined>

## Usage

### Conditionally render UI based on capabilities

ToolPanel.vue
    
    
    <script setup lang="ts">
    import { useCapabilities } from "@copilotkit/vue/v2";
    
    const capabilities = useCapabilities();
    </script>
    
    <template>
      <!-- Hide the panel when the agent doesn't support tools -->
      <div v-if="capabilities?.tools?.supported">
        <h3>Tools</h3>
        <p v-if="capabilities.tools.clientProvided">
          This agent accepts client-provided tools.
        </p>
      </div>
    </template>

### Read capabilities for a specific agent

AgentInfo.vue
    
    
    <script setup lang="ts">
    import { useCapabilities } from "@copilotkit/vue/v2";
    
    const props = defineProps<{ agentId: string }>();
    
    const capabilities = useCapabilities(props.agentId);
    </script>
    
    <template>
      <p v-if="!capabilities">Loading capabilities...</p>
      <ul v-else>
        <li>Streaming: {{ capabilities.transport?.streaming ? "Yes" : "No" }}</li>
        <li>Tools: {{ capabilities.tools?.supported ? "Yes" : "No" }}</li>
        <li>Human-in-the-loop: {{ capabilities.humanInTheLoop?.supported ? "Yes" : "No" }}</li>
      </ul>
    </template>

### Read the value in script

Because the composable returns a `ComputedRef`, access the value with `.value` outside the template (for example inside a `watch` or computed):
    
    
    import { watch } from "vue";
    import { useCapabilities } from "@copilotkit/vue/v2";
    
    const capabilities = useCapabilities();
    
    watch(capabilities, (caps) => {
      if (caps?.tools?.supported) {
        console.log("Agent supports tools");
      }
    });

## Behavior

  * **Synchronous read.** The composable reads `capabilities` directly from the agent instance via [`useAgent`](https://docs.copilotkit.ai/reference/vue/hooks/useAgent). There is no separate loading state or async fetch: the value is `undefined` until the runtime `/info` handshake populates it, then becomes defined.
  * **Reactive computed.** The returned `ComputedRef` recomputes when the underlying agent ref changes, so your component (or watcher) updates once capabilities arrive.



## Related

  * [`useAgent`](https://docs.copilotkit.ai/reference/vue/hooks/useAgent) \- access the full agent instance (capabilities are derived from the agent)
  * [AG-UI Protocol](https://docs.ag-ui.com/concepts/capabilities) \- the protocol that defines the capabilities schema


