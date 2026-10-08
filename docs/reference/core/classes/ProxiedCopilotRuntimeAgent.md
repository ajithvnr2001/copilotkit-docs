---
url: https://docs.copilotkit.ai/reference/core/classes/ProxiedCopilotRuntimeAgent/
title: ProxiedCopilotRuntimeAgent
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:33.154081+00:00
---

# ProxiedCopilotRuntimeAgent

> Source: https://docs.copilotkit.ai/reference/core/classes/ProxiedCopilotRuntimeAgent/

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

# ProxiedCopilotRuntimeAgent

AG-UI agent that proxies a CopilotRuntime agent over REST, single-route, or Intelligence transports.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`ProxiedCopilotRuntimeAgent` is the AG-UI [`AbstractAgent`](https://docs.ag-ui.com/sdk/js/client/abstract-agent) implementation (extending `HttpAgent`) that `CopilotKitCore` uses to talk to a CopilotRuntime. It builds the correct runtime URLs, picks the transport (`rest`, `single`, or auto-detected), and transparently delegates to an Intelligence agent when the runtime is in Intelligence mode. You rarely construct it directly — `CopilotKitCore` creates one per runtime agent — but you reach for it (via [`registerProxiedAgent`](https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore)) when mounting several frontend agents against a single runtime agent.

## Import
    
    
    import { ProxiedCopilotRuntimeAgent } from "@copilotkit/core";

## Constructor
    
    
    new ProxiedCopilotRuntimeAgent(config: ProxiedCopilotRuntimeAgentConfig)

Prop

Type

`config`ProxiedCopilotRuntimeAgentConfig

## Methods

Prop

Type

`run(input: RunAgentInput): Observable<BaseEvent>?`method

Prop

Type

`connect(input: RunAgentInput): Observable<BaseEvent>?`method

Prop

Type

`connectAgent(parameters?, subscriber?): Promise<RunAgentResult>?`method

Prop

Type

`abortRun(): void?`method

Prop

Type

`detachActiveRun(): Promise<void>?`method

Prop

Type

`getCapabilities(): Promise<AgentCapabilities>?`method

Prop

Type

`clearReplayCursor(threadId: string): void?`method

Prop

Type

`clone(): ProxiedCopilotRuntimeAgent?`method

Prop

Type

`capabilities: AgentCapabilities | undefined?`getter

Prop

Type

`runtimeAgentId: string | undefined?`property

## Usage
    
    
    import { CopilotKitCore } from "@copilotkit/core";
    
    const copilotkit = new CopilotKitCore({ runtimeUrl: "/api/copilotkit" });
    
    // Mount a second frontend agent against the same runtime agent.
    const { agent, unregister } = copilotkit.registerProxiedAgent({
      agentId: "chat-1",
      runtimeAgentId: "default",
    });
    
    await copilotkit.runAgent({ agent });
    
    // On cleanup:
    unregister();

## Behavior

  * **Transport auto-detection** — with `transport: "auto"`, the agent issues `GET /info`; a 2xx response selects REST, otherwise it falls back to single-route (`POST { method: "info" }`).
  * **Lazy mode resolution** — a `"pending"` runtime mode is resolved via a runtime-info fetch only when the agent enters the Intelligence delegate path; plain HTTP `run`/`connect` proceed without resolving it.
  * **Intelligence delegation** — in Intelligence mode the proxy creates an internal `IntelligenceAgent` delegate (websocket) and mirrors its messages, state, and `isRunning` back onto itself.
  * **Immutable routing id** — `runtimeAgentId` is `readonly`; the REST run URL is baked at construction, so mutating it would desync routing.
  * **Abort/Zod errors are swallowed** — `AbortError` and Zod validation errors complete the stream silently rather than propagating, so cancelling a run does not surface as an error.



## Related

  * [@copilotkit/core overview](https://docs.copilotkit.ai/reference/core)
  * [CopilotKitCore](https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore)
  * [ProxiedCopilotRuntimeAgentConfig](https://docs.copilotkit.ai/reference/core/types/ProxiedCopilotRuntimeAgentConfig)
  * [AG-UI AbstractAgent](https://docs.ag-ui.com/sdk/js/client/abstract-agent)


