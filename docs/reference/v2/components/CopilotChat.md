---
url: https://docs.copilotkit.ai/reference/v2/components/CopilotChat/
title: CopilotChat
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:34:33.220752+00:00
---

# CopilotChat

> Source: https://docs.copilotkit.ai/reference/v2/components/CopilotChat/

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

# CopilotChat

High-level chat component that connects an agent to a chat view

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotChat` is a high-level chat container that wires an agent into `CopilotChatView` while providing configuration context. It obtains the agent via `useAgent`, triggers an initial `runAgent` when mounting CopilotKit agents, manages pending state, and auto-clears the input after submission. Override any of the internal slots by passing `CopilotChatView` props directly.

`CopilotChat` manages messages, running state, and suggestions automatically -- you only need to specify which agent to connect and, optionally, customise labels or slot overrides.

## Import
    
    
    import { CopilotChat } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

## Props

### Own Props

Prop

Type

`agentId?`string

Prop

Type

`threadId?`string

Prop

Type

`labels?`Partial<CopilotChatLabels>

Prop

Type

`chatView?`SlotValue<typeof CopilotChatView>

Prop

Type

`inspectorTools?`boolean

Prop

Type

`onError?`(event: { error: Error; code: CopilotKitCoreErrorCode; context: Record<string, any> }) => void | Promise<void>

Prop

Type

`isModalDefaultOpen?`boolean

### Inherited CopilotChatView Props

`CopilotChat` accepts all props from [`CopilotChatViewProps`](https://docs.copilotkit.ai/reference/components/CopilotChatView) **except** `messages`, `isRunning`, `suggestions`, `suggestionLoadingIndexes`, and `onSelectSuggestion`, which are managed internally by the agent connection.

This means you can pass slot overrides such as `messageView`, `input`, `scrollView`, `inputContainer`, `feather`, `disclaimer`, `suggestionView`, and `welcomeScreen` directly to `CopilotChat`.

Prop

Type

`autoScroll?`boolean

Prop

Type

`inputProps?`Partial<Omit<CopilotChatInputProps, 'children'>>

Prop

Type

`welcomeScreen?`SlotValue<React.FC<WelcomeScreenProps>> | boolean

## Slot System

All slot props inherited from `CopilotChatView` follow the same override pattern. Each slot accepts one of three value types:

Value| Behavior  
---|---  
**Component**|  Replaces the default component entirely. Receives the same props the default would.  
**`className` string**| Merged into the default component's class list via `twMerge`.  
**Partial props object**|  Spread into the default component as additional or overriding props.  
  
Additionally, a `children` render-prop can be used to receive all composed slot elements and arrange them in a custom layout.

## Usage

### Basic Usage
    
    
    function App() {
      return (
        <CopilotChat
          agentId="my-agent"
          labels={{ chatInputPlaceholder: "Ask me anything..." }}
        />
      );
    }

### Custom Welcome Screen
    
    
    function App() {
      return (
        <CopilotChat
          agentId="my-agent"
          welcomeScreen={({ input, suggestionView }) => (
            <div className="flex flex-col items-center justify-center h-full gap-4">
              <h2>Welcome to the assistant</h2>
              {suggestionView}
              {input}
            </div>
          )}
        />
      );
    }

### Overriding the Chat View Slot
    
    
    function App() {
      return (
        <CopilotChat
          agentId="my-agent"
          chatView="bg-gray-50 rounded-xl shadow-lg"
        />
      );
    }

## Behavior

  * **Agent wiring** : On mount, `CopilotChat` calls `useAgent` with the provided `agentId` and binds the agent's `messages`, `isRunning`, and suggestion state to `CopilotChatView`.
  * **Initial run** : If the agent has not been run yet, `CopilotChat` triggers `runAgent` automatically so the agent can send an initial greeting or set up state.
  * **Auto-clear input** : After a message is submitted, the input field is cleared automatically.
  * **Configuration context** : Wraps children in `CopilotChatConfigurationProvider`, making `labels`, `agentId`, `threadId`, and modal state available to all descendant components via `useCopilotChatConfiguration`.
  * **Suggestion management** : Subscribes to the agent's suggestion system and passes suggestions, loading states, and selection callbacks down to `CopilotChatView`.



## Related

  * [`CopilotChatView`](https://docs.copilotkit.ai/reference/components/CopilotChatView) \-- the layout component used internally
  * [`CopilotPopup`](https://docs.copilotkit.ai/reference/components/CopilotPopup) \-- popup variant of `CopilotChat`
  * [`CopilotSidebar`](https://docs.copilotkit.ai/reference/components/CopilotSidebar) \-- sidebar variant of `CopilotChat`
  * [`useAgent`](https://docs.copilotkit.ai/reference/hooks/useAgent) \-- hook used internally to access the agent


