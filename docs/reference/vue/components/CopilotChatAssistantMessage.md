---
url: https://docs.copilotkit.ai/reference/vue/components/CopilotChatAssistantMessage/
title: CopilotChatAssistantMessage
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:06.578914+00:00
---

# CopilotChatAssistantMessage

> Source: https://docs.copilotkit.ai/reference/vue/components/CopilotChatAssistantMessage/

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

# CopilotChatAssistantMessage

Vue 3 component for displaying assistant messages with Markdown, tool calls, and an action toolbar

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotChatAssistantMessage` is a Vue 3 component that displays assistant messages with Markdown support, tool call rendering, and an action toolbar. Markdown is rendered with `streamdown-vue` (`StreamMarkdown`), which supports GitHub Flavored Markdown tables, math expressions (KaTeX styles are loaded automatically), and syntax-highlighted code blocks via Shiki (`github-light` / `github-dark` themes). Tables and code blocks include built-in copy and download actions, and images get a hover download button.

The toolbar provides copy, thumbs up, thumbs down, read aloud, and regenerate buttons. Tooltip and aria labels are sourced from the nearest `CopilotChatConfigurationProvider` (see [`useCopilotChatConfiguration`](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotChatConfiguration)). The thumbs up, thumbs down, read aloud, and regenerate buttons are only rendered when a listener for the corresponding event is attached; the copy button is always shown when the toolbar is visible.

The toolbar is hidden while the latest assistant message is still streaming (when `isRunning` is `true` for the last message) and when the message has no text content. It also respects the `toolbarVisible` prop.

## Import
    
    
    <script setup lang="ts">
    import { CopilotChatAssistantMessage } from "@copilotkit/vue/v2";
    </script>

## Example
    
    
    <script setup lang="ts">
    import { CopilotChatAssistantMessage } from "@copilotkit/vue/v2";
    import type { AssistantMessage } from "@ag-ui/core";
    
    const message: AssistantMessage = {
      id: "1",
      role: "assistant",
      content: "Here is **Markdown** with a `code` sample.",
    };
    </script>
    
    <template>
      <CopilotChatAssistantMessage
        :message="message"
        @thumbs-up="(msg) => console.log('Thumbs up:', msg.id)"
        @thumbs-down="(msg) => console.log('Thumbs down:', msg.id)"
      />
    </template>

## Props

Prop

Type

`message`AssistantMessage

Prop

Type

`messages?`Message[]

Prop

Type

`isRunning?`boolean

Prop

Type

`toolbarVisible?`boolean

## Events

Each event emits the current `message` as its payload. Attaching a listener for `thumbs-up`, `thumbs-down`, `read-aloud`, or `regenerate` also causes the matching toolbar button to render; without a listener the button is omitted.

Prop

Type

`thumbs-up?`(message: AssistantMessage) => void

Prop

Type

`thumbs-down?`(message: AssistantMessage) => void

Prop

Type

`read-aloud?`(message: AssistantMessage) => void

Prop

Type

`regenerate?`(message: AssistantMessage) => void

Copying the message to the clipboard is handled internally by the copy button. There is no `copy` event; the copy button is always present when the toolbar is visible.

## Slots

The component exposes named slots so you can override individual pieces of the default layout. Each slot receives scoped props (shown below) that wire its behavior to the message and toolbar handlers.

Prop

Type

`layout?`slot

Prop

Type

`message-renderer?`slot

Prop

Type

`tool-calls-view?`slot

Prop

Type

`toolbar?`slot

Prop

Type

`copy-button?`slot

Prop

Type

`thumbs-up-button?`slot

Prop

Type

`thumbs-down-button?`slot

Prop

Type

`read-aloud-button?`slot

Prop

Type

`regenerate-button?`slot

Prop

Type

`toolbar-items?`slot

## Usage

### Basic assistant message
    
    
    <script setup lang="ts">
    import { CopilotChatAssistantMessage } from "@copilotkit/vue/v2";
    import type { AssistantMessage } from "@ag-ui/core";
    
    defineProps<{ message: AssistantMessage }>();
    </script>
    
    <template>
      <CopilotChatAssistantMessage
        :message="message"
        @thumbs-up="(msg) => console.log('Thumbs up:', msg.id)"
        @thumbs-down="(msg) => console.log('Thumbs down:', msg.id)"
      />
    </template>

### Adding regenerate and read aloud

Attaching the listeners makes the corresponding buttons appear automatically.
    
    
    <script setup lang="ts">
    import { CopilotChatAssistantMessage } from "@copilotkit/vue/v2";
    import type { AssistantMessage } from "@ag-ui/core";
    
    defineProps<{ message: AssistantMessage }>();
    
    function handleRegenerate(msg: AssistantMessage) {
      // re-run the agent for this message
    }
    
    function handleReadAloud(msg: AssistantMessage) {
      // speak msg.content
    }
    </script>
    
    <template>
      <CopilotChatAssistantMessage
        :message="message"
        @regenerate="handleRegenerate"
        @read-aloud="handleReadAloud"
      />
    </template>

### Adding custom toolbar items
    
    
    <script setup lang="ts">
    import { CopilotChatAssistantMessage } from "@copilotkit/vue/v2";
    import type { AssistantMessage } from "@ag-ui/core";
    
    defineProps<{ message: AssistantMessage }>();
    </script>
    
    <template>
      <CopilotChatAssistantMessage :message="message">
        <template #toolbar-items>
          <button type="button" @click="shareMessage(message)">Share</button>
        </template>
      </CopilotChatAssistantMessage>
    </template>

### Hiding the toolbar
    
    
    <script setup lang="ts">
    import { CopilotChatAssistantMessage } from "@copilotkit/vue/v2";
    import type { AssistantMessage } from "@ag-ui/core";
    
    defineProps<{ message: AssistantMessage }>();
    </script>
    
    <template>
      <CopilotChatAssistantMessage :message="message" :toolbar-visible="false" />
    </template>

### Custom Markdown renderer
    
    
    <script setup lang="ts">
    import { CopilotChatAssistantMessage } from "@copilotkit/vue/v2";
    import type { AssistantMessage } from "@ag-ui/core";
    
    defineProps<{ message: AssistantMessage }>();
    </script>
    
    <template>
      <CopilotChatAssistantMessage :message="message">
        <template #message-renderer="{ content }">
          <div class="custom-markdown">{{ content }}</div>
        </template>
      </CopilotChatAssistantMessage>
    </template>

### Customizing a toolbar button
    
    
    <script setup lang="ts">
    import { CopilotChatAssistantMessage } from "@copilotkit/vue/v2";
    import type { AssistantMessage } from "@ag-ui/core";
    
    defineProps<{ message: AssistantMessage }>();
    </script>
    
    <template>
      <CopilotChatAssistantMessage
        :message="message"
        @regenerate="(msg) => regenerate(msg)"
      >
        <template #regenerate-button="{ onRegenerate, label }">
          <button type="button" :title="label" @click="onRegenerate">
            Regenerate
          </button>
        </template>
      </CopilotChatAssistantMessage>
    </template>

## Related

  * `CopilotChatToolCallsView` \- Renders the tool calls contained in an assistant message
  * [`CopilotChatUserMessage`](https://docs.copilotkit.ai/reference/vue/components/CopilotChatUserMessage) \- Companion component for user messages
  * [`CopilotChatMessageView`](https://docs.copilotkit.ai/reference/vue/components/CopilotChatMessageView) \- Parent component that renders this as the default assistant message
  * [`useCopilotChatConfiguration`](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotChatConfiguration) \- Provides the localized toolbar labels


