---
url: https://docs.copilotkit.ai/reference/angular/components/CopilotPopup/
title: CopilotPopup
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:55.924041+00:00
---

# CopilotPopup

> Source: https://docs.copilotkit.ai/reference/angular/components/CopilotPopup/

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

# CopilotPopup

Accessible floating Copilot chat dialog for Angular.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

`CopilotPopup` renders a floating launcher and responsive chat dialog. It is a standalone, OnPush component with the selector `copilot-popup`.
    
    
    import { Component, signal } from "@angular/core";
    import { CopilotPopup } from "@copilotkit/angular";
    
    @Component({
      imports: [CopilotPopup],
      template: `
        <copilot-popup
          [(open)]="open"
          title="Support assistant"
          [width]="420"
          [height]="560"
          [clickOutsideToClose]="false"
        />
      `,
    })
    export class SupportAssistant {
      readonly open = signal(false);
    }

## Inputs and model

Name| Type| Default| Behavior  
---|---|---|---  
`open`| `ModelSignal<boolean>`| `true`| Two-way bindable open state  
`title`| `string`| `"Copilot"`| Accessible dialog name and default header text  
`width`| `number | string`| `420`| Pixel number or CSS dimension  
`height`| `number | string`| `560`| Pixel number or CSS dimension  
`clickOutsideToClose`| `boolean`| `false`| Opts into backdrop-click closing  
`chatComponent`| `Type<unknown>`| `CopilotChat`| Replacement chat body component  
`headerComponent`| `Type<unknown> | undefined`| `undefined`| Replacement header component  
  
The dialog traps focus, moves initial focus to its close control, closes on Escape, and restores focus to the launcher. It becomes full-screen on compact viewports and disables its entrance animation when reduced motion is requested. Destroying the component removes its rendered dialog and Angular CDK focus-trap state. Browser focus work starts after rendering and is inert during SSR; keep the initial `open` value unchanged until hydration completes.
