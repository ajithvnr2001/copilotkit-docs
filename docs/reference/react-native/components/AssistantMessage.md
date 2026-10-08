---
url: https://docs.copilotkit.ai/reference/react-native/components/AssistantMessage/
title: AssistantMessage
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:43.676448+00:00
---

# AssistantMessage

> Source: https://docs.copilotkit.ai/reference/react-native/components/AssistantMessage/

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

# AssistantMessage

A left-aligned assistant chat bubble that renders Markdown content, with an optional typing indicator and timestamp.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`AssistantMessage` renders a left-aligned chat bubble for assistant turns. Content is rendered as Markdown through [`CopilotMarkdown`](https://docs.copilotkit.ai/reference/react-native/components/CopilotMarkdown). When `isLoading` is set, it shows an animated typing indicator instead of content. Useful when building a custom chat UI on top of the headless [`CopilotChat`](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat).

## Import
    
    
    import { AssistantMessage } from "@copilotkit/react-native/components";

## Props

Prop

Type

`content`string

Prop

Type

`isLoading?`boolean

Prop

Type

`timestamp?`Date

Prop

Type

`style?`ViewStyle

## Usage
    
    
    import { AssistantMessage } from "@copilotkit/react-native/components";
    
    <AssistantMessage content="Hello! How can I help?" timestamp={new Date()} />;
    
    // While the agent is responding:
    <AssistantMessage content="" isLoading />;

## Related

  * [`UserMessage`](https://docs.copilotkit.ai/reference/react-native/components/UserMessage): the user-side counterpart
  * [`CopilotMarkdown`](https://docs.copilotkit.ai/reference/react-native/components/CopilotMarkdown): the Markdown renderer used internally


