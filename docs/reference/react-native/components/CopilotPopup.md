---
url: https://docs.copilotkit.ai/reference/react-native/components/CopilotPopup/
title: CopilotPopup
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:45.572908+00:00
---

# CopilotPopup

> Source: https://docs.copilotkit.ai/reference/react-native/components/CopilotPopup/

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

# CopilotPopup

A prebuilt floating action button that opens a CopilotChat session in a modal overlay card.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotPopup` renders a floating action button (FAB) that opens a chat in a modal overlay card with a header and a dismissible backdrop. Like [`CopilotSidebar`](https://docs.copilotkit.ai/reference/react-native/components/CopilotSidebar), its chat area wraps a headless [`CopilotChat`](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat). Provide your chat UI as `children`, or drop in the prebuilt UI `CopilotChat` from `@copilotkit/react-native/components`.

Control it imperatively through a `CopilotPopupHandle` ref.

## Import
    
    
    import { CopilotPopup, type CopilotPopupHandle } from "@copilotkit/react-native";

## Props

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

`throttleMs?`number

Prop

Type

`defaultOpen?`boolean

Prop

Type

`height?`number | string

Prop

Type

`onError?`(error: Error) => void

Prop

Type

`headerTitle?`string

Prop

Type

`attachments?`NativeAttachmentsConfig

Prop

Type

`children?`ReactNode

Prop

Type

`onOpen?`() => void

Prop

Type

`onClose?`() => void

Prop

Type

`dismissOnBackdropPress?`boolean

Prop

Type

`showToggleButton?`boolean

Prop

Type

`style?`ViewStyle

## Ref handle

Prop

Type

`CopilotPopupHandle?`{ open(): void; close(): void; toggle(): void }

## Usage
    
    
    import { CopilotPopup, type CopilotPopupHandle } from "@copilotkit/react-native";
    import { CopilotChat } from "@copilotkit/react-native/components";
    import { useRef } from "react";
    
    export function ChatScreen() {
      const popupRef = useRef<CopilotPopupHandle>(null);
    
      return (
        <CopilotPopup ref={popupRef} agentId="default" headerTitle="Chat">
          <CopilotChat agentName="default" showHeader={false} />
        </CopilotPopup>
      );
    }

## Behavior

  * **Overlay** : the popup opens as a modal card floating above your content, with a semi-transparent backdrop.
  * **Backdrop dismiss** : tapping the backdrop closes the popup when `dismissOnBackdropPress` is `true`.
  * **FAB** : when `showToggleButton` is `true`, a floating action button opens the popup and hides while it is open.
  * **Height** : a percentage `height` (e.g. `"60%"`) resolves against the screen height; a number is used as points.



## Related

  * [`CopilotSidebar`](https://docs.copilotkit.ai/reference/react-native/components/CopilotSidebar): slide-in drawer variant
  * [`CopilotChat`](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat): the chat primitive wrapped inside the popup


