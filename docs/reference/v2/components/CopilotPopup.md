---
url: https://docs.copilotkit.ai/reference/v2/components/CopilotPopup/
title: CopilotPopup
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:34:38.665669+00:00
---

# CopilotPopup

> Source: https://docs.copilotkit.ai/reference/v2/components/CopilotPopup/

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

# CopilotPopup

Popup variant of CopilotChat that renders in a floating panel with a toggle button

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotPopup` renders a floating chat popup with a toggle button. It wraps [`CopilotChat`](https://docs.copilotkit.ai/reference/components/CopilotChat) and provides popup-specific layout, sizing, and open/close behavior. The popup includes a header with a title and close button, and can be dismissed by clicking outside.

See [`CopilotSidebar`](https://docs.copilotkit.ai/reference/components/CopilotSidebar) for a sidebar variant of this component.

## Import
    
    
    import { CopilotPopup } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

## Props

### Own Props

Prop

Type

`header?`SlotValue<typeof CopilotModalHeader>

Prop

Type

`defaultOpen?`boolean

Prop

Type

`open?`boolean

Prop

Type

`onOpenChange?`(open: boolean) => void

Prop

Type

`width?`number | string

Prop

Type

`height?`number | string

Prop

Type

`clickOutsideToClose?`boolean

### Inherited CopilotChat Props

`CopilotPopup` accepts all props from [`CopilotChatProps`](https://docs.copilotkit.ai/reference/components/CopilotChat) **except** `chatView`, which is set internally to `CopilotPopupView`. This includes:

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

`autoScroll?`boolean

Prop

Type

`inputProps?`Partial<Omit<CopilotChatInputProps, 'children'>>

Prop

Type

`welcomeScreen?`SlotValue<React.FC<WelcomeScreenProps>> | boolean

All `CopilotChatView` slot props (`messageView`, `input`, `scrollView`, `inputContainer`, `feather`, `disclaimer`, `suggestionView`) are also accepted and forwarded through.

## Slot System

All slot props follow the same override pattern used across CopilotKit v2 components. Each slot accepts one of three value types:

Value| Behavior  
---|---  
**Component**|  Replaces the default component entirely. Receives the same props the default would.  
**`className` string**| Merged into the default component's class list via `twMerge`.  
**Partial props object**|  Spread into the default component as additional or overriding props.  
  
## Usage

### Basic Usage
    
    
    function App() {
      return (
        <CopilotPopup
          agentId="my-agent"
          labels={{ modalHeaderTitle: "Assistant" }}
        />
      );
    }

### Custom Size and Default Open
    
    
    function App() {
      return (
        <CopilotPopup
          agentId="my-agent"
          defaultOpen={true}
          width={450}
          height="80vh"
          clickOutsideToClose={false}
        />
      );
    }

### Custom Header
    
    
    function App() {
      return <CopilotPopup agentId="my-agent" header="bg-blue-600 text-white" />;
    }

## Behavior

  * **Toggle button** : Renders a floating toggle button (typically in the bottom-right corner) that opens and closes the popup. The button uses `CopilotChatToggleButton` internally.
  * **Modal state** : Open/close state is managed via the chat configuration context. The `defaultOpen` prop sets the initial state; after that, state changes come from user interaction (toggle button, close button, clicking outside). Pass `open` and `onOpenChange` to own the state yourself, and to open or close the popup from your own UI.
  * **Click outside** : When `clickOutsideToClose` is `true` (the default), clicking anywhere outside the popup panel closes it.
  * **Layout** : The popup uses `CopilotPopupView` internally, which provides a popup-specific welcome screen layout with the welcome message centered vertically and suggestions just above the input.
  * **Agent connection** : All agent wiring (messages, running state, suggestions) is handled by the parent `CopilotChat` logic.



## Related

  * [`CopilotChat`](https://docs.copilotkit.ai/reference/components/CopilotChat) \-- the base chat component used internally
  * [`CopilotSidebar`](https://docs.copilotkit.ai/reference/components/CopilotSidebar) \-- sidebar variant
  * [`CopilotChatView`](https://docs.copilotkit.ai/reference/components/CopilotChatView) \-- the layout component used internally


