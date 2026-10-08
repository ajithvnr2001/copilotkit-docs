---
url: https://docs.copilotkit.ai/reference/angular/components/CopilotChat/
title: CopilotChat
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:53.275674+00:00
---

# CopilotChat

> Source: https://docs.copilotkit.ai/reference/angular/components/CopilotChat/

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

# CopilotChat

Angular standalone component that wires an agent to a complete chat UI

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotChat` is the all-in-one chat component. It wires an agent into [`CopilotChatView`](https://docs.copilotkit.ai/reference/angular/components/CopilotChatView) so you get a working chat interface with one selector. It resolves the agent through [`injectAgentStore`](https://docs.copilotkit.ai/reference/angular/functions/injectAgentStore), subscribes to that agent's messages and running state, manages suggestions, tracks the input value, handles audio transcription, wires file attachments, and clears the input after each message is sent.

`CopilotChat` extends `ChatState` and provides itself to the view and input beneath it. You usually only need to point it at an agent.

For the layout without the agent wiring, use [`CopilotChatView`](https://docs.copilotkit.ai/reference/angular/components/CopilotChatView) directly.

## Usage

`CopilotChat` is a standalone component with the selector `copilot-chat`. Import the class into your component's `imports` array and use the element in the template. The chat reads its configuration from [`provideCopilotKit`](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit), so the provider must be in scope.

src/app/app.component.ts
    
    
    import { Component } from "@angular/core";
    import { CopilotChat } from "@copilotkit/angular";
    
    @Component({
      selector: "app-root",
      standalone: true,
      imports: [CopilotChat],
      template: `<copilot-chat />`,
    })
    export class AppComponent {}

Remember to import the stylesheet once in your global styles:

src/styles.css
    
    
    @import "@copilotkit/angular/styles.css";

## Inputs

Prop

Type

`agentId?`string

Prop

Type

`threadId?`string

Prop

Type

`attachments?`AttachmentsConfig

Prop

Type

`inputComponent?`Type<any>

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

## Outputs

`CopilotChat` does not declare its own outputs. It handles message submission, suggestion selection, and transcription internally through the `ChatState` it provides to the input and view. To observe lower-level interactions, render a custom input via `inputComponent` (or use [`CopilotChatInput`](https://docs.copilotkit.ai/reference/angular/components/CopilotChatInput) directly), which exposes outputs such as `submitMessage` and the transcription events.

## Customization

`CopilotChat` keeps the layout simple and delegates slot customization to the view it renders. Swap the input area with the `inputComponent` input, or compose the layout yourself with [`CopilotChatView`](https://docs.copilotkit.ai/reference/angular/components/CopilotChatView), which exposes the full set of slot inputs and content-projection templates (message view, scroll view, feather, disclaimer, input container, and the input toolbar buttons).

To customize the text strings (input placeholder, welcome message, toolbar labels, disclaimer), provide labels through [`provideCopilotChatLabels`](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotChatLabels). The chat reads them through `injectChatLabels` internally.

## Related

### [CopilotChatViewThe layout-only chat view used internally. Use it when you manage messages and handlers yourself.](https://docs.copilotkit.ai/reference/angular/components/CopilotChatView)### [CopilotChatInputThe input area: textarea, send button, tools menu, file upload, and transcription.](https://docs.copilotkit.ai/reference/angular/components/CopilotChatInput)### [provideCopilotKitConfigures the runtime connection and agents that CopilotChat reads from.](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit)
