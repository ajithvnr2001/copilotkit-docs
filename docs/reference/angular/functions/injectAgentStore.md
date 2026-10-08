---
url: https://docs.copilotkit.ai/reference/angular/functions/injectAgentStore/
title: injectAgentStore
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:59.170319+00:00
---

# injectAgentStore

> Source: https://docs.copilotkit.ai/reference/angular/functions/injectAgentStore/

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

# injectAgentStore

Angular function that subscribes to an AG-UI agent and returns a signal of reactive agent state (messages, state, isRunning) for @copilotkit/angular.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`injectAgentStore` subscribes to an [AG-UI agent](https://docs.ag-ui.com/sdk/js/client/abstract-agent) and returns an Angular `Signal<AgentStore>`. The `AgentStore` exposes the agent instance plus its reactive state (messages, shared state, and run status) as Angular signals, so your component re-renders automatically when the agent changes.

Read the store by calling the outer signal, then read each member by calling its signal: `store().messages()`, `store().isRunning()`, `store().state()`. The `agent` member is the plain AG-UI instance (not a signal), so you read it directly: `store().agent`.

Call it from an injection context such as a constructor or field initializer. The subscription is torn down automatically when the owning component or service is destroyed.

Resolution of the agent is lazy and reactive. If no agent can be resolved for the given `agentId` after the runtime has synced (for example, the id does not match any agent reported by your runtime `/info` or configured through `agents` or `selfManagedAgents`), reading the store signal throws an error listing the known agents.

## Signature
    
    
    import { injectAgentStore } from "@copilotkit/angular";
    import type { Signal } from "@angular/core";
    
    function injectAgentStore(
      agentId: string | Signal<string | undefined>,
    ): Signal<AgentStore>;

## Parameters

Prop

Type

`agentId`string | Signal<string | undefined>

## Return Value

Prop

Type

`store?`Signal<AgentStore>

## Usage

### Basic usage

src/app/agent-status.component.ts
    
    
    import { Component } from "@angular/core";
    import { injectAgentStore } from "@copilotkit/angular";
    
    @Component({
      selector: "app-agent-status",
      standalone: true,
      template: `
        <div>Messages: {{ store().messages().length }}</div>
        <div>Running: {{ store().isRunning() ? "Yes" : "No" }}</div>
      `,
    })
    export class AgentStatusComponent {
      readonly store = injectAgentStore("default");
    }

### Reading and updating shared state

Read the state via the signal, and write it through the agent instance.

src/app/theme-panel.component.ts
    
    
    import { Component } from "@angular/core";
    import { injectAgentStore } from "@copilotkit/angular";
    
    @Component({
      selector: "app-theme-panel",
      standalone: true,
      template: `
        <pre>{{ store().state() | json }}</pre>
        <button (click)="setDark()">Dark theme</button>
      `,
    })
    export class ThemePanelComponent {
      readonly store = injectAgentStore("default");
    
      setDark() {
        const agent = this.store().agent;
        agent.setState({ ...(agent.state as object), theme: "dark" });
      }
    }

### Switching agents reactively

Pass a signal so the store re-resolves when the selected agent id changes.

src/app/multi-agent.component.ts
    
    
    import { Component, signal } from "@angular/core";
    import { injectAgentStore } from "@copilotkit/angular";
    
    @Component({
      selector: "app-multi-agent",
      standalone: true,
      template: `
        <button (click)="agentId.set('support')">Support</button>
        <button (click)="agentId.set('sales')">Sales</button>
        <div>Active: {{ store().agent.agentId }}</div>
        <div>Messages: {{ store().messages().length }}</div>
      `,
    })
    export class MultiAgentComponent {
      readonly agentId = signal<string | undefined>("support");
      readonly store = injectAgentStore(this.agentId);
    }

## Behavior

  * **Reactive resolution.** The returned signal recomputes when the `agentId`, the set of available agents, the runtime connection status, the runtime URL or transport, or the request headers change.
  * **Provisional agents.** When a runtime is configured but not yet connected, a provisional proxied runtime agent is created and cached so the store has something to render before the runtime syncs.
  * **Automatic cleanup.** The agent subscription is unsubscribed when the owning component or service is destroyed. Switching to a new agent tears down the previous store's subscription first, including its interrupt controller.
  * **Error on missing agent.** If no agent resolves after the runtime has synced, reading the store signal throws an error that lists the known agent ids.



## Related

### [connectAgentContextShare application state with the agent reactively from a function.](https://docs.copilotkit.ai/reference/angular/functions/connectAgentContext)### [CopilotKit serviceThe central handle on agents, tools, and the runtime connection.](https://docs.copilotkit.ai/reference/angular/services/CopilotKit)### [AG-UI AbstractAgentFull agent interface: methods, messages, state, and subscriptions.](https://docs.ag-ui.com/sdk/js/client/abstract-agent)
