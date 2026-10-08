---
url: https://docs.copilotkit.ai/reference/v2/hooks/useCopilotChatConfiguration/
title: useCopilotChatConfiguration
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:34:41.161759+00:00
---

# useCopilotChatConfiguration

> Source: https://docs.copilotkit.ai/reference/v2/hooks/useCopilotChatConfiguration/

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

[Reference](https://docs.copilotkit.ai/reference)[v2](https://docs.copilotkit.ai/reference/v2)Hooks

# useCopilotChatConfiguration

React hook and provider for chat UI configuration and labels

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useCopilotChatConfiguration` is a React hook that reads the chat configuration context. It returns the configuration value from the nearest `CopilotChatConfigurationProvider`, or `null` if no provider is present.

This page documents both the **hook** and the **`CopilotChatConfigurationProvider`** component, which together provide a lightweight context for localized labels, agent/thread binding, and modal state used by the chat UI components.

## CopilotChatConfigurationProvider

A provider component that exposes localized labels, agent and thread IDs, and optional modal state to all descendant chat components.

### Signature
    
    
    import { CopilotChatConfigurationProvider } from "@copilotkit/react-core/v2";
    
    <CopilotChatConfigurationProvider
      labels={...}
      agentId="my-agent"
      threadId="thread-123"
      isModalDefaultOpen={true}
    >
      {children}
    </CopilotChatConfigurationProvider>

### Props

Prop

Type

`children`ReactNode

Prop

Type

`labels?`Partial<CopilotChatLabels>

Prop

Type

`agentId?`string

Prop

Type

`threadId?`string

Prop

Type

`isModalDefaultOpen?`boolean

## useCopilotChatConfiguration

### Signature
    
    
    import { useCopilotChatConfiguration } from "@copilotkit/react-core/v2";
    
    function useCopilotChatConfiguration(): CopilotChatConfigurationValue | null;

### Parameters

This hook takes no parameters.

### Return Value

Returns `null` if used outside of a `CopilotChatConfigurationProvider`. Otherwise returns a `CopilotChatConfigurationValue` object:

Prop

Type

`config?`CopilotChatConfigurationValue

## CopilotChatLabels

The `CopilotChatLabels` type defines all customizable text strings used by the chat UI. The following keys are available with their default values:

Key| Default Value  
---|---  
`chatInputPlaceholder`| `"Type a message..."`  
`chatInputToolbarStartTranscribeButtonLabel`| `"Transcribe"`  
`chatInputToolbarCancelTranscribeButtonLabel`| `"Cancel"`  
`chatInputToolbarFinishTranscribeButtonLabel`| `"Finish"`  
`chatInputToolbarAddButtonLabel`| `"Add photos or files"`  
`chatInputToolbarToolsButtonLabel`| `"Tools"`  
`assistantMessageToolbarCopyCodeLabel`| `"Copy"`  
`assistantMessageToolbarCopyCodeCopiedLabel`| `"Copied"`  
`assistantMessageToolbarCopyMessageLabel`| `"Copy"`  
`assistantMessageToolbarThumbsUpLabel`| `"Good response"`  
`assistantMessageToolbarThumbsDownLabel`| `"Bad response"`  
`assistantMessageToolbarReadAloudLabel`| `"Read aloud"`  
`assistantMessageToolbarRegenerateLabel`| `"Regenerate"`  
`userMessageToolbarCopyMessageLabel`| `"Copy"`  
`userMessageToolbarEditMessageLabel`| `"Edit"`  
`chatDisclaimerText`| `"AI can make mistakes. Please verify important information."`  
`chatToggleOpenLabel`| `"Open chat"`  
`chatToggleCloseLabel`| `"Close chat"`  
`modalHeaderTitle`| `"CopilotKit Chat"`  
`welcomeMessageText`| `"How can I help you today?"`  
  
## Usage

### Basic Label Customization
    
    
    import {
      CopilotChatConfigurationProvider,
      useCopilotChatConfiguration,
    } from "@copilotkit/react-core/v2";
    
    function App() {
      return (
        <CopilotChatConfigurationProvider
          labels={{
            chatInputPlaceholder: "Ask me anything...",
            modalHeaderTitle: "AI Assistant",
            welcomeMessageText: "Hello! What can I do for you?",
            chatDisclaimerText: "Responses are AI-generated.",
          }}
        >
          <ChatUI />
        </CopilotChatConfigurationProvider>
      );
    }

### Reading Configuration in a Component
    
    
    function ChatHeader() {
      const config = useCopilotChatConfiguration();
    
      if (!config) {
        return <h2>Chat</h2>;
      }
    
      return <h2>{config.labels.modalHeaderTitle}</h2>;
    }

### Binding to a Specific Agent and Thread
    
    
    function SupportChat() {
      return (
        <CopilotChatConfigurationProvider
          agentId="support-agent"
          threadId="ticket-456"
          labels={{
            chatInputPlaceholder: "Describe your issue...",
            modalHeaderTitle: "Support Chat",
          }}
        >
          <ChatWindow />
        </CopilotChatConfigurationProvider>
      );
    }

### Modal State Management
    
    
    import {
      CopilotChatConfigurationProvider,
      useCopilotChatConfiguration,
    } from "@copilotkit/react-core/v2";
    
    function App() {
      return (
        <CopilotChatConfigurationProvider isModalDefaultOpen={false}>
          <ToggleButton />
          <ChatModal />
        </CopilotChatConfigurationProvider>
      );
    }
    
    function ToggleButton() {
      const config = useCopilotChatConfiguration();
    
      if (!config?.setModalOpen) return null;
    
      return (
        <button onClick={() => config.setModalOpen!(!config.isModalOpen)}>
          {config.isModalOpen
            ? config.labels.chatToggleCloseLabel
            : config.labels.chatToggleOpenLabel}
        </button>
      );
    }

### Nested Providers

Providers can be nested. Child providers inherit and merge labels from their parent, with child overrides taking precedence.
    
    
    function App() {
      return (
        <CopilotChatConfigurationProvider
          labels={{ chatDisclaimerText: "Company-wide disclaimer." }}
        >
          <CopilotChatConfigurationProvider
            agentId="sales"
            labels={{ modalHeaderTitle: "Sales Assistant" }}
          >
            {/* This context has both the company disclaimer and the sales title */}
            <SalesChat />
          </CopilotChatConfigurationProvider>
        </CopilotChatConfigurationProvider>
      );
    }

## Behavior

  * **Label Merging** : Labels are merged in order: built-in defaults, then parent provider labels, then current provider labels. This allows partial overrides at any level.
  * **Agent ID Resolution** : The `agentId` resolves from the nearest provider, falling back to parent providers, then to `"default"`.
  * **Thread ID Generation** : If no `threadId` is provided at any level, a random UUID is generated and remains stable for the lifetime of the provider.
  * **Modal State Ownership** : Modal state (`isModalOpen` / `setModalOpen`) is only created when a provider explicitly sets `isModalDefaultOpen`. Providers without this prop pass through the parent's modal state.
  * **Null Return** : The hook returns `null` when used outside any `CopilotChatConfigurationProvider`, rather than throwing an error. Components should handle this case gracefully.



## Related

  * [`useSuggestions`](https://docs.copilotkit.ai/reference/hooks/useSuggestions) \-- Uses `CopilotChatConfigurationProvider` context for agent ID resolution
  * [`CopilotChat`](https://docs.copilotkit.ai/reference/components/CopilotChat) \-- Chat component that wraps its children with this provider


