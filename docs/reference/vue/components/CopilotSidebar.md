---
url: https://docs.copilotkit.ai/reference/vue/components/CopilotSidebar/
title: CopilotSidebar
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:09.334509+00:00
---

# CopilotSidebar

> Source: https://docs.copilotkit.ai/reference/vue/components/CopilotSidebar/

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

# CopilotSidebar

Sidebar variant of CopilotChat that renders in a fixed side panel

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotSidebar` renders a fixed sidebar panel for chat interaction. It wraps [`CopilotChat`](https://docs.copilotkit.ai/reference/vue/components/CopilotChat) and provides sidebar-specific layout and open/close behavior. The sidebar includes a header with a title and a close button, and can be toggled via a floating toggle button.

Because it builds on `CopilotChat`, it resolves the agent, subscribes to messages and running state, manages suggestions, and wires input and transcription for you. You typically only need to pick the agent and, optionally, set the initial open state, width, or override one of the named slots.

The `sidebar` feature requires a license. When it is not licensed, the component renders an inline warning and logs a console warning. Visit [copilotkit.ai/pricing](https://copilotkit.ai/pricing) for details.

## Import
    
    
    <script setup lang="ts">
    import { CopilotSidebar } from "@copilotkit/vue/v2";
    import "@copilotkit/vue/styles.css";
    </script>

## Props

All reactive props are declared with `defineProps`. `CopilotSidebar` extends the `CopilotChat` props (and through them the inherited `CopilotChatView` props) and adds two of its own.

### Own props

Prop

Type

`defaultOpen?`boolean

Prop

Type

`width?`number | string

### Inherited CopilotChat props

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

`CopilotSidebar` re-emits the chat events from `CopilotChat` (listen with `@event-name` in templates). These fire in addition to the component's internal handling.

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

Vue uses named slots in place of React's render props and sub-component props. Provide a slot to replace the corresponding piece of the sidebar. Each slot receives scoped props you can destructure with `v-slot`.

Prop

Type

`header?`{ title: string; onClose: () => void; isOpen: boolean }

Prop

Type

`toggle-button?`{ isOpen: boolean; toggle: () => void; open: () => void; close: () => void }

Prop

Type

`chat-view?`CopilotChatViewOverrideSlotProps

Prop

Type

`message-view?`{ messages: Message[]; isRunning: boolean }

Prop

Type

`input?`CopilotSidebarWelcomeScreenInputSlotProps

Prop

Type

`suggestion-view?`CopilotSidebarWelcomeScreenSuggestionViewSlotProps

Prop

Type

`welcome-screen?`CopilotChatWelcomeScreenSlotProps

Prop

Type

`welcome-message?`() => unknown

The sidebar welcome screen lays out suggestions at the top, the welcome message in the middle, and the input fixed at the bottom. Override the `welcome-screen` slot to replace this layout entirely, or `welcome-message` to change just the greeting.

## Usage

### Basic usage
    
    
    <script setup lang="ts">
    import { CopilotSidebar } from "@copilotkit/vue/v2";
    import "@copilotkit/vue/styles.css";
    </script>
    
    <template>
      <CopilotSidebar
        agent-id="my-agent"
        :labels="{ chatInputPlaceholder: 'Ask me anything...' }"
      />
    </template>

### Closed on mount with a custom width
    
    
    <script setup lang="ts">
    import { CopilotSidebar } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotSidebar agent-id="my-agent" :default-open="false" :width="500" />
    </template>

### Custom header
    
    
    <script setup lang="ts">
    import { CopilotSidebar } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotSidebar agent-id="my-agent">
        <template #header="{ title, onClose }">
          <div class="flex items-center justify-between bg-indigo-700 px-4 py-3 text-white">
            <span>{{ title }}</span>
            <button @click="onClose">Close</button>
          </div>
        </template>
      </CopilotSidebar>
    </template>

### Custom toggle button
    
    
    <script setup lang="ts">
    import { CopilotSidebar } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotSidebar agent-id="my-agent">
        <template #toggle-button="{ isOpen, toggle }">
          <button class="fixed bottom-6 right-6" @click="toggle">
            {{ isOpen ? "Close chat" : "Open chat" }}
          </button>
        </template>
      </CopilotSidebar>
    </template>

### Observing events
    
    
    <script setup lang="ts">
    import { CopilotSidebar } from "@copilotkit/vue/v2";
    
    function onSubmit(value: string) {
      console.log("user submitted:", value);
    }
    </script>
    
    <template>
      <CopilotSidebar agent-id="my-agent" @submit-message="onSubmit" />
    </template>

## Related

  * [`CopilotChat`](https://docs.copilotkit.ai/reference/vue/components/CopilotChat) \- the base chat component used internally
  * [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider) \- provides the agent configuration `CopilotSidebar` connects to
  * [`useAgent`](https://docs.copilotkit.ai/reference/vue/hooks/useAgent) \- composable used internally to resolve the agent


