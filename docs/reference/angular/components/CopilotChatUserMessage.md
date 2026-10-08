---
url: https://docs.copilotkit.ai/reference/angular/components/CopilotChatUserMessage/
title: CopilotChatUserMessage
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:55.973715+00:00
---

# CopilotChatUserMessage

> Source: https://docs.copilotkit.ai/reference/angular/components/CopilotChatUserMessage/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁AngularSDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Guides

[Public API inventory](https://docs.copilotkit.ai/reference/angular/public-api)[Production and lifecycle](https://docs.copilotkit.ai/reference/angular/production-lifecycle)

Components

[CopilotActivity](https://docs.copilotkit.ai/reference/angular/components/CopilotActivity)[CopilotChat](https://docs.copilotkit.ai/reference/angular/components/CopilotChat)[CopilotChatAssistantMessage](https://docs.copilotkit.ai/reference/angular/components/CopilotChatAssistantMessage)[CopilotChatInput](https://docs.copilotkit.ai/reference/angular/components/CopilotChatInput)[CopilotChatMessageView](https://docs.copilotkit.ai/reference/angular/components/CopilotChatMessageView)[CopilotChatUserMessage](https://docs.copilotkit.ai/reference/angular/components/CopilotChatUserMessage)[CopilotChatView](https://docs.copilotkit.ai/reference/angular/components/CopilotChatView)[CopilotPopup](https://docs.copilotkit.ai/reference/angular/components/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/angular/components/CopilotSidebar)

Functions

[connectAgentContext](https://docs.copilotkit.ai/reference/angular/functions/connectAgentContext)[injectAgentStore](https://docs.copilotkit.ai/reference/angular/functions/injectAgentStore)[injectCapabilities](https://docs.copilotkit.ai/reference/angular/functions/injectCapabilities)[injectChatLabels](https://docs.copilotkit.ai/reference/angular/functions/injectChatLabels)[injectCopilotKitConfig](https://docs.copilotkit.ai/reference/angular/functions/injectCopilotKitConfig)[injectInterrupt](https://docs.copilotkit.ai/reference/angular/functions/injectInterrupt)[injectThreads](https://docs.copilotkit.ai/reference/angular/functions/injectThreads)[provideCopilotChatLabels](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotChatLabels)[provideCopilotKit](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit)[provideMCPApps](https://docs.copilotkit.ai/reference/angular/functions/provideMCPApps)[registerComponent](https://docs.copilotkit.ai/reference/angular/functions/registerComponent)[registerFrontendTool](https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool)[registerHumanInTheLoop](https://docs.copilotkit.ai/reference/angular/functions/registerHumanInTheLoop)[registerRenderActivityMessage](https://docs.copilotkit.ai/reference/angular/functions/registerRenderActivityMessage)[registerRenderToolCall](https://docs.copilotkit.ai/reference/angular/functions/registerRenderToolCall)

Services

[CopilotKit](https://docs.copilotkit.ai/reference/angular/services/CopilotKit)

Directives

[CopilotKitAgentContext](https://docs.copilotkit.ai/reference/angular/directives/CopilotKitAgentContext)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[angular](https://docs.copilotkit.ai/reference/angular)Components

# CopilotChatUserMessage

Angular standalone component that renders a single user message with attachments, copy and edit actions, and branch navigation.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotChatUserMessage` renders one user message. It shows image or file attachments, renders the message text, and shows a toolbar with copy and edit actions. When the message belongs to a set of regenerated branches, a branch control lets you move between them.

The copy and edit buttons always render. The branch navigation control renders only when `numberOfBranches` is greater than 1.

The component is standalone and uses `OnPush` change detection. Reactive inputs are Angular [signals](https://angular.dev/guide/signals).

## Usage

Import the component class and use its `copilot-chat-user-message` selector.

src/app/user-message.component.ts
    
    
    import { Component, signal } from "@angular/core";
    import { CopilotChatUserMessage } from "@copilotkit/angular";
    import type { UserMessage } from "@ag-ui/core";
    
    @Component({
      selector: "app-user-message",
      standalone: true,
      imports: [CopilotChatUserMessage],
      template: `
        <copilot-chat-user-message
          [message]="message()"
          (editMessage)="onEdit($event)"
        />
      `,
    })
    export class UserMessageComponent {
      message = signal<UserMessage>({
        id: "1",
        role: "user",
        content: "What is the weather today?",
      });
    
      onEdit(event: { message: UserMessage }) {
        console.log("edit", event.message.id);
      }
    }

## Inputs

Prop

Type

`message?`UserMessage

Prop

Type

`branchIndex?`number

Prop

Type

`numberOfBranches?`number

Prop

Type

`additionalToolbarItems?`TemplateRef<any>

Prop

Type

`inputClass?`string

### Slot class inputs

Each of these passes extra CSS classes to the corresponding default sub-component.

Prop

Type

`messageRendererClass?`string

Prop

Type

`toolbarClass?`string

Prop

Type

`copyButtonClass?`string

Prop

Type

`editButtonClass?`string

Prop

Type

`branchNavigationClass?`string

### Slot component inputs

Each of these replaces the corresponding default sub-component with a component class of your own. Content-projection templates (see below) take precedence over these.

Prop

Type

`messageRendererComponent?`Type<any>

Prop

Type

`toolbarComponent?`Type<any>

Prop

Type

`copyButtonComponent?`Type<any>

Prop

Type

`editButtonComponent?`Type<any>

Prop

Type

`branchNavigationComponent?`Type<any>

## Outputs

Prop

Type

`editMessage?`CopilotChatUserMessageOnEditMessageProps

Prop

Type

`switchToBranch?`CopilotChatUserMessageOnSwitchToBranchProps

## Slots and content projection

You can override any piece of the message by projecting a named template. A projected template takes precedence over the matching `*Component` input. Each template receives a typed context object.

Template name| Context type| Replaces  
---|---|---  
`messageRenderer`| `MessageRendererContext` (`{ content: string }`)| The message text renderer  
`toolbar`| `UserMessageToolbarContext` (`{ children?: any }`)| The whole toolbar  
`copyButton`| `CopyButtonContext` (`{ content?: string; copied?: boolean }`)| The copy button  
`editButton`| `EditButtonContext` (empty; click via outputs)| The edit button  
`branchNavigation`| `BranchNavigationContext` (`{ currentBranch, numberOfBranches, onSwitchToBranch?, message }`)| The branch navigation control  
  
src/app/user-message.component.html
    
    
    <copilot-chat-user-message [message]="message()">
      <ng-template #messageRenderer let-content="content">
        <p class="my-user-text">{{ content }}</p>
      </ng-template>
    </copilot-chat-user-message>

## Related

### [CopilotChatMessageViewRenders a list of messages, routing each to assistant, user, reasoning, or activity rendering.](https://docs.copilotkit.ai/reference/angular/components/CopilotChatMessageView)### [CopilotChatAssistantMessageRenders a single assistant message with markdown content, a toolbar, and tool calls.](https://docs.copilotkit.ai/reference/angular/components/CopilotChatAssistantMessage)### [CopilotChatViewThe full chat layout: scroll container, message view, and input.](https://docs.copilotkit.ai/reference/angular/components/CopilotChatView)
