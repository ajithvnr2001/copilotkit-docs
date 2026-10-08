---
url: https://docs.copilotkit.ai/reference/angular/services/CopilotKit/
title: CopilotKit
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:14.043657+00:00
---

# CopilotKit

> Source: https://docs.copilotkit.ai/reference/angular/services/CopilotKit/

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

[Reference](https://docs.copilotkit.ai/reference)[angular](https://docs.copilotkit.ai/reference/angular)Services

# CopilotKit

The root Angular service that exposes CopilotKit agents, tools, runtime state, and suggestions as signals

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotKit` is the central injectable service for `@copilotkit/angular`. It is `providedIn: "root"`, so a single instance is shared across your application. It builds and owns the underlying `CopilotKitCore` from the [`CopilotKitConfig`](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit#parameters) you registered with [`provideCopilotKit`](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit), exposes reactive runtime state as Angular [signals](https://angular.dev/guide/signals), and provides methods to register tools, manage suggestions, and update the runtime connection.

In most apps you do not call its methods directly. The injectable functions such as [`registerFrontendTool`](https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool), [`registerRenderToolCall`](https://docs.copilotkit.ai/reference/angular/functions/registerRenderToolCall), and [`registerHumanInTheLoop`](https://docs.copilotkit.ai/reference/angular/functions/registerHumanInTheLoop) register against the current injector and remove registrations with the same name and optional agent id when that injector is destroyed. Inject the service when you need direct access to its signals or the `core` instance.

## Accessing the service

Inject it from any injection context, for example a component or service.

src/app/status.component.ts
    
    
    import { Component, inject } from "@angular/core";
    import { CopilotKit } from "@copilotkit/angular";
    
    @Component({
      selector: "app-status",
      standalone: true,
      template: `<p>Status: {{ copilotKit.runtimeConnectionStatus() }}</p>`,
    })
    export class StatusComponent {
      protected readonly copilotKit = inject(CopilotKit);
    }

## Signals

All reactive state is exposed as read-only Angular signals. Read a signal by calling it, for example `copilotKit.agents()`.

Prop

Type

`agents?`Signal<Record<string, AbstractAgent>>

Prop

Type

`runtimeConnectionStatus?`Signal<CopilotKitCoreRuntimeConnectionStatus>

Prop

Type

`runtimeUrl?`Signal<string | undefined>

Prop

Type

`runtimeTransport?`Signal<CopilotRuntimeTransport>

Prop

Type

`headers?`Signal<Record<string, string>>

Prop

Type

`credentials?`Signal<RequestCredentials | undefined>

Prop

Type

`threadEndpoints?`Signal<ThreadEndpointRuntimeInfo | undefined>

Prop

Type

`audioFileTranscriptionEnabled?`Signal<boolean>

Prop

Type

`intelligence?`Signal<IntelligenceRuntimeInfo | undefined>

Prop

Type

`licenseStatus?`Signal<RuntimeLicenseStatus | undefined>

Prop

Type

`suggestionsByAgent?`Signal<Record<string, CopilotKitCoreGetSuggestionsResult>>

Prop

Type

`toolCallRenderConfigs?`Signal<RenderToolCallConfig[]>

Prop

Type

`clientToolCallRenderConfigs?`Signal<FrontendToolConfig[]>

Prop

Type

`humanInTheLoopToolRenderConfigs?`Signal<HumanInTheLoopConfig[]>

Prop

Type

`activityMessageRenderConfigs?`Signal<RenderActivityMessageConfig[]>

## Properties

Prop

Type

`core?`CopilotKitCore

Prop

Type

`defaultToolRenderingEnabled?`boolean

## Methods

Prop

Type

`addFrontendTool?`(tool: FrontendToolConfig & { injector: Injector }) => void

Prop

Type

`addRenderToolCall?`(renderConfig: RenderToolCallConfig) => void

Prop

Type

`addRenderActivityMessage?`(renderConfig: RenderActivityMessageConfig) => void

Prop

Type

`removeRenderActivityMessage?`(renderConfig: RenderActivityMessageConfig) => void

Prop

Type

`addHumanInTheLoop?`(humanInTheLoopTool: HumanInTheLoopConfig) => void

Prop

Type

`addSuggestionsConfig?`(config: SuggestionsConfig) => string

Prop

Type

`removeSuggestionsConfig?`(id: string) => void

Prop

Type

`getSuggestions?`(agentId: string) => CopilotKitCoreGetSuggestionsResult

Prop

Type

`reloadSuggestions?`(agentId: string) => void

Prop

Type

`clearSuggestions?`(agentId: string) => void

Prop

Type

`removeTool?`(toolName: string, agentId?: string) => void

Prop

Type

`getAgent?`(agentId: string) => AbstractAgent | undefined

Prop

Type

`updateRuntime?`(options) => void

## Usage

### Read agents and connection status in a template

src/app/agents-panel.component.ts
    
    
    import { Component, inject } from "@angular/core";
    import { CopilotKit } from "@copilotkit/angular";
    
    @Component({
      selector: "app-agents-panel",
      standalone: true,
      template: `
        <p>Status: {{ copilotKit.runtimeConnectionStatus() }}</p>
        <ul>
          @for (id of agentIds(); track id) {
            <li>{{ id }}</li>
          }
        </ul>
      `,
    })
    export class AgentsPanelComponent {
      protected readonly copilotKit = inject(CopilotKit);
      protected readonly agentIds = () => Object.keys(this.copilotKit.agents());
    }

### Switch the runtime URL at runtime

src/app/runtime-switcher.component.ts
    
    
    import { Component, inject } from "@angular/core";
    import { CopilotKit } from "@copilotkit/angular";
    
    @Component({
      selector: "app-runtime-switcher",
      standalone: true,
      template: `<button (click)="useStaging()">Use staging</button>`,
    })
    export class RuntimeSwitcherComponent {
      private readonly copilotKit = inject(CopilotKit);
    
      protected useStaging(): void {
        this.copilotKit.updateRuntime({
          runtimeUrl: "https://staging.example.com/api/copilotkit",
        });
      }
    }

### Reload suggestions for an agent

src/app/suggestions.component.ts
    
    
    import { Component, inject } from "@angular/core";
    import { CopilotKit } from "@copilotkit/angular";
    
    @Component({
      selector: "app-suggestions",
      standalone: true,
      template: `<button (click)="refresh()">Refresh suggestions</button>`,
    })
    export class SuggestionsComponent {
      private readonly copilotKit = inject(CopilotKit);
    
      protected refresh(): void {
        this.copilotKit.reloadSuggestions("default");
      }
    }

## Related

### [provideCopilotKitRegister the configuration that this service reads to build its core.](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit)### [registerFrontendToolRegister a client-side tool from an injection context, with name-based cleanup on destroy.](https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool)### [injectAgentStoreSubscribe to a single agent's reactive state (messages, running status, and more).](https://docs.copilotkit.ai/reference/angular/functions/injectAgentStore)
