---
url: https://docs.copilotkit.ai/reference/vue/hooks/useCopilotKit/
title: useCopilotKit
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:22.142658+00:00
---

# useCopilotKit

> Source: https://docs.copilotkit.ai/reference/vue/hooks/useCopilotKit/

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

# useCopilotKit

Low-level Vue 3 composable for accessing the CopilotKit context

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useCopilotKit` is a low-level Vue 3 composable that injects the CopilotKit provider context, giving direct access to the core instance and provider-level reactive state. Because the values it returns are Vue refs, reading them inside a `computed`, `watch`, or template keeps your code reactive to runtime changes such as connection status or in-flight tool calls.

`useCopilotKit` is a low-level composable. Most applications should use higher-level composables like `useAgent` or `useFrontendTool` instead.

**Throws an error** if called outside of a `CopilotKitProvider`. The composable injects the provider context, so it must run within a component tree that has `CopilotKitProvider` as an ancestor.

## Signature
    
    
    import { useCopilotKit } from "@copilotkit/vue/v2";
    
    function useCopilotKit(): CopilotKitContextValue;

## Parameters

This composable takes no parameters.

## Return Value

The composable returns the `CopilotKitContextValue` object. Every member is a Vue ref (or computed ref), so access the underlying value with `.value` (or let the template unwrap it for you).

Prop

Type

`copilotkit?`ShallowRef<CopilotKitCoreVue>

Prop

Type

`executingToolCallIds?`Ref<ReadonlySet<string>>

Prop

Type

`a2uiTheme?`ComputedRef<A2UITheme | undefined>

Prop

Type

`a2uiCatalog?`ComputedRef<unknown>

Prop

Type

`a2uiLoadingComponent?`ComputedRef<unknown>

Prop

Type

`a2uiIncludeSchema?`ComputedRef<boolean>

## Usage

### Accessing the Core Instance
    
    
    <script setup lang="ts">
    import { computed } from "vue";
    import { useCopilotKit } from "@copilotkit/vue/v2";
    
    const { copilotkit } = useCopilotKit();
    
    const agentIds = computed(() => Object.keys(copilotkit.value.agents ?? {}));
    </script>
    
    <template>
      <div>
        <h3>Registered Agents</h3>
        <ul>
          <li v-for="id in agentIds" :key="id">{{ id }}</li>
        </ul>
      </div>
    </template>

### Subscribing to Core Events

Subscribe in `onMounted` and tear the subscription down in `onUnmounted`.
    
    
    <script setup lang="ts">
    import { onMounted, onUnmounted } from "vue";
    import { useCopilotKit } from "@copilotkit/vue/v2";
    
    const { copilotkit } = useCopilotKit();
    
    let subscription: { unsubscribe: () => void } | undefined;
    
    onMounted(() => {
      subscription = copilotkit.value.subscribe({
        onRuntimeConnectionStatusChanged: () => {
          console.log("Runtime connection status changed");
        },
      });
    });
    
    onUnmounted(() => {
      subscription?.unsubscribe();
    });
    </script>

### Running a Tool Programmatically

`copilotkit.value.runTool()` lets you execute a registered frontend tool directly from code, with no LLM turn required. The tool's handler runs, render components appear in the UI, and both the tool call and its result are added to the agent's message history.
    
    
    <script setup lang="ts">
    import { z } from "zod";
    import { useCopilotKit, useFrontendTool } from "@copilotkit/vue/v2";
    
    const { copilotkit } = useCopilotKit();
    
    // Register the tool
    useFrontendTool({
      name: "exportData",
      description: "Export data as CSV",
      parameters: z.object({ format: z.string() }),
      handler: async ({ format }) => {
        const csv = await generateCsv(format);
        downloadFile(csv);
        return `Exported as ${format}`;
      },
    });
    
    // Trigger it from a button, no LLM needed
    async function handleExport() {
      try {
        const { result, error } = await copilotkit.value.runTool({
          name: "exportData",
          parameters: { format: "csv" },
        });
        // `error` is set when the handler itself throws.
        if (error) console.error(error);
      } catch (err) {
        // `runTool` rejects if the tool (or its agent) cannot be found.
        console.error(err);
      }
    }
    </script>
    
    <template>
      <button @click="handleExport">Export CSV</button>
    </template>

#### `runTool` Parameters

Prop

Type

`params?`CopilotKitCoreRunToolParams

#### `runTool` Return Value

Prop

Type

`result?`CopilotKitCoreRunToolResult

### Checking Tool Execution State

Because `executingToolCallIds` is a ref, drive UI off it with a `computed` or read it directly in the template.
    
    
    <script setup lang="ts">
    import { computed } from "vue";
    import { useCopilotKit } from "@copilotkit/vue/v2";
    
    const { executingToolCallIds } = useCopilotKit();
    
    const executingCount = computed(() => executingToolCallIds.value.size);
    </script>
    
    <template>
      <div v-if="executingCount > 0">
        Executing {{ executingCount }} tool call(s)...
      </div>
    </template>

## Behavior

  * **Error on missing provider** : Throws `useCopilotKit must be used within CopilotKitProvider` if the composable is called outside of a `CopilotKitProvider`.
  * **Refs, not plain values** : Every returned member is a Vue ref or computed ref. Read `copilotkit.value` to reach the core instance and `executingToolCallIds.value` to reach the live set. Keep usage reactive with `computed`, `watch`, or template bindings.
  * **Stable core reference** : The `copilotkit` ref is a `shallowRef` created once per provider and remains stable for the provider's lifetime. Only `executingToolCallIds` changes as tool calls begin and complete.
  * **Provider-level tool tracking** : `executingToolCallIds` is tracked at the provider level rather than in individual components, so tool execution start events fired before child components mount are not lost.



## Related

  * [`useAgent`](https://docs.copilotkit.ai/reference/vue/hooks/useAgent) \-- High-level composable for accessing agent instances
  * [`useFrontendTool`](https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool) \-- Register frontend tools that `runTool()` can execute
  * [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider) \-- The provider component that creates the context


