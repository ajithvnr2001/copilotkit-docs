---
url: https://docs.copilotkit.ai/reference/angular/components/CopilotChatMessageView/
title: CopilotChatMessageView
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:53.453607+00:00
---

# CopilotChatMessageView

> Source: https://docs.copilotkit.ai/reference/angular/components/CopilotChatMessageView/

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

# CopilotChatMessageView

Angular standalone component that renders a list of chat messages, routing each message to assistant, user, reasoning, or activity rendering with slot customization.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotChatMessageView` renders an array of messages and routes each one to the correct renderer based on its `role`: assistant messages go to [`CopilotChatAssistantMessage`](https://docs.copilotkit.ai/reference/angular/components/CopilotChatAssistantMessage), user messages to [`CopilotChatUserMessage`](https://docs.copilotkit.ai/reference/angular/components/CopilotChatUserMessage), reasoning messages to the reasoning renderer, and activity messages to [`CopilotActivity`](https://docs.copilotkit.ai/reference/angular/components/CopilotActivity), which resolves the registered activity renderer. It optionally renders a typing cursor at the end of the list while the agent is streaming.

This is the message-list layer used by [`CopilotChatView`](https://docs.copilotkit.ai/reference/angular/components/CopilotChatView). Use it directly when you manage your own `messages` array and want the list without the surrounding scroll container and input.

The component is standalone and uses `OnPush` change detection. Reactive inputs are Angular [signals](https://angular.dev/guide/signals).

## Usage

Import the component class and use its `copilot-chat-message-view` selector in your template.

src/app/messages.component.ts
    
    
    import { Component, signal } from "@angular/core";
    import { CopilotChatMessageView } from "@copilotkit/angular";
    import type { Message } from "@ag-ui/core";
    
    @Component({
      selector: "app-messages",
      standalone: true,
      imports: [CopilotChatMessageView],
      template: `
        <copilot-chat-message-view
          [messages]="messages()"
          [showCursor]="isLoading()"
          [isLoading]="isLoading()"
        />
      `,
    })
    export class MessagesComponent {
      messages = signal<Message[]>([]);
      isLoading = signal(false);
    }

## Inputs

Prop

Type

`messages?`Message[]

Prop

Type

`showCursor?`boolean

Prop

Type

`isLoading?`boolean

Prop

Type

`state?`unknown

Prop

Type

`inputClass?`string

Prop

Type

`agentId?`string

### Assistant message slot inputs

Prop

Type

`assistantMessageComponent?`Type<any>

Prop

Type

`assistantMessageTemplate?`TemplateRef<any>

Prop

Type

`assistantMessageClass?`string

### User message slot inputs

Prop

Type

`userMessageComponent?`Type<any>

### Reasoning message slot inputs

Prop

Type

`reasoningMessageComponent?`Type<any>

Prop

Type

`reasoningMessageTemplate?`TemplateRef<any>

Prop

Type

`reasoningMessageClass?`string

### Content after the message list

Prop

Type

`childrenComponent?`Type<any>

Prop

Type

`childrenTemplate?`TemplateRef<any>

Prop

Type

`childrenClass?`string

Prop

Type

`userMessageTemplate?`TemplateRef<any>

Prop

Type

`userMessageClass?`string

### Cursor slot inputs

Prop

Type

`cursorComponent?`Type<any>

Prop

Type

`cursorTemplate?`TemplateRef<any>

Prop

Type

`cursorClass?`string

## Outputs

Assistant actions bubble up from the assistant-message child component. Each payload is `{ message: Message }`.

Prop

Type

`assistantMessageThumbsUp?`{ message: Message }

Prop

Type

`assistantMessageThumbsDown?`{ message: Message }

Prop

Type

`assistantMessageReadAloud?`{ message: Message }

Prop

Type

`assistantMessageRegenerate?`{ message: Message }

The current release declares `userMessageCopy` and `userMessageEdit`, but the default user-message child does not forward those events. Listen on a custom user-message component when you need them.

## Custom layout

For full control over how the list is laid out, project a template named `customLayout`. It receives a context object with the current `messages`, the `isLoading` and `showCursor` flags, and `messageElements` (the messages filtered to the renderable roles). When this template is present, the default list rendering is replaced entirely.

src/app/messages.component.html
    
    
    <copilot-chat-message-view [messages]="messages()" [showCursor]="isLoading()">
      <ng-template #customLayout let-messages="messages" let-showCursor="showCursor">
        <div class="my-list">
          @for (message of messages; track message.id) {
            <div class="my-row">{{ message.content }}</div>
          }
          @if (showCursor) {
            <span class="my-cursor">...</span>
          }
        </div>
      </ng-template>
    </copilot-chat-message-view>

## Customizing message rendering

To swap out how a whole role is rendered without rebuilding the layout, pass a slot input. The slot accepts either a component class or a template, with the template taking precedence.

src/app/messages.component.ts
    
    
    import { Component, signal } from "@angular/core";
    import { CopilotChatMessageView } from "@copilotkit/angular";
    import { MyAssistantMessage } from "./my-assistant-message.component";
    import type { Message } from "@ag-ui/core";
    
    @Component({
      selector: "app-messages",
      standalone: true,
      imports: [CopilotChatMessageView],
      template: `
        <copilot-chat-message-view
          [messages]="messages()"
          [assistantMessageComponent]="assistantMessage"
        />
      `,
    })
    export class MessagesComponent {
      messages = signal<Message[]>([]);
      protected readonly assistantMessage = MyAssistantMessage;
    }

## Related

### [CopilotChatAssistantMessageRenders a single assistant message with markdown content, a toolbar, and tool calls.](https://docs.copilotkit.ai/reference/angular/components/CopilotChatAssistantMessage)### [CopilotChatUserMessageRenders a single user message with copy, edit, and branch navigation.](https://docs.copilotkit.ai/reference/angular/components/CopilotChatUserMessage)### [CopilotChatViewThe full chat layout: scroll container, message view, and input.](https://docs.copilotkit.ai/reference/angular/components/CopilotChatView)
