---
url: https://docs.copilotkit.ai/reference/react-native/components/CopilotSidebar/
title: CopilotSidebar
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:45.603447+00:00
---

# CopilotSidebar

> Source: https://docs.copilotkit.ai/reference/react-native/components/CopilotSidebar/

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

# CopilotSidebar

A prebuilt slide-in drawer from the right edge of the screen that wraps a CopilotChat session.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotSidebar` renders a slide-in drawer from the right edge of the screen, with a header bar, a backdrop, and an optional floating action button (FAB) to toggle it. The drawer's chat area wraps a headless [`CopilotChat`](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat). Render your chat UI as `children` (consuming [`useCopilotChatContext`](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat#usecopilotchatcontext)) or drop in the prebuilt UI `CopilotChat` from `@copilotkit/react-native/components`.

Control it imperatively through a `CopilotSidebarHandle` ref.

## Import
    
    
    import { CopilotSidebar, type CopilotSidebarHandle } from "@copilotkit/react-native";

## Props

Accepts the headless [`CopilotChat` props](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat#props) (`agentId`, `agentName`, `threadId`, `onError`, `throttleMs`, `attachments`) except `children` is repurposed for the drawer body, plus:

Prop

Type

`defaultOpen?`boolean

Prop

Type

`width?`number | string

Prop

Type

`headerTitle?`string

Prop

Type

`showToggleButton?`boolean

Prop

Type

`onOpen?`() => void

Prop

Type

`onClose?`() => void

Prop

Type

`style?`ViewStyle

Prop

Type

`children?`ReactNode

## Ref handle

Prop

Type

`CopilotSidebarHandle?`{ open(): void; close(): void; toggle(): void }

## Usage
    
    
    import { CopilotSidebar, type CopilotSidebarHandle } from "@copilotkit/react-native";
    import { CopilotChat } from "@copilotkit/react-native/components";
    import { useRef } from "react";
    
    export function ChatScreen() {
      const sidebarRef = useRef<CopilotSidebarHandle>(null);
    
      return (
        <CopilotSidebar ref={sidebarRef} agentId="default" headerTitle="Assistant">
          <CopilotChat agentName="default" showHeader={false} />
        </CopilotSidebar>
      );
    }

## Behavior

  * **Animation** : slides in/out over 300ms using the React Native `Animated` API.
  * **Backdrop** : a semi-transparent, pressable backdrop dismisses the drawer.
  * **FAB** : when `showToggleButton` is `true`, a floating button opens the drawer and hides while it is open.



## Related

  * [`CopilotPopup`](https://docs.copilotkit.ai/reference/react-native/components/CopilotPopup): floating action button plus centered overlay
  * [`CopilotChat`](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat): the chat primitive wrapped inside the drawer


