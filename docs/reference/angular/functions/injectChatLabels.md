---
url: https://docs.copilotkit.ai/reference/angular/functions/injectChatLabels/
title: injectChatLabels
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:58.947304+00:00
---

# injectChatLabels

> Source: https://docs.copilotkit.ai/reference/angular/functions/injectChatLabels/

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

[Reference](https://docs.copilotkit.ai/reference)[angular](https://docs.copilotkit.ai/reference/angular)Functions

# injectChatLabels

Angular function that returns the CopilotKit chat labels, with provided overrides merged over the defaults

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`injectChatLabels` returns the full set of [`CopilotChatLabels`](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotChatLabels#parameters) in scope: any labels you provided through [`provideCopilotChatLabels`](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotChatLabels) merged over `COPILOT_CHAT_DEFAULT_LABELS`. If no labels were provided, it returns the defaults unchanged.

It reads the `COPILOT_CHAT_LABELS` injection token (optionally), so it must run inside an Angular injection context (a constructor, a field initializer, or a factory). The prebuilt chat components call it internally; use it directly when you build your own chat UI and want the same configurable strings.

## Signature
    
    
    import { injectChatLabels } from "@copilotkit/angular";
    
    function injectChatLabels(): CopilotChatLabels;

## Return Value

Returns a complete `CopilotChatLabels` object. Because the value is the merge of your overrides over the defaults, every field is always present (never `undefined`).

## Usage

Call it from an injection context and read the labels you need.

src/app/my-chat.component.ts
    
    
    import { Component } from "@angular/core";
    import { injectChatLabels } from "@copilotkit/angular";
    
    @Component({
      selector: "app-my-chat",
      standalone: true,
      template: `<input [placeholder]="labels.chatInputPlaceholder" />`,
    })
    export class MyChatComponent {
      protected readonly labels = injectChatLabels();
    }

## Related

### [provideCopilotChatLabelsProvide the label overrides that this function merges over the defaults.](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotChatLabels)### [CopilotChatThe prebuilt chat component that uses these labels internally.](https://docs.copilotkit.ai/reference/angular/components/CopilotChat)
