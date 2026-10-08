---
url: https://docs.copilotkit.ai/google-adk/human-in-the-loop/useInterrupt/
title: Pausing the Agent for Input
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:03:11.240677+00:00
---

# Pausing the Agent for Input

> Source: https://docs.copilotkit.ai/google-adk/human-in-the-loop/useInterrupt/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendGoogle ADK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/google-adk)[Quickstart](https://docs.copilotkit.ai/google-adk/quickstart)[Build with agents](https://docs.copilotkit.ai/google-adk/build-with-agents)[Intelligence](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/google-adk/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[HITL Overview](https://docs.copilotkit.ai/google-adk/human-in-the-loop/index)[Pausing the Agent for Input](https://docs.copilotkit.ai/google-adk/human-in-the-loop/useInterrupt)[Headless Interrupts](https://docs.copilotkit.ai/google-adk/human-in-the-loop/headless)[Governed Action Approval UI](https://docs.copilotkit.ai/google-adk/human-in-the-loop/governed-actions)

[WebMCP](https://docs.copilotkit.ai/google-adk/webmcp)

Agent capabilities

Google ADK

[Sub-agents](https://docs.copilotkit.ai/google-adk/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/google-adk/learning)

[User Memories](https://docs.copilotkit.ai/google-adk/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/google-adk/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/google-adk/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/google-adk/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/google-adk/intelligence/analytics)[Channels](https://docs.copilotkit.ai/google-adk/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

Learn

Concepts

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/google-adk/telemetry)[Community frameworks](https://docs.copilotkit.ai/google-adk/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

InteractivityHuman-in-the-loop

# Pausing the Agent for Input

Pause an agent run mid-tool, hand control to a custom React component, and resume with the user's answer.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

interrupt_agent.py

page.tsx

time-picker-card.tsx

route.ts
    
    
    """ADK scheduling agent backing the gen-ui-interrupt demo (Strategy-B).In langgraph-python the gen-ui-interrupt demo relies on the native`interrupt()` primitive with checkpoint/resume. ADK has no such primitive,so we adapt with the same "Strategy B" pattern used by the agno andms-agent-framework ports: the agent's instruction tells Gemini to call the`schedule_meeting` tool, but NO backend tool is registered. CopilotKit's`AGUIToolset()` injects the frontend-registered `schedule_meeting`(`useHumanInTheLoop` in src/app/demos/gen-ui-interrupt/page.tsx) into themodel's tool list; the model's call is routed to the frontend, which rendersthe time-picker inline and resolves the call once the user picks a slot —equivalent to `interrupt()` in the LangGraph reference.`after_model_callback=stop_on_terminal_text` is the canonical ADK terminalguard (see shared_chat.py): without it the configured Gemini model(from `get_model()`) re-issues the same tool call indefinitely after thefrontend tool resolves."""from __future__ import annotations# region: setupfrom google.adk.agents import LlmAgentfrom ag_ui_adk import AGUIToolsetfrom agents.shared_chat import get_model, stop_on_terminal_text_INSTRUCTION = (    "You are a scheduling assistant. Whenever the user asks you to book a "    "call or schedule a meeting, you MUST call the `schedule_meeting` tool. "    "Pass a short `topic` describing the purpose of the meeting and, if "    "known, an `attendee` describing who the meeting is with.\n\n"    "The `schedule_meeting` tool is implemented on the client: it surfaces a "    "time-picker UI and returns the user's selection. After the tool "    "returns, briefly confirm whether the meeting was scheduled and at what "    "time, or note that the user cancelled. Do NOT ask for approval "    "yourself — always call the tool and let the picker handle the decision. "    "Keep responses short and friendly, and always send a brief final "    "assistant message summarising what happened so it persists.")interrupt_agent = LlmAgent(    name="InterruptAgent",    model=get_model(),    instruction=_INSTRUCTION,    # No backend tools. `schedule_meeting` is registered on the frontend via    # useHumanInTheLoop; AGUIToolset() exposes CopilotKit's frontend-tool    # channel to the model.    tools=[AGUIToolset()],    after_model_callback=stop_on_terminal_text,)# endregion

## What is this?#

`useInterrupt` lets your agent pause mid-run, hand control to the user through a custom React component, and resume with whatever the user returns. How that pause is implemented depends on the framework's runtime.

> **Not available on this framework.** `useInterrupt` is only meaningful when the underlying runtime exposes either a native `interrupt(...)` primitive (LangGraph, AWS Strands) or a Promise-resolving frontend tool path. For all other integrations, use [`useHumanInTheLoop`](https://docs.copilotkit.ai/google-adk/human-in-the-loop/human-in-the-loop) instead — it's the standard hook for tool-call-based pause/resume flows and works on every framework that supports tool calls.

## When should I use this?#

Reach for `useInterrupt` when the pause is a **graph-enforced checkpoint** where the code path _must_ stop and wait for a human, not an LLM-initiated tool call. Typical cases:

  * A sensitive action (payments, irreversible writes) must be approved
  * A required piece of state isn't known and can only be collected from the user
  * The agent explicitly reaches an approval node in a longer workflow
  * You want the server-side contract to be `interrupt(...)` and resume with a payload



For LLM-initiated pauses where the model decides on the fly to ask the user, prefer [`useHumanInTheLoop`](https://docs.copilotkit.ai/google-adk/human-in-the-loop/human-in-the-loop).

## AG-UI standard interrupt flow vs. legacy#

`useInterrupt` supports two interrupt transports. Understanding which one your agent uses helps you write the right `render` code.

### Standard flow (`RUN_FINISHED` with `outcome.type === "interrupt"`)#

When the agent backend conforms to the AG-UI protocol, it signals an interrupt by emitting a `RUN_FINISHED` event whose outcome carries the interrupts array:
    
    
    outcome.type === "interrupt"
    outcome.interrupts  // Interrupt[]

The hook detects this on `onRunFinishedEvent` and exposes the interrupts on the render props **after** `onRunFinalized` fires. Your `render` function receives:

  * **`interrupt`** — the primary `Interrupt` (`interrupts[0]`), with shape `{ id, reason, message?, toolCallId?, responseSchema?, expiresAt?, metadata? }`.
  * **`interrupts`** — the full open set (usually one, but multi-interrupt is supported — see below).
  * **`resolve(payload?, interruptId?)`** — records `{ status: "resolved", payload }` for the targeted interrupt (defaults to the primary). The agent run resumes once every open interrupt has a response.
  * **`cancel(interruptId?)`** — records `{ status: "cancelled" }` for the targeted interrupt. Same accumulate-then-submit logic applies.



### Legacy flow (`on_interrupt` custom event)#

Older agents (or agents not yet migrated to the AG-UI interrupt spec) emit a custom `on_interrupt` event. The hook detects this on `onCustomEvent` and sets `interrupt` to `null` and `interrupts` to `[]`. The payload is in `event.value`. Calling `resolve(payload)` resumes via `forwardedProps.command` (the legacy resume mechanism). `cancel()` dismisses the interrupt without resuming — the agent never receives a response.

### Priority#

If both signals appear on the same run (unlikely but possible during migration), the standard flow wins.

### Approve / Cancel example#
    
    
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

`resolve({ approved: true })` records a resolved entry and submits the `resume` array to the agent. `cancel()` records a cancelled entry and does the same. Both return the `RunAgentResult` once the run restarts.

### Multi-interrupt behavior#

Some agents issue more than one interrupt in a single run (e.g. two independent approvals). Each interrupt has its own `id`. Address them individually:
    
    
    useInterrupt({
      render: ({ interrupts, resolve, cancel }) => (
        <ul>
          {interrupts.map((i) => (
            <li key={i.id}>
              {i.message}
              <button onClick={() => resolve({ ok: true }, i.id)}>Approve</button>
              <button onClick={() => cancel(i.id)}>Cancel</button>
            </li>
          ))}
        </ul>
      ),
    });

The agent run only resumes once **every** open interrupt has been addressed. Calling `resolve` or `cancel` with a specific `interruptId` marks that interrupt done; the hook auto-submits the accumulated responses when the last one is addressed. If you omit `interruptId`, the primary interrupt (`interrupts[0]`) is targeted.

### `responseSchema` — surface only, no client-side validation#

The `Interrupt` type exposes a `responseSchema` field (a JSON Schema object) that the agent can use to describe the expected payload shape. `useInterrupt` surfaces this field on `interrupt.responseSchema` for your UI to read (e.g. to drive a form), but it does **not** validate `resolve` payloads against it. Validation is the agent's responsibility on resume.

## Going further#

  * [Tool-based HITL with `useHumanInTheLoop`](https://docs.copilotkit.ai/google-adk/human-in-the-loop/human-in-the-loop) — for LLM-initiated pauses.
  * [Headless interrupts](https://docs.copilotkit.ai/google-adk/human-in-the-loop/useInterrupt/headless) — compose the lower-level primitives (`useAgent`, `agent.subscribe`, `copilotkit.runAgent`) to resolve interrupts outside a chat surface.


