---
url: https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreConfig/
title: CopilotKitCoreConfig
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:33.293449+00:00
---

# CopilotKitCoreConfig

> Source: https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreConfig/

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

# CopilotKitCoreConfig

Configuration object passed to the CopilotKitCore constructor.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotKitCoreConfig` is the configuration object accepted by the [`CopilotKitCore`](https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore) constructor. It wires the core to a CopilotRuntime endpoint and seeds it with frontend tools, suggestions, request headers, and forwarded properties.

## Import
    
    
    import type { CopilotKitCoreConfig } from "@copilotkit/core";

## Definition
    
    
    interface CopilotKitCoreConfig {
      runtimeUrl?: string;
      runtimeTransport?: CopilotRuntimeTransport;
      agents__unsafe_dev_only?: Record<string, AbstractAgent>;
      headers?: Record<string, string>;
      credentials?: RequestCredentials;
      messageFilter?: CopilotKitMessageFilter;
      properties?: Record<string, unknown>;
      tools?: FrontendTool<any>[];
      suggestionsConfig?: SuggestionsConfig[];
      debug?: DebugConfig;
    }

## Properties

Prop

Type

`runtimeUrl?`string

Prop

Type

`runtimeTransport?`"rest" | "single" | "auto"

Prop

Type

`agents__unsafe_dev_only?`Record<string, AbstractAgent>

Prop

Type

`headers?`Record<string, string>

Prop

Type

`credentials?`RequestCredentials

Prop

Type

`messageFilter?`CopilotKitMessageFilter

Prop

Type

`properties?`Record<string, unknown>

Prop

Type

`tools?`FrontendTool<any>[]

Prop

Type

`suggestionsConfig?`SuggestionsConfig[]

Prop

Type

`debug?`DebugConfig

## Usage
    
    
    import { CopilotKitCore } from "@copilotkit/core";
    import { z } from "zod";
    
    const copilotkit = new CopilotKitCore({
      runtimeUrl: "/api/copilotkit",
      headers: { Authorization: "Bearer token" },
      properties: { userId: "user_123" },
      tools: [
        {
          name: "sayHello",
          description: "Greet the user",
          parameters: z.object({ name: z.string() }),
          handler: async ({ name }) => `Hello, ${name}!`,
        },
      ],
    });

## Related

  * [CopilotKitCore](https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore)
  * [FrontendTool](https://docs.copilotkit.ai/reference/core/types/FrontendTool)
  * [SuggestionsConfig](https://docs.copilotkit.ai/reference/core/types/SuggestionsConfig)


