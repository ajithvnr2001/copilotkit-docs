---
url: https://docs.copilotkit.ai/reference/angular/
title: Angular
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:53.313335+00:00
---

# Angular

> Source: https://docs.copilotkit.ai/reference/angular/

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

[Reference](https://docs.copilotkit.ai/reference)[angular](https://docs.copilotkit.ai/reference/angular)

# Angular

API reference for @copilotkit/angular: the CopilotKit providers, prebuilt chat components, services, and functions for building CopilotKit into an Angular app.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

`@copilotkit/angular` provides [providers](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit), prebuilt chat components, a `CopilotKit` service, and standalone functions for Angular applications. Everything is built on the [AG-UI](https://docs.ag-ui.com) agent protocol.

The package targets Angular 22, and ships as standalone components and providers. Import the main API from `@copilotkit/angular`. MCP Apps uses the `@copilotkit/angular/mcp-apps` entry point. There is no `/v2` subpath.

## Installation
    
    
    npm install @copilotkit/angular @angular/cdk

`@angular/cdk` and `rxjs` are peer dependencies. If your agent connects directly over AG-UI, also install `@ag-ui/client`.

## Styling

When using the prebuilt UI components, import the stylesheet once in your global styles. It is self-contained, so the chat renders without any other CSS.

src/styles.css
    
    
    @import "@copilotkit/angular/styles.css";

## Provider setup

Add [`provideCopilotKit`](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit) to your application providers and configure the runtime connection there. The root `CopilotKit` service reads this application-level configuration.

src/app/app.config.ts
    
    
    import { ApplicationConfig } from "@angular/core";
    import { provideCopilotKit } from "@copilotkit/angular";
    
    export const appConfig: ApplicationConfig = {
      providers: [
        provideCopilotKit({
          runtimeUrl: "/api/copilotkit",
        }),
      ],
    };

To connect directly to an AG-UI agent without a runtime, pass `selfManagedAgents` instead of `runtimeUrl`:

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

Then drop the chat into a standalone component's template:

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

## Angular conventions

CopilotKit follows Angular's dependency-injection and signal patterns:

  * Register [`provideCopilotKit`](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit) in application providers.
  * Read reactive state by calling signals such as `agentStore().messages()`.
  * Call injectable helpers from a constructor, field initializer, or another injection context.
  * Import standalone components in the component `imports` array.
  * Customize UI with component inputs, templates, directives, and content projection.



## Lifecycle and rendering environments

Injectable helpers bind their effects, subscriptions, runtime registrations, timers, and observers to the owning Angular `DestroyRef`. Call them from a field initializer, constructor, or explicit injection context. Do not cache an injected controller beyond that injector's lifetime. Application-owned work started inside a tool handler, such as a fetch, remains the application's responsibility to cancel.

CopilotKit's main chat components use signals and support zoneless change detection. Browser-only behavior is inert during server rendering and activates after hydration. Keep configuration and initial model/input values identical for the server and the first client render, avoid running agents or tools on the server, and place application-owned DOM work behind an Angular platform guard or `afterNextRender`.

A2UI, Open Generative UI, audio capture, and MCP Apps can be present in an SSR tree, but their custom elements, media APIs, sandboxes, and iframes become interactive only in the browser. See [Angular production and lifecycle](https://docs.copilotkit.ai/reference/angular/production-lifecycle) for the full setup, cleanup, error, SSR, hydration, and zoneless contract.

## API Reference

Looking for tool rendering? Start with [`registerComponent`](https://docs.copilotkit.ai/reference/angular/functions/registerComponent) to let the agent display one of your components, [`registerFrontendTool`](https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool), [`registerRenderToolCall`](https://docs.copilotkit.ai/reference/angular/functions/registerRenderToolCall), and [`registerHumanInTheLoop`](https://docs.copilotkit.ai/reference/angular/functions/registerHumanInTheLoop).

### [UI ComponentsPrebuilt chat, popup, sidebar, and supported component-slot primitives.](https://docs.copilotkit.ai/reference/angular/components/CopilotChat)### [FunctionsSetup providers and injectable functions for agents, tools, context, and chat labels.](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit)### [ServicesThe CopilotKit service: the central handle on agents, tools, runtime connection, and suggestions.](https://docs.copilotkit.ai/reference/angular/services/CopilotKit)### [DirectivesThe CopilotKitAgentContext directive for sharing application state with the agent from a template.](https://docs.copilotkit.ai/reference/angular/directives/CopilotKitAgentContext)### [Public API InventoryThe complete root and MCP Apps export contract, including the explicitly internal extension token.](https://docs.copilotkit.ai/reference/angular/public-api)
