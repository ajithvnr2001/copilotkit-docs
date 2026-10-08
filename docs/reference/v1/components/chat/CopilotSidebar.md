---
url: https://docs.copilotkit.ai/reference/v1/components/chat/CopilotSidebar/
title: CopilotSidebar
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:57.941452+00:00
---

# CopilotSidebar

> Source: https://docs.copilotkit.ai/reference/v1/components/chat/CopilotSidebar/

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

# CopilotSidebar

The CopilotSidebar component, providing a sidebar interface for interacting with your copilot.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

  
![](https://cdn.copilotkit.ai/docs/copilotkit/images/CopilotSidebar.gif)

A chatbot sidebar component for the CopilotKit framework. Highly customizable through various props and custom CSS.

See [CopilotPopup](https://docs.copilotkit.ai/reference/v1/components/chat/CopilotPopup) for a popup version of this component.

## Install Dependencies

This component is part of the [@copilotkit/react-ui](https://npmjs.com/package/@copilotkit/react-ui) package.
    
    
    npm install @copilotkit/react-core @copilotkit/react-ui

## Usage
    
    
    import { CopilotSidebar } from "@copilotkit/react-ui";
    import "@copilotkit/react-ui/styles.css";
     
    <CopilotSidebar
      labels={{
        title: "Your Assistant",
        initial: "Hi! 👋 How can I assist you today?",
      }}
    >
      <YourApp/>
    </CopilotSidebar>

### With Observability Hooks

To monitor user interactions, provide the `observabilityHooks` prop.
    
    
    <CopilotKit>
      <CopilotSidebar
        observabilityHooks={{
          onChatExpanded: () => {
            console.log("Sidebar opened");
          },
          onChatMinimized: () => {
            console.log("Sidebar closed");
          },
        }}
      >
        <YourApp/>
      </CopilotSidebar>
    </CopilotKit>

### Look & Feel

By default, CopilotKit components do not have any styles. You can import CopilotKit's stylesheet at the root of your project:

YourRootComponent.tsx
    
    
    ...
    import "@copilotkit/react-ui/styles.css"; 
     
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

`instructions?`string

Prop

Type

`suggestions?`ChatSuggestions

Prop

Type

`onInProgress?`(inProgress: boolean) => void

Prop

Type

`onSubmitMessage?`(message: string) => void | Promise<void>

Prop

Type

`onStopGeneration?`OnStopGeneration

Prop

Type

`onReloadMessages?`OnReloadMessages

Prop

Type

`onRegenerate?`(messageId: string) => void

Prop

Type

`onCopy?`(message: string) => void

Prop

Type

`onThumbsUp?`(message: Message, isActive?: boolean) => void

Prop

Type

`onThumbsDown?`(message: Message, isActive?: boolean) => void

Prop

Type

`markdownTagRenderers?`ComponentsMap

Prop

Type

`icons?`CopilotChatIcons

Prop

Type

`labels?`CopilotChatLabels

Prop

Type

`attachments?`AttachmentsConfig

Prop

Type

`makeSystemMessage?`SystemMessageFunction

Prop

Type

`disableSystemMessage?`boolean

Prop

Type

`AssistantMessage?`React.ComponentType<AssistantMessageProps>

Prop

Type

`UserMessage?`React.ComponentType<UserMessageProps>

Prop

Type

`ErrorMessage?`React.ComponentType<ErrorMessageProps>

Prop

Type

`Messages?`React.ComponentType<MessagesProps>

Prop

Type

`RenderMessage?`React.ComponentType<RenderMessageProps>

Prop

Type

`RenderSuggestionsList?`React.ComponentType<RenderSuggestionsListProps>

Prop

Type

`Input?`React.ComponentType<InputProps>

Prop

Type

`className?`string

Prop

Type

`children?`React.ReactNode

Prop

Type

`hideStopButton?`boolean

Prop

Type

`observabilityHooks?`CopilotObservabilityHooks

Prop

Type

`renderError?`(error: { message: string; operation?: string; timestamp: number; onDismiss: () => void; onRetry?: () => void; }) => React.ReactNode

Prop

Type

`onError?`CopilotErrorHandler

Prop

Type

`defaultOpen?`boolean

Prop

Type

`clickOutsideToClose?`boolean

Prop

Type

`hitEscapeToClose?`boolean

Prop

Type

`shortcut?`string

Prop

Type

`onSetOpen?`(open: boolean) => void

Prop

Type

`Window?`React.ComponentType<WindowProps>

Prop

Type

`Button?`React.ComponentType<ButtonProps>

Prop

Type

`Header?`React.ComponentType<HeaderProps>

Prop

Type

`fullHeightChildren?`boolean
