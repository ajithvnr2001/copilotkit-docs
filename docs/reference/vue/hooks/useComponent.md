---
url: https://docs.copilotkit.ai/reference/vue/hooks/useComponent/
title: useComponent
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:20.326874+00:00
---

# useComponent

> Source: https://docs.copilotkit.ai/reference/vue/hooks/useComponent/

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

# useComponent

Register a Vue component as a frontend tool renderer in chat

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useComponent` is a convenience composable built on top of [`useFrontendTool`](https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool). It registers a tool and renders a Vue component in chat using the tool call parameters as the component's props.

Use this when you want a visual component renderer without writing a full frontend tool config manually. For lower-level control over render status (in progress, executing, complete) or to render any tool with a wildcard, reach for [`useRenderTool`](https://docs.copilotkit.ai/reference/vue/hooks/useRenderTool) instead.

Import from the `/v2` subpath: `@copilotkit/vue/v2`. Like all CopilotKit composables, `useComponent` must be called from within a component that is a descendant of [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider).

## Signature
    
    
    import type { Component, WatchSource } from "vue";
    import type { StandardSchemaV1 } from "@copilotkit/shared";
    import { useComponent } from "@copilotkit/vue/v2";
    
    function useComponent<TSchema extends StandardSchemaV1 | undefined = undefined>(
      config: {
        name: string;
        description?: string;
        parameters?: TSchema;
        // When parameters is provided, props are inferred from the schema output.
        // When omitted, the component accepts any props.
        render: Component<NoInfer<InferRenderProps<TSchema>>>;
        agentId?: string;
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

## Behavior

  * **Default instruction.** The composable prepends a default instruction to the description: _"Use this tool to display the " <name>" component in the chat. This tool renders a visual UI component for the user."_. Your `description`, if provided, is appended after it.
  * **Built on`useFrontendTool`.** It calls [`useFrontendTool`](https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool) internally with a render function that mounts your component (via Vue's `h`) and spreads the tool's `args` as the component's props.
  * **Inherited lifecycle.** It inherits `useFrontendTool` behavior: a duplicate-name registration logs an override warning and replaces the previous tool, and the tool is removed automatically when the owning scope is disposed.
  * **Reactivity.** The registration is reactive to `config.name` and the `deps` watch sources. Pass any changing reactive values you depend on through `deps`.



## Usage

Define a Zod schema for the parameters, a Vue component that receives them as props, and register both with `useComponent`.
    
    
    <!-- WeatherCard.vue -->
    <script setup lang="ts">
    defineProps<{
      city: string;
      unit: "c" | "f";
    }>();
    </script>
    
    <template>
      <div class="rounded border p-3">
        <div class="text-sm text-zinc-500">Weather request</div>
        <div class="font-medium">{{ city }} ({{ unit.toUpperCase() }})</div>
      </div>
    </template>
    
    
    <!-- App.vue -->
    <script setup lang="ts">
    import { z } from "zod";
    import { useComponent } from "@copilotkit/vue/v2";
    import WeatherCard from "./WeatherCard.vue";
    
    const weatherCardSchema = z.object({
      city: z.string().describe("City name"),
      unit: z.enum(["c", "f"]).default("c"),
    });
    
    useComponent({
      name: "showWeatherCard",
      description: "Render a weather card in chat for the requested city.",
      parameters: weatherCardSchema,
      render: WeatherCard,
    });
    </script>

### Without parameters

When you omit `parameters`, the component accepts any props and the agent can invoke the tool with no arguments.
    
    
    <script setup lang="ts">
    import { useComponent } from "@copilotkit/vue/v2";
    import LoadingSpinner from "./LoadingSpinner.vue";
    
    useComponent({
      name: "showSpinner",
      render: LoadingSpinner,
    });
    </script>

### Refreshing on reactive changes

Pass reactive watch sources through `deps` so the registration re-runs when captured values change.
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { z } from "zod";
    import { useComponent } from "@copilotkit/vue/v2";
    import WeatherCard from "./WeatherCard.vue";
    
    // Pass any reactive watch sources the registration should track through `deps`;
    // the tool is re-registered whenever one of them changes.
    const refreshKey = ref(0);
    
    useComponent(
      {
        name: "showWeatherCard",
        parameters: z.object({ city: z.string() }),
        render: WeatherCard,
      },
      [refreshKey],
    );
    </script>

`agentId` is read once when the composable runs, so it cannot be made reactive through `deps`. To scope a component to a different agent at runtime, conditionally render the component that calls `useComponent`.

## Related

### [useFrontendToolRegister a frontend tool with an optional renderer. useComponent is built on top of this.](https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool)### [useRenderToolRender a tool call with full access to status (in progress, executing, complete) and results.](https://docs.copilotkit.ai/reference/vue/hooks/useRenderTool)
