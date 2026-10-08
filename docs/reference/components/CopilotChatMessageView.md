---
url: https://docs.copilotkit.ai/reference/components/CopilotChatMessageView/
title: CopilotChatMessageView
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:26.461285+00:00
---

# CopilotChatMessageView

> Source: https://docs.copilotkit.ai/reference/components/CopilotChatMessageView/

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

# CopilotChatMessageView

Component for rendering a list of chat messages

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotChatMessageView` renders a list of chat messages and, optionally, a typing cursor while the agent is running. It delegates rendering of individual messages to slot components (`assistantMessage` and `userMessage`) and supports a render-prop `children` function for full control over layout.

## Import
    
    
    import { CopilotChatMessageView } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

## Props

Prop

Type

`isRunning?`boolean

Prop

Type

`messages?`Message[]

Prop

Type

`transformMessages?`(messages: Message[]) => Message[]

Prop

Type

`groupMessages?`(messages: Message[]) => MessageRow[]

Prop

Type

`children?`(props: { isRunning: boolean; messages: Message[]; messageElements: React.ReactElement[] }) => React.ReactElement

## Slots

All slot props follow the CopilotKit slot system: each accepts a replacement React component, a `className` string that is merged into the default component's classes, or a partial props object that extends the default component.

Prop

Type

`assistantMessage?`SlotProp<typeof CopilotChatAssistantMessage>

Prop

Type

`userMessage?`SlotProp<typeof CopilotChatUserMessage>

Prop

Type

`cursor?`SlotProp<typeof CopilotChatMessageView.Cursor>

## Usage

### Basic Message List
    
    
    function MessageList() {
      const { agent } = useAgent();
    
      return (
        <CopilotChatMessageView
          messages={agent.messages}
          isRunning={agent.isRunning}
        />
      );
    }

### Customizing Message Slots
    
    
    function CustomMessages() {
      const { agent } = useAgent();
    
      return (
        <CopilotChatMessageView
          messages={agent.messages}
          isRunning={agent.isRunning}
          assistantMessage="bg-blue-50 p-4 rounded-xl"
          userMessage="bg-gray-100 p-4 rounded-xl"
          cursor={() => (
            <div className="animate-pulse text-gray-400">Thinking...</div>
          )}
        />
      );
    }

### Render-Prop Children for Custom Layout
    
    
    function CustomLayout() {
      const { agent } = useAgent();
    
      return (
        <CopilotChatMessageView
          messages={agent.messages}
          isRunning={agent.isRunning}
        >
          {({ isRunning, messages, messageElements }) => (
            <div className="flex flex-col gap-4 p-6">
              <div className="text-sm text-gray-500">
                {messages.length} message{messages.length !== 1 ? "s" : ""}
              </div>
              {messageElements}
              {isRunning && (
                <div className="text-sm text-blue-500 animate-pulse">
                  Agent is responding...
                </div>
              )}
            </div>
          )}
        </CopilotChatMessageView>
      );
    }

### Hiding the Toolbar on Assistant Messages
    
    
    function MinimalChat() {
      const { agent } = useAgent();
    
      return (
        <CopilotChatMessageView
          messages={agent.messages}
          isRunning={agent.isRunning}
          assistantMessage={{ toolbarVisible: false }}
        />
      );
    }

## Behavior

  * **Message Rendering** : Each message in the `messages` array is rendered using the corresponding slot component based on its `role`. Assistant messages use the `assistantMessage` slot; user messages use the `userMessage` slot.
  * **Cursor Display** : The `cursor` slot is only rendered when `isRunning` is `true`. It appears after the last message in the list, and is hidden when the last rendered message is a reasoning message, which shows its own indicator.
  * **Virtualization** : Inside a chat scroll container, once more than 50 messages render, only the rows on screen are mounted. The count is of the messages that render: the ones `transformMessages` returns or, with `groupMessages`, the ones in the rows it returns. The window itself moves by rows, and each group is one row. Providing `children` turns virtualization off; in development the component warns once when that is what keeps a long thread mounted in full.
  * **Latest Message** : The last rendered message is passed to its slot as `isLatest`. While `isRunning` is `true`, the latest assistant message hides its toolbar and a latest reasoning message shows as streaming.
  * **Render-Prop Override** : When `children` is provided as a function, the component delegates all layout to that function. The `messageElements` array is pre-built from the slot components, so custom layouts still benefit from slot customization.
  * **Slot System** : Each slot prop accepts three forms -- a replacement component, a className string merged into the default, or a partial props object that extends the default component's props.



## Related

  * [`CopilotChatAssistantMessage`](https://docs.copilotkit.ai/reference/components/CopilotChatAssistantMessage) \-- Default assistant message slot component
  * [`CopilotChatUserMessage`](https://docs.copilotkit.ai/reference/components/CopilotChatUserMessage) \-- Default user message slot component
  * [`CopilotChatView`](https://docs.copilotkit.ai/reference/components/CopilotChatView) \-- Higher-level chat view that composes this component


