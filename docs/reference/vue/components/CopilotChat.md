---
url: https://docs.copilotkit.ai/reference/vue/components/CopilotChat/
title: CopilotChat
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:06.473802+00:00
---

# CopilotChat

> Source: https://docs.copilotkit.ai/reference/vue/components/CopilotChat/

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

# CopilotChat

Vue 3 component that connects an agent to a chat view

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotChat` is a high-level chat container that wires an agent into [`CopilotChatView`](https://docs.copilotkit.ai/reference/vue/components/CopilotChatView) while providing configuration context. It resolves the agent via [`useAgent`](https://docs.copilotkit.ai/reference/vue/hooks/useAgent), subscribes to the agent's messages and running state, manages suggestions, handles input value and audio transcription, wires file attachments, and auto-clears the input after a message is submitted.

You typically only need to specify which agent to connect and, optionally, customize labels or override one of the named slots.

`CopilotChat` also exposes the underlying layout component as `CopilotChat.View`, which is the same component documented at [`CopilotChatView`](https://docs.copilotkit.ai/reference/vue/components/CopilotChatView). Use it directly when you want the layout without the agent wiring.

## Import
    
    
    <script setup lang="ts">
    import { CopilotChat } from "@copilotkit/vue/v2";
    import "@copilotkit/vue/styles.css";
    </script>

## Props

All reactive props are declared with `defineProps`. `CopilotChat` extends `CopilotChatView` props but omits the ones it manages internally (`messages`, `isRunning`, `suggestions`, `suggestionLoadingIndexes`, `attachments`, `onRemoveAttachment`, `onAddFile`, `dragOver`, `onDragOver`, `onDragLeave`, `onDrop`).

### Own props

Prop

Type

`agentId?`string

Prop

Type

`threadId?`string

Prop

Type

`throttleMs?`number

Prop

Type

`labels?`Partial<CopilotChatLabels>

Prop

Type

`attachments?`AttachmentsConfig

Prop

Type

`onError?`(event: { error: Error; code: CopilotKitCoreErrorCode; context: Record<string, any> }) => void | Promise<void>

### Inherited CopilotChatView props

Prop

Type

`autoScroll?`AutoScrollMode | boolean

Prop

Type

`welcomeScreen?`boolean

Prop

Type

`inputValue?`string

Prop

Type

`inputMode?`"input" | "transcribe" | "processing"

Prop

Type

`inputToolsMenu?`(ToolsMenuItem | "-")[]

Prop

Type

`onFinishTranscribeWithAudio?`(audioBlob: Blob) => void | Promise<void>

## Events

`CopilotChat` emits the following events (listen with `@event-name` in templates). These fire in addition to the component's internal handling, so you can observe interactions without disabling default behavior.

Event| Payload| Fired when  
---|---|---  
`submit-message`| `value: string`| A message is submitted  
`stop`| none| The stop button is pressed  
`input-change`| `value: string`| The input value changes  
`select-suggestion`| `suggestion: Suggestion, index: number`| A suggestion pill is selected  
`add-file`| none| The add-file action is triggered  
`start-transcribe`| none| Audio transcription starts  
`cancel-transcribe`| none| Audio transcription is cancelled  
`finish-transcribe`| none| Audio transcription finishes  
  
## Slots

Vue uses named slots in place of React's render props and sub-component props. Provide a slot to replace the corresponding piece of the chat. Each slot receives scoped props you can destructure with `v-slot`. Any slot not listed below is forwarded down through `CopilotChatView` to the message view.

Prop

Type

`chat-view?`CopilotChatViewOverrideSlotProps

Prop

Type

`message-view?`{ messages: Message[]; isRunning: boolean }

Prop

Type

`input?`CopilotChatInputSlotProps

Prop

Type

`suggestion-view?`CopilotChatSuggestionViewSlotProps

Prop

Type

`welcome-screen?`CopilotChatWelcomeScreenSlotProps

Prop

Type

`welcome-message?`() => unknown

Prop

Type

`interrupt?`CopilotChatInterruptSlotProps

Slots forwarded to the message view (for example custom assistant- or user-message slots) are passed straight through and rendered by `CopilotChatMessageView`. See [`CopilotChatView`](https://docs.copilotkit.ai/reference/vue/components/CopilotChatView) for the full set of layout-level slots such as `scroll-view`, `feather`, and `scroll-to-bottom-button`.

## Usage

### Basic usage
    
    
    <script setup lang="ts">
    import { CopilotChat } from "@copilotkit/vue/v2";
    import "@copilotkit/vue/styles.css";
    </script>
    
    <template>
      <CopilotChat
        agent-id="my-agent"
        :labels="{ chatInputPlaceholder: 'Ask me anything...' }"
      />
    </template>

### Custom welcome screen
    
    
    <script setup lang="ts">
    import { CopilotChat } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotChat agent-id="my-agent">
        <template #welcome-screen="{ onSubmitMessage, suggestions, onSelectSuggestion }">
          <div class="flex h-full flex-col items-center justify-center gap-4">
            <h2>Welcome to the assistant</h2>
            <button
              v-for="(suggestion, index) in suggestions"
              :key="index"
              @click="onSelectSuggestion(suggestion, index)"
            >
              {{ suggestion.title }}
            </button>
          </div>
        </template>
      </CopilotChat>
    </template>

### Observing events
    
    
    <script setup lang="ts">
    import { CopilotChat } from "@copilotkit/vue/v2";
    
    function onSubmit(value: string) {
      console.log("user submitted:", value);
    }
    </script>
    
    <template>
      <CopilotChat agent-id="my-agent" @submit-message="onSubmit" />
    </template>

### Using the layout directly

`CopilotChat.View` is the layout component without agent wiring. Use it when you manage `messages` and handlers yourself.
    
    
    <script setup lang="ts">
    import { CopilotChat } from "@copilotkit/vue/v2";
    import { ref } from "vue";
    
    // Vue SFC templates cannot resolve dotted tags like `<CopilotChat.View>`,
    // so alias the layout to a local component first.
    const ChatView = CopilotChat.View;
    
    const messages = ref([]);
    
    function handleSubmit(value: string) {
      // manage your own message state
    }
    </script>
    
    <template>
      <ChatView :messages="messages" @submit-message="handleSubmit" />
    </template>

## Related

  * [`CopilotChatView`](https://docs.copilotkit.ai/reference/vue/components/CopilotChatView) \- the layout component used internally (also exposed as `CopilotChat.View`)
  * [`useAgent`](https://docs.copilotkit.ai/reference/vue/hooks/useAgent) \- composable used internally to resolve the agent
  * [`useSuggestions`](https://docs.copilotkit.ai/reference/vue/hooks/useSuggestions) \- composable that powers the suggestion pills
  * [`useCopilotChatConfiguration`](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotChatConfiguration) \- reads the labels, agent id, and thread id provided by `CopilotChat`


