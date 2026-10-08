---
url: https://docs.copilotkit.ai/reference/v2/components/CopilotChatAssistantMessage/
title: CopilotChatAssistantMessage
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:34:34.033041+00:00
---

# CopilotChatAssistantMessage

> Source: https://docs.copilotkit.ai/reference/v2/components/CopilotChatAssistantMessage/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁React (V2)SDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Components

[CopilotChat](https://docs.copilotkit.ai/reference/v2/components/CopilotChat)[CopilotChatAssistantMessage](https://docs.copilotkit.ai/reference/v2/components/CopilotChatAssistantMessage)[CopilotChatInput](https://docs.copilotkit.ai/reference/v2/components/CopilotChatInput)[CopilotChatMessageView](https://docs.copilotkit.ai/reference/v2/components/CopilotChatMessageView)[CopilotChatUserMessage](https://docs.copilotkit.ai/reference/v2/components/CopilotChatUserMessage)[CopilotChatView](https://docs.copilotkit.ai/reference/v2/components/CopilotChatView)[CopilotKit](https://docs.copilotkit.ai/reference/v2/components/CopilotKit)[CopilotPopup](https://docs.copilotkit.ai/reference/v2/components/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/v2/components/CopilotSidebar)[CopilotThreadsDrawer](https://docs.copilotkit.ai/reference/v2/components/CopilotThreadsDrawer)

Hooks

[useAgent](https://docs.copilotkit.ai/reference/v2/hooks/useAgent)[useAgentContext](https://docs.copilotkit.ai/reference/v2/hooks/useAgentContext)[useCapabilities](https://docs.copilotkit.ai/reference/v2/hooks/useCapabilities)[useComponent](https://docs.copilotkit.ai/reference/v2/hooks/useComponent)[useConfigureSuggestions](https://docs.copilotkit.ai/reference/v2/hooks/useConfigureSuggestions)[useCopilotChatConfiguration](https://docs.copilotkit.ai/reference/v2/hooks/useCopilotChatConfiguration)[useCopilotKit](https://docs.copilotkit.ai/reference/v2/hooks/useCopilotKit)[useDefaultRenderTool](https://docs.copilotkit.ai/reference/v2/hooks/useDefaultRenderTool)[useFrontendTool](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTool)[useFrontendTools](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTools)[useHumanInTheLoop](https://docs.copilotkit.ai/reference/v2/hooks/useHumanInTheLoop)[useInterrupt](https://docs.copilotkit.ai/reference/v2/hooks/useInterrupt)[useRenderTool](https://docs.copilotkit.ai/reference/v2/hooks/useRenderTool)[useRenderToolCall](https://docs.copilotkit.ai/reference/v2/hooks/useRenderToolCall)[useSuggestions](https://docs.copilotkit.ai/reference/v2/hooks/useSuggestions)[useThreads](https://docs.copilotkit.ai/reference/v2/hooks/useThreads)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[v2](https://docs.copilotkit.ai/reference/v2)Components

# CopilotChatAssistantMessage

Component for displaying assistant messages with Markdown, tool calls, and an action toolbar

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotChatAssistantMessage` displays assistant messages with Markdown support, tool call rendering, and an action toolbar. The Markdown renderer uses `remark-gfm`, `remark-math`, syntax highlighting via `rehype-pretty-code`, and KaTeX support for mathematical expressions. The toolbar provides copy, rating (thumbs up/down), read aloud, and regenerate buttons with localized tooltips sourced from `CopilotChatConfigurationProvider`.

## Import
    
    
    import { CopilotChatAssistantMessage } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

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

`isLatest?`boolean

Prop

Type

`onThumbsUp?`(message: AssistantMessage) => void

Prop

Type

`onThumbsDown?`(message: AssistantMessage) => void

Prop

Type

`onReadAloud?`(message: AssistantMessage) => void

Prop

Type

`onRegenerate?`(message: AssistantMessage) => void

Prop

Type

`additionalToolbarItems?`React.ReactNode

Prop

Type

`toolbarVisible?`boolean

## Slots

All slot props follow the CopilotKit slot system: each accepts a replacement React component, a `className` string that is merged into the default component's classes, or a partial props object that extends the default component.

Prop

Type

`markdownRenderer?`SlotProp<typeof CopilotChatAssistantMessage.MarkdownRenderer>

Prop

Type

`toolbar?`SlotProp<typeof CopilotChatAssistantMessage.Toolbar>

Prop

Type

`copyButton?`SlotProp<typeof CopilotChatAssistantMessage.CopyButton>

Prop

Type

`thumbsUpButton?`SlotProp<typeof CopilotChatAssistantMessage.ThumbsUpButton>

Prop

Type

`thumbsDownButton?`SlotProp<typeof CopilotChatAssistantMessage.ThumbsDownButton>

Prop

Type

`readAloudButton?`SlotProp<typeof CopilotChatAssistantMessage.ReadAloudButton>

Prop

Type

`regenerateButton?`SlotProp<typeof CopilotChatAssistantMessage.RegenerateButton>

Prop

Type

`toolCallsView?`SlotProp<typeof CopilotChatToolCallsView>

## CopilotChatToolCallsView

A companion component that renders the tool calls contained in an assistant message. Given an assistant message, it iterates over each tool call and renders it using the closest registered tool renderer (registered via `useFrontendTool`, `useHumanInTheLoop`, or `renderToolCalls` on the provider).

### Import


### Props

Prop

Type

`message`AssistantMessage

Prop

Type

`messages?`Message[]

## Usage

### Basic Assistant Message
    
    
    function AssistantBubble({ message }) {
      return (
        <CopilotChatAssistantMessage
          message={message}
          onThumbsUp={(msg) => console.log("Thumbs up:", msg.id)}
          onThumbsDown={(msg) => console.log("Thumbs down:", msg.id)}
        />
      );
    }

### Customizing the Toolbar
    
    
    function CustomToolbarMessage({ message }) {
      return (
        <CopilotChatAssistantMessage
          message={message}
          onRegenerate={(msg) => handleRegenerate(msg)}
          onReadAloud={(msg) => speak(msg.content)}
          additionalToolbarItems={
            <button onClick={() => shareMessage(message)}>Share</button>
          }
          toolbar="border-t border-gray-200 pt-2"
        />
      );
    }

### Hiding the Toolbar
    
    
    function MinimalMessage({ message }) {
      return (
        <CopilotChatAssistantMessage message={message} toolbarVisible={false} />
      );
    }

### Custom Markdown Renderer
    
    
    function CustomRendererMessage({ message }) {
      return (
        <CopilotChatAssistantMessage
          message={message}
          markdownRenderer={({ content }) => (
            <ReactMarkdown>{content}</ReactMarkdown>
          )}
        />
      );
    }

### Standalone Tool Calls View
    
    
    function ToolCallsList({ message, allMessages }) {
      return (
        <div className="tool-calls">
          <CopilotChatToolCallsView message={message} messages={allMessages} />
        </div>
      );
    }

## Behavior

  * **Markdown Support** : The default Markdown renderer supports GitHub Flavored Markdown (tables, strikethrough, task lists), math expressions rendered with KaTeX, and syntax-highlighted code blocks via `rehype-pretty-code`.
  * **Toolbar Visibility** : The toolbar appears on hover or focus by default, except on the latest message while `isRunning` is `true`. Individual buttons are only rendered when their corresponding callback prop (`onThumbsUp`, `onThumbsDown`, `onReadAloud`, `onRegenerate`) is provided. The copy button is always visible when the toolbar is shown.
  * **Localized Labels** : All toolbar button tooltips are sourced from the nearest `CopilotChatConfigurationProvider`. See [`useCopilotChatConfiguration`](https://docs.copilotkit.ai/reference/hooks/useCopilotChatConfiguration) for the full list of label keys.
  * **Tool Call Rendering** : Tool calls embedded in the assistant message are rendered by the `toolCallsView` slot. Each tool call is resolved using the `useRenderToolCall` hook, which looks up registered renderers by tool name.
  * **Slot System** : Each slot prop accepts three forms -- a replacement component, a className string merged into the default, or a partial props object that extends the default component's props.



## Related

  * [`CopilotChatMessageView`](https://docs.copilotkit.ai/reference/components/CopilotChatMessageView) \-- Parent component that uses this as the default assistant message slot
  * [`CopilotChatUserMessage`](https://docs.copilotkit.ai/reference/components/CopilotChatUserMessage) \-- Companion component for user messages
  * [`useRenderToolCall`](https://docs.copilotkit.ai/reference/hooks/useRenderToolCall) \-- Hook used internally for resolving tool call renderers
  * [`useCopilotChatConfiguration`](https://docs.copilotkit.ai/reference/hooks/useCopilotChatConfiguration) \-- Provider for localized toolbar labels


