---
url: https://docs.copilotkit.ai/reference/angular/functions/provideCopilotChatLabels/
title: provideCopilotChatLabels
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:05.012604+00:00
---

# provideCopilotChatLabels

> Source: https://docs.copilotkit.ai/reference/angular/functions/provideCopilotChatLabels/

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

# provideCopilotChatLabels

Angular provider that overrides the default text labels used by the CopilotKit chat components

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`provideCopilotChatLabels` returns an Angular [`Provider`](https://angular.dev/guide/di/dependency-injection-providers) that customizes the text labels used throughout the prebuilt chat components, such as the input placeholder, toolbar button labels, the disclaimer text, and the welcome message. You pass a partial set of labels and they are merged over the defaults, so you only override the strings you want to change.

Add it to an application or component `providers` array. Components read the merged labels through [`injectChatLabels`](https://docs.copilotkit.ai/reference/angular/functions/injectChatLabels).

The full set of defaults lives in `COPILOT_CHAT_DEFAULT_LABELS`. Any field you omit falls back to its default value.

## Signature
    
    
    import { provideCopilotChatLabels } from "@copilotkit/angular";
    import type { Provider } from "@angular/core";
    
    function provideCopilotChatLabels(
      config: Partial<CopilotChatLabels>,
    ): Provider;

## Parameters

Prop

Type

`config`Partial<CopilotChatLabels>

## Return Value

Returns an Angular `Provider` that binds the merged labels to the `COPILOT_CHAT_LABELS` injection token.

## Usage

Override a few labels in your application config. Everything you do not list keeps its default.

src/app/app.config.ts
    
    
    import { ApplicationConfig } from "@angular/core";
    import {
      provideCopilotKit,
      provideCopilotChatLabels,
    } from "@copilotkit/angular";
    
    export const appConfig: ApplicationConfig = {
      providers: [
        provideCopilotKit({ runtimeUrl: "/api/copilotkit" }),
        provideCopilotChatLabels({
          chatInputPlaceholder: "Ask me anything...",
          welcomeMessageText: "Welcome! What can I help you build?",
        }),
      ],
    };

You can also scope labels to part of your app by adding the provider to a feature component's `providers` array instead of the application config.

## Related

### [injectChatLabelsRead the merged chat labels from within an injection context.](https://docs.copilotkit.ai/reference/angular/functions/injectChatLabels)### [CopilotChatThe prebuilt chat component whose text these labels customize.](https://docs.copilotkit.ai/reference/angular/components/CopilotChat)
