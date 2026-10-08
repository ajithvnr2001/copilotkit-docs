---
url: https://docs.copilotkit.ai/reference/vue/components/CopilotChatMessageView/
title: CopilotChatMessageView
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:09.385587+00:00
---

# CopilotChatMessageView

> Source: https://docs.copilotkit.ai/reference/vue/components/CopilotChatMessageView/

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

# CopilotChatMessageView

Vue 3 component for rendering a list of chat messages

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotChatMessageView` renders a list of chat messages and, optionally, a typing cursor while the agent is running. It dispatches each message to a default child component based on its `role` (assistant, user, or reasoning) and exposes named slots so you can replace or wrap that rendering. A pulsing cursor is shown after the last message while `isRunning` is `true`.

Unlike the React reference component, customization in Vue is driven entirely through named slots rather than render props or a slot-prop system. The component also surfaces slots for interrupts, activity messages, tool calls, and custom message renderers registered on the CopilotKit instance.

## Import
    
    
    <script setup lang="ts">
    import { CopilotChatMessageView } from "@copilotkit/vue/v2";
    import "@copilotkit/vue/styles.css";
    </script>

## Example
    
    
    <script setup lang="ts">
    import { CopilotChatMessageView } from "@copilotkit/vue/v2";
    import { useAgent } from "@copilotkit/vue/v2";
    
    const { agent } = useAgent();
    </script>
    
    <template>
      <copilot-chat-message-view
        :messages="agent?.messages ?? []"
        :is-running="agent?.isRunning ?? false"
      />
    </template>

## Props

Prop

Type

`messages?`Message[]

Prop

Type

`isRunning?`boolean

Attributes that are not declared props (such as `class`, `style`, or `data-*`) are forwarded to the component's root `<div>` via `v-bind="$attrs"`.

## Slots

Each slot below is named. Use a `<template #slot-name="slotProps">` block to override or wrap the default rendering. Where a slot has a default, omitting it falls back to the built-in child component.

Prop

Type

`assistant-message?`{ message: AssistantMessage; messages: Message[]; isRunning: boolean }

Prop

Type

`user-message?`{ message: UserMessage }

Prop

Type

`reasoning-message?`{ message: ReasoningMessage; messages: Message[]; isRunning: boolean }

Prop

Type

`cursor?`() => unknown

Prop

Type

`interrupt?`{ event: unknown; result: unknown; resolve: (value: unknown) => void }

Prop

Type

`message-before?`{ message: Message; position: 'before'; runId: string; messageIndex: number; messageIndexInRun: number; numberOfMessagesInRun: number; agentId: string; stateSnapshot: unknown }

Prop

Type

`message-after?`{ message: Message; position: 'after'; runId: string; messageIndex: number; messageIndexInRun: number; numberOfMessagesInRun: number; agentId: string; stateSnapshot: unknown }

Prop

Type

`activity-message?`{ activityType: string; content: unknown; message: ActivityMessage; agent: unknown }

Prop

Type

`tool-call?`{ name: string; args: unknown; status: string; result: string | undefined; toolCall: unknown; toolMessage: ToolMessage | undefined }

## Usage

### Basic message list
    
    
    <script setup lang="ts">
    import { CopilotChatMessageView } from "@copilotkit/vue/v2";
    import { useAgent } from "@copilotkit/vue/v2";
    
    const { agent } = useAgent();
    </script>
    
    <template>
      <copilot-chat-message-view
        :messages="agent?.messages ?? []"
        :is-running="agent?.isRunning ?? false"
      />
    </template>

### Customizing assistant and user messages
    
    
    <script setup lang="ts">
    import { CopilotChatMessageView } from "@copilotkit/vue/v2";
    import { useAgent } from "@copilotkit/vue/v2";
    
    const { agent } = useAgent();
    </script>
    
    <template>
      <copilot-chat-message-view
        :messages="agent?.messages ?? []"
        :is-running="agent?.isRunning ?? false"
      >
        <template #assistant-message="{ message }">
          <div class="bg-blue-50 p-4 rounded-xl">{{ message.content }}</div>
        </template>
    
        <template #user-message="{ message }">
          <div class="bg-gray-100 p-4 rounded-xl">{{ message.content }}</div>
        </template>
      </copilot-chat-message-view>
    </template>

### Custom typing indicator
    
    
    <script setup lang="ts">
    import { CopilotChatMessageView } from "@copilotkit/vue/v2";
    import { useAgent } from "@copilotkit/vue/v2";
    
    const { agent } = useAgent();
    </script>
    
    <template>
      <copilot-chat-message-view
        :messages="agent?.messages ?? []"
        :is-running="agent?.isRunning ?? false"
      >
        <template #cursor>
          <div class="animate-pulse text-gray-400">Thinking...</div>
        </template>
      </copilot-chat-message-view>
    </template>

### Rendering a specific tool call
    
    
    <script setup lang="ts">
    import { CopilotChatMessageView } from "@copilotkit/vue/v2";
    import { useAgent } from "@copilotkit/vue/v2";
    
    const { agent } = useAgent();
    </script>
    
    <template>
      <copilot-chat-message-view
        :messages="agent?.messages ?? []"
        :is-running="agent?.isRunning ?? false"
      >
        <template #tool-call-get_weather="{ args, status, result }">
          <div class="rounded-lg border p-3">
            <p>Status: {{ status }}</p>
            <p v-if="result">Result: {{ result }}</p>
          </div>
        </template>
      </copilot-chat-message-view>
    </template>

## Behavior

  * **Message rendering** : Each message is dispatched to the matching default child component based on its `role` (assistant, user, reasoning, or activity), unless the corresponding named slot is provided.
  * **Deduplication** : Messages sharing an `id` are deduplicated; assistant fragments with the same id are merged (content and tool calls combined). In development, a console warning is logged when duplicates are dropped.
  * **Cursor display** : The `cursor` slot is rendered only when `isRunning` is `true` and the last message is not a reasoning message. It appears after the last message.
  * **Slot forwarding** : Slots passed to `CopilotChatMessageView` (including `tool-call` and `tool-call-<name>`) are forwarded to the default assistant and user message children, so tool rendering works without re-implementing those components.
  * **Custom and activity renderers** : When `message-before`, `message-after`, or `activity-message` slots are omitted, the component falls back to renderers registered on the CopilotKit instance, scoped to the active `agentId` when applicable.



## Related

  * [`CopilotChatAssistantMessage`](https://docs.copilotkit.ai/reference/vue/components/CopilotChatAssistantMessage) \- Default assistant message child component
  * [`CopilotChatUserMessage`](https://docs.copilotkit.ai/reference/vue/components/CopilotChatUserMessage) \- Default user message child component
  * [`CopilotChatView`](https://docs.copilotkit.ai/reference/vue/components/CopilotChatView) \- Higher-level chat view that composes this component
  * [`useAgent`](https://docs.copilotkit.ai/reference/vue/hooks/useAgent) \- Composable for accessing the agent's `messages` and `isRunning` state


