---
url: https://docs.copilotkit.ai/reference/core/types/FrontendTool/
title: FrontendTool
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:35.908890+00:00
---

# FrontendTool

> Source: https://docs.copilotkit.ai/reference/core/types/FrontendTool/

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

# FrontendTool

Definition of a frontend tool the agent can call in the browser.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`FrontendTool` describes a tool that runs in the browser and can be invoked by an agent. You register frontend tools via [`CopilotKitCoreConfig.tools`](https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreConfig) (or at runtime on [`CopilotKitCore`](https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore)). A tool has a name, an optional parameter schema, and a handler that receives the parsed arguments and an execution context.

## Import
    
    
    import type { FrontendTool } from "@copilotkit/core";

## Definition
    
    
    type FrontendTool<T extends Record<string, unknown> = Record<string, unknown>> = {
      name: string;
      description?: string;
      parameters?: StandardSchemaV1<any, T>;
      handler?: (args: T, context: FrontendToolHandlerContext) => Promise<unknown>;
      followUp?: boolean;
      reconnectBehavior?: "passive" | "resume-pending";
      agentId?: string;
      available?: boolean;
    };
    
    type FrontendToolHandlerContext = {
      toolCall: ToolCall;
      agent: AbstractAgent;
      signal?: AbortSignal;
      isReplay?: boolean;
    };

## Properties

Prop

Type

`name`string

Prop

Type

`description?`string

Prop

Type

`parameters?`StandardSchemaV1<any, T>

Prop

Type

`handler?`(args: T, context: FrontendToolHandlerContext) => Promise<unknown>

Prop

Type

`followUp?`boolean

Prop

Type

`reconnectBehavior?`"passive" | "resume-pending"

Prop

Type

`agentId?`string

Prop

Type

`available?`boolean

## Usage
    
    
    import type { FrontendTool } from "@copilotkit/core";
    import { z } from "zod";
    
    const setThemeTool: FrontendTool<{ theme: "light" | "dark" }> = {
      name: "setTheme",
      description: "Switch the app between light and dark mode",
      parameters: z.object({ theme: z.enum(["light", "dark"]) }),
      handler: async ({ theme }, { signal }) => {
        if (signal?.aborted) return;
        document.documentElement.dataset.theme = theme;
        return `Theme set to ${theme}`;
      },
    };

## Related

  * [CopilotKitCore](https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore)
  * [CopilotKitCoreConfig](https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreConfig)
  * [ToolCallStatus](https://docs.copilotkit.ai/reference/core/enums/ToolCallStatus)


