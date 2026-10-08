---
url: https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool/
title: useFrontendTool
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:24.955772+00:00
---

# useFrontendTool

> Source: https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool/

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

# useFrontendTool

Vue composable for registering a client-side tool with an optional Vue renderer

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useFrontendTool` registers a client-side tool with CopilotKit at the current component scope. When the agent decides to call the tool, the provided `handler` function executes in the browser. Optionally, you can supply a `render` (a Vue component or render function) to display custom UI in the chat showing the tool's execution progress and result.

The composable manages the full registration lifecycle: it registers the tool (and its optional renderer) immediately, re-runs the registration when reactive dependencies change, and removes the tool automatically when the owning scope is disposed. Parameter schemas are defined with a [Standard Schema](https://standardschema.dev) such as a [Zod](https://zod.dev) object, for the advertised tool schema and TypeScript inference. Runtime arguments are JSON-parsed but are not validated against that schema.

Import from the `/v2` subpath: `@copilotkit/vue/v2`. Like all CopilotKit composables, `useFrontendTool` must be called from within a component that is a descendant of [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider).

## Signature
    
    
    import type { WatchSource } from "vue";
    import { useFrontendTool } from "@copilotkit/vue/v2";
    
    function useFrontendTool<T extends Record<string, unknown>>(
      tool: VueFrontendTool<T>,
      deps?: WatchSource<unknown>[],
    ): void;

## Parameters

Prop

Type

`tool`VueFrontendTool<T>

Prop

Type

`deps?`WatchSource<unknown>[]

## Behavior

  * **Immediate registration.** The tool is registered as soon as the composable runs (the underlying `watch` uses `{ immediate: true }`).
  * **Duplicate handling.** If a tool with the same `name` already exists for the same `agentId`, the previous registration is removed, the new one is added, and an override warning is logged. Only one tool per name (per agent) is active at a time.
  * **Renderer registration.** When `render` is provided, it is registered as a tool call renderer. The renderer is registered even when `parameters` is omitted, so parameter-free tools (for example confirm dialogs) can still render UI in the chat.
  * **Reactivity.** The registration re-runs when `tool.name`, `tool.available`, or any `deps` watch source changes. Pass changing reactive values through `deps`.
  * **WebMCP registration.** With `webmcp` set, the tool is also registered on `document.modelContext` and removed with the tool. The tool needs a `description` for this (WebMCP rejects tools without one).
  * **Automatic cleanup.** The tool is removed when the watch cleans up, including when the owning component scope is disposed. A `render` registered alongside the tool is intentionally left in place so earlier chat history can still render it.
  * **No return value.** The composable returns `void`.



## Usage

### Basic tool with a Zod schema and async handler
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { z } from "zod";
    import { useFrontendTool } from "@copilotkit/vue/v2";
    
    const todos = ref<string[]>([]);
    
    useFrontendTool({
      name: "addTodo",
      description: "Add a new item to the user's todo list",
      parameters: z.object({
        text: z.string().describe("The todo item text"),
        priority: z.enum(["low", "medium", "high"]).describe("Priority level"),
      }),
      handler: async ({ text, priority }) => {
        todos.value.push(text);
        return `Added "${text}" with ${priority} priority`;
      },
    });
    </script>
    
    <template>
      <ul>
        <li v-for="(todo, i) in todos" :key="i">{{ todo }}</li>
      </ul>
    </template>

### Tool with a custom Vue renderer

Provide a `render` component to visualize the tool call in chat. The component receives `args`, `status`, and `result` as props.
    
    
    <!-- WeatherToolView.vue -->
    <script setup lang="ts">
    import { ToolCallStatus } from "@copilotkit/core";
    
    defineProps<{
      name: string;
      toolCallId: string;
      args: { city?: string; units?: "celsius" | "fahrenheit" };
      status: ToolCallStatus;
      result?: string;
    }>();
    </script>
    
    <template>
      <div v-if="status === ToolCallStatus.InProgress" class="animate-pulse">
        Fetching weather for {{ args.city }}...
      </div>
      <div v-else-if="status === ToolCallStatus.Complete && result" class="rounded border p-4">
        <h3>{{ JSON.parse(result).city }}</h3>
        <p>{{ JSON.parse(result).temperature }}&deg; {{ JSON.parse(result).units }}</p>
        <p>{{ JSON.parse(result).conditions }}</p>
      </div>
    </template>
    
    
    <!-- App.vue -->
    <script setup lang="ts">
    import { z } from "zod";
    import { useFrontendTool } from "@copilotkit/vue/v2";
    import WeatherToolView from "./WeatherToolView.vue";
    
    useFrontendTool({
      name: "getWeather",
      description: "Fetch and display weather information for a city",
      parameters: z.object({
        city: z.string().describe("City name"),
        units: z.enum(["celsius", "fahrenheit"]).default("celsius"),
      }),
      handler: async ({ city, units }, { signal }) => {
        const response = await fetch(`/api/weather?city=${city}&units=${units}`, {
          signal,
        });
        return JSON.stringify(await response.json());
      },
      render: WeatherToolView,
    });
    </script>

### Conditionally available tool

Expose `available` as a getter that reads a reactive value. The registration watch re-reads `available` when that value changes, so the tool is shown or hidden automatically. (Passing the value through `deps` as well is harmless but not required.)
    
    
    <script setup lang="ts">
    import { computed, toRef } from "vue";
    import { z } from "zod";
    import { useFrontendTool } from "@copilotkit/vue/v2";
    
    const props = defineProps<{ isAdmin: boolean }>();
    const isAdmin = toRef(props, "isAdmin");
    
    useFrontendTool(
      {
        name: "deleteUser",
        description: "Delete a user account by ID (admin only)",
        parameters: z.object({
          userId: z.string().describe("The ID of the user to delete"),
        }),
        handler: async ({ userId }) => {
          await fetch(`/api/users/${userId}`, { method: "DELETE" });
          return `User ${userId} deleted`;
        },
        // Expose `available` as a getter so the registration watch re-reads it
        // whenever `isAdmin` changes.
        get available() {
          return isAdmin.value;
        },
      },
      [isAdmin],
    );
    </script>

## Related

### [useComponentConvenience composable that renders a Vue component from tool args. Built on useFrontendTool.](https://docs.copilotkit.ai/reference/vue/hooks/useComponent)### [useRenderToolRegister a renderer for a tool call with full access to status (in progress, executing, complete) and results.](https://docs.copilotkit.ai/reference/vue/hooks/useRenderTool)### [CopilotKitProviderThe provider that must wrap any component calling useFrontendTool.](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider)
