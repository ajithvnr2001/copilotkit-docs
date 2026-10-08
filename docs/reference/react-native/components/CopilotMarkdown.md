---
url: https://docs.copilotkit.ai/reference/react-native/components/CopilotMarkdown/
title: CopilotMarkdown
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:45.629729+00:00
---

# CopilotMarkdown

> Source: https://docs.copilotkit.ai/reference/react-native/components/CopilotMarkdown/

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

# CopilotMarkdown

Render Markdown text with React Native styling tuned for chat. Handles streaming content gracefully.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotMarkdown` renders a Markdown string with sensible React Native styling, built on [`react-native-streamdown`](https://www.npmjs.com/package/react-native-streamdown). It handles incomplete (streaming) Markdown gracefully, rendering incrementally as content arrives, which makes it ideal for assistant messages. Requires the `react-native-streamdown` peer dependency.

## Import
    
    
    import { CopilotMarkdown, defaultMarkdownStyles } from "@copilotkit/react-native/components";

## Props

Prop

Type

`content`string

Prop

Type

`style?`MarkdownStyle

Prop

Type

`streamingAnimation?`boolean

## `defaultMarkdownStyles`

The default style map. Spread it to extend rather than replace the built-in styling:
    
    
    import { CopilotMarkdown, defaultMarkdownStyles } from "@copilotkit/react-native/components";
    
    const styles = {
      ...defaultMarkdownStyles,
      h1: { fontSize: 28, fontWeight: "800" },
    };
    
    <CopilotMarkdown content="# Hello\nThis is **bold**." style={styles} />;

## Usage
    
    
    import { CopilotMarkdown } from "@copilotkit/react-native/components";
    
    <CopilotMarkdown content="**Hello** from CopilotKit!" />;

## Related

  * [`AssistantMessage`](https://docs.copilotkit.ai/reference/react-native/components/AssistantMessage): renders its content through `CopilotMarkdown`


