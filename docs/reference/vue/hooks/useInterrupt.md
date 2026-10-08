---
url: https://docs.copilotkit.ai/reference/vue/hooks/useInterrupt/
title: useInterrupt
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:24.816250+00:00
---

# useInterrupt

> Source: https://docs.copilotkit.ai/reference/vue/hooks/useInterrupt/

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

# useInterrupt

Vue 3 composable for handling agent interrupt events and resuming execution with user input

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useInterrupt` is a Vue 3 composable that listens for agent custom events named `on_interrupt`, captures the latest interrupt payload for a run, and surfaces it once the run finalizes. Your UI calls `resolveInterrupt(response)` to resume the agent with a resume payload.

Unlike a render-prop API, the Vue composable does not return UI. Instead it returns reactive state (`interrupt`, `result`, `hasInterrupt`, `slotProps`) plus the `resolveInterrupt` function, and (by default) publishes that state into `<CopilotChat>` so you can render interrupts through the chat's `#interrupt` slot.

`event.value` is typed by the `TValue` type parameter (defaults to `unknown`), since the interrupt payload shape depends on your agent. Type-narrow it in your `handler` and `enabled` callbacks, or pass an explicit `TValue` when calling the composable.

By default (`renderInChat` omitted or `true`), the composable pushes interrupt state into `<CopilotChat>`, where you render it via the `#interrupt` slot. Set `renderInChat: false` to manage rendering yourself from the returned reactive refs.

## Signature
    
    
    import { useInterrupt } from "@copilotkit/vue/v2";
    
    function useInterrupt<TValue = unknown, TResult = never>(
      config?: UseInterruptConfig<TValue, TResult>,
    ): UseInterruptResult<TValue, TResult>;

## Parameters

Prop

Type

`config?`UseInterruptConfig<TValue, TResult>

## Return Value

Prop

Type

`object?`UseInterruptResult<TValue, TResult>

## Usage

### In-chat interrupt UI (default)

By default the composable publishes interrupt state into `<CopilotChat>`. Mount the composable, then render the interrupt through the chat's `#interrupt` slot.
    
    
    <script setup lang="ts">
    import { useInterrupt } from "@copilotkit/vue/v2";
    import { CopilotChat } from "@copilotkit/vue/v2";
    
    interface Approval {
      question: string;
    }
    
    // Publishes interrupt state into <CopilotChat>.
    useInterrupt<Approval>();
    </script>
    
    <template>
      <CopilotChat>
        <template #interrupt="{ event, resolve }">
          <div class="rounded border p-3">
            <!-- `#interrupt` slot props are typed with `unknown` value; cast to your payload type. -->
            <p>{{ (event.value as Approval).question }}</p>
            <div class="mt-2 flex gap-2">
              <button @click="resolve({ approved: true })">Approve</button>
              <button @click="resolve({ approved: false })">Reject</button>
            </div>
          </div>
        </template>
      </CopilotChat>
    </template>

### Manual placement with async preprocessing

Set `renderInChat: false` and render directly from the returned reactive refs.
    
    
    <script setup lang="ts">
    import { useInterrupt } from "@copilotkit/vue/v2";
    
    const { interrupt, result, hasInterrupt, resolveInterrupt } = useInterrupt<
      string,
      { label: string }
    >({
      renderInChat: false,
      enabled: (event) => event.value.startsWith("approval:"),
      handler: async ({ event }) => ({ label: event.value.toUpperCase() }),
    });
    </script>
    
    <template>
      <aside v-if="hasInterrupt" class="rounded border p-3">
        <div class="font-medium">{{ result?.label ?? "" }}</div>
        <div class="mt-2">{{ interrupt?.value }}</div>
        <button class="mt-2" @click="resolveInterrupt({ accepted: true })">
          Continue
        </button>
      </aside>
    </template>

### Reading reactive state in script
    
    
    import { useInterrupt } from "@copilotkit/vue/v2";
    
    const { interrupt, hasInterrupt, result, resolveInterrupt } = useInterrupt({
      handler: ({ event }) => ({ label: String(event.value) }),
    });
    
    // `interrupt` and `result` are reactive refs; `hasInterrupt` is a computed.
    // Call `resolveInterrupt(response)` to resume the agent.

## Behavior

  * Interrupts are collected from agent custom events named `on_interrupt`.
  * The pending interrupt is surfaced when the run finalizes (`onRunFinalized`).
  * Starting a new run (`onRunStartedEvent`) clears pending interrupt state, and a failed run (`onRunFailed`) discards the in-flight interrupt.
  * `event.value` is typed by `TValue` (defaults to `unknown`); narrow it in `handler` / `enabled` or pass an explicit `TValue`.
  * `result` is inferred from the `handler` return type and is always `TResult | null`. If `handler` returns a rejected promise, `result` is set to `null`; a synchronous `throw` is not caught (it surfaces from the watcher that runs the handler) and `result` is left unchanged.
  * When `enabled` returns `false`, the interrupt is ignored: `result` and `slotProps` stay `null` and nothing is published to chat.
  * With `renderInChat` omitted or `true`, `slotProps` is published into `<CopilotChat>` for the `#interrupt` slot. With `renderInChat: false`, no chat publishing occurs and you render from the returned refs.
  * `resolveInterrupt(response)` resumes the agent via `runAgent` with `forwardedProps.command.resume = response` (along with the originating `interruptEvent`); it no-ops if no agent is resolved.



## Related

### [useAgentAccess and subscribe to AG-UI agent instances and events.](https://docs.copilotkit.ai/reference/vue/hooks/useAgent)### [useFrontendToolRegister a client-side tool with an optional renderer.](https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool)### [CopilotChatChat component that renders interrupt UI via the #interrupt slot.](https://docs.copilotkit.ai/reference/vue/components/CopilotChat)
