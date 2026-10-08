---
url: https://docs.copilotkit.ai/reference/angular/components/CopilotChatView/
title: CopilotChatView
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:56.052402+00:00
---

# CopilotChatView

> Source: https://docs.copilotkit.ai/reference/angular/components/CopilotChatView/

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

# CopilotChatView

Angular standalone component that renders the chat layout without agent wiring

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotChatView` is the layout-only chat view. It renders the message feed, the input container, the feather effect, the disclaimer, the suggestion pills, and a welcome screen when there are no messages. It does not wire an agent on its own. You pass it `messages` and read interaction handlers from the surrounding `ChatState`.

[`CopilotChat`](https://docs.copilotkit.ai/reference/angular/components/CopilotChat) wires the agent, messages, running state, suggestions, and submission, then renders `CopilotChatView`. Use `CopilotChatView` directly when you manage those values and handlers, or when you need full control over the layout and its slots.

The active slot inputs accept a component class (`*Component`) or an Angular template (`*Template`). The template takes precedence when both are set.

## Usage

`CopilotChatView` is a standalone component with the selector `copilot-chat-view`. Its default input needs a `ChatState` provider. The example below supplies one.

src/app/chat.component.ts
    
    
    import { Component, forwardRef, signal } from "@angular/core";
    import { ChatState, CopilotChatView } from "@copilotkit/angular";
    import type { Message } from "@ag-ui/client";
    
    @Component({
      selector: "app-chat",
      standalone: true,
      imports: [CopilotChatView],
      providers: [
        {
          provide: ChatState,
          useExisting: forwardRef(() => ChatComponent),
        },
      ],
      template: `
        <copilot-chat-view [messages]="messages()" [autoScroll]="true" />
      `,
    })
    export class ChatComponent extends ChatState {
      readonly messages = signal<Message[]>([]);
      readonly inputValue = signal("");
    
      submitInput(value: string) {
        // Send the message through your chat state owner.
      }
    
      changeInput(value: string) {
        this.inputValue.set(value);
      }
    }

## Inputs

### Core inputs

Prop

Type

`messages?`Message[]

Prop

Type

`state?`unknown

Prop

Type

`agentId?`string

Prop

Type

`autoScroll?`boolean

Prop

Type

`showCursor?`boolean

Prop

Type

`hasExplicitThreadId?`boolean

### Slot inputs

The view forwards message, input, scroll-button, input-container, feather, and disclaimer slots.

Prop

Type

`messageViewComponent?`Type<any>

Prop

Type

`messageViewTemplate?`TemplateRef<any>

Prop

Type

`messageViewClass?`string

The current release declares `scrollViewComponent`, `scrollViewTemplate`, and `scrollViewClass`, but the default layout always uses its built-in scroll view. Use `customLayout` when you need to replace it.

Prop

Type

`assistantMessageComponent?`Type<any>

Prop

Type

`assistantMessageTemplate?`TemplateRef<any>

Prop

Type

`assistantMessageClass?`string

Prop

Type

`reasoningMessageComponent?`Type<any>

Prop

Type

`reasoningMessageTemplate?`TemplateRef<any>

Prop

Type

`reasoningMessageClass?`string

Prop

Type

`messageViewChildrenComponent?`Type<any>

Prop

Type

`messageViewChildrenTemplate?`TemplateRef<any>

Prop

Type

`messageViewChildrenClass?`string

Prop

Type

`scrollToBottomButtonComponent?`Type<any>

Prop

Type

`scrollToBottomButtonTemplate?`TemplateRef<any>

Prop

Type

`scrollToBottomButtonClass?`string

Prop

Type

`inputComponent?`Type<any>

Prop

Type

`inputTemplate?`TemplateRef<any>

Prop

Type

`inputContainerComponent?`Type<any>

Prop

Type

`inputContainerTemplate?`TemplateRef<any>

Prop

Type

`inputContainerClass?`string

Prop

Type

`featherComponent?`Type<any>

Prop

Type

`featherTemplate?`TemplateRef<any>

`featherClass` is declared but the current release does not pass its string value to the feather slot. Use a feather component or template to style that region.

Prop

Type

`disclaimerComponent?`Type<any>

Prop

Type

`disclaimerTemplate?`TemplateRef<any>

Prop

Type

`disclaimerClass?`string

Prop

Type

`disclaimerText?`string

## Outputs

`CopilotChatView` bubbles assistant-message actions from the message feed. Each payload is an object with the relevant `message`.

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

The current release declares `userMessageCopy` and `userMessageEdit`, but the default message view does not emit them.

## Content projection

`CopilotChatView` supports one active projected template named `customLayout`.

Prop

Type

`customLayout?`TemplateRef<CopilotChatViewLayoutContext>

The class declares projected templates for input buttons and assistant-message parts, but the current release does not forward them. Configure those parts through `inputComponent`, the message slot inputs, or a custom layout.

### Custom layout example

src/app/chat.component.ts
    
    
    import { Component, forwardRef, signal } from "@angular/core";
    import {
      ChatState,
      CopilotChatInput,
      CopilotChatMessageView,
      CopilotChatView,
    } from "@copilotkit/angular";
    import type { Message } from "@ag-ui/client";
    
    @Component({
      selector: "app-chat",
      standalone: true,
      imports: [CopilotChatInput, CopilotChatMessageView, CopilotChatView],
      providers: [
        {
          provide: ChatState,
          useExisting: forwardRef(() => ChatComponent),
        },
      ],
      template: `
        <copilot-chat-view [messages]="messages()">
          <ng-template #customLayout>
            <div class="my-layout">
              <copilot-chat-message-view [messages]="messages()" />
              <copilot-chat-input />
            </div>
          </ng-template>
        </copilot-chat-view>
      `,
    })
    export class ChatComponent extends ChatState {
      readonly messages = signal<Message[]>([]);
      readonly inputValue = signal("");
    
      submitInput(value: string) {
        // Send the message through your chat state owner.
      }
    
      changeInput(value: string) {
        this.inputValue.set(value);
      }
    }

## Related

### [CopilotChatThe all-in-one component that wires an agent and renders this view.](https://docs.copilotkit.ai/reference/angular/components/CopilotChat)### [CopilotChatInputThe default input rendered inside the view: textarea, send, tools menu, file upload, and transcription.](https://docs.copilotkit.ai/reference/angular/components/CopilotChatInput)### [provideCopilotKitConfigures the runtime connection and agents that power the chat.](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit)
