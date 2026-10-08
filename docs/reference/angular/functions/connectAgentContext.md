---
url: https://docs.copilotkit.ai/reference/angular/functions/connectAgentContext/
title: connectAgentContext
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:56.133834+00:00
---

# connectAgentContext

> Source: https://docs.copilotkit.ai/reference/angular/functions/connectAgentContext/

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

# connectAgentContext

Angular function that adds reactive context for the agent and cleans it up automatically for @copilotkit/angular.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`connectAgentContext` registers [context](https://docs.ag-ui.com/concepts/context) with the agent so it can read your application state. It accepts a static `Context` object or a zero-argument accessor. The internal Angular `effect` tracks any signals read by the accessor and updates the context when they change.

The registration is wrapped in an Angular `effect`, so the context is cleaned up automatically when the owning component or service is destroyed.

For a template-driven alternative, use the [`CopilotKitAgentContext`](https://docs.copilotkit.ai/reference/angular/directives/CopilotKitAgentContext) directive.

Call this from an Angular injection context, such as a constructor or field initializer. The current implementation resolves the ambient injector before it reads the config, so passing `config.injector` does not make an outside-context call valid.

## Signature
    
    
    import { connectAgentContext } from "@copilotkit/angular";
    import type { Injector } from "@angular/core";
    import type { Context } from "@ag-ui/client";
    
    interface ConnectAgentContextConfig {
      injector?: Injector;
    }
    
    function connectAgentContext(
      context: Context | (() => Context),
      config?: ConnectAgentContextConfig,
    ): void;

## Parameters

Prop

Type

`context`Context | (() => Context)

Prop

Type

`config?`ConnectAgentContextConfig

## Usage

### Static context

src/app/preferences.component.ts
    
    
    import { Component } from "@angular/core";
    import { connectAgentContext } from "@copilotkit/angular";
    
    @Component({
      selector: "app-preferences",
      standalone: true,
      template: `<!-- ... -->`,
    })
    export class PreferencesComponent {
      constructor() {
        connectAgentContext({
          description: "User preferences",
          value: JSON.stringify({ theme: "dark", locale: "en-US" }),
        });
      }
    }

### Reactive context with an accessor

Pass an accessor that reads signals so the agent always sees the current value.

src/app/cart.component.ts
    
    
    import { Component, signal } from "@angular/core";
    import { connectAgentContext } from "@copilotkit/angular";
    
    @Component({
      selector: "app-cart",
      standalone: true,
      template: `<button (click)="add()">Add item</button>`,
    })
    export class CartComponent {
      readonly items = signal<string[]>([]);
    
      constructor() {
        // Re-registers with the agent whenever the cart changes.
        connectAgentContext(() => ({
          description: "Current shopping cart",
          value: JSON.stringify(this.items()),
        }));
      }
    
      add() {
        this.items.update((items) => [...items, "Item"]);
      }
    }

## Behavior

  * **Reactive updates.** When an accessor reads signals, the context is removed and re-added whenever one of those signals changes.
  * **Automatic cleanup.** Registration runs inside an Angular `effect`; the context is removed when the effect is torn down, which happens when the owning component, service, or injector is destroyed.
  * **Injection context required.** Angular throws `NG0203` when you call the function outside an injection context.



## Related

### [CopilotKitAgentContext directiveShare context with the agent from a template instead of a function.](https://docs.copilotkit.ai/reference/angular/directives/CopilotKitAgentContext)### [injectAgentStoreSubscribe to an agent and read its messages, state, and run status.](https://docs.copilotkit.ai/reference/angular/functions/injectAgentStore)### [CopilotKit serviceThe central handle on agents, tools, and the runtime connection.](https://docs.copilotkit.ai/reference/angular/services/CopilotKit)
