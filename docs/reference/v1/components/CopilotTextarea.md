---
url: https://docs.copilotkit.ai/reference/v1/components/CopilotTextarea/
title: CopilotTextarea
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:55.827949+00:00
---

# CopilotTextarea

> Source: https://docs.copilotkit.ai/reference/v1/components/CopilotTextarea/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁React (V1)SDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Components

[CopilotKit](https://docs.copilotkit.ai/reference/v1/components/CopilotKit)[CopilotTextarea](https://docs.copilotkit.ai/reference/v1/components/CopilotTextarea)[CopilotChat](https://docs.copilotkit.ai/reference/v1/components/chat/CopilotChat)[CopilotPopup](https://docs.copilotkit.ai/reference/v1/components/chat/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/v1/components/chat/CopilotSidebar)[All Chat Components](https://docs.copilotkit.ai/reference/v1/components/chat)

Hooks

[useAgent](https://docs.copilotkit.ai/reference/v1/hooks/useAgent)[useCoAgent](https://docs.copilotkit.ai/reference/v1/hooks/useCoAgent)[useCoAgentStateRender](https://docs.copilotkit.ai/reference/v1/hooks/useCoAgentStateRender)[useCopilotAction](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotAction)[useCopilotAdditionalInstructions](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotAdditionalInstructions)[useCopilotChat](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotChat)[useCopilotChatHeadless_c](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotChatHeadless_c)[useCopilotChatSuggestions](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotChatSuggestions)[useCopilotReadable](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotReadable)[useDefaultTool](https://docs.copilotkit.ai/reference/v1/hooks/useDefaultTool)[useFrontendTool](https://docs.copilotkit.ai/reference/v1/hooks/useFrontendTool)[useHumanInTheLoop](https://docs.copilotkit.ai/reference/v1/hooks/useHumanInTheLoop)[useLangGraphInterrupt](https://docs.copilotkit.ai/reference/v1/hooks/useLangGraphInterrupt)[useRenderToolCall](https://docs.copilotkit.ai/reference/v1/hooks/useRenderToolCall)

Classes

[CopilotRuntime](https://docs.copilotkit.ai/reference/v1/classes/CopilotRuntime)[CopilotTask](https://docs.copilotkit.ai/reference/v1/classes/CopilotTask)[AnthropicAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/AnthropicAdapter)[GoogleGenerativeAIAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/GoogleGenerativeAIAdapter)[GroqAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/GroqAdapter)[LangChainAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/LangChainAdapter)[OpenAIAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/OpenAIAdapter)[OpenAIAssistantAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/OpenAIAssistantAdapter)

SDKs

[LangGraph SDK](https://docs.copilotkit.ai/reference/v1/sdk/js/LangGraph)[CrewAI SDK](https://docs.copilotkit.ai/reference/v1/sdk/python/CrewAI)[CrewAIAgent](https://docs.copilotkit.ai/reference/v1/sdk/python/CrewAIAgent)[LangGraph SDK](https://docs.copilotkit.ai/reference/v1/sdk/python/LangGraph)[LangGraphAGUIAgent](https://docs.copilotkit.ai/reference/v1/sdk/python/LangGraphAGUIAgent)[Remote Endpoints](https://docs.copilotkit.ai/reference/v1/sdk/python/RemoteEndpoints)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[v1](https://docs.copilotkit.ai/reference/v1)Components

# CopilotTextarea

An AI-powered textarea component for your application, which serves as a drop-in replacement for any textarea.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

  
![](https://cdn.copilotkit.ai/docs/copilotkit/images/CopilotTextarea.gif)

`<CopilotTextarea>` is a React component that acts as a drop-in replacement for the standard `<textarea>`, offering enhanced autocomplete features powered by AI. It is context-aware, integrating seamlessly with the [`useCopilotReadable`](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotReadable) hook to provide intelligent suggestions based on the application context.

In addition, it provides a hovering editor window (available by default via `Cmd + K` on Mac and `Ctrl + K` on Windows) that allows the user to suggest changes to the text, for example providing a summary or rephrasing the text.

## Example
    
    
    import { CopilotTextarea } from '@copilotkit/react-textarea';
    import "@copilotkit/react-textarea/styles.css";
     
    <CopilotTextarea
      autosuggestionsConfig={{
        textareaPurpose:
         "the body of an email message",
        chatApiConfigs: {},
      }}
    />

## Usage

### Install Dependencies

This component is part of the [@copilotkit/react-textarea](https://npmjs.com/package/@copilotkit/react-textarea) package.
    
    
    npm install @copilotkit/react-core @copilotkit/react-textarea

### Usage

Use the CopilotTextarea component in your React application similarly to a standard `<textarea />`, with additional configurations for AI-powered features.

For example:
    
    
    import { useState } from "react";
    import { CopilotTextarea } from "@copilotkit/react-textarea";
    import "@copilotkit/react-textarea/styles.css";
     
    export function ExampleComponent() {
      const [text, setText] = useState("");
     
      return (
        <CopilotTextarea
          className="custom-textarea-class"
          value={text}
          onValueChange={(value: string) => setText(value)}
          placeholder="Enter your text here..."
          autosuggestionsConfig={{
            textareaPurpose: "Provide context or purpose of the textarea.",
            chatApiConfigs: {
              suggestionsApiConfig: {
                maxTokens: 20,
                stop: [".", "?", "!"],
              },
            },
          }}
        />
      );
    }

### Look & Feel

By default, CopilotKit components do not have any styles. You can import CopilotKit's stylesheet at the root of your project:

YourRootComponent.tsx
    
    
    ...
    import "@copilotkit/react-textarea/styles.css"; 
     
    export function YourRootComponent() {
      return (
        <CopilotKit>
          ...
        </CopilotKit>
      );
    }

For more information about how to customize the styles, check out the [Customize Look & Feel](https://docs.copilotkit.ai/guides/custom-look-and-feel/customize-built-in-ui-components) guide.

## Properties

Prop

Type

`disableBranding?`boolean

Prop

Type

`placeholderStyle?`React.CSSProperties

Prop

Type

`suggestionsStyle?`React.CSSProperties

Prop

Type

`hoverMenuClassname?`string

Prop

Type

`value?`string

Prop

Type

`onValueChange?`(value: string) => void

Prop

Type

`onChange?`(event: React.ChangeEvent<HTMLTextAreaElement>) => void

Prop

Type

`shortcut?`string

Prop

Type

`autosuggestionsConfig`AutosuggestionsConfigUserSpecified
