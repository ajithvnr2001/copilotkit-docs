---
url: https://docs.copilotkit.ai/reference/core/types/ProxiedCopilotRuntimeAgentConfig/
title: ProxiedCopilotRuntimeAgentConfig
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:35.839860+00:00
---

# ProxiedCopilotRuntimeAgentConfig

> Source: https://docs.copilotkit.ai/reference/core/types/ProxiedCopilotRuntimeAgentConfig/

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

[Reference](https://docs.copilotkit.ai/reference)[core](https://docs.copilotkit.ai/reference/core)Types

# ProxiedCopilotRuntimeAgentConfig

Configuration object for constructing a ProxiedCopilotRuntimeAgent.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`ProxiedCopilotRuntimeAgentConfig` is the constructor argument for [`ProxiedCopilotRuntimeAgent`](https://docs.copilotkit.ai/reference/core/classes/ProxiedCopilotRuntimeAgent). It extends AG-UI's `HttpAgentConfig` (omitting `url`, which is derived from `runtimeUrl`) and adds the routing, transport, and runtime-mode fields the proxy needs to reach a CopilotRuntime.

## Import
    
    
    import type { ProxiedCopilotRuntimeAgentConfig } from "@copilotkit/core";

## Definition
    
    
    interface ProxiedCopilotRuntimeAgentConfig
      extends Omit<HttpAgentConfig, "url"> {
      runtimeUrl?: string;
      transport?: CopilotRuntimeTransport;
      credentials?: RequestCredentials;
      runtimeMode?: RuntimeMode | "pending";
      intelligence?: IntelligenceRuntimeInfo;
      capabilities?: AgentCapabilities;
      debug?: ResolvedDebugConfig;
      runtimeAgentId?: string;
    }

## Properties

Prop

Type

`runtimeUrl?`string

Prop

Type

`transport?`"rest" | "single" | "auto"

Prop

Type

`credentials?`RequestCredentials

Prop

Type

`runtimeMode?`"sse" | "intelligence" | "pending"

Prop

Type

`intelligence?`IntelligenceRuntimeInfo

Prop

Type

`capabilities?`AgentCapabilities

Prop

Type

`debug?`ResolvedDebugConfig

Prop

Type

`runtimeAgentId?`string

## Usage
    
    
    import { ProxiedCopilotRuntimeAgent } from "@copilotkit/core";
    
    const agent = new ProxiedCopilotRuntimeAgent({
      runtimeUrl: "/api/copilotkit",
      agentId: "default",
      transport: "auto",
      credentials: "include",
    });

## Related

  * [ProxiedCopilotRuntimeAgent](https://docs.copilotkit.ai/reference/core/classes/ProxiedCopilotRuntimeAgent)
  * [CopilotKitCore](https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore)


