---
url: https://docs.copilotkit.ai/reference/core/
title: @copilotkit/core
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:30.098857+00:00
---

# @copilotkit/core

> Source: https://docs.copilotkit.ai/reference/core/

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

[Reference](https://docs.copilotkit.ai/reference)[core](https://docs.copilotkit.ai/reference/core)

# @copilotkit/core

Framework-agnostic TypeScript client for CopilotKit. Runs anywhere JavaScript runs.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

`@copilotkit/core` is the framework-agnostic TypeScript client at the heart of CopilotKit. It connects to a CopilotRuntime over the AG-UI protocol, manages agents, frontend tools, shared context, and suggestions, and emits state changes to subscribers. It has no UI or React dependency, so it runs in browsers, Node, workers, and inside the React, Angular, and vanilla bindings.

## Install
    
    
    npm install @copilotkit/core

## Quick start
    
    
    import { CopilotKitCore } from "@copilotkit/core";
    
    const copilotkit = new CopilotKitCore({
      runtimeUrl: "/api/copilotkit",
    });
    
    // Register a frontend tool the agent can call.
    copilotkit.addTool({
      name: "showAlert",
      handler: ({ message }: { message: string }) => {
        window.alert(message);
      },
    });
    
    // Agents populate after the runtime responds. In real apps, react via
    // `copilotkit.subscribe({ onAgentsChanged })`; here we assume it's ready.
    const agent = copilotkit.getAgent("default");
    if (agent) {
      await copilotkit.runAgent({ agent });
    }

## Reference

  * [CopilotKitCore](https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore) — the main client class.
  * [ProxiedCopilotRuntimeAgent](https://docs.copilotkit.ai/reference/core/classes/ProxiedCopilotRuntimeAgent) — AG-UI agent that proxies a CopilotRuntime agent.
  * [CopilotKitCoreConfig](https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreConfig) — options accepted by the `CopilotKitCore` constructor.
  * [ProxiedCopilotRuntimeAgentConfig](https://docs.copilotkit.ai/reference/core/types/ProxiedCopilotRuntimeAgentConfig) — options accepted by the `ProxiedCopilotRuntimeAgent` constructor.
  * [FrontendTool](https://docs.copilotkit.ai/reference/core/types/FrontendTool) — shape of a tool registered with `addTool`.
  * [CopilotKitCoreSubscriber](https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreSubscriber) — callbacks passed to `subscribe`.
  * [Suggestion](https://docs.copilotkit.ai/reference/core/types/Suggestion) / [SuggestionsConfig](https://docs.copilotkit.ai/reference/core/types/SuggestionsConfig) — suggestion data and configuration.
  * [ToolCallStatus](https://docs.copilotkit.ai/reference/core/enums/ToolCallStatus) — tool-call lifecycle states.
  * [CopilotKitCoreErrorCode](https://docs.copilotkit.ai/reference/core/enums/CopilotKitCoreErrorCode) — error codes surfaced through `onError`.
  * [CopilotKitCoreRuntimeConnectionStatus](https://docs.copilotkit.ai/reference/core/enums/CopilotKitCoreRuntimeConnectionStatus) — runtime connection states.


