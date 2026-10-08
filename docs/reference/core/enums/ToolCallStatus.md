---
url: https://docs.copilotkit.ai/reference/core/enums/ToolCallStatus/
title: ToolCallStatus
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:33.253731+00:00
---

# ToolCallStatus

> Source: https://docs.copilotkit.ai/reference/core/enums/ToolCallStatus/

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

# ToolCallStatus

Lifecycle states of a tool call as it streams in and executes.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`ToolCallStatus` describes where a tool call is in its lifecycle, from arguments still streaming in to a fully executed result. You encounter it when rendering or reacting to tool calls in a frontend tool handler or custom render logic.

## Import
    
    
    import { ToolCallStatus } from "@copilotkit/core";

## Definition
    
    
    enum ToolCallStatus {
      InProgress = "inProgress",
      Executing = "executing",
      Complete = "complete",
    }

## Members

Prop

Type

`InProgress?`inProgress

Prop

Type

`Executing?`executing

Prop

Type

`Complete?`complete

## Usage
    
    
    import { ToolCallStatus } from "@copilotkit/core";
    
    function renderToolCall(status: ToolCallStatus) {
      switch (status) {
        case ToolCallStatus.InProgress:
          return "Receiving arguments…";
        case ToolCallStatus.Executing:
          return "Running…";
        case ToolCallStatus.Complete:
          return "Done";
      }
    }

## Related

  * [FrontendTool](https://docs.copilotkit.ai/reference/core/types/FrontendTool) — tool handlers observe these statuses as a call progresses.
  * [CopilotKitCore](https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore)


