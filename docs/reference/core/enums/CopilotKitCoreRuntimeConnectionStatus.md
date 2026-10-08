---
url: https://docs.copilotkit.ai/reference/core/enums/CopilotKitCoreRuntimeConnectionStatus/
title: CopilotKitCoreRuntimeConnectionStatus
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:33.085202+00:00
---

# CopilotKitCoreRuntimeConnectionStatus

> Source: https://docs.copilotkit.ai/reference/core/enums/CopilotKitCoreRuntimeConnectionStatus/

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

[Reference](https://docs.copilotkit.ai/reference)[core](https://docs.copilotkit.ai/reference/core)Enums

# CopilotKitCoreRuntimeConnectionStatus

Connection states between CopilotKitCore and the CopilotRuntime.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotKitCoreRuntimeConnectionStatus` represents the state of the connection between `CopilotKitCore` and its runtime. You encounter it via `copilotkit.runtimeConnectionStatus` and the `onRuntimeConnectionStatusChanged` subscriber callback.

**The status reports the outcome of the last actual contact with the runtime.** It is not a claim about the present moment. A failed runtime request moves it to `Error`, a successful one moves it back — and nothing else moves it. There is no polling and no heartbeat, so an outage that begins while your application is idle is not noticed until something is sent.

## Import
    
    
    import { CopilotKitCoreRuntimeConnectionStatus } from "@copilotkit/core";

## Definition
    
    
    enum CopilotKitCoreRuntimeConnectionStatus {
      Disconnected = "disconnected",
      Connected = "connected",
      Connecting = "connecting",
      Error = "error",
    }

## Members

Prop

Type

`Disconnected?`disconnected

Prop

Type

`Connected?`connected

Prop

Type

`Connecting?`connecting

Prop

Type

`Error?`error

## Usage
    
    
    copilotkit.subscribe({
      onRuntimeConnectionStatusChanged: ({ status }) => {
        if (status === CopilotKitCoreRuntimeConnectionStatus.Connected) {
          enableChat();
          return;
        }
    
        if (status === CopilotKitCoreRuntimeConnectionStatus.Error) {
          showConnectionError();
          if (Object.keys(copilotkit.agents).length === 0) {
            disableChat();
          }
        }
      },
    });

## Related

  * [CopilotKitCore](https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore) — exposes the connection lifecycle via `runtimeConnectionStatus`.
  * [CopilotKitCoreSubscriber](https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreSubscriber) — `onRuntimeConnectionStatusChanged` receives this status.


