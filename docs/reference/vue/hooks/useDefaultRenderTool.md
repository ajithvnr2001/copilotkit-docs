---
url: https://docs.copilotkit.ai/reference/vue/hooks/useDefaultRenderTool/
title: useDefaultRenderTool
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:22.094620+00:00
---

# useDefaultRenderTool

> Source: https://docs.copilotkit.ai/reference/vue/hooks/useDefaultRenderTool/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁VueSDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Components

[CopilotChat](https://docs.copilotkit.ai/reference/vue/components/CopilotChat)[CopilotChatAssistantMessage](https://docs.copilotkit.ai/reference/vue/components/CopilotChatAssistantMessage)[CopilotChatInput](https://docs.copilotkit.ai/reference/vue/components/CopilotChatInput)[CopilotChatMessageView](https://docs.copilotkit.ai/reference/vue/components/CopilotChatMessageView)[CopilotChatUserMessage](https://docs.copilotkit.ai/reference/vue/components/CopilotChatUserMessage)[CopilotChatView](https://docs.copilotkit.ai/reference/vue/components/CopilotChatView)[CopilotKitProvider](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider)[CopilotPopup](https://docs.copilotkit.ai/reference/vue/components/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/vue/components/CopilotSidebar)

Hooks

[useAgent](https://docs.copilotkit.ai/reference/vue/hooks/useAgent)[useAgentContext](https://docs.copilotkit.ai/reference/vue/hooks/useAgentContext)[useCapabilities](https://docs.copilotkit.ai/reference/vue/hooks/useCapabilities)[useComponent](https://docs.copilotkit.ai/reference/vue/hooks/useComponent)[useConfigureSuggestions](https://docs.copilotkit.ai/reference/vue/hooks/useConfigureSuggestions)[useCopilotChatConfiguration](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotChatConfiguration)[useCopilotKit](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotKit)[useDefaultRenderTool](https://docs.copilotkit.ai/reference/vue/hooks/useDefaultRenderTool)[useFrontendTool](https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool)[useHumanInTheLoop](https://docs.copilotkit.ai/reference/vue/hooks/useHumanInTheLoop)[useInterrupt](https://docs.copilotkit.ai/reference/vue/hooks/useInterrupt)[useRenderTool](https://docs.copilotkit.ai/reference/vue/hooks/useRenderTool)[useSuggestions](https://docs.copilotkit.ai/reference/vue/hooks/useSuggestions)[useThreads](https://docs.copilotkit.ai/reference/vue/hooks/useThreads)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[vue](https://docs.copilotkit.ai/reference/vue)Hooks

# useDefaultRenderTool

Vue 3 composable that registers a wildcard default renderer for unhandled tool calls

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useDefaultRenderTool` is a Vue 3 convenience composable, a thin wrapper around [`useRenderTool`](https://docs.copilotkit.ai/reference/vue/hooks/useRenderTool) with `name: "*"`. It registers a catch-all renderer for tool calls that do not have a specific named renderer.

  * With no config, it registers CopilotKit's built-in default tool-call UI: an expandable card showing the tool name, status, arguments, and result.
  * With a `render` config, it replaces that default UI with your own wildcard renderer.



In Vue, the renderer is a Vue render function or a Vue component (not JSX). It returns a `VNodeChild` (anything Vue can render: a VNode, a string, an array of VNodes, `null`, etc.). Whatever shape the underlying call site passes, your renderer always receives the documented `DefaultRenderProps`.

`useDefaultRenderTool` must be called within a component that has access to the CopilotKit instance provided by `CopilotKitProvider`. Like all Vue composables, call it synchronously inside `<script setup>` or a `setup()` function so its reactive scope is bound to the component lifecycle.

## Signature
    
    
    import { useDefaultRenderTool } from "@copilotkit/vue/v2";
    import type { Component, VNodeChild, WatchSource } from "vue";
    
    type DefaultRenderProps = {
      name: string;
      toolCallId: string;
      parameters: unknown;
      status: "inProgress" | "executing" | "complete";
      result: string | undefined;
    };
    
    function useDefaultRenderTool(
      config?: {
        render?:
          | ((props: DefaultRenderProps) => VNodeChild)
          | Component<DefaultRenderProps>;
      },
      deps?: WatchSource<unknown>[],
    ): void;

## Parameters

Prop

Type

`config?`{ render?: RenderFn | Component }

Prop

Type

`deps?`WatchSource<unknown>[]

## DefaultRenderProps

The props your renderer receives. These are normalized from the framework's internal renderer props, so `parameters` is always populated (from `args` when needed) and `status` is always the string union below (mapped from the `ToolCallStatus` enum).

Prop

Type

`name?`string

Prop

Type

`toolCallId?`string

Prop

Type

`parameters?`unknown

Prop

Type

`status?`"inProgress" | "executing" | "complete"

Prop

Type

`result?`string | undefined

## Usage

### Built-in default renderer

Call the composable with no arguments to register CopilotKit's built-in expandable tool-call card.
    
    
    <script setup lang="ts">
    import { useDefaultRenderTool } from "@copilotkit/vue/v2";
    
    useDefaultRenderTool();
    </script>
    
    <template>
      <!-- Unhandled tool calls render with the built-in default card -->
    </template>

### Custom wildcard renderer (render function)

Provide a `render` function. It receives `DefaultRenderProps` and returns a `VNodeChild`. Use the `h` helper from Vue to build VNodes.
    
    
    <script setup lang="ts">
    import { h } from "vue";
    import { useDefaultRenderTool } from "@copilotkit/vue/v2";
    
    useDefaultRenderTool({
      render: ({ name, status, result }) =>
        h("div", [
          h("strong", name),
          `: ${status}`,
          status === "complete" && result ? h("pre", result) : null,
        ]),
    });
    </script>
    
    <template>
      <!-- Unhandled tool calls render with the custom function above -->
    </template>

### Custom wildcard renderer (Vue component)

Pass a Vue component instead of a function. It receives `DefaultRenderProps` as its props. Define `props` with `defineProps` so the values are typed.
    
    
    <!-- ToolCallCard.vue -->
    <script setup lang="ts">
    defineProps<{
      name: string;
      toolCallId: string;
      parameters: unknown;
      status: "inProgress" | "executing" | "complete";
      result: string | undefined;
    }>();
    </script>
    
    <template>
      <div :data-status="status">
        <strong>{{ name }}</strong>
        <span>{{ status }}</span>
        <pre v-if="status === 'complete' && result">{{ result }}</pre>
      </div>
    </template>
    
    
    <!-- App.vue -->
    <script setup lang="ts">
    import { useDefaultRenderTool } from "@copilotkit/vue/v2";
    import ToolCallCard from "./ToolCallCard.vue";
    
    useDefaultRenderTool({ render: ToolCallCard });
    </script>
    
    <template>
      <!-- Unhandled tool calls render with ToolCallCard -->
    </template>

### Re-registering on dependency changes

Pass reactive `deps` to re-register the renderer when they change. The renderer itself should generally be stable, but any reactive source the renderer closes over can be listed here.
    
    
    <script setup lang="ts">
    import { h, ref } from "vue";
    import { useDefaultRenderTool } from "@copilotkit/vue/v2";
    
    const compact = ref(false);
    
    useDefaultRenderTool(
      {
        render: ({ name, status }) =>
          compact.value
            ? h("span", `${name}: ${status}`)
            : h("div", [h("strong", name), h("span", status)]),
      },
      [compact],
    );
    </script>
    
    <template>
      <button @click="compact = !compact">Toggle layout</button>
    </template>

## Behavior

  * **Wildcard registration** : Internally calls `useRenderTool({ name: "*", render })`. The `"*"` name matches any tool call that has no specific named renderer.
  * **Default UI** : When `config.render` is omitted, an expandable card is rendered. It shows the tool name, a status label (`Running` while active, `Done` when complete), and, when expanded, the JSON-stringified arguments and the result.
  * **Prop normalization** : Your `render` is always wrapped so it receives the documented `DefaultRenderProps`, regardless of whether the call site passes raw internal props (`args` plus a `ToolCallStatus` enum) or already-adapted props (`parameters` plus a string-union status). Both render functions and components are wrapped this way.
  * **Status mapping** : The `ToolCallStatus` enum is mapped to the `"inProgress" | "executing" | "complete"` union. An unknown or future enum value falls back to `"inProgress"` and logs a one-time `console.warn` per distinct value.
  * **No cleanup removal** : Registered renderers are intentionally not removed on cleanup, so past tool calls keep rendering correctly in chat history.
  * **Return value** : The composable returns `void`.



## Related

  * [`useRenderTool`](https://docs.copilotkit.ai/reference/vue/hooks/useRenderTool) \- register a renderer for a specific named tool, or the wildcard this composable wraps
  * [`useFrontendTool`](https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool) \- define a browser-side tool the agent can call
  * [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider) \- provides the CopilotKit instance to descendant composables


