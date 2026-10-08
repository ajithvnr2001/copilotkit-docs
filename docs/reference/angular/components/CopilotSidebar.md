---
url: https://docs.copilotkit.ai/reference/angular/components/CopilotSidebar/
title: CopilotSidebar
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:55.885575+00:00
---

# CopilotSidebar

> Source: https://docs.copilotkit.ai/reference/angular/components/CopilotSidebar/

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

# CopilotSidebar

Responsive docked or overlay Copilot chat sidebar for Angular.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

`CopilotSidebar` renders a left- or right-positioned assistant in docked or overlay mode. It is a standalone, OnPush component with the selector `copilot-sidebar`.
    
    
    import { Component, signal } from "@angular/core";
    import { CopilotSidebar } from "@copilotkit/angular";
    
    @Component({
      imports: [CopilotSidebar],
      template: `
        <copilot-sidebar
          [(open)]="open"
          mode="docked"
          position="right"
          [width]="480"
          title="Workspace assistant"
        />
      `,
    })
    export class WorkspaceAssistant {
      readonly open = signal(false);
    }

## Inputs and model

Name| Type| Default| Behavior  
---|---|---|---  
`open`| `ModelSignal<boolean>`| `true`| Two-way bindable open state  
`mode`| `"docked" | "overlay"`| `"docked"`| Desktop presentation mode  
`position`| `"left" | "right"`| `"right"`| Logical side of the viewport  
`width`| `number | string`| `480`| Pixel number or CSS dimension  
`title`| `string`| `"Copilot"`| Landmark/dialog name and header text  
`clickOutsideToClose`| `boolean`| `false`| Opts into overlay backdrop closing  
`chatComponent`| `Type<unknown>`| `CopilotChat`| Replacement chat body component  
`headerComponent`| `Type<unknown> | undefined`| `undefined`| Replacement header component  
  
Overlay mode uses modal dialog semantics, focus trapping, Escape closing, and launcher-focus restoration. Docked mode uses a complementary landmark and adjusts the document's logical body margin. Compact viewports always use the modal presentation.

Only one docked sidebar may own document layout at a time. A second open docked sidebar is rejected and logs a clear warning; independent overlay sidebars are allowed. On close or destroy, the owner restores the exact prior body margin and removes its media-query listener. DOM and media-query work is browser-only and begins after render, so SSR remains inert. Keep `open`, `mode`, and `position` stable through hydration.
