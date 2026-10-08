---
url: https://docs.copilotkit.ai/reference/angular/directives/CopilotKitAgentContext/
title: CopilotKitAgentContext
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:56.087180+00:00
---

# CopilotKitAgentContext

> Source: https://docs.copilotkit.ai/reference/angular/directives/CopilotKitAgentContext/

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

[Reference](https://docs.copilotkit.ai/reference)[angular](https://docs.copilotkit.ai/reference/angular)Directives

# CopilotKitAgentContext

Angular standalone directive that shares application state with the agent as context from a template for @copilotkit/angular.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotKitAgentContext` is a standalone Angular directive that shares a piece of [context](https://docs.ag-ui.com/concepts/context) with the agent from your template. Apply it to any element. It adds a complete context when the element initializes, updates an existing registration when its inputs change, and removes it when the element is destroyed.

You can supply the context either as a single object via the directive selector input, or as separate `description` and `value` inputs. The context object takes precedence when both are provided.

This is the template-based alternative to [`connectAgentContext`](https://docs.copilotkit.ai/reference/angular/functions/connectAgentContext).

## Import

The directive is standalone. Import the class into your component's `imports` array, then use the `copilotkitAgentContext` attribute selector in the template.

src/app/profile.component.ts
    
    
    import { Component } from "@angular/core";
    import { CopilotKitAgentContext } from "@copilotkit/angular";
    
    @Component({
      selector: "app-profile",
      standalone: true,
      imports: [CopilotKitAgentContext],
      template: `
        <div copilotkitAgentContext
             description="User profile"
             [value]="profileJson">
        </div>
      `,
    })
    export class ProfileComponent {
      profile = { name: "Ada", plan: "pro" };
      profileJson = JSON.stringify(this.profile);
    }

## Selector
    
    
    [copilotkitAgentContext]

It is an attribute directive, so apply it to any element.

## Inputs

Prop

Type

`copilotkitAgentContext?`Context

Prop

Type

`description?`string

Prop

Type

`value?`any

## Usage

### Separate inputs
    
    
    <div copilotkitAgentContext
         description="User preferences"
         [value]="userSettingsJson">
    </div>

### Context object

Pass a complete `{ description, value }` object through the selector input.
    
    
    <div [copilotkitAgentContext]="contextObject"></div>

### Updating a registered context

The directive re-registers a context when inputs change after a complete context was registered during initialization. Supply both fields at initialization.
    
    
    <div [copilotkitAgentContext]="formContext"></div>

If the initial object or separate value is missing, a later input change does not create the first registration. Render the directive only after the complete context is available, or use [`connectAgentContext`](https://docs.copilotkit.ai/reference/angular/functions/connectAgentContext) for a reactive accessor.

## Behavior

  * **Adds on init.** The context is registered with the agent in `ngOnInit`.
  * **Updates an existing registration.** When `copilotkitAgentContext`, `description`, or `value` changes after initialization registered a context, the directive removes the previous context and adds the new one.
  * **Does not add after an empty initialization.** If initialization has no complete context, later input changes do not create the first registration.
  * **Removes on destroy.** The context is removed when the host element is destroyed.
  * **Object input precedence.** When the `copilotkitAgentContext` object input is set, it is used and the separate `description` and `value` inputs are ignored. Otherwise, the context is built from `description` and `value`, and is only registered when both are set.



## Related

### [connectAgentContextShare context with the agent from a function instead of a template.](https://docs.copilotkit.ai/reference/angular/functions/connectAgentContext)### [injectAgentStoreSubscribe to an agent and read its messages, state, and run status.](https://docs.copilotkit.ai/reference/angular/functions/injectAgentStore)### [CopilotKit serviceThe central handle on agents, tools, and the runtime connection.](https://docs.copilotkit.ai/reference/angular/services/CopilotKit)
