---
url: https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore/
title: CopilotKitCore
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:33.231695+00:00
---

# CopilotKitCore

> Source: https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁Core (TypeScript)SDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Classes

[CopilotKitCore](https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore)[ProxiedCopilotRuntimeAgent](https://docs.copilotkit.ai/reference/core/classes/ProxiedCopilotRuntimeAgent)

Types

[CopilotKitCoreConfig](https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreConfig)[CopilotKitCoreSubscriber](https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreSubscriber)[FrontendTool](https://docs.copilotkit.ai/reference/core/types/FrontendTool)[ProxiedCopilotRuntimeAgentConfig](https://docs.copilotkit.ai/reference/core/types/ProxiedCopilotRuntimeAgentConfig)[Suggestion](https://docs.copilotkit.ai/reference/core/types/Suggestion)[SuggestionsConfig](https://docs.copilotkit.ai/reference/core/types/SuggestionsConfig)

Enums

[CopilotKitCoreErrorCode](https://docs.copilotkit.ai/reference/core/enums/CopilotKitCoreErrorCode)[CopilotKitCoreRuntimeConnectionStatus](https://docs.copilotkit.ai/reference/core/enums/CopilotKitCoreRuntimeConnectionStatus)[ToolCallStatus](https://docs.copilotkit.ai/reference/core/enums/ToolCallStatus)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[core](https://docs.copilotkit.ai/reference/core)Classes

# CopilotKitCore

Framework-agnostic client that connects to a CopilotRuntime and manages agents, tools, context, and suggestions.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotKitCore` is the main entry point of `@copilotkit/core`. It connects to a CopilotRuntime over the AG-UI protocol, exposes the available agents, holds the registry of frontend tools, shared context, and suggestions, and notifies subscribers when any of that state changes. The React, Angular, and vanilla bindings all wrap a single instance of this class — reach for it directly when you need an agent client outside of those frameworks.

## Import
    
    
    import { CopilotKitCore } from "@copilotkit/core";

## Constructor
    
    
    new CopilotKitCore(config: CopilotKitCoreConfig)

Prop

Type

`config`CopilotKitCoreConfig

## Methods

### Agents

Prop

Type

`getAgent(id: string): AbstractAgent | undefined?`method

Prop

Type

`runAgent(params: CopilotKitCoreRunAgentParams): Promise<RunAgentResult>?`method

Prop

Type

`connectAgent(params: CopilotKitCoreConnectAgentParams): Promise<RunAgentResult>?`method

Prop

Type

`stopAgent(params: CopilotKitCoreStopAgentParams): void?`method

Prop

Type

`registerProxiedAgent(params): { agent; unregister }?`method

Prop

Type

`addAgent__unsafe_dev_only(params: CopilotKitCoreAddAgentParams): void?`method

Prop

Type

`removeAgent__unsafe_dev_only(id: string): void?`method

Prop

Type

`setAgents__unsafe_dev_only(agents: Record<string, AbstractAgent>): void?`method

### Tools

Prop

Type

`addTool(tool: FrontendTool): void?`method

Prop

Type

`removeTool(id: string, agentId?: string): void?`method

Prop

Type

`getTool(params: CopilotKitCoreGetToolParams): FrontendTool<any> | undefined?`method

Prop

Type

`setTools(tools: FrontendTool<any>[]): void?`method

Prop

Type

`runTool(params: CopilotKitCoreRunToolParams): Promise<CopilotKitCoreRunToolResult>?`method

### Context

Prop

Type

`addContext(context: Context): string?`method

Prop

Type

`removeContext(id: string): void?`method

### Suggestions

Prop

Type

`addSuggestionsConfig(config: SuggestionsConfig): string?`method

Prop

Type

`removeSuggestionsConfig(id: string): void?`method

Prop

Type

`getSuggestions(agentId: string): CopilotKitCoreGetSuggestionsResult?`method

Prop

Type

`reloadSuggestions(agentId: string): void?`method

Prop

Type

`clearSuggestions(agentId: string): void?`method

### Subscriptions

Prop

Type

`subscribe(subscriber: CopilotKitCoreSubscriber): CopilotKitCoreSubscription?`method

Prop

Type

`subscribeToAgentWithOptions(agent, subscriber, options?): CopilotKitCoreSubscription?`method

### Inspector metadata

Prop

Type

`refreshInspectorMetadata(): Promise<void>?`method

### Configuration

Prop

Type

`setRuntimeUrl(runtimeUrl: string | undefined): void?`method

Prop

Type

`setRuntimeTransport(runtimeTransport: CopilotRuntimeTransport): void?`method

Prop

Type

`setHeaders(headers: Record<string, string | null | undefined>): void?`method

Prop

Type

`setCredentials(credentials: RequestCredentials | undefined): void?`method

Prop

Type

`setMessageFilter(messageFilter: CopilotKitMessageFilter | undefined): void?`method

Prop

Type

`setProperties(properties: Record<string, unknown>): void?`method

Prop

Type

`setDebug(debug: DebugConfig | undefined): void?`method

Prop

Type

`setDefaultThrottleMs(value: number | undefined): void?`method

### State queries

Prop

Type

`getStateByRun(agentId, threadId, runId): State | undefined?`method

Prop

Type

`getRunIdForMessage(agentId, threadId, messageId): string | undefined?`method

Prop

Type

`getRunIdsForThread(agentId, threadId): string[]?`method

### Properties (read-only)

Prop

Type

`agents: Readonly<Record<string, AbstractAgent>>?`getter

Prop

Type

`tools: Readonly<FrontendTool<any>[]>?`getter

Prop

Type

`context: Readonly<Record<string, Context>>?`getter

Prop

Type

`runtimeUrl: string | undefined?`getter

Prop

Type

`runtimeConnectionStatus: CopilotKitCoreRuntimeConnectionStatus?`getter

Prop

Type

`inspectorMetadata: InspectorMetadataV1 | undefined?`getter

Prop

Type

`headers / credentials / properties?`getter

## Usage
    
    
    import { CopilotKitCore } from "@copilotkit/core";
    
    const copilotkit = new CopilotKitCore({
      runtimeUrl: "/api/copilotkit",
      tools: [
        {
          name: "showAlert",
          handler: ({ message }: { message: string }) => window.alert(message),
        },
      ],
    });
    
    const subscription = copilotkit.subscribe({
      onRuntimeConnectionStatusChanged: ({ status }) => console.log(status),
    });
    
    // `agents` populates after the runtime responds — `onAgentsChanged` (above)
    // fires when they're ready; this guarded lookup is for illustration.
    const agent = copilotkit.getAgent("default");
    if (agent) {
      await copilotkit.runAgent({ agent });
    }
    
    subscription.unsubscribe();

## Behavior

  * **Asynchronous agent population** — `agents` is populated after the runtime responds, so it may be empty immediately after construction. Use `subscribe({ onAgentsChanged })` to react when agents become available.
  * **Error surfacing** — failures (runtime fetch, agent run, tool execution, subscriber callbacks) are delivered through the `onError` subscriber callback with a [CopilotKitCoreErrorCode](https://docs.copilotkit.ai/reference/core/enums/CopilotKitCoreErrorCode); they are not thrown from the originating method — except `runTool()`, which also throws when the named tool or its resolved agent cannot be found.
  * **Subscriber isolation** — a throw in one subscriber callback is caught and logged; it does not stall notifications to other subscribers.
  * **Inspector metadata isolation** — metadata loads after the connected and agent notifications finish. Header or credential changes refresh it. Runtime URL, transport, auth, connection, and capability checks prevent a stale request from replacing a newer value.
  * **`__unsafe_dev_only` APIs** — the `*Agent__unsafe_dev_only` methods register local in-memory agents for development. Production setups must go through a CopilotRuntime.



## Related

  * [@copilotkit/core overview](https://docs.copilotkit.ai/reference/core)
  * [CopilotKitCoreConfig](https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreConfig)
  * [CopilotKitCoreSubscriber](https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreSubscriber)
  * [ProxiedCopilotRuntimeAgent](https://docs.copilotkit.ai/reference/core/classes/ProxiedCopilotRuntimeAgent)
  * [FrontendTool](https://docs.copilotkit.ai/reference/core/types/FrontendTool)


