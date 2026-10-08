---
url: https://docs.copilotkit.ai/reference/vue/hooks/useRenderTool/
title: useRenderTool
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:25.032924+00:00
---

# useRenderTool

> Source: https://docs.copilotkit.ai/reference/vue/hooks/useRenderTool/

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

# useRenderTool

Register typed Vue renderers for tool calls, by tool name or wildcard

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useRenderTool` is a Vue 3 composable that registers a chat renderer for tool calls. You can target a specific tool name (with a typed Zod `parameters` schema) or use a wildcard (`"*"`) fallback renderer.

The render target is a Vue render function (returning a `VNodeChild`) or a Vue `Component`. It receives the tool `name`, the parsed `parameters`, the current `status`, and the `result` (when complete). This is not JSX; you render with Vue's `h()`, a setup-defined render function, or by passing a single-file Vue component.

This composable only handles rendering. It does not register a frontend handler.

Call `useRenderTool` from inside `setup()` (or `<script setup>`) of a component mounted under [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider). It reads the active CopilotKit instance from provider context, so it cannot be called outside that tree.

## Import
    
    
    import { useRenderTool } from "@copilotkit/vue/v2";

## Signature

### Wildcard overload
    
    
    import { useRenderTool } from "@copilotkit/vue/v2";
    import type { WatchSource } from "vue";
    
    useRenderTool(
      {
        name: "*",
        render: ((props) => VNodeChild) | Component,
        agentId?: string,
      },
      deps?: WatchSource<unknown>[],
    ): void;

### Named overload
    
    
    import { z } from "zod";
    import { useRenderTool } from "@copilotkit/vue/v2";
    import type { WatchSource } from "vue";
    
    useRenderTool<S>(
      {
        name: string,
        parameters: S, // a Zod / Standard Schema; parameters are inferred from it
        render: ((props: RenderToolProps<S>) => VNodeChild) | Component<RenderToolProps<S>>,
        agentId?: string,
      },
      deps?: WatchSource<unknown>[],
    ): void;

## Parameters

Prop

Type

`config`object

Prop

Type

`deps?`WatchSource<unknown>[]

## Render Props

`render` receives a discriminated union (`RenderToolProps`) keyed on `status`. `name` and `toolCallId` are present in all states.

Prop

Type

`name`string

Prop

Type

`toolCallId`string

Prop

Type

`status`"inProgress" | "executing" | "complete"

Prop

Type

`parameters`Partial<T> | T

Prop

Type

`result?`string | undefined

The three states are:

  * `{ status: "inProgress", parameters: Partial<T>, result: undefined }` \-- arguments are still being streamed.
  * `{ status: "executing", parameters: T, result: undefined }` \-- arguments are fully resolved; the tool is executing.
  * `{ status: "complete", parameters: T, result: string }` \-- execution finished and a result is available.



## Behavior

  * Builds a renderer entry with `defineToolCallRenderer` and registers it on the active CopilotKit instance via `addHookRenderToolCall`.
  * Maps the internal `args` prop onto `parameters` before calling `render`, so your render function always sees `parameters`.
  * Deduplicates by `agentId:name` key (latest registration wins).
  * Intentionally does not remove the renderer on cleanup, so previous chat history can still render.
  * Re-registers reactively (via `watch`, `immediate: true`) when `name`, `agentId`, or any value in `deps` changes. Include changing reactive captures in `deps`.



## Usage

### Named tool renderer (render function)
    
    
    <script setup lang="ts">
    import { h } from "vue";
    import { z } from "zod";
    import { useRenderTool } from "@copilotkit/vue/v2";
    
    useRenderTool({
      name: "searchDocs",
      parameters: z.object({ query: z.string() }),
      render: (props) => {
        if (props.status === "inProgress") {
          return h("div", `Preparing ${props.name}...`);
        }
        if (props.status === "executing") {
          return h("div", `Searching for: ${props.parameters.query}`);
        }
        return h("div", `Done: ${props.result}`);
      },
    });
    </script>
    
    <template>
      <slot />
    </template>

### Named tool renderer (Vue component)

Pass a Vue component instead of a render function. The render props become the component's props.
    
    
    <!-- SearchDocsRenderer.vue -->
    <script setup lang="ts">
    defineProps<{
      name: string;
      toolCallId: string;
      status: "inProgress" | "executing" | "complete";
      parameters: { query?: string };
      result?: string;
    }>();
    </script>
    
    <template>
      <div v-if="status === 'inProgress'">Preparing {{ name }}...</div>
      <div v-else-if="status === 'executing'">Searching for: {{ parameters.query }}</div>
      <div v-else>Done: {{ result }}</div>
    </template>
    
    
    <!-- App.vue -->
    <script setup lang="ts">
    import { z } from "zod";
    import { useRenderTool } from "@copilotkit/vue/v2";
    import SearchDocsRenderer from "./SearchDocsRenderer.vue";
    
    useRenderTool({
      name: "searchDocs",
      parameters: z.object({ query: z.string() }),
      render: SearchDocsRenderer,
    });
    </script>
    
    <template>
      <slot />
    </template>

### Wildcard fallback renderer

Omit `parameters` and use `name: "*"` to provide a generic UI for any unhandled tool call.
    
    
    <script setup lang="ts">
    import { h } from "vue";
    import { useRenderTool } from "@copilotkit/vue/v2";
    
    useRenderTool({
      name: "*",
      render: (props) =>
        h("div", `${props.status === "complete" ? "done" : "running"} ${props.name}`),
    });
    </script>
    
    <template>
      <slot />
    </template>

### Reacting to changing values with `deps`

`deps` are Vue `WatchSource` values (refs or getters), not a dependency array. Pass them when `render` reads reactive state so the renderer re-registers on change.
    
    
    <script setup lang="ts">
    import { h, ref } from "vue";
    import { z } from "zod";
    import { useRenderTool } from "@copilotkit/vue/v2";
    
    const locale = ref("en");
    
    useRenderTool(
      {
        name: "searchDocs",
        parameters: z.object({ query: z.string() }),
        render: (props) =>
          h("div", `[${locale.value}] ${props.name}: ${props.status}`),
      },
      [locale],
    );
    </script>
    
    <template>
      <slot />
    </template>

## Related

  * `defineToolCallRenderer` \-- build a renderer entry directly
  * [`useFrontendTool`](https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool) \-- register tools with handlers
  * [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider) \-- provide the CopilotKit instance to the tree


