---
url: https://docs.copilotkit.ai/reference/react-native/components/CopilotModal/
title: CopilotModal
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:45.687786+00:00
---

# CopilotModal

> Source: https://docs.copilotkit.ai/reference/react-native/components/CopilotModal/

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

# CopilotModal

Headless modal wrapper around CopilotChat, plus a prebuilt bottom-sheet chat from the /components subpath.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

Like [`CopilotChat`](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat), `CopilotModal` ships in **two** versions, chosen by import path:

  * **Headless** (`@copilotkit/react-native`) is a thin wrapper around `CopilotChat` that mirrors the web SDK's `CopilotModal` API. It provides agent wiring only; you handle modal presentation with React Native's `Modal` (or any overlay) and build the chat UI from [`useCopilotChatContext`](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat#usecopilotchatcontext).
  * **Prebuilt UI** (`@copilotkit/react-native/components`) is a ready-made chat in a [`@gorhom/bottom-sheet`](https://ui.gorhom.dev/components/bottom-sheet/) with snap points and swipe-to-dismiss. See Prebuilt UI.



## Headless `CopilotModal`
    
    
    import { CopilotModal } from "@copilotkit/react-native";

Accepts all [headless `CopilotChat` props](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat#props) (`agentId`, `agentName`, `threadId`, `onError`, `throttleMs`, `attachments`), plus:

Prop

Type

`children?`ReactNode

### Usage
    
    
    import { CopilotModal } from "@copilotkit/react-native";
    import { Modal } from "react-native";
    
    function App({ isOpen }: { isOpen: boolean }) {
      return (
        <Modal visible={isOpen} animationType="slide">
          <CopilotModal agentId="default">
            <MyChatUI />
          </CopilotModal>
        </Modal>
      );
    }

## Prebuilt UI

Import `CopilotModal` from the `/components` subpath for a bottom-sheet chat. Control it imperatively through a `CopilotModalRef`, or declaratively with the `visible` prop. Requires the `@gorhom/bottom-sheet`, `react-native-gesture-handler`, and `react-native-reanimated` peer dependencies.
    
    
    import { CopilotModal, type CopilotModalRef } from "@copilotkit/react-native/components";

### Props

Like the prebuilt `CopilotChat`, this component selects its agent with `agentName` (the prop the prebuilt UI currently exposes), not the headless `agentId`.

Prop

Type

`visible?`boolean

Prop

Type

`onDismiss?`() => void

Prop

Type

`snapPoints?`(string | number)[]

Prop

Type

`initialSnapIndex?`number

Prop

Type

`enableDismissOnClose?`boolean

Prop

Type

`backdropOpacity?`number

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

`headerTitle?`string

### Ref handle

Prop

Type

`CopilotModalRef?`{ open(): void; close(): void }

### Usage
    
    
    import { CopilotModal, type CopilotModalRef } from "@copilotkit/react-native/components";
    import { useRef } from "react";
    import { Button, View } from "react-native";
    
    export function ChatScreen() {
      const modalRef = useRef<CopilotModalRef>(null);
    
      return (
        <View style={{ flex: 1 }}>
          <Button title="Open chat" onPress={() => modalRef.current?.open()} />
          <CopilotModal
            ref={modalRef}
            agentName="default"
            headerTitle="Assistant"
            snapPoints={["50%", "90%"]}
          />
        </View>
      );
    }

## Related

  * [`CopilotChat`](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat): the underlying chat primitive and prebuilt UI
  * [`CopilotSidebar`](https://docs.copilotkit.ai/reference/react-native/components/CopilotSidebar): slide-in drawer variant
  * [`CopilotPopup`](https://docs.copilotkit.ai/reference/react-native/components/CopilotPopup): floating action button + overlay


