---
url: https://docs.copilotkit.ai/reference/react-native/components/CopilotChat/
title: CopilotChat
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:43.918471+00:00
---

# CopilotChat

> Source: https://docs.copilotkit.ai/reference/react-native/components/CopilotChat/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁React NativeSDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Components

[AssistantMessage](https://docs.copilotkit.ai/reference/react-native/components/AssistantMessage)[CopilotChat](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat)[CopilotKitProvider](https://docs.copilotkit.ai/reference/react-native/components/CopilotKitProvider)[CopilotMarkdown](https://docs.copilotkit.ai/reference/react-native/components/CopilotMarkdown)[CopilotModal](https://docs.copilotkit.ai/reference/react-native/components/CopilotModal)[CopilotPopup](https://docs.copilotkit.ai/reference/react-native/components/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/react-native/components/CopilotSidebar)[UserMessage](https://docs.copilotkit.ai/reference/react-native/components/UserMessage)

Hooks

[useAgent](https://docs.copilotkit.ai/reference/react-native/hooks/useAgent)[useAgentContext](https://docs.copilotkit.ai/reference/react-native/hooks/useAgentContext)[useAttachments](https://docs.copilotkit.ai/reference/react-native/hooks/useAttachments)[useCapabilities](https://docs.copilotkit.ai/reference/react-native/hooks/useCapabilities)[useComponent](https://docs.copilotkit.ai/reference/react-native/hooks/useComponent)[useConfigureSuggestions](https://docs.copilotkit.ai/reference/react-native/hooks/useConfigureSuggestions)[useCopilotKit](https://docs.copilotkit.ai/reference/react-native/hooks/useCopilotKit)[useFrontendTool](https://docs.copilotkit.ai/reference/react-native/hooks/useFrontendTool)[useHumanInTheLoop](https://docs.copilotkit.ai/reference/react-native/hooks/useHumanInTheLoop)[useInterrupt](https://docs.copilotkit.ai/reference/react-native/hooks/useInterrupt)[useRenderTool](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool)[useSuggestions](https://docs.copilotkit.ai/reference/react-native/hooks/useSuggestions)[useThreads](https://docs.copilotkit.ai/reference/react-native/hooks/useThreads)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[react-native](https://docs.copilotkit.ai/reference/react-native)Components

# CopilotChat

Headless chat primitive that wires an agent into context, plus a prebuilt full-screen chat UI from the /components subpath.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotChat` connects an agent and exposes its conversation state to descendants. There are **two** versions, chosen by import path:

  * **Headless** (`@copilotkit/react-native`) renders no UI. It wires up [`useAgent`](https://docs.copilotkit.ai/reference/react-native/hooks/useAgent), manages attachments, and exposes everything through `useCopilotChatContext` so you build the interface from React Native views.
  * **Prebuilt UI** (`@copilotkit/react-native/components`) is a ready-made full-screen chat with a message list, input bar, and optional header. See Prebuilt UI.



## Headless `CopilotChat`
    
    
    import { CopilotChat, useCopilotChatContext } from "@copilotkit/react-native";

### Props

Prop

Type

`agentId?`string

Prop

Type

`agentName?`string

Prop

Type

`threadId?`string

Prop

Type

`onError?`(event: { error: Error; code: CopilotKitCoreErrorCode; context: Record<string, any> }) => void | Promise<void>

Prop

Type

`throttleMs?`number

Prop

Type

`attachments?`NativeAttachmentsConfig

Prop

Type

`children?`ReactNode

### `useCopilotChatContext`

Call inside a `<CopilotChat>` tree to read the conversation state and actions. Throws if called outside a `<CopilotChat>`.
    
    
    function useCopilotChatContext(): CopilotChatContextValue;

Prop

Type

`agent?`AbstractAgent

Prop

Type

`isRunning?`boolean

Prop

Type

`messages?`Message[]

Prop

Type

`attachments?`Attachment[]

Prop

Type

`attachmentsEnabled?`boolean

Prop

Type

`openPicker?`() => Promise<void>

Prop

Type

`removeAttachment?`(id: string) => void

Prop

Type

`submitMessage?`(text: string) => Promise<void>

### Usage
    
    
    import { CopilotChat, useCopilotChatContext } from "@copilotkit/react-native";
    import { useState } from "react";
    import { FlatList, Text, TextInput, TouchableOpacity, View } from "react-native";
    
    function ChatUI() {
      const { messages, isRunning, submitMessage } = useCopilotChatContext();
      const [text, setText] = useState("");
    
      return (
        <View style={{ flex: 1 }}>
          <FlatList
            data={messages.filter((m) => m.content)}
            keyExtractor={(m, i) => m.id ?? String(i)}
            renderItem={({ item }) => (
              <Text style={{ padding: 12 }}>{item.content}</Text>
            )}
          />
          <View style={{ flexDirection: "row", padding: 8 }}>
            <TextInput
              style={{ flex: 1, borderWidth: 1, borderRadius: 8, padding: 8 }}
              value={text}
              onChangeText={setText}
              placeholder="Type a message..."
            />
            <TouchableOpacity
              disabled={isRunning}
              onPress={() => {
                submitMessage(text);
                setText("");
              }}
              style={{ padding: 8 }}
            >
              <Text>Send</Text>
            </TouchableOpacity>
          </View>
        </View>
      );
    }
    
    export function ChatScreen() {
      return (
        <CopilotChat agentId="default">
          <ChatUI />
        </CopilotChat>
      );
    }

## Prebuilt UI

For a ready-made interface, import `CopilotChat` from the `/components` subpath. It renders a full-screen chat with a message list, input bar, optional header, and inline tool-call rendering — it reads the shared renderer registry that [`useRenderTool`](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool), `useFrontendTool` and `useComponent` write to.
    
    
    import { CopilotChat } from "@copilotkit/react-native/components";

### Props

The prebuilt UI components select their agent with `agentName` (not the headless `agentId`). The two are equivalent; `agentName` is simply the prop name the prebuilt components currently expose.

Prop

Type

`agentName?`string

Prop

Type

`placeholder?`string

Prop

Type

`initialMessages?`string[]

Prop

Type

`emptyStateTitle?`string

Prop

Type

`emptyStateSubtitle?`string

Prop

Type

`headerTitle?`string

Prop

Type

`showHeader?`boolean

Prop

Type

`style?`ViewStyle

Prop

Type

`messageContainerStyle?`ViewStyle

Prop

Type

`inputContainerStyle?`ViewStyle

Prop

Type

`onSendMessage?`(text: string) => void

Prop

Type

`FlatListComponent?`React.ComponentType<any>

Prop

Type

`disableKeyboardAvoiding?`boolean

### Usage
    
    
    import { CopilotChat } from "@copilotkit/react-native/components";
    
    export function ChatScreen() {
      return (
        <CopilotChat
          agentName="default"
          headerTitle="Assistant"
          placeholder="Ask me anything..."
          initialMessages={["What's the weather?", "Summarize my tasks"]}
        />
      );
    }

## Related

  * [`useCopilotKit`](https://docs.copilotkit.ai/reference/react-native/hooks/useCopilotKit): access the runtime client directly
  * [`useRenderTool`](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool): render React Native UI for agent tool calls
  * [`CopilotModal`](https://docs.copilotkit.ai/reference/react-native/components/CopilotModal): modal variants of the chat
  * [`CopilotSidebar`](https://docs.copilotkit.ai/reference/react-native/components/CopilotSidebar) · [`CopilotPopup`](https://docs.copilotkit.ai/reference/react-native/components/CopilotPopup): prebuilt chrome


