---
url: https://docs.copilotkit.ai/reference/core/types/Suggestion/
title: Suggestion
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:35.994472+00:00
---

# Suggestion

> Source: https://docs.copilotkit.ai/reference/core/types/Suggestion/

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

# Suggestion

A single suggested prompt presented to the user.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`Suggestion` represents one suggested prompt shown to the user (typically as a clickable pill). Suggestions are produced from a [`SuggestionsConfig`](https://docs.copilotkit.ai/reference/core/types/SuggestionsConfig) and surfaced through [`CopilotKitCoreSubscriber.onSuggestionsChanged`](https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreSubscriber).

## Import
    
    
    import type { Suggestion } from "@copilotkit/core";

## Definition
    
    
    type Suggestion = {
      title: string;
      message: string;
      isLoading: boolean;
      className?: string;
    };

## Properties

Prop

Type

`title`string

Prop

Type

`message`string

Prop

Type

`isLoading`boolean

Prop

Type

`className?`string

## Usage
    
    
    import type { Suggestion } from "@copilotkit/core";
    
    const suggestion: Suggestion = {
      title: "Summarize",
      message: "Summarize the current document",
      isLoading: false,
    };

## Related

  * [SuggestionsConfig](https://docs.copilotkit.ai/reference/core/types/SuggestionsConfig)
  * [CopilotKitCoreSubscriber](https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreSubscriber)


