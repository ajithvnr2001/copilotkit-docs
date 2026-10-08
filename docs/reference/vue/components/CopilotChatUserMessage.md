---
url: https://docs.copilotkit.ai/reference/vue/components/CopilotChatUserMessage/
title: CopilotChatUserMessage
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:09.508162+00:00
---

# CopilotChatUserMessage

> Source: https://docs.copilotkit.ai/reference/vue/components/CopilotChatUserMessage/

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

[Reference](https://docs.copilotkit.ai/reference)[vue](https://docs.copilotkit.ai/reference/vue)Components

# CopilotChatUserMessage

Vue 3 component for displaying user-authored messages with copy, edit, and branch navigation.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

This is the Vue 3 component. Import it from `@copilotkit/vue/v2`.

## Overview

`CopilotChatUserMessage` renders a user-authored message aligned to the right of the chat. The default message renderer flattens the message content to text and displays it with `white-space: pre-wrap` so line breaks and spacing are preserved.

Below the message it renders a toolbar containing a copy-to-clipboard button, an optional edit button, and optional branch navigation controls. The toolbar becomes visible on hover. The edit button is only shown when an `@edit-message` listener is attached, and the branch navigation is only shown when `numberOfBranches` is greater than 1 and a `@switch-to-branch` listener is attached.

## Example
    
    
    <script setup lang="ts">
    import { CopilotChatUserMessage } from "@copilotkit/vue/v2";
    import "@copilotkit/vue/styles.css";
    import type { UserMessage } from "@ag-ui/core";
    
    const message: UserMessage = {
      id: "1",
      role: "user",
      content: "What is the capital of France?",
    };
    </script>
    
    <template>
      <CopilotChatUserMessage :message="message" />
    </template>

## Props

Prop

Type

`message`UserMessage

Prop

Type

`branchIndex?`number

Prop

Type

`numberOfBranches?`number

## Events

The action callbacks are emitted as Vue events. Attaching a listener for an event also enables the corresponding control: the edit button only renders when an `@edit-message` listener is present, and the branch navigation only renders when a `@switch-to-branch` listener is present (and `numberOfBranches` is greater than 1).

Prop

Type

`edit-message?`(payload: { message: UserMessage }) => void

Prop

Type

`switch-to-branch?`(payload: { message: UserMessage; branchIndex: number; numberOfBranches: number }) => void

## Slots

Each slot exposes scoped slot props (handlers and state) and falls back to the default rendering when not provided. Use a named template (`<template #slot-name="...">`) to override a slot.

Prop

Type

`message-renderer?`{ message: UserMessage; content: string; isMultiline: boolean }

Prop

Type

`toolbar?`{ message: UserMessage; showBranchNavigation: boolean; hasEditAction: boolean }

Prop

Type

`toolbar-items?`(no props)

Prop

Type

`copy-button?`{ onCopy: () => Promise<void>; copied: boolean; label: string }

Prop

Type

`edit-button?`{ onEdit: () => void; label: string }

Prop

Type

`branch-navigation?`{ branchIndex: number; numberOfBranches: number; canGoPrev: boolean; canGoNext: boolean; goPrev: () => void; goNext: () => void }

Prop

Type

`layout?`{ message; content; isMultiline; showBranchNavigation; hasEditAction; branchIndex; numberOfBranches; canGoPrev; canGoNext; onCopy; onEdit; goPrev; goNext; copied }

## Usage

### Basic user message
    
    
    <script setup lang="ts">
    import { CopilotChatUserMessage } from "@copilotkit/vue/v2";
    import type { UserMessage } from "@ag-ui/core";
    
    defineProps<{ message: UserMessage }>();
    </script>
    
    <template>
      <CopilotChatUserMessage :message="message" />
    </template>

### With edit support
    
    
    <script setup lang="ts">
    import { CopilotChatUserMessage } from "@copilotkit/vue/v2";
    import type { UserMessage } from "@ag-ui/core";
    
    defineProps<{ message: UserMessage }>();
    
    function handleEdit(payload: { message: UserMessage }) {
      console.log("Edit", payload.message.id);
    }
    </script>
    
    <template>
      <CopilotChatUserMessage :message="message" @edit-message="handleEdit" />
    </template>

### With branch navigation
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { CopilotChatUserMessage } from "@copilotkit/vue/v2";
    import type { UserMessage } from "@ag-ui/core";
    
    defineProps<{ message: UserMessage; branches: UserMessage[] }>();
    
    const currentBranch = ref(0);
    
    function handleSwitch(payload: { branchIndex: number }) {
      currentBranch.value = payload.branchIndex;
    }
    </script>
    
    <template>
      <CopilotChatUserMessage
        :message="message"
        :branch-index="currentBranch"
        :number-of-branches="branches.length"
        @switch-to-branch="handleSwitch"
      />
    </template>

### Customizing appearance with slots
    
    
    <script setup lang="ts">
    import { CopilotChatUserMessage } from "@copilotkit/vue/v2";
    import type { UserMessage } from "@ag-ui/core";
    
    defineProps<{ message: UserMessage }>();
    </script>
    
    <template>
      <CopilotChatUserMessage
        :message="message"
        @edit-message="({ message }) => console.log('Edit:', message.id)"
      >
        <template #message-renderer="{ content }">
          <div class="rounded-2xl bg-blue-600 px-4 py-2 text-white">
            {{ content }}
          </div>
        </template>
        <template #toolbar-items>
          <button @click="$emit('pin')">Pin</button>
        </template>
      </CopilotChatUserMessage>
    </template>

### Full edit and branch workflow
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { CopilotChatUserMessage } from "@copilotkit/vue/v2";
    import type { UserMessage } from "@ag-ui/core";
    
    defineProps<{ message: UserMessage; branches: UserMessage[] }>();
    
    const currentBranch = ref(0);
    
    function openEditModal(message: UserMessage) {
      // open your edit modal
    }
    </script>
    
    <template>
      <CopilotChatUserMessage
        :message="message"
        :branch-index="currentBranch"
        :number-of-branches="branches.length"
        @switch-to-branch="({ branchIndex }) => (currentBranch = branchIndex)"
        @edit-message="({ message }) => openEditModal(message)"
      />
    </template>

## Behavior

  * **Right-aligned layout** : User messages are rendered with right-aligned positioning to visually distinguish them from assistant messages.
  * **Content flattening** : When `message.content` is an array of parts, the default renderer joins the `text` parts with newlines. String content is rendered as-is.
  * **Whitespace preservation** : The default message renderer uses `white-space: pre-wrap`, so line breaks and spacing are preserved. The bubble gets extra vertical padding when the content is multiline.
  * **Hover-revealed toolbar** : The toolbar is invisible by default and becomes visible when the message is hovered.
  * **Transient copied state** : After a successful copy, the copy button shows a check icon for 2 seconds before reverting.
  * **Conditional edit button** : The edit button only appears when an `@edit-message` listener is attached.
  * **Conditional branch navigation** : The branch navigation only appears when `numberOfBranches` is greater than 1 and a `@switch-to-branch` listener is attached.
  * **Localized labels** : Toolbar button tooltips are sourced from the nearest configuration provider. See [`useCopilotChatConfiguration`](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotChatConfiguration) for available label keys.



## Related

  * [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider) \- Supplies the CopilotKit context to descendant components.
  * [`useCopilotChatConfiguration`](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotChatConfiguration) \- Provider for localized toolbar labels.


