---
url: https://docs.copilotkit.ai/reference/vue/components/CopilotChatView/
title: CopilotChatView
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:09.452893+00:00
---

# CopilotChatView

> Source: https://docs.copilotkit.ai/reference/vue/components/CopilotChatView/

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

# CopilotChatView

Vue 3 layout component that combines a scrollable transcript with the input area

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotChatView` is a Vue 3 component that combines a scrollable message transcript with the chat input area, suggestion pills, a scroll-to-bottom button, an attachment queue, and an optional welcome screen. It is the visual core of the chat interface and is used internally by the higher-level chat components in `@copilotkit/vue`.

Every visual piece of `CopilotChatView` is exposed as a named **slot** , so you can replace, style, or extend any part of the layout (this is the Vue equivalent of React's render-prop sub-component customization). The component drives its own behavior (auto-scroll, mobile keyboard handling, resize observation) and emits events for the actions a parent needs to handle.

## Import
    
    
    <script setup lang="ts">
    import { CopilotChatView } from "@copilotkit/vue/v2";
    </script>

`CopilotChatView` is a controlled, presentational component. It does not own the messages, agent state, or input value. When you use it standalone you must supply `messages`, react to its emitted events, and (optionally) drive the input value yourself.

## Example
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { CopilotChatView } from "@copilotkit/vue/v2";
    import type { Message } from "@ag-ui/core";
    
    const messages = ref<Message[]>([]);
    const isRunning = ref(false);
    
    function handleSubmit(value: string) {
      // append the user message, kick off your agent run, etc.
    }
    </script>
    
    <template>
      <CopilotChatView
        :messages="messages"
        :is-running="isRunning"
        auto-scroll="pin-to-bottom"
        @submit-message="handleSubmit"
      />
    </template>

## Props

Prop

Type

`messages?`Message[]

Prop

Type

`autoScroll?`AutoScrollMode | boolean

Prop

Type

`isRunning?`boolean

Prop

Type

`suggestions?`Suggestion[]

Prop

Type

`suggestionLoadingIndexes?`ReadonlyArray<number>

Prop

Type

`welcomeScreen?`boolean

Prop

Type

`attachments?`Attachment[]

Prop

Type

`dragOver?`boolean

Prop

Type

`inputValue?`string

Prop

Type

`inputMode?`CopilotChatInputMode

Prop

Type

`inputToolsMenu?`(ToolsMenuItem | "-")[]

Prop

Type

`isConnecting?`boolean

Prop

Type

`hasExplicitThreadId?`boolean

Prop

Type

`onRemoveAttachment?`(id: string) => void

Prop

Type

`onAddFile?`() => void

Prop

Type

`onDragOver?`(event: DragEvent) => void

Prop

Type

`onDragLeave?`(event: DragEvent) => void

Prop

Type

`onDrop?`(event: DragEvent) => void

Prop

Type

`onFinishTranscribeWithAudio?`(audioBlob: Blob) => void | Promise<void>

## Events

`CopilotChatView` emits the following events. Listen with `@event-name` in the template.

Prop

Type

`submit-message?`(value: string) => void

Prop

Type

`stop?`() => void

Prop

Type

`input-change?`(value: string) => void

Prop

Type

`select-suggestion?`(suggestion: Suggestion, index: number) => void

Prop

Type

`add-file?`() => void

Prop

Type

`start-transcribe?`() => void

Prop

Type

`cancel-transcribe?`() => void

Prop

Type

`finish-transcribe?`() => void

## Slots

Each named slot has a sensible default. Override a slot to replace, restyle, or extend that part of the layout. Slots receive scoped props (data and handlers) that the default implementation also consumes, so a replacement can reuse them.

Prop

Type

`message-view?`{ messages: Message[]; isRunning: boolean }

Prop

Type

`scroll-view?`{ messages: Message[]; isRunning: boolean; suggestions: Suggestion[]; loadingIndexes: ReadonlyArray<number>; messagePaddingBottom: string; showScrollToBottomButton: boolean; onSelectSuggestion: (suggestion, index) => void; onScroll: () => void; scrollToBottom: () => void }

Prop

Type

`feather?`() => unknown

Prop

Type

`scroll-to-bottom-button?`{ onClick: () => void }

Prop

Type

`interrupt?`{ event: InterruptEvent; result: unknown; resolve: (response: unknown) => void }

Prop

Type

`input?`{ modelValue: string; isRunning: boolean; inputMode: CopilotChatInputMode; inputToolsMenu: (ToolsMenuItem | '-')[]; attachments: Attachment[]; canStop: boolean; canAddFile: boolean; canTranscribe: boolean; onUpdateModelValue; onSubmitMessage; onStop; onAddFile; onStartTranscribe; onCancelTranscribe; onFinishTranscribe; onFinishTranscribeWithAudio }

Prop

Type

`suggestion-view?`{ suggestions: Suggestion[]; loadingIndexes: ReadonlyArray<number>; onSelectSuggestion: (suggestion, index) => void }

Prop

Type

`welcome-screen?`{ suggestions: Suggestion[]; loadingIndexes: ReadonlyArray<number>; attachments: Attachment[]; modelValue: string; isRunning: boolean; inputMode: CopilotChatInputMode; inputToolsMenu: (ToolsMenuItem | '-')[]; canStop: boolean; canAddFile: boolean; canTranscribe: boolean; onUpdateModelValue; onSubmitMessage; onStop; onAddFile; onStartTranscribe; onCancelTranscribe; onFinishTranscribe; onFinishTranscribeWithAudio; onSelectSuggestion }

Prop

Type

`welcome-message?`() => unknown

## Usage

### Standalone Usage
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { CopilotChatView } from "@copilotkit/vue/v2";
    import type { Message } from "@ag-ui/core";
    
    const messages = ref<Message[]>([]);
    const isRunning = ref(false);
    </script>
    
    <template>
      <CopilotChatView :messages="messages" :is-running="isRunning" />
    </template>

### Controlling the Input Value
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { CopilotChatView } from "@copilotkit/vue/v2";
    
    const inputValue = ref("");
    
    function handleInputChange(value: string) {
      inputValue.value = value;
    }
    
    function handleSubmit(value: string) {
      // send the message, then clear the input
      inputValue.value = "";
    }
    </script>
    
    <template>
      <CopilotChatView
        :input-value="inputValue"
        @input-change="handleInputChange"
        @submit-message="handleSubmit"
      />
    </template>

### Replacing a Slot
    
    
    <script setup lang="ts">
    import { CopilotChatView } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotChatView :messages="messages" :is-running="isRunning">
        <template #welcome-message>
          <h1 class="text-2xl font-semibold">How can I help you today?</h1>
        </template>
    
        <template #scroll-to-bottom-button="{ onClick }">
          <button type="button" @click="onClick">Jump to latest</button>
        </template>
      </CopilotChatView>
    </template>

### Custom Input via the `input` Slot
    
    
    <script setup lang="ts">
    import { CopilotChatView } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotChatView :messages="messages" :is-running="isRunning">
        <template #input="{ modelValue, onUpdateModelValue, onSubmitMessage }">
          <form @submit.prevent="onSubmitMessage(modelValue)">
            <input
              :value="modelValue"
              @input="onUpdateModelValue(($event.target as HTMLInputElement).value)"
            />
            <button type="submit">Send</button>
          </form>
        </template>
      </CopilotChatView>
    </template>

## Behavior

  * **Auto-scroll** : `pin-to-bottom` keeps the latest message visible while the user is at the bottom; `pin-to-send` anchors the latest user message near the top while the assistant streams. A scroll-to-bottom button appears when the user scrolls up.
  * **Welcome screen** : Rendered when `messages` is empty and the welcome screen is not suppressed by `welcomeScreen="false"`, `isConnecting`, or `hasExplicitThreadId`. The welcome screen embeds the input and suggestion slots.
  * **Input overlay positioning** : The input is rendered in an absolutely positioned overlay at the bottom of the chat, and the scroll content is padded to avoid overlap. The component measures the overlay height with a `ResizeObserver` and keeps the padding in sync.
  * **Mobile keyboard** : The view tracks the on-screen keyboard height so the input can translate above the keyboard on mobile devices.



## Related

  * [`useAgent`](https://docs.copilotkit.ai/reference/vue/hooks/useAgent) \-- access and subscribe to an AG-UI agent to drive the chat view
  * [`useSuggestions`](https://docs.copilotkit.ai/reference/vue/hooks/useSuggestions) \-- generate the suggestion pills shown by this view
  * [`useCopilotChatConfiguration`](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotChatConfiguration) \-- read the labels (including the welcome message text) consumed by the default slots


