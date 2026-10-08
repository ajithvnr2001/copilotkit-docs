---
url: https://docs.copilotkit.ai/reference/vue/hooks/useCopilotChatConfiguration/
title: useCopilotChatConfiguration
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:20.630532+00:00
---

# useCopilotChatConfiguration

> Source: https://docs.copilotkit.ai/reference/vue/hooks/useCopilotChatConfiguration/

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

# useCopilotChatConfiguration

Vue 3 composable for reading reactive chat UI configuration and labels

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useCopilotChatConfiguration` is a Vue 3 composable that reads the chat configuration context injected by the nearest `CopilotChatConfigurationProvider`. That provider is mounted automatically by the CopilotKit chat components (`CopilotChat`, `CopilotPopup`, and `CopilotSidebar`) — `CopilotKitProvider` does **not** mount it — or you can mount it directly. It returns a `ComputedRef` that resolves to the current `CopilotChatConfigurationValue`, or `null` when no provider is present in the component tree.

Because the composable returns a `ComputedRef`, the value stays reactive: when labels, the active agent or thread, or the modal state change, the resolved value updates automatically. This provides a lightweight, reactive context for localized labels, agent/thread binding, and modal state used by the chat UI components.

Like all Vue composables, call `useCopilotChatConfiguration` synchronously inside `<script setup>` or a `setup()` function so the injection resolves against the surrounding component tree. The returned ref resolves to `null` when no `CopilotChatConfigurationProvider` (or a CopilotKit chat component that mounts one) is an ancestor, so guard against that case rather than assuming a value.

## CopilotChatConfigurationProvider

A provider component that injects localized labels, agent and thread IDs, and optional modal state for all descendant chat components. The CopilotKit chat components (`CopilotChat`, `CopilotPopup`, `CopilotSidebar`) mount one automatically, so you only need to mount it directly when you want to read configuration outside a chat component, or scope or override configuration for a subtree.

### Usage
    
    
    <script setup lang="ts">
    import { CopilotChatConfigurationProvider } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotChatConfigurationProvider
        :labels="{ chatInputPlaceholder: 'Ask me anything...' }"
        agent-id="my-agent"
        thread-id="thread-123"
        :is-modal-default-open="true"
      >
        <slot />
      </CopilotChatConfigurationProvider>
    </template>

### Props

Prop

Type

`labels?`Partial<CopilotChatLabels>

Prop

Type

`agentId?`string

Prop

Type

`threadId?`string

Prop

Type

`hasExplicitThreadId?`boolean

Prop

Type

`isModalDefaultOpen?`boolean

The provider renders its default `<slot />`, so descendant components placed inside it receive the injected configuration.

## useCopilotChatConfiguration

### Signature
    
    
    import { useCopilotChatConfiguration } from "@copilotkit/vue/v2";
    import type { ComputedRef } from "vue";
    import type { CopilotChatConfigurationValue } from "@copilotkit/vue/v2";
    
    function useCopilotChatConfiguration(): ComputedRef<CopilotChatConfigurationValue | null>;

### Parameters

This composable takes no parameters.

### Return Value

Returns a `ComputedRef`. Its `.value` is `null` when the composable is used outside any `CopilotChatConfigurationProvider`, and otherwise a `CopilotChatConfigurationValue` object:

Prop

Type

`labels?`CopilotChatLabels

Prop

Type

`agentId?`string

Prop

Type

`threadId?`string

Prop

Type

`hasExplicitThreadId?`boolean

Prop

Type

`isModalOpen?`boolean | undefined

Prop

Type

`setModalOpen?`((open: boolean) => void) | undefined

## CopilotChatLabels

The `CopilotChatLabels` type defines all customizable text strings used by the chat UI. The type is derived from `CopilotChatDefaultLabels`. The following keys are available with their default values:

Key| Default Value  
---|---  
`chatInputPlaceholder`| `"Type a message..."`  
`chatInputToolbarStartTranscribeButtonLabel`| `"Transcribe"`  
`chatInputToolbarCancelTranscribeButtonLabel`| `"Cancel"`  
`chatInputToolbarFinishTranscribeButtonLabel`| `"Finish"`  
`chatInputToolbarAddButtonLabel`| `"Add photos or files"`  
`chatInputToolbarToolsButtonLabel`| `"Tools"`  
`assistantMessageToolbarCopyCodeLabel`| `"Copy"`  
`assistantMessageToolbarCopyCodeCopiedLabel`| `"Copied"`  
`assistantMessageToolbarCopyMessageLabel`| `"Copy"`  
`assistantMessageToolbarThumbsUpLabel`| `"Good response"`  
`assistantMessageToolbarThumbsDownLabel`| `"Bad response"`  
`assistantMessageToolbarReadAloudLabel`| `"Read aloud"`  
`assistantMessageToolbarRegenerateLabel`| `"Regenerate"`  
`userMessageToolbarCopyMessageLabel`| `"Copy"`  
`userMessageToolbarEditMessageLabel`| `"Edit"`  
`chatDisclaimerText`| `"AI can make mistakes. Please verify important information."`  
`chatToggleOpenLabel`| `"Open chat"`  
`chatToggleCloseLabel`| `"Close chat"`  
`modalHeaderTitle`| `"CopilotKit Chat"`  
`welcomeMessageText`| `"How can I help you today?"`  
  
## Usage

### Reading Configuration in a Component

Call the composable once, then read from the returned ref. Guard against `null` for the case where no provider is present.
    
    
    <script setup lang="ts">
    import { useCopilotChatConfiguration } from "@copilotkit/vue/v2";
    
    const config = useCopilotChatConfiguration();
    </script>
    
    <template>
      <h2 v-if="config">{{ config.labels.modalHeaderTitle }}</h2>
      <h2 v-else>Chat</h2>
    </template>

### Basic Label Customization

Scope label overrides by mounting a provider around the chat UI.
    
    
    <script setup lang="ts">
    import { CopilotChatConfigurationProvider } from "@copilotkit/vue/v2";
    import ChatUI from "./ChatUI.vue";
    
    const labels = {
      chatInputPlaceholder: "Ask me anything...",
      modalHeaderTitle: "AI Assistant",
      welcomeMessageText: "Hello! What can I do for you?",
      chatDisclaimerText: "Responses are AI-generated.",
    };
    </script>
    
    <template>
      <CopilotChatConfigurationProvider :labels="labels">
        <ChatUI />
      </CopilotChatConfigurationProvider>
    </template>

### Binding to a Specific Agent and Thread
    
    
    <script setup lang="ts">
    import { CopilotChatConfigurationProvider } from "@copilotkit/vue/v2";
    import ChatWindow from "./ChatWindow.vue";
    </script>
    
    <template>
      <CopilotChatConfigurationProvider
        agent-id="support-agent"
        thread-id="ticket-456"
        :labels="{
          chatInputPlaceholder: 'Describe your issue...',
          modalHeaderTitle: 'Support Chat',
        }"
      >
        <ChatWindow />
      </CopilotChatConfigurationProvider>
    </template>

### Modal State Management

When a provider sets `is-modal-default-open`, descendants can read `isModalOpen` and call `setModalOpen`. Because the composable returns a `ComputedRef`, the toggle stays in sync automatically.
    
    
    <!-- App.vue -->
    <script setup lang="ts">
    import { CopilotChatConfigurationProvider } from "@copilotkit/vue/v2";
    import ToggleButton from "./ToggleButton.vue";
    import ChatModal from "./ChatModal.vue";
    </script>
    
    <template>
      <CopilotChatConfigurationProvider :is-modal-default-open="false">
        <ToggleButton />
        <ChatModal />
      </CopilotChatConfigurationProvider>
    </template>
    
    
    <!-- ToggleButton.vue -->
    <script setup lang="ts">
    import { useCopilotChatConfiguration } from "@copilotkit/vue/v2";
    
    const config = useCopilotChatConfiguration();
    
    function toggle() {
      const value = config.value;
      if (!value?.setModalOpen) return;
      value.setModalOpen(!value.isModalOpen);
    }
    </script>
    
    <template>
      <button v-if="config?.setModalOpen" @click="toggle">
        {{
          config.isModalOpen
            ? config.labels.chatToggleCloseLabel
            : config.labels.chatToggleOpenLabel
        }}
      </button>
    </template>

### Nested Providers

Providers can be nested. Child providers inherit and merge labels from their parent, with child overrides taking precedence.
    
    
    <script setup lang="ts">
    import { CopilotChatConfigurationProvider } from "@copilotkit/vue/v2";
    import SalesChat from "./SalesChat.vue";
    </script>
    
    <template>
      <CopilotChatConfigurationProvider
        :labels="{ chatDisclaimerText: 'Company-wide disclaimer.' }"
      >
        <CopilotChatConfigurationProvider
          agent-id="sales"
          :labels="{ modalHeaderTitle: 'Sales Assistant' }"
        >
          <!-- This context has both the company disclaimer and the sales title -->
          <SalesChat />
        </CopilotChatConfigurationProvider>
      </CopilotChatConfigurationProvider>
    </template>

## Behavior

  * **Reactive ref** : The composable returns a `ComputedRef<CopilotChatConfigurationValue | null>`. Read it via `config.value` in script and `config` (auto-unwrapped) in templates. The value recomputes whenever the injected configuration changes.
  * **Label merging** : Labels are merged in order: built-in defaults (`CopilotChatDefaultLabels`), then parent provider labels, then the current provider's labels. This allows partial overrides at any level.
  * **Agent ID resolution** : `agentId` resolves from the nearest provider, falling back to parent providers, then to the default agent ID (`"default"`).
  * **Thread ID generation** : If no `threadId` is provided at any level, a random UUID is generated and remains stable for the lifetime of the provider. `hasExplicitThreadId` reports whether the resolved thread ID was a caller choice rather than an internally minted UUID.
  * **Modal state ownership** : Modal state (`isModalOpen` / `setModalOpen`) is only created when a provider sets `isModalDefaultOpen`. Providers without this prop pass through the parent's modal state, and both fields are `undefined` when no provider owns modal state.
  * **Null resolution** : The returned ref resolves to `null` when used outside any `CopilotChatConfigurationProvider`, rather than throwing. Components should handle this case gracefully.



## Related

  * [`useCopilotKit`](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotKit) \- access the underlying CopilotKit instance
  * [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider) \- provides the CopilotKit instance to descendant composables (the chat configuration context is mounted by the chat components, not by `CopilotKitProvider`)


