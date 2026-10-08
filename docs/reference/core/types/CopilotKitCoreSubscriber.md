---
url: https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreSubscriber/
title: CopilotKitCoreSubscriber
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:35.877331+00:00
---

# CopilotKitCoreSubscriber

> Source: https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreSubscriber/

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

# CopilotKitCoreSubscriber

Set of optional callbacks notified of CopilotKitCore lifecycle events.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotKitCoreSubscriber` is the object passed to [`CopilotKitCore.subscribe`](https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore). Every callback is optional, receives an event object that always includes the `copilotkit` instance, and may return `void` or a `Promise<void>`. Use it to react to connection status, tool execution, suggestions, configuration changes, and errors.

## Import
    
    
    import type { CopilotKitCoreSubscriber } from "@copilotkit/core";

## Definition

Every callback is optional, receives an event object that always includes the `copilotkit` instance, and returns `void` or `Promise<void>`. The shape below shows the representative `onRuntimeConnectionStatusChanged` callback; the Properties section documents each callback's exact event shape.
    
    
    interface CopilotKitCoreSubscriber {
      onRuntimeConnectionStatusChanged?: (event: {
        copilotkit: CopilotKitCore;
        status: CopilotKitCoreRuntimeConnectionStatus;
      }) => void | Promise<void>;
      // ...one optional callback per lifecycle event (tool execution, agents,
      // context, suggestions, properties, headers, Inspector metadata, errors,
      // and thread stores).
      // See the Properties section below for each callback's event shape.
    }

## Properties

Prop

Type

`onRuntimeConnectionStatusChanged?`(event) => void | Promise<void>

Prop

Type

`onToolExecutionStart?`(event) => void | Promise<void>

Prop

Type

`onToolExecutionEnd?`(event) => void | Promise<void>

Prop

Type

`onAgentsChanged?`(event) => void | Promise<void>

Prop

Type

`onContextChanged?`(event) => void | Promise<void>

Prop

Type

`onSuggestionsConfigChanged?`(event) => void | Promise<void>

Prop

Type

`onSuggestionsChanged?`(event) => void | Promise<void>

Prop

Type

`onSuggestionsStartedLoading?`(event) => void | Promise<void>

Prop

Type

`onSuggestionsFinishedLoading?`(event) => void | Promise<void>

Prop

Type

`onPropertiesChanged?`(event) => void | Promise<void>

Prop

Type

`onHeadersChanged?`(event) => void | Promise<void>

Prop

Type

`onInspectorMetadataChanged?`(event) => void | Promise<void>

Prop

Type

`onError?`(event) => void | Promise<void>

Prop

Type

`onThreadStoreRegistered?`(event) => void | Promise<void>

Prop

Type

`onThreadStoreUnregistered?`(event) => void | Promise<void>

## Usage
    
    
    const subscription = copilotkit.subscribe({
      onRuntimeConnectionStatusChanged: ({ status }) => {
        console.log("connection:", status);
      },
      onError: ({ code, error }) => {
        console.error(code, error);
      },
      onInspectorMetadataChanged: ({ inspectorMetadata }) => {
        console.log("project context:", inspectorMetadata);
      },
    });
    
    // later
    subscription.unsubscribe();

## Related

  * [CopilotKitCore](https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore)
  * [CopilotKitCoreErrorCode](https://docs.copilotkit.ai/reference/core/enums/CopilotKitCoreErrorCode)
  * [CopilotKitCoreRuntimeConnectionStatus](https://docs.copilotkit.ai/reference/core/enums/CopilotKitCoreRuntimeConnectionStatus)


