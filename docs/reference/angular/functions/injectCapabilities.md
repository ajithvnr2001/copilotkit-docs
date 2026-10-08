---
url: https://docs.copilotkit.ai/reference/angular/functions/injectCapabilities/
title: injectCapabilities
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:59.053304+00:00
---

# injectCapabilities

> Source: https://docs.copilotkit.ai/reference/angular/functions/injectCapabilities/

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

# injectCapabilities

Angular function for reading an agent's declared capabilities as a readonly signal.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`injectCapabilities` returns the [AG-UI `AgentCapabilities`](https://docs.ag-ui.com/concepts/capabilities) declared by the resolved agent as an Angular signal.

Capabilities are populated from the runtime `/info` response. This function is a convenience selector over `injectAgentStore`; it does not keep separate capability state or make its own request. The signal is `undefined` until runtime discovery completes or when the agent does not declare capabilities.

## Signature
    
    
    import { injectCapabilities } from "@copilotkit/angular";
    import type { Signal } from "@angular/core";
    import type { AgentCapabilities } from "@ag-ui/core";
    
    function injectCapabilities(
      agentId?: string | Signal<string | undefined>,
    ): Signal<AgentCapabilities | undefined>;

## Parameters

Prop

Type

`agentId?`string | Signal<string | undefined>

## Return Value

Prop

Type

`capabilities?`Signal<AgentCapabilities | undefined>

## Usage

src/app/tool-panel.component.ts
    
    
    import { Component } from "@angular/core";
    import { injectCapabilities } from "@copilotkit/angular";
    
    @Component({
      selector: "app-tool-panel",
      standalone: true,
      template: `
        @if (capabilities()?.tools?.supported === true) {
          <p>This agent supports tools.</p>
        }
      `,
    })
    export class ToolPanelComponent {
      readonly capabilities = injectCapabilities();
    }

To read another agent or switch reactively, pass its id or an id signal from a component class:
    
    
    import { signal } from "@angular/core";
    import { injectCapabilities } from "@copilotkit/angular";
    
    export class AgentCapabilitiesComponent {
      readonly agentId = signal<string | undefined>("support");
      readonly capabilities = injectCapabilities(this.agentId);
    }

## Related

### [injectAgentStoreAccess the resolved agent and its reactive messages, state, and run status.](https://docs.copilotkit.ai/reference/angular/functions/injectAgentStore)
