---
url: https://docs.copilotkit.ai/reference/angular/components/CopilotChatAssistantMessage/
title: CopilotChatAssistantMessage
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:53.232856+00:00
---

# CopilotChatAssistantMessage

> Source: https://docs.copilotkit.ai/reference/angular/components/CopilotChatAssistantMessage/

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

# CopilotChatAssistantMessage

Angular standalone component that renders a single assistant message with markdown content, tool calls, and a toolbar of copy, thumbs, read-aloud, and regenerate actions.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotChatAssistantMessage` renders one assistant message. It shows the message content through a markdown renderer, renders attached tool calls, and shows a toolbar with copy, thumbs up/down, read-aloud, and regenerate actions.

The toolbar appears only when the message has non-empty text content. The copy button always renders; the thumbs up and thumbs down buttons render when you provide a custom slot for them or when a thumbs handler is available from a surrounding [`CopilotChatView`](https://docs.copilotkit.ai/reference/angular/components/CopilotChatView). The read-aloud and regenerate buttons render only when you provide a custom slot for them.

The component is standalone and uses `OnPush` change detection. Reactive inputs are Angular [signals](https://angular.dev/guide/signals).

## Usage

Import the component class and use its `copilot-chat-assistant-message` selector. The `message` input is required.

src/app/assistant.component.ts
    
    
    import { Component, signal } from "@angular/core";
    import { CopilotChatAssistantMessage } from "@copilotkit/angular";
    import type { AssistantMessage } from "@ag-ui/client";
    
    @Component({
      selector: "app-assistant",
      standalone: true,
      imports: [CopilotChatAssistantMessage],
      template: `
        <copilot-chat-assistant-message [message]="message()" />
      `,
    })
    export class AssistantComponent {
      message = signal<AssistantMessage>({
        id: "1",
        role: "assistant",
        content: "Hello, how can I help?",
      });
    }

## Inputs

Prop

Type

`message`AssistantMessage

Prop

Type

`messages?`Message[]

Prop

Type

`agentId?`string

Prop

Type

`isLoading?`boolean

Prop

Type

`toolbarVisible?`boolean

Prop

Type

`additionalToolbarItems?`TemplateRef<any>

### Slot class inputs

The current release applies `markdownRendererClass`, `toolbarClass`, and `copyButtonClass` to their default parts.

Prop

Type

`markdownRendererClass?`string

Prop

Type

`toolbarClass?`string

Prop

Type

`copyButtonClass?`string

`inputClass`, the thumbs, read-aloud, regenerate class inputs, and `toolCallsViewClass` are declared but do not affect rendering in the current release. Use component or template overrides for those parts.

### Slot component inputs

Each of these replaces the corresponding default sub-component with a component class of your own. Content-projection templates (see below) take precedence over these.

Prop

Type

`markdownRendererComponent?`Type<any>

Prop

Type

`toolbarComponent?`Type<any>

Prop

Type

`copyButtonComponent?`Type<any>

Prop

Type

`thumbsUpButtonComponent?`Type<any>

Prop

Type

`thumbsDownButtonComponent?`Type<any>

Prop

Type

`readAloudButtonComponent?`Type<any>

Prop

Type

`regenerateButtonComponent?`Type<any>

Prop

Type

`toolCallsViewComponent?`Type<any>

## Outputs

Prop

Type

`thumbsUp?`CopilotChatAssistantMessageOnThumbsUpProps

Prop

Type

`thumbsDown?`CopilotChatAssistantMessageOnThumbsDownProps

Prop

Type

`readAloud?`CopilotChatAssistantMessageOnReadAloudProps

Prop

Type

`regenerate?`CopilotChatAssistantMessageOnRegenerateProps

## Slots and content projection

You can override any piece of the message by projecting a named template. A projected template takes precedence over the matching `*Component` input. Each template receives a typed context object.

Template name| Context type| Replaces  
---|---|---  
`markdownRenderer`| `AssistantMessageMarkdownRendererContext` (`{ content: string }`)| The markdown content renderer  
`toolbar`| `AssistantMessageToolbarContext` (`{ children?: any }`)| The whole toolbar  
`copyButton`| `AssistantMessageCopyButtonContext` (`{ content?: string }`)| The copy button  
`thumbsUpButton`| `ThumbsUpButtonContext` (empty; click via outputs)| The thumbs-up button  
`thumbsDownButton`| `ThumbsDownButtonContext` (empty; click via outputs)| The thumbs-down button  
`readAloudButton`| `ReadAloudButtonContext` (empty; click via outputs)| The read-aloud button  
`regenerateButton`| `RegenerateButtonContext` (empty; click via outputs)| The regenerate button  
`toolCallsView`| `any`| The tool calls view  
  
src/app/assistant.component.html
    
    
    <copilot-chat-assistant-message [message]="message()">
      <ng-template #markdownRenderer let-content="content">
        <article class="my-markdown">{{ content }}</article>
      </ng-template>
    </copilot-chat-assistant-message>

## Related

### [CopilotChatMessageViewRenders a list of messages, routing each to assistant, user, reasoning, or activity rendering.](https://docs.copilotkit.ai/reference/angular/components/CopilotChatMessageView)### [CopilotChatUserMessageRenders a single user message with copy, edit, and branch navigation.](https://docs.copilotkit.ai/reference/angular/components/CopilotChatUserMessage)### [CopilotChatViewThe full chat layout: scroll container, message view, and input.](https://docs.copilotkit.ai/reference/angular/components/CopilotChatView)
