---
url: https://docs.copilotkit.ai/reference/angular/functions/injectCopilotKitConfig/
title: injectCopilotKitConfig
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:58.972573+00:00
---

# injectCopilotKitConfig

> Source: https://docs.copilotkit.ai/reference/angular/functions/injectCopilotKitConfig/

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

# injectCopilotKitConfig

Angular function that reads the CopilotKitConfig provided through provideCopilotKit from the current injection context

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`injectCopilotKitConfig` returns the [`CopilotKitConfig`](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit#parameters) that you registered with [`provideCopilotKit`](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit). It reads the value bound to the `COPILOT_KIT_CONFIG` injection token, so it must run inside an Angular injection context (a constructor, a field initializer, or a factory).

Most applications do not call this directly. The [`CopilotKit`](https://docs.copilotkit.ai/reference/angular/services/CopilotKit) service uses it internally to build its core. Reach for it when you need to read the raw config you provided, for example to read your own `properties` or `runtimeUrl`.

## Signature
    
    
    import { injectCopilotKitConfig } from "@copilotkit/angular";
    
    function injectCopilotKitConfig(): CopilotKitConfig;

## Return Value

Returns the `CopilotKitConfig` bound to the `COPILOT_KIT_CONFIG` token. Note that the `headers` field reflects the merged headers computed by `provideCopilotKit`, which may include the `X-CopilotCloud-Public-Api-Key` header derived from your `licenseKey`.

## Usage

Call it from an injection context, such as a service constructor or a component field initializer.

src/app/runtime-info.service.ts
    
    
    import { Injectable } from "@angular/core";
    import { injectCopilotKitConfig } from "@copilotkit/angular";
    
    @Injectable({ providedIn: "root" })
    export class RuntimeInfoService {
      private readonly config = injectCopilotKitConfig();
    
      get runtimeUrl(): string | undefined {
        return this.config.runtimeUrl;
      }
    }

## Related

### [provideCopilotKitRegister the CopilotKitConfig that this function reads back.](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit)### [CopilotKitThe service that consumes the configuration and exposes runtime state as signals.](https://docs.copilotkit.ai/reference/angular/services/CopilotKit)
