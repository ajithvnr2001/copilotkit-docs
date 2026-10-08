---
url: https://docs.copilotkit.ai/reference/v2/components/CopilotSidebar/
title: CopilotSidebar
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:34:38.858442+00:00
---

# CopilotSidebar

> Source: https://docs.copilotkit.ai/reference/v2/components/CopilotSidebar/

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

# CopilotSidebar

Sidebar variant of CopilotChat that renders in a fixed side panel

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotSidebar` renders a fixed sidebar panel for chat interaction. It wraps [`CopilotChat`](https://docs.copilotkit.ai/reference/components/CopilotChat) and provides sidebar-specific layout and open/close behavior. The sidebar includes a header with a title and close button, and can be toggled via a floating button.

See [`CopilotPopup`](https://docs.copilotkit.ai/reference/components/CopilotPopup) for a popup variant of this component.

## Import
    
    
    import { CopilotSidebar } from "@copilotkit/react-core/v2";
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

### Inherited CopilotChat Props

`CopilotSidebar` accepts all props from [`CopilotChatProps`](https://docs.copilotkit.ai/reference/components/CopilotChat) **except** `chatView`, which is set internally to `CopilotSidebarView`. This includes:

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
        <CopilotSidebar
          agentId="my-agent"
          labels={{ modalHeaderTitle: "Assistant" }}
        />
      );
    }

### Default Open with Custom Width
    
    
    function App() {
      return <CopilotSidebar agentId="my-agent" defaultOpen={true} width={500} />;
    }

### Custom Header
    
    
    function App() {
      return (
        <CopilotSidebar agentId="my-agent" header="bg-indigo-700 text-white" />
      );
    }

## Behavior

  * **Toggle button** : Renders a floating toggle button that opens and closes the sidebar. The button uses `CopilotChatToggleButton` internally.
  * **Modal state** : Open/close state is managed via the chat configuration context. The `defaultOpen` prop sets the initial state; after that, state changes come from user interaction (toggle button, close button in the header). Pass `open` and `onOpenChange` to own the state yourself, and to open or close the sidebar from your own UI.
  * **Layout** : The sidebar uses `CopilotSidebarView` internally, which provides a sidebar-specific welcome screen layout with suggestions at the top, the welcome message in the middle, and the input fixed at the bottom.
  * **Fixed positioning** : The sidebar renders as a fixed panel on one side of the viewport, pushing or overlaying content depending on CSS.
  * **Agent connection** : All agent wiring (messages, running state, suggestions) is handled by the parent `CopilotChat` logic.



## Related

  * [`CopilotChat`](https://docs.copilotkit.ai/reference/components/CopilotChat) \-- the base chat component used internally
  * [`CopilotPopup`](https://docs.copilotkit.ai/reference/components/CopilotPopup) \-- popup variant
  * [`CopilotChatView`](https://docs.copilotkit.ai/reference/components/CopilotChatView) \-- the layout component used internally


