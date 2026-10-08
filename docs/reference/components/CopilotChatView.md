---
url: https://docs.copilotkit.ai/reference/components/CopilotChatView/
title: CopilotChatView
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:30.289018+00:00
---

# CopilotChatView

> Source: https://docs.copilotkit.ai/reference/components/CopilotChatView/

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

# CopilotChatView

Layout component that combines a scrollable transcript with the input area

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotChatView` is a layout component that combines a scrollable message transcript with the chat input area, suggestion pills, a scroll-to-bottom button, and an optional welcome screen. It is the visual core of the chat interface and is used internally by [`CopilotChat`](https://docs.copilotkit.ai/reference/components/CopilotChat), [`CopilotPopup`](https://docs.copilotkit.ai/reference/components/CopilotPopup), and [`CopilotSidebar`](https://docs.copilotkit.ai/reference/components/CopilotSidebar).

Every visual piece of `CopilotChatView` is exposed as a **slot** , so you can replace, style, or extend any part without rewriting the entire layout.

## Import
    
    
    import { CopilotChatView } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

`CopilotChatView` is a **named** export of the `@copilotkit/react-core/v2` entry point. The package root, `@copilotkit/react-core`, does not export it.

## Slots

`CopilotChatView` uses the `WithSlots` pattern. Each slot prop accepts one of three value types:

Value| Behavior  
---|---  
**Component**|  Replaces the default component entirely. Receives the same props the default would.  
**`className` string**| Merged into the default component's class list via `twMerge`.  
**Partial props object**|  Spread into the default component as additional or overriding props.  
  
Passing a `children` render-prop gives you access to all composed slot elements plus data props, letting you arrange them in a fully custom layout.

### Slot Props

Prop

Type

`messageView?`SlotValue<typeof CopilotChatMessageView>

Prop

Type

`scrollView?`SlotValue<React.FC<React.HTMLAttributes<HTMLDivElement>>>

Prop

Type

`scrollToBottomButton?`SlotValue<React.FC<React.ButtonHTMLAttributes<HTMLButtonElement>>>

Prop

Type

`input?`SlotValue<typeof CopilotChatInput>

Prop

Type

`inputContainer?`SlotValue<React.FC<React.HTMLAttributes<HTMLDivElement> & { children: React.ReactNode }>>

Prop

Type

`feather?`SlotValue<React.FC<React.HTMLAttributes<HTMLDivElement>>>

Prop

Type

`disclaimer?`SlotValue<React.FC<React.HTMLAttributes<HTMLDivElement>>>

Prop

Type

`suggestionView?`SlotValue<typeof CopilotChatSuggestionView>

## Data Props

Prop

Type

`messages?`Message[]

Prop

Type

`autoScroll?`boolean

Prop

Type

`inputProps?`Partial<Omit<CopilotChatInputProps, 'children'>>

Prop

Type

`isRunning?`boolean

Prop

Type

`suggestions?`Suggestion[]

Prop

Type

`suggestionLoadingIndexes?`ReadonlyArray<number>

Prop

Type

`onSelectSuggestion?`(suggestion: Suggestion, index: number) => void

Prop

Type

`welcomeScreen?`SlotValue<React.FC<WelcomeScreenProps>> | boolean

## Static Sub-Components

`CopilotChatView` exposes its default slot implementations as static properties for use in custom compositions:

  * `CopilotChatView.ScrollView` \-- default scroll container with auto-scroll support
  * `CopilotChatView.ScrollToBottomButton` \-- default scroll-to-bottom button
  * `CopilotChatView.Feather` \-- default gradient overlay
  * `CopilotChatView.InputContainer` \-- default input container
  * `CopilotChatView.Disclaimer` \-- default disclaimer text
  * `CopilotChatView.WelcomeMessage` \-- default welcome message
  * `CopilotChatView.WelcomeScreen` \-- default welcome screen layout



## Usage

### Standalone Usage
    
    
    function CustomChat({ messages, isRunning }) {
      return (
        <CopilotChatView
          messages={messages}
          isRunning={isRunning}
          autoScroll={true}
        />
      );
    }

### Replacing a Slot with a Custom Component
    
    
    function CustomDisclaimer(props) {
      return (
        <div {...props}>Powered by CopilotKit. Responses may contain errors.</div>
      );
    }
    
    function Chat({ messages, isRunning }) {
      return (
        <CopilotChatView
          messages={messages}
          isRunning={isRunning}
          disclaimer={CustomDisclaimer}
        />
      );
    }

### Styling a Slot with a className
    
    
    function Chat({ messages, isRunning }) {
      return (
        <CopilotChatView
          messages={messages}
          isRunning={isRunning}
          scrollView="bg-gray-50"
          inputContainer="border-t border-gray-200"
        />
      );
    }

### Custom Layout with Children Render-Prop
    
    
    function Chat({ messages, isRunning }) {
      return (
        <CopilotChatView messages={messages} isRunning={isRunning}>
          {({
            scrollView,
            input,
            inputContainer,
            feather,
            disclaimer,
            suggestionView,
          }) => (
            <div className="flex flex-col h-full">
              <div className="flex-1 overflow-hidden">{scrollView}</div>
              {feather}
              {suggestionView}
              {inputContainer}
            </div>
          )}
        </CopilotChatView>
      );
    }

## Behavior

  * **Auto-scroll** : When `autoScroll` is `true`, the view uses a stick-to-bottom strategy that keeps the latest message visible. A scroll-to-bottom button appears when the user scrolls up.
  * **Welcome screen** : When `messages` is empty and `welcomeScreen` is not `false`, a welcome screen is rendered in place of the transcript. The welcome screen receives the `input` and `suggestionView` elements so they can be placed within the welcome layout.
  * **Input container positioning** : The input container is absolutely positioned at the bottom of the chat, and the scroll area pads its content to avoid overlap.
  * **Resize handling** : The scroll view monitors input container height changes to keep padding in sync and hides the scroll-to-bottom button during resize transitions.



## Related

  * [`CopilotChat`](https://docs.copilotkit.ai/reference/components/CopilotChat) \-- high-level component that wires an agent into `CopilotChatView`
  * [`CopilotPopup`](https://docs.copilotkit.ai/reference/components/CopilotPopup) \-- popup variant that uses `CopilotPopupView` (extends `CopilotChatView`)
  * [`CopilotSidebar`](https://docs.copilotkit.ai/reference/components/CopilotSidebar) \-- sidebar variant that uses `CopilotSidebarView` (extends `CopilotChatView`)


