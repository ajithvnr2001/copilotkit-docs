---
url: https://docs.copilotkit.ai/reference/vue/hooks/useThreads/
title: useThreads
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:25.165220+00:00
---

# useThreads

> Source: https://docs.copilotkit.ai/reference/vue/hooks/useThreads/

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

# useThreads

Vue 3 composable for listing, managing, and syncing conversation threads with useThreads -- rename, archive, delete, and paginate threads with realtime updates.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

[useThreads needs a CopilotKit Intelligence projectConnect your runtime to a cloud-hosted project to start syncing threads.Start cloud-hosted setup](https://ssr-placeholder.invalid/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_reference_vue_use_threads)

## Overview

`useThreads` is a Vue 3 composable for managing conversation threads in CopilotKit Intelligence. It fetches the thread list for a given agent, keeps it synchronized in realtime via the core thread store's realtime channel, and exposes mutation methods for renaming, archiving, and deleting threads.

Threads are sorted by recency — by `lastRunAt` when present, falling back to `updatedAt`, then `createdAt` (most recent first). The composable supports cursor-based pagination when a `limit` is provided. All inputs accept refs, computeds, or getters (`MaybeRefOrGetter`), so changing the thread context reactively re-fetches the list.

Return values are Vue refs and computeds. Read them with `.value` in `<script setup>`, or unwrap them automatically in `<template>`.

## Signature
    
    
    import { useThreads } from "@copilotkit/vue/v2";
    
    function useThreads(input: UseThreadsInput): UseThreadsResult

## Parameters

Prop

Type

`input?`UseThreadsInput

## Return Value

Prop

Type

`result?`UseThreadsResult

## Usage

ThreadList.vue
    
    
    <script setup lang="ts">
    import { useThreads } from "@copilotkit/vue/v2"; 
    
    const {
      threads,
      isLoading,
      renameThread,
      archiveThread,
      deleteThread,
    } = useThreads({ agentId: "my-agent" }); 
    </script>
    
    <template>
      <div v-if="isLoading">Loading threads...</div>
      <ul v-else>
        <li v-for="thread in threads" :key="thread.id">
          <span>{{ thread.name ?? "Untitled" }}</span>
          <button @click="renameThread(thread.id, 'New name')">Rename</button>
          <button @click="archiveThread(thread.id)">Archive</button>
          <button @click="deleteThread(thread.id)">Delete</button>
        </li>
      </ul>
    </template>

### Reactive agent context

Because inputs accept refs and getters, you can drive the thread list from reactive state. Switching `agentId` automatically re-fetches the list.

ReactiveThreads.vue
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { useThreads } from "@copilotkit/vue/v2";
    
    const agentId = ref("support-agent");
    const includeArchived = ref(false);
    
    const { threads, hasMoreThreads, fetchMoreThreads } = useThreads({
      agentId, // ref -- changing it re-fetches threads
      includeArchived,
      limit: 20,
    });
    </script>
    
    <template>
      <select v-model="agentId">
        <option value="support-agent">Support</option>
        <option value="sales-agent">Sales</option>
      </select>
    
      <label>
        <input type="checkbox" v-model="includeArchived" />
        Show archived
      </label>
    
      <ul>
        <li v-for="thread in threads" :key="thread.id">
          {{ thread.name ?? "Untitled" }}
        </li>
      </ul>
    
      <button v-if="hasMoreThreads" @click="fetchMoreThreads">Load more</button>
    </template>

## Behavior

  * On mount, fetches the thread list and establishes a realtime subscription via the core thread store.
  * Thread creates, renames, archives, and deletes from any client are reflected immediately without polling.
  * All mutation methods use **pessimistic updates** : the list updates only after the server confirms the operation, not immediately on dispatch. Promises resolve on confirmation and reject on failure.
  * The composable defers its first fetch until the runtime reports a Connected status, so it issues a single list request plus a single subscribe request rather than refetching once realtime details resolve.
  * While the runtime is connecting (a runtime URL is set but no context has been dispatched yet), `isLoading` stays `true` to avoid an empty-list flash.
  * When no runtime URL is configured, `error` reports a configuration error and the thread store is cleared.
  * The `threads` array stays sorted by recency descending — by `lastRunAt` when present, falling back to `updatedAt`, then `createdAt`.
  * New threads are **automatically named** by the LLM after their first run (a 2 to 5 word title). This is configurable via `generateThreadNames` on the runtime.
  * The composable cleans up its store subscriptions and stops the store automatically when the owning scope is disposed (`onScopeDispose`).



## Next steps

### [CopilotKitProviderConfigure the runtime URL that powers thread syncing. For cloud-hosted Intelligence, keep `CPK_INTELLIGENCE_API_KEY` on the runtime server.](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider)### [useAgentAccess and run the agent whose threads you are listing.](https://docs.copilotkit.ai/reference/vue/hooks/useAgent)
