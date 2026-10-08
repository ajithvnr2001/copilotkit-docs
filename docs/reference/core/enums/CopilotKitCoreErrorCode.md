---
url: https://docs.copilotkit.ai/reference/core/enums/CopilotKitCoreErrorCode/
title: CopilotKitCoreErrorCode
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:33.119626+00:00
---

# CopilotKitCoreErrorCode

> Source: https://docs.copilotkit.ai/reference/core/enums/CopilotKitCoreErrorCode/

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

# CopilotKitCoreErrorCode

Stable error codes surfaced through the onError subscriber callback.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotKitCoreErrorCode` enumerates the stable, machine-readable codes that `CopilotKitCore` attaches to errors. You encounter it in the `onError` callback of a subscriber, where you can branch on `code` to handle specific failures.

## Import
    
    
    import { CopilotKitCoreErrorCode } from "@copilotkit/core";

## Definition
    
    
    enum CopilotKitCoreErrorCode {
      RUNTIME_INFO_FETCH_FAILED = "runtime_info_fetch_failed",
      AGENT_CONNECT_FAILED = "agent_connect_failed",
      AGENT_RUN_FAILED = "agent_run_failed",
      AGENT_RUN_FAILED_EVENT = "agent_run_failed_event",
      AGENT_RUN_ERROR_EVENT = "agent_run_error_event",
      TOOL_ARGUMENT_PARSE_FAILED = "tool_argument_parse_failed",
      TOOL_HANDLER_FAILED = "tool_handler_failed",
      TOOL_NOT_FOUND = "tool_not_found",
      AGENT_NOT_FOUND = "agent_not_found",
      AGENT_THREAD_LOCKED = "agent_thread_locked",
      TRANSCRIPTION_FAILED = "transcription_failed",
      TRANSCRIPTION_SERVICE_NOT_CONFIGURED = "transcription_service_not_configured",
      TRANSCRIPTION_INVALID_AUDIO = "transcription_invalid_audio",
      TRANSCRIPTION_RATE_LIMITED = "transcription_rate_limited",
      TRANSCRIPTION_AUTH_FAILED = "transcription_auth_failed",
      TRANSCRIPTION_NETWORK_ERROR = "transcription_network_error",
      SUBSCRIBER_CALLBACK_FAILED = "subscriber_callback_failed",
    }

## Members

Prop

Type

`RUNTIME_INFO_FETCH_FAILED?`runtime_info_fetch_failed

Prop

Type

`AGENT_CONNECT_FAILED?`agent_connect_failed

Prop

Type

`AGENT_RUN_FAILED?`agent_run_failed

Prop

Type

`AGENT_RUN_FAILED_EVENT?`agent_run_failed_event

Prop

Type

`AGENT_RUN_ERROR_EVENT?`agent_run_error_event

Prop

Type

`TOOL_ARGUMENT_PARSE_FAILED?`tool_argument_parse_failed

Prop

Type

`TOOL_HANDLER_FAILED?`tool_handler_failed

Prop

Type

`TOOL_NOT_FOUND?`tool_not_found

Prop

Type

`AGENT_NOT_FOUND?`agent_not_found

Prop

Type

`AGENT_THREAD_LOCKED?`agent_thread_locked

Prop

Type

`TRANSCRIPTION_FAILED?`transcription_failed

Prop

Type

`TRANSCRIPTION_SERVICE_NOT_CONFIGURED?`transcription_service_not_configured

Prop

Type

`TRANSCRIPTION_INVALID_AUDIO?`transcription_invalid_audio

Prop

Type

`TRANSCRIPTION_RATE_LIMITED?`transcription_rate_limited

Prop

Type

`TRANSCRIPTION_AUTH_FAILED?`transcription_auth_failed

Prop

Type

`TRANSCRIPTION_NETWORK_ERROR?`transcription_network_error

Prop

Type

`SUBSCRIBER_CALLBACK_FAILED?`subscriber_callback_failed

## Usage
    
    
    copilotkit.subscribe({
      onError: ({ code, error, context }) => {
        if (code === CopilotKitCoreErrorCode.AGENT_THREAD_LOCKED) {
          // Show "Agent is busy, retry?" UI
          return;
        }
        console.error(code, error, context);
      },
    });

## Related

  * [CopilotKitCoreSubscriber](https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreSubscriber) — the `onError` callback receives this code.
  * [CopilotKitCore](https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore)


