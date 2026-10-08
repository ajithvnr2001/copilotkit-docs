---
url: https://docs.copilotkit.ai/reference/v2/hooks/useInterrupt/
title: useInterrupt
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:34:44.472185+00:00
---

# useInterrupt

> Source: https://docs.copilotkit.ai/reference/v2/hooks/useInterrupt/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁React (V2)SDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Components

[CopilotChat](https://docs.copilotkit.ai/reference/v2/components/CopilotChat)[CopilotChatAssistantMessage](https://docs.copilotkit.ai/reference/v2/components/CopilotChatAssistantMessage)[CopilotChatInput](https://docs.copilotkit.ai/reference/v2/components/CopilotChatInput)[CopilotChatMessageView](https://docs.copilotkit.ai/reference/v2/components/CopilotChatMessageView)[CopilotChatUserMessage](https://docs.copilotkit.ai/reference/v2/components/CopilotChatUserMessage)[CopilotChatView](https://docs.copilotkit.ai/reference/v2/components/CopilotChatView)[CopilotKit](https://docs.copilotkit.ai/reference/v2/components/CopilotKit)[CopilotPopup](https://docs.copilotkit.ai/reference/v2/components/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/v2/components/CopilotSidebar)[CopilotThreadsDrawer](https://docs.copilotkit.ai/reference/v2/components/CopilotThreadsDrawer)

Hooks

[useAgent](https://docs.copilotkit.ai/reference/v2/hooks/useAgent)[useAgentContext](https://docs.copilotkit.ai/reference/v2/hooks/useAgentContext)[useCapabilities](https://docs.copilotkit.ai/reference/v2/hooks/useCapabilities)[useComponent](https://docs.copilotkit.ai/reference/v2/hooks/useComponent)[useConfigureSuggestions](https://docs.copilotkit.ai/reference/v2/hooks/useConfigureSuggestions)[useCopilotChatConfiguration](https://docs.copilotkit.ai/reference/v2/hooks/useCopilotChatConfiguration)[useCopilotKit](https://docs.copilotkit.ai/reference/v2/hooks/useCopilotKit)[useDefaultRenderTool](https://docs.copilotkit.ai/reference/v2/hooks/useDefaultRenderTool)[useFrontendTool](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTool)[useFrontendTools](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTools)[useHumanInTheLoop](https://docs.copilotkit.ai/reference/v2/hooks/useHumanInTheLoop)[useInterrupt](https://docs.copilotkit.ai/reference/v2/hooks/useInterrupt)[useRenderTool](https://docs.copilotkit.ai/reference/v2/hooks/useRenderTool)[useRenderToolCall](https://docs.copilotkit.ai/reference/v2/hooks/useRenderToolCall)[useSuggestions](https://docs.copilotkit.ai/reference/v2/hooks/useSuggestions)[useThreads](https://docs.copilotkit.ai/reference/v2/hooks/useThreads)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[v2](https://docs.copilotkit.ai/reference/v2)Hooks

# useInterrupt

React hook for handling agent interrupt events and resuming execution with user input

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useInterrupt` handles agent interrupts and resumes execution with user input. It supports the **AG-UI standard interrupt flow** — `RUN_FINISHED` with `outcome.type === "interrupt"` carrying an `interrupts` array — and the legacy custom-event flow (`on_interrupt`). For standard interrupts, your `render`/`handler` receive `interrupt` (the primary one) and `interrupts` (the full open set); call `resolve(payload)` to resume or `cancel()` to cancel.

By default, interrupt UI is rendered inside `<CopilotChat>` automatically. If you set `renderInChat: false`, the hook returns the element so you can place it manually.

`event.value` is typed as `any` since the interrupt payload shape depends on your agent. Type-narrow it in your callbacks (e.g. `handler`, `enabled`, `render`) as needed.

## Signature
    
    
    import { useInterrupt } from "@copilotkit/react-core/v2";
    
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
    
    
    function ApprovalInterrupt() {
      useInterrupt({
        render: ({ event, resolve }) => (
          <div className="p-3 border rounded">
            <p>{event.value.question}</p>
            <div className="mt-2 flex gap-2">
              <button onClick={() => resolve({ approved: true })}>Approve</button>
              <button onClick={() => resolve({ approved: false })}>Reject</button>
            </div>
          </div>
        ),
      });
    
      return null;
    }

### Manual placement with async preprocessing
    
    
    function SidePanelInterrupt() {
      const element = useInterrupt({
        renderInChat: false,
        enabled: (event) => event.value.startsWith("approval:"),
        handler: async ({ event }) => ({ label: event.value.toUpperCase() }),
        render: ({ event, result, resolve }) => (
          <aside className="rounded border p-3">
            <div className="font-medium">{result?.label ?? ""}</div>
            <div className="mt-2">{event.value}</div>
            <button className="mt-2" onClick={() => resolve({ accepted: true })}>
              Continue
            </button>
          </aside>
        ),
      });
    
      return <>{element}</>;
    }

### AG-UI standard interrupt (approve / cancel)
    
    
    function ApprovalInterrupt() {
      useInterrupt({
        render: ({ interrupt, resolve, cancel }) => (
          <div className="p-3 border rounded">
            <p>{interrupt?.message ?? "Approve this action?"}</p>
            <div className="mt-2 flex gap-2">
              <button onClick={() => resolve({ approved: true })}>Approve</button>
              <button onClick={() => cancel()}>Cancel</button>
            </div>
          </div>
        ),
      });
      return null;
    }

## Behavior

  * Standard interrupts are detected from `RUN_FINISHED` (`outcome.type === "interrupt"`); legacy interrupts from `on_interrupt` custom events. Standard takes precedence if both appear in the same run.
  * `resolve`/`cancel` accumulate one response per open interrupt; the resume run starts once every open interrupt is addressed. Standard resumes use a fresh `runId` on the same thread and identify the pending interrupts through `resume[].interruptId`.
  * Expired interrupts (past `expiresAt`) are not resumed — the hook logs an error and clears pending state.
  * Interrupt UI is surfaced when the run finalizes.
  * Starting a new run clears pending interrupt state.
  * `event.value` is `any` \-- type-narrow in your callbacks as needed.
  * `render.result` is inferred from `handler` return type and is always `TResult | null`.
  * If `handler` throws or rejects, `result` is set to `null`.



## Related

  * [`useHumanInTheLoop`](https://docs.copilotkit.ai/reference/hooks/useHumanInTheLoop) \-- structured interactive tool workflows
  * [`useFrontendTool`](https://docs.copilotkit.ai/reference/hooks/useFrontendTool) \-- client-side tool registration
  * [`useAgent`](https://docs.copilotkit.ai/reference/hooks/useAgent) \-- access and subscribe to agent events


