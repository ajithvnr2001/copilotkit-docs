---
url: https://docs.copilotkit.ai/reference/react-native/hooks/useInterrupt/
title: useInterrupt
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:51.909238+00:00
---

# useInterrupt

> Source: https://docs.copilotkit.ai/reference/react-native/hooks/useInterrupt/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁React NativeSDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Components

[AssistantMessage](https://docs.copilotkit.ai/reference/react-native/components/AssistantMessage)[CopilotChat](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat)[CopilotKitProvider](https://docs.copilotkit.ai/reference/react-native/components/CopilotKitProvider)[CopilotMarkdown](https://docs.copilotkit.ai/reference/react-native/components/CopilotMarkdown)[CopilotModal](https://docs.copilotkit.ai/reference/react-native/components/CopilotModal)[CopilotPopup](https://docs.copilotkit.ai/reference/react-native/components/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/react-native/components/CopilotSidebar)[UserMessage](https://docs.copilotkit.ai/reference/react-native/components/UserMessage)

Hooks

[useAgent](https://docs.copilotkit.ai/reference/react-native/hooks/useAgent)[useAgentContext](https://docs.copilotkit.ai/reference/react-native/hooks/useAgentContext)[useAttachments](https://docs.copilotkit.ai/reference/react-native/hooks/useAttachments)[useCapabilities](https://docs.copilotkit.ai/reference/react-native/hooks/useCapabilities)[useComponent](https://docs.copilotkit.ai/reference/react-native/hooks/useComponent)[useConfigureSuggestions](https://docs.copilotkit.ai/reference/react-native/hooks/useConfigureSuggestions)[useCopilotKit](https://docs.copilotkit.ai/reference/react-native/hooks/useCopilotKit)[useFrontendTool](https://docs.copilotkit.ai/reference/react-native/hooks/useFrontendTool)[useHumanInTheLoop](https://docs.copilotkit.ai/reference/react-native/hooks/useHumanInTheLoop)[useInterrupt](https://docs.copilotkit.ai/reference/react-native/hooks/useInterrupt)[useRenderTool](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool)[useSuggestions](https://docs.copilotkit.ai/reference/react-native/hooks/useSuggestions)[useThreads](https://docs.copilotkit.ai/reference/react-native/hooks/useThreads)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[react-native](https://docs.copilotkit.ai/reference/react-native)Hooks

# useInterrupt

React hook for handling agent interrupt events and resuming execution with user input

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useInterrupt` handles agent interrupts and resumes execution with user input. It supports the **AG-UI standard interrupt flow** — `RUN_FINISHED` with `outcome.type === "interrupt"` carrying an `interrupts` array — and the legacy custom-event flow (`on_interrupt`). For standard interrupts, your `render`/`handler` receive `interrupt` (the primary one) and `interrupts` (the full open set); call `resolve(payload)` to resume or `cancel()` to cancel.

Re-exported from `@copilotkit/react-core/v2`. It is identical to the [React (V2) `useInterrupt`](https://docs.copilotkit.ai/reference/v2/hooks/useInterrupt); only the import path differs.

By default, interrupt UI is rendered inside [`CopilotChat`](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat) automatically. If you set `renderInChat: false`, the hook returns the element so you can place it manually. The element returned by `render` is a React Native element.

`event.value` is typed as `any` since the interrupt payload shape depends on your agent. Type-narrow it in your callbacks (e.g. `handler`, `enabled`, `render`) as needed.

## Signature
    
    
    import { useInterrupt } from "@copilotkit/react-native";
    
    function useInterrupt<
      TResult = never,
      TRenderInChat extends boolean | undefined = undefined,
    >(
      config: UseInterruptConfig<any, TResult, TRenderInChat>,
    ): TRenderInChat extends false
      ? React.ReactElement | null
      : TRenderInChat extends true | undefined
        ? void
        : React.ReactElement | null | void;

## Parameters

Prop

Type

`config`UseInterruptConfig<any, TResult, TRenderInChat>

## Return Value

Prop

Type

`element?`Conditional by renderInChat

## Usage

### In-chat interrupt UI (default)
    
    
    import { Text, TouchableOpacity, View } from "react-native";
    import { useInterrupt } from "@copilotkit/react-native";
    
    function ApprovalInterrupt() {
      useInterrupt({
        render: ({ event, resolve }) => (
          <View style={{ padding: 12, borderWidth: 1, borderRadius: 8 }}>
            <Text>{event.value.question}</Text>
            <View style={{ marginTop: 8, flexDirection: "row", gap: 8 }}>
              <TouchableOpacity onPress={() => resolve({ approved: true })}>
                <Text>Approve</Text>
              </TouchableOpacity>
              <TouchableOpacity onPress={() => resolve({ approved: false })}>
                <Text>Reject</Text>
              </TouchableOpacity>
            </View>
          </View>
        ),
      });
    
      return null;
    }

### AG-UI standard interrupt (approve / cancel)
    
    
    import { Text, TouchableOpacity, View } from "react-native";
    import { useInterrupt } from "@copilotkit/react-native";
    
    function ApprovalInterrupt() {
      useInterrupt({
        render: ({ interrupt, resolve, cancel }) => (
          <View style={{ padding: 12, borderWidth: 1, borderRadius: 8 }}>
            <Text>{interrupt?.message ?? "Approve this action?"}</Text>
            <View style={{ marginTop: 8, flexDirection: "row", gap: 8 }}>
              <TouchableOpacity onPress={() => resolve({ approved: true })}>
                <Text>Approve</Text>
              </TouchableOpacity>
              <TouchableOpacity onPress={() => cancel()}>
                <Text>Cancel</Text>
              </TouchableOpacity>
            </View>
          </View>
        ),
      });
    
      return null;
    }

### Manual placement with async preprocessing
    
    
    import { Text, TouchableOpacity, View } from "react-native";
    import { useInterrupt } from "@copilotkit/react-native";
    
    function SidePanelInterrupt() {
      const element = useInterrupt({
        renderInChat: false,
        enabled: (event) => event.value.startsWith("approval:"),
        handler: async ({ event }) => ({ label: event.value.toUpperCase() }),
        render: ({ event, result, resolve }) => (
          <View style={{ borderWidth: 1, borderRadius: 8, padding: 12 }}>
            <Text style={{ fontWeight: "500" }}>{result?.label ?? ""}</Text>
            <Text style={{ marginTop: 8 }}>{event.value}</Text>
            <TouchableOpacity style={{ marginTop: 8 }} onPress={() => resolve({ accepted: true })}>
              <Text>Continue</Text>
            </TouchableOpacity>
          </View>
        ),
      });
    
      return <>{element}</>;
    }

## Behavior

  * Standard interrupts are detected from `RUN_FINISHED` (`outcome.type === "interrupt"`); legacy interrupts from `on_interrupt` custom events.
  * `resolve`/`cancel` accumulate one response per open interrupt; the resume run starts once every open interrupt is addressed.
  * Expired interrupts (past `expiresAt`) are not resumed.
  * Interrupt UI is surfaced when the run finalizes.
  * Starting a new run clears pending interrupt state.
  * `event.value` is `any`; type-narrow in your callbacks as needed. For standard interrupts, `event.value` is the primary `Interrupt`.
  * `render.result` is inferred from `handler` return type and is always `TResult | null`.
  * If `handler` throws or rejects, `result` is set to `null`.



## Related

  * [`useHumanInTheLoop`](https://docs.copilotkit.ai/reference/react-native/hooks/useHumanInTheLoop): structured interactive tool workflows
  * [`useFrontendTool`](https://docs.copilotkit.ai/reference/react-native/hooks/useFrontendTool): client-side tool registration
  * [`useAgent`](https://docs.copilotkit.ai/reference/react-native/hooks/useAgent): access and subscribe to agent events
  * [React (V2) reference](https://docs.copilotkit.ai/reference/v2/hooks/useInterrupt)


