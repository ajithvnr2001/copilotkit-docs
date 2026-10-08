---
url: https://docs.copilotkit.ai/reference/vue/hooks/useAgentContext/
title: useAgentContext
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:20.794372+00:00
---

# useAgentContext

> Source: https://docs.copilotkit.ai/reference/vue/hooks/useAgentContext/

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

# useAgentContext

Vue 3 composable for providing reactive context to agents

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useAgentContext` registers reactive contextual data that is sent with agent runs. The context entry is added while the composable is active and removed automatically on scope cleanup, so the agent always sees an up-to-date snapshot of your application state without manual teardown.

Because the parameters accept `MaybeRefOrGetter`, you can pass plain values, refs, computeds, or getter functions. When any reactive source changes, the registered context is updated automatically. This lets you surface any serializable application state (user preferences, selected items, computed values, etc.) as context that agents can reference when generating responses or making decisions.

`useAgentContext` must be called within a component that has access to the CopilotKit instance provided by `CopilotKitProvider`. Like all Vue composables, call it synchronously inside `<script setup>` or a `setup()` function so its reactive scope is bound to the component lifecycle.

## Signature
    
    
    import { useAgentContext } from "@copilotkit/vue/v2";
    
    function useAgentContext(context: AgentContextInput): void;

## Parameters

Prop

Type

`context`AgentContextInput

## Usage

### Basic Usage

Provide simple, static application state as context for the agent.
    
    
    <script setup lang="ts">
    import { useAgentContext } from "@copilotkit/vue/v2";
    
    useAgentContext({
      description: "Current workspace",
      value: "copilotkit-vue",
    });
    </script>
    
    <template>
      <div>Workspace ready</div>
    </template>

### Reactive Context from Component State

Pass refs or getters so the context updates automatically whenever the underlying state changes. There is no need to re-register.
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { useAgentContext } from "@copilotkit/vue/v2";
    
    const selectedCategory = ref("electronics");
    const priceRange = ref({ min: 0, max: 500 });
    
    useAgentContext({
      description: "The user's current product filter settings",
      value: () => ({
        category: selectedCategory.value,
        priceRange: priceRange.value,
      }),
    });
    </script>
    
    <template>
      <select v-model="selectedCategory">
        <option value="electronics">Electronics</option>
        <option value="books">Books</option>
        <option value="clothing">Clothing</option>
      </select>
      <!-- ... price range controls ... -->
    </template>

### Using a Computed Value

A `computed` ref works anywhere a `MaybeRefOrGetter` is accepted, including the `description`.
    
    
    <script setup lang="ts">
    import { computed, ref } from "vue";
    import { useAgentContext } from "@copilotkit/vue/v2";
    
    const props = defineProps<{
      user: { name: string; role: string };
    }>();
    
    const userContext = computed(() => ({
      name: props.user.name,
      role: props.user.role,
    }));
    
    useAgentContext({
      description: computed(() => `Profile for ${props.user.name}`),
      value: userContext,
    });
    </script>
    
    <template>
      <div>Welcome, {{ user.name }}</div>
    </template>

### Multiple Contexts

Each component can register its own context. All registered contexts are visible to the agent simultaneously.
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { useAgentContext } from "@copilotkit/vue/v2";
    
    const collapsed = ref(false);
    
    useAgentContext({
      description: "Current dashboard view and layout",
      value: { view: "analytics", columns: 3 },
    });
    
    useAgentContext({
      description: "Sidebar navigation state",
      value: () => ({ collapsed: collapsed.value, activeSection: "reports" }),
    });
    </script>
    
    <template>
      <div>
        <!-- dashboard layout -->
      </div>
    </template>

## What the agent receives

Every registered entry reaches the agent as `{ description, value }`, and `value` is a **JSON string** \- not the object or array you passed. The AG-UI protocol types it as a string, so this is not an implementation detail you can ignore when writing the agent.

Registering this:
    
    
    <script setup lang="ts">
    import { useAgentContext } from "@copilotkit/vue/v2";
    
    useAgentContext({
      description: "Incident dashboard records",
      value: [{ id: "INC-1041", severity: "sev1" }],
    });
    </script>

delivers this to the agent:
    
    
    {
      "description": "Incident dashboard records",
      "value": "[{\"id\":\"INC-1041\",\"severity\":\"sev1\"}]"
    }

Parse it before reading any field. In a Python agent:
    
    
    import json
    
    def dashboard_records(context):
        entry = next(
            (item for item in context if item["description"] == "Incident dashboard records"),
            None,
        )
        return None if entry is None else json.loads(entry["value"])

In a TypeScript agent:
    
    
    const entry = context.find(
      (item) => item.description === "Incident dashboard records",
    );
    const records = entry ? JSON.parse(entry.value) : undefined;

Where that context list surfaces in your agent depends on your framework's AG-UI adapter - see your integration's guide for the field it populates.

Do not type-check `value` against the shape you registered. `isinstance(entry["value"], list)` in Python, or `Array.isArray(entry.value)` in TypeScript, can never be true, because `value` is always a string on the wire. An agent that reads such a failed check as "no context was sent" will refuse every request while the app is registering context correctly, and the two cases are indistinguishable from the UI.

## Behavior

  * **Scope lifecycle** : The context is registered while the composable's reactive scope is active and is removed automatically on scope cleanup (component unmount). No manual cleanup is required.
  * **Reactive updates** : `description` and `value` are resolved with `toValue`, so refs, computeds, and getters are tracked. When a resolved value changes, the previous context entry is removed and the new value is re-registered, keeping the agent in sync.
  * **Serialization** : String values are passed through as-is. Any other value is serialized with `JSON.stringify`, so it must conform to `JsonSerializable` (`string | number | boolean | null | JsonSerializable[] | { [key: string]: JsonSerializable }`). Non-serializable values such as functions, class instances, or symbols will not serialize correctly. The agent therefore always reads a string - see What the agent receives.
  * **Multiple contexts** : Multiple `useAgentContext` calls across your component tree are all visible to the agent concurrently. Each is identified internally by an ID returned from `addContext` and removed on cleanup.
  * **No return value** : The composable returns `void`.



## Related

  * [`useCopilotKit`](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotKit) \- access the underlying CopilotKit instance
  * [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider) \- provides the CopilotKit instance to descendant composables


