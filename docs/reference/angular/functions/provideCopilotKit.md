---
url: https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit/
title: provideCopilotKit
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:09.125191+00:00
---

# provideCopilotKit

> Source: https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit/

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

# provideCopilotKit

Angular provider that configures CopilotKit through dependency injection: runtime URL, agents, tools, headers, and more

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`provideCopilotKit` is the primary setup entry point for `@copilotkit/angular`. It returns an Angular [`Provider`](https://angular.dev/guide/di/dependency-injection-providers) that you add to your application providers. The provider stores your `CopilotKitConfig` behind the `COPILOT_KIT_CONFIG` injection token, where the root [`CopilotKit`](https://docs.copilotkit.ai/reference/angular/services/CopilotKit) service reads it.

Register it once in `app.config.ts`. A component-local config provider alone does not configure the root `CopilotKit` service.

You typically configure the connection one of two ways: point at a CopilotKit runtime with `runtimeUrl`, or connect directly to one or more AG-UI agents with `selfManagedAgents`.

## Signature
    
    
    import { provideCopilotKit } from "@copilotkit/angular";
    import type { Provider } from "@angular/core";
    
    function provideCopilotKit(config: CopilotKitConfig): Provider;

## Parameters

Prop

Type

`config`CopilotKitConfig

## Return Value

Returns an Angular `Provider` that binds your (header-augmented) config to the `COPILOT_KIT_CONFIG` injection token. Add it to the application providers.

## Usage

### Connect through a runtime

Point `runtimeUrl` at your CopilotKit runtime endpoint and register the provider in your application config.

src/app/app.config.ts
    
    
    import { ApplicationConfig } from "@angular/core";
    import { provideCopilotKit } from "@copilotkit/angular";
    
    export const appConfig: ApplicationConfig = {
      providers: [
        provideCopilotKit({
          runtimeUrl: "/api/copilotkit",
          headers: {
            Authorization: "Bearer <token>",
          },
          properties: {
            userId: "user_123",
          },
        }),
      ],
    };

### Connect directly to an AG-UI agent

To talk to an agent server without a CopilotKit runtime, pass `selfManagedAgents` with an `@ag-ui/client` agent such as `HttpAgent`.

src/app/app.config.ts
    
    
    import { ApplicationConfig } from "@angular/core";
    import { provideCopilotKit } from "@copilotkit/angular";
    import { HttpAgent } from "@ag-ui/client";
    
    export const appConfig: ApplicationConfig = {
      providers: [
        provideCopilotKit({
          selfManagedAgents: {
            default: new HttpAgent({ url: "http://localhost:8000/" }),
          },
        }),
      ],
    };

### Register startup tools

Pass `frontendTools` to register client tools when the application starts. Their handlers run inside the root injection context, so they can use `inject()`.

src/app/app.config.ts
    
    
    import { ApplicationConfig } from "@angular/core";
    import { provideCopilotKit } from "@copilotkit/angular";
    import { z } from "zod";
    
    export const appConfig: ApplicationConfig = {
      providers: [
        provideCopilotKit({
          runtimeUrl: "/api/copilotkit",
          frontendTools: [
            {
              name: "sayHello",
              description: "Greet the user by name",
              parameters: z.object({ name: z.string() }),
              handler: async ({ name }) => `Hello, ${name}!`,
            },
          ],
        }),
      ],
    };

## Behavior

  * The provided config is bound to the `COPILOT_KIT_CONFIG` injection token. Read it with [`injectCopilotKitConfig`](https://docs.copilotkit.ai/reference/angular/functions/injectCopilotKitConfig).
  * A format-valid `licenseKey` is merged into the `X-CopilotCloud-Public-Api-Key` header unless that header is already present. The current package does not render a watermark or log a missing-key warning.
  * `agents` and `selfManagedAgents` are merged together when the underlying core is created, so an id present in both resolves to the `selfManagedAgents` entry.
  * The Inspector receives that same core instance. Angular reuses an existing `cpk-web-inspector` element when present and removes only an element it created when the root service is destroyed.



## Related

### [injectCopilotKitConfigRead the CopilotKitConfig you provided here from within an injection context.](https://docs.copilotkit.ai/reference/angular/functions/injectCopilotKitConfig)### [CopilotKitThe service that consumes this configuration and exposes agents, tools, and runtime state.](https://docs.copilotkit.ai/reference/angular/services/CopilotKit)### [CopilotChatThe prebuilt chat component to drop into a template once the provider is registered.](https://docs.copilotkit.ai/reference/angular/components/CopilotChat)
