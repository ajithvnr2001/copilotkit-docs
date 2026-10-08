---
url: https://docs.copilotkit.ai/reference/v2/components/CopilotChatUserMessage/
title: CopilotChatUserMessage
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:34:38.999355+00:00
---

# CopilotChatUserMessage

> Source: https://docs.copilotkit.ai/reference/v2/components/CopilotChatUserMessage/

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

# CopilotChatUserMessage

Component for displaying user-authored messages with branch navigation

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotChatUserMessage` shows user-authored messages aligned to the right with optional branch navigation. The default message renderer formats content with `white-space: pre-wrap` to preserve line breaks. Branch navigation controls only render when `numberOfBranches` is greater than 1 and an `onSwitchToBranch` handler is provided, enabling users to navigate between alternative conversation branches.

## Import
    
    
    import { CopilotChatUserMessage } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

## Props

Prop

Type

`message`UserMessage

Prop

Type

`onEditMessage?`(props: { message: UserMessage }) => void

Prop

Type

`onSwitchToBranch?`(props: { message: UserMessage; branchIndex: number; numberOfBranches: number }) => void

Prop

Type

`branchIndex?`number

Prop

Type

`numberOfBranches?`number

Prop

Type

`additionalToolbarItems?`React.ReactNode

## Slots

All slot props follow the CopilotKit slot system: each accepts a replacement React component, a `className` string that is merged into the default component's classes, or a partial props object that extends the default component.

Prop

Type

`messageRenderer?`SlotProp<typeof CopilotChatUserMessage.MessageRenderer>

Prop

Type

`toolbar?`SlotProp<typeof CopilotChatUserMessage.Toolbar>

Prop

Type

`copyButton?`SlotProp<typeof CopilotChatUserMessage.CopyButton>

Prop

Type

`editButton?`SlotProp<typeof CopilotChatUserMessage.EditButton>

Prop

Type

`branchNavigation?`SlotProp<typeof CopilotChatUserMessage.BranchNavigation>

## Usage

### Basic User Message
    
    
    function UserBubble({ message }) {
      return <CopilotChatUserMessage message={message} />;
    }

### With Edit Support
    
    
    function EditableUserMessage({ message, onEdit }) {
      return (
        <CopilotChatUserMessage
          message={message}
          onEditMessage={({ message }) => onEdit(message)}
        />
      );
    }

### With Branch Navigation
    
    
    function BranchedUserMessage({
      message,
      branchIndex,
      totalBranches,
      onSwitch,
    }) {
      return (
        <CopilotChatUserMessage
          message={message}
          branchIndex={branchIndex}
          numberOfBranches={totalBranches}
          onSwitchToBranch={({ branchIndex }) => onSwitch(branchIndex)}
        />
      );
    }

### Customizing Appearance with Slots
    
    
    function StyledUserMessage({ message }) {
      return (
        <CopilotChatUserMessage
          message={message}
          messageRenderer="bg-blue-600 text-white rounded-2xl px-4 py-2"
          toolbar="mt-1"
          onEditMessage={({ message }) => console.log("Edit:", message.id)}
          additionalToolbarItems={
            <button onClick={() => console.log("Pin:", message.id)}>Pin</button>
          }
        />
      );
    }

### Full Edit and Branch Workflow
    
    
    function FullFeaturedUserMessage({ message, branches }) {
      const [currentBranch, setCurrentBranch] = useState(0);
    
      return (
        <CopilotChatUserMessage
          message={message}
          branchIndex={currentBranch}
          numberOfBranches={branches.length}
          onSwitchToBranch={({ branchIndex }) => setCurrentBranch(branchIndex)}
          onEditMessage={({ message }) => {
            // Open edit modal
            openEditModal(message);
          }}
        />
      );
    }

## Behavior

  * **Right-Aligned Layout** : User messages are rendered with right-aligned positioning to visually distinguish them from assistant messages.
  * **Whitespace Preservation** : The default message renderer uses `white-space: pre-wrap`, so line breaks and spacing in the original message are preserved.
  * **Conditional Branch Navigation** : The branch navigation controls are only rendered when both conditions are met: `numberOfBranches > 1` and `onSwitchToBranch` is provided. This prevents showing navigation for single-branch conversations.
  * **Conditional Edit Button** : The edit button only appears in the toolbar when `onEditMessage` is provided.
  * **Localized Labels** : Toolbar button tooltips are sourced from the nearest `CopilotChatConfigurationProvider`. See [`useCopilotChatConfiguration`](https://docs.copilotkit.ai/reference/hooks/useCopilotChatConfiguration) for available label keys.
  * **Slot System** : Each slot prop accepts three forms -- a replacement component, a className string merged into the default, or a partial props object that extends the default component's props.



## Related

  * [`CopilotChatMessageView`](https://docs.copilotkit.ai/reference/components/CopilotChatMessageView) \-- Parent component that uses this as the default user message slot
  * [`CopilotChatAssistantMessage`](https://docs.copilotkit.ai/reference/components/CopilotChatAssistantMessage) \-- Companion component for assistant messages
  * [`useCopilotChatConfiguration`](https://docs.copilotkit.ai/reference/hooks/useCopilotChatConfiguration) \-- Provider for localized toolbar labels


