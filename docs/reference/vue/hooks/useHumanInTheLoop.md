---
url: https://docs.copilotkit.ai/reference/vue/hooks/useHumanInTheLoop/
title: useHumanInTheLoop
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:25.123159+00:00
---

# useHumanInTheLoop

> Source: https://docs.copilotkit.ai/reference/vue/hooks/useHumanInTheLoop/

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

# useHumanInTheLoop

Vue 3 composable for interactive tools that pause agent execution and wait for user input

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useHumanInTheLoop` registers an interactive frontend tool that pauses agent execution until the user responds through your custom UI. Unlike `useFrontendTool`, you do not supply a `handler`. Instead, the composable manages an internal status machine (`InProgress` -> `Executing` -> `Complete`) and passes a `respond` callback to your render component while the tool is in the `executing` phase. The agent stays paused until `respond` is called with the user's input.

Internally the composable wraps `useFrontendTool`. It generates a handler that returns a promise, holds onto that promise's `resolve` in a ref, and resolves it when `respond` is invoked, which sends the result back to the agent and resumes execution. Use it for confirmation dialogs, approval workflows, form collection, or any scenario where a human must provide input before the agent can continue.

`useHumanInTheLoop` must be called within a component that has access to the CopilotKit instance provided by `CopilotKitProvider`. Like all Vue composables, call it synchronously inside `<script setup>` or a `setup()` function so its reactive scope is bound to the component lifecycle. The tool is unregistered automatically on scope cleanup.

## Signature
    
    
    import { useHumanInTheLoop } from "@copilotkit/vue/v2";
    
    function useHumanInTheLoop<T extends Record<string, unknown>>(
      tool: VueHumanInTheLoop<T>,
      deps?: WatchSource<unknown>[],
    ): void;

## Parameters

Prop

Type

`tool`VueHumanInTheLoop<T>

Prop

Type

`deps?`WatchSource<unknown>[]

## Usage

Define the render component as a separate Vue SFC, then register it with `useHumanInTheLoop`. The component receives `status`, `args`, `respond`, `name`, and `description` as props.

### Confirmation Dialog

A common pattern where the agent asks the user to confirm a destructive action.

`ConfirmDeletion.vue` (the render component):
    
    
    <script setup lang="ts">
    import { ToolCallStatus } from "@copilotkit/core";
    
    defineProps<{
      status: ToolCallStatus;
      args: { itemName?: string; itemCount?: number };
      name: string;
      description: string;
      result?: string;
      respond?: (result: unknown) => Promise<void>;
    }>();
    </script>
    
    <template>
      <div v-if="status === ToolCallStatus.InProgress" class="p-4 text-gray-500">
        Preparing confirmation...
      </div>
    
      <div
        v-else-if="status === ToolCallStatus.Executing && respond"
        class="p-4 border rounded"
      >
        <p>Are you sure you want to delete {{ args.itemCount }} {{ args.itemName }}(s)?</p>
        <div class="flex gap-2 mt-4">
          <button
            class="bg-red-500 text-white px-4 py-2 rounded"
            @click="respond({ confirmed: true })"
          >
            Delete
          </button>
          <button
            class="bg-gray-300 px-4 py-2 rounded"
            @click="respond({ confirmed: false })"
          >
            Cancel
          </button>
        </div>
      </div>
    
      <div
        v-else-if="status === ToolCallStatus.Complete && result"
        class="p-2 text-sm text-gray-600"
      >
        {{ JSON.parse(result).confirmed ? "Items deleted." : "Deletion cancelled." }}
      </div>
    </template>

Register it from a component in scope of `CopilotKitProvider`:
    
    
    <script setup lang="ts">
    import { useHumanInTheLoop } from "@copilotkit/vue/v2";
    import { z } from "zod";
    import ConfirmDeletion from "./ConfirmDeletion.vue";
    
    useHumanInTheLoop({
      name: "confirmDeletion",
      description: "Ask the user to confirm before deleting items",
      parameters: z.object({
        itemName: z.string().describe("Name of the item to delete"),
        itemCount: z.number().describe("Number of items to delete"),
      }),
      render: ConfirmDeletion,
    });
    </script>
    
    <template>
      <!-- nothing to render here; the tool UI is shown in the chat -->
    </template>

### Form Input Collection

Collect structured input from the user before the agent proceeds. Local form state lives in the render component using `ref`.

`ShippingAddressForm.vue`:
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { ToolCallStatus } from "@copilotkit/core";
    
    defineProps<{
      status: ToolCallStatus;
      args: { orderSummary?: string };
      name: string;
      description: string;
      result?: string;
      respond?: (result: unknown) => Promise<void>;
    }>();
    
    const address = ref({ street: "", city: "", zip: "" });
    </script>
    
    <template>
      <div
        v-if="status === ToolCallStatus.Executing && respond"
        class="p-4 border rounded space-y-3"
      >
        <p class="font-medium">Order: {{ args.orderSummary }}</p>
        <p>Please enter your shipping address:</p>
        <input
          v-model="address.street"
          placeholder="Street address"
          class="w-full border p-2 rounded"
        />
        <input
          v-model="address.city"
          placeholder="City"
          class="w-full border p-2 rounded"
        />
        <input
          v-model="address.zip"
          placeholder="ZIP code"
          class="w-full border p-2 rounded"
        />
        <button
          class="bg-blue-500 text-white px-4 py-2 rounded"
          @click="respond({ ...address })"
        >
          Submit Address
        </button>
      </div>
    
      <div v-else-if="status === ToolCallStatus.Complete" class="p-2 text-green-600">
        Shipping address submitted.
      </div>
    </template>

Registration:
    
    
    <script setup lang="ts">
    import { useHumanInTheLoop } from "@copilotkit/vue/v2";
    import { z } from "zod";
    import ShippingAddressForm from "./ShippingAddressForm.vue";
    
    useHumanInTheLoop({
      name: "collectShippingAddress",
      description: "Collect shipping address from the user before placing an order",
      parameters: z.object({
        orderSummary: z.string().describe("A summary of the order being placed"),
      }),
      render: ShippingAddressForm,
    });
    </script>
    
    <template>
      <!-- tool UI renders inside the chat -->
    </template>

### Approval Workflow with Context

`ExpenseApproval.vue`:
    
    
    <script setup lang="ts">
    import { ToolCallStatus } from "@copilotkit/core";
    
    defineProps<{
      status: ToolCallStatus;
      args: {
        employeeName?: string;
        amount?: number;
        category?: string;
        description?: string;
      };
      name: string;
      description: string;
      result?: string;
      respond?: (result: unknown) => Promise<void>;
    }>();
    </script>
    
    <template>
      <div
        v-if="status === ToolCallStatus.Executing && respond"
        class="p-4 border rounded"
      >
        <h3 class="font-bold">Expense Approval Required</h3>
        <div class="mt-2 space-y-1 text-sm">
          <p>Employee: {{ args.employeeName }}</p>
          <p>Amount: ${{ args.amount?.toFixed(2) }}</p>
          <p>Category: {{ args.category }}</p>
          <p>Description: {{ args.description }}</p>
        </div>
        <div class="flex gap-2 mt-4">
          <button
            class="bg-green-500 text-white px-4 py-2 rounded"
            @click="respond({ approved: true })"
          >
            Approve
          </button>
          <button
            class="bg-red-500 text-white px-4 py-2 rounded"
            @click="respond({ approved: false, reason: 'Needs more detail' })"
          >
            Reject
          </button>
        </div>
      </div>
    
      <div
        v-else-if="status === ToolCallStatus.Complete && result"
        class="p-2 text-sm"
        :class="JSON.parse(result).approved ? 'text-green-600' : 'text-red-600'"
      >
        {{
          JSON.parse(result).approved
            ? "Expense approved."
            : `Expense rejected: ${JSON.parse(result).reason}`
        }}
      </div>
    </template>

Registration:
    
    
    <script setup lang="ts">
    import { useHumanInTheLoop } from "@copilotkit/vue/v2";
    import { z } from "zod";
    import ExpenseApproval from "./ExpenseApproval.vue";
    
    useHumanInTheLoop({
      name: "approveExpense",
      description: "Request manager approval for an expense report",
      parameters: z.object({
        employeeName: z.string().describe("Name of the employee"),
        amount: z.number().describe("Expense amount in dollars"),
        category: z.string().describe("Expense category"),
        description: z.string().describe("Description of the expense"),
      }),
      render: ExpenseApproval,
    });
    </script>
    
    <template>
      <!-- tool UI renders inside the chat -->
    </template>

## Behavior

  * **Blocks agent execution** : The internally generated handler returns a promise that does not resolve until `respond` is called, so the agent pauses on this tool call and waits for the user.
  * **Internal status machine** : The composable drives three phases - `inProgress` (arguments streaming in), `executing` (waiting for the user, `respond` available), and `complete` (user has responded, `result` available). Your render component receives the appropriate props for each phase.
  * **`respond` is only passed during `executing`**: In the `inProgress` and `complete` phases, `respond` is `undefined`. Guard on `status === ToolCallStatus.Executing && respond` before calling it.
  * **Single response** : Calling `respond` resolves the pending promise once and clears the stored resolver, so subsequent calls are no-ops for that tool invocation.
  * **Built on`useFrontendTool`**: The composable forwards a `VueFrontendTool` (your tool plus the generated `handler` and a wrapping render component) to `useFrontendTool`, so the same registration lifecycle applies.
  * **Scope lifecycle** : The tool and its render component are registered while the composable's reactive scope is active and removed automatically on scope cleanup — the render component via `onScopeDispose`, and the tool via the underlying `useFrontendTool` watch's cleanup.
  * **No return value** : The composable returns `void`.



## Related

### [useFrontendToolRegister tools with automated handlers that do not require user interaction.](https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool)### [useCopilotKitAccess the underlying CopilotKit instance.](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotKit)### [CopilotKitProviderProvides the CopilotKit instance to descendant composables.](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider)

## ToolCallStatus

The `ToolCallStatus` enum is exported from `@copilotkit/core` and defines the three phases of tool execution. Its string values are what appear in the render component's `status` prop.

Value| String value| Description  
---|---|---  
`ToolCallStatus.InProgress`| `"inProgress"`| Arguments are being streamed from the agent. The tool has not started executing yet.  
`ToolCallStatus.Executing`| `"executing"`| Arguments are fully resolved. For `useHumanInTheLoop`, the `respond` callback is passed.  
`ToolCallStatus.Complete`| `"complete"`| Execution is finished. The `result` string is available.
