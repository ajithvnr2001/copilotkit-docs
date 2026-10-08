---
url: https://docs.copilotkit.ai/slack/google-adk/human-in-the-loop/
title: HITL Overview
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:39:38.035732+00:00
---

# HITL Overview

> Source: https://docs.copilotkit.ai/slack/google-adk/human-in-the-loop/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

ChannelSlackAgent backendGoogle ADK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Getting Started

[Overview](https://docs.copilotkit.ai/slack/google-adk)[Configure the Channel in Intelligence](https://docs.copilotkit.ai/slack/google-adk/intelligence)[Connect and run your agent](https://docs.copilotkit.ai/slack/google-adk/connect)

Build

[Tools and context](https://docs.copilotkit.ai/slack/google-adk/tools)[Identity and Memory](https://docs.copilotkit.ai/slack/google-adk/identity-and-memory)[Rich messages and components](https://docs.copilotkit.ai/slack/google-adk/rich-messages)[Interactive messages and approvals](https://docs.copilotkit.ai/slack/google-adk/interactive)[Commands and reactions](https://docs.copilotkit.ai/slack/google-adk/commands-and-reactions)[Files and multimodal input](https://docs.copilotkit.ai/slack/google-adk/files-and-multimodality)[Threads and state](https://docs.copilotkit.ai/slack/google-adk/threads-and-state)

Production

[Persistence and scaling](https://docs.copilotkit.ai/slack/google-adk/persistence-and-scaling)[History and transcripts](https://docs.copilotkit.ai/slack/google-adk/history-and-transcripts)[Deploy and operate](https://docs.copilotkit.ai/slack/google-adk/deploy-and-operate)[API reference](https://docs.copilotkit.ai/reference/channels)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[Google ADK](https://docs.copilotkit.ai/slack/google-adk)

# HITL Overview

Allow your agent and users to collaborate on complex tasks.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

hitl_in_chat_book_call_agent.py

page.tsx

time-picker-card.tsx

route.ts
    
    
    """ADK agent backing the In-Chat HITL (book_call) demo.
    
    The `book_call` tool is defined on the frontend via `useHumanInTheLoop`, so
    there is no backend tool implementation here — the frontend renders a time
    picker, the user's choice is forwarded back to the agent as the tool result.
    
    This mirrors the langgraph-python reference (hitl_in_chat_agent.py) but
    adapted to ADK: ADK doesn't need an explicit tool stub on the backend for
    frontend-defined tools — the ag-ui-adk middleware injects the frontend's
    tool list at request time.
    """
    
    from __future__ import annotations
    
    from google.adk.agents import LlmAgent
    from ag_ui_adk import AGUIToolset
    
    from agents.shared_chat import get_model, stop_on_terminal_text
    
    _INSTRUCTION = (
        "You help users book an onboarding call with the sales team. "
        "When they ask to book a call, call the frontend-provided "
        "`book_call` tool with a short topic and the user's name. "
        "Keep any chat reply to one short sentence."
    )
    
    hitl_in_chat_book_call_agent = LlmAgent(
        name="HitlInChatBookCallAgent",
        model=get_model(),
        instruction=_INSTRUCTION,
        tools=[AGUIToolset()],
        after_model_callback=stop_on_terminal_text,
    )
    

See this in Inspector

Open Inspector on localhost. Go to **Agents** , then **Frontend Tools**. Your tool and its schema are listed.

More detail: [Inspector](https://docs.copilotkit.ai/slack/google-adk/inspector).

## What is this?#

Human-in-the-loop (HITL) lets an agent pause mid-run to collect input, confirmation, or a choice from the user, then resume with that answer folded back into its reasoning. It's what turns an autonomous workflow into a collaborative one: the agent keeps its context, the user keeps the steering wheel.

## When should I use this?#

Use HITL when you need:

  * **Quality control** — a human gate at high-stakes decision points
  * **Edge cases** — graceful fallbacks when the agent's confidence is low
  * **Expert input** — lean on the user for domain knowledge the model lacks
  * **Reliability** — a more robust loop for real-world, production traffic



## Two patterns for HITL in CopilotKit#

### Install the ADK + AG-UI bridge
    
    
    pip install ag-ui-adk

### Add `AGUIToolset()` to your agent

Tool-based HITL (`useHumanInTheLoop`) registers the picker UI on the frontend; CopilotKit forwards the tool definition to your model through `AGUIToolset()`. ADK doesn't have a native `interrupt(...)` primitive like LangGraph — for graph-paused pauses, use the frontend Promise-based `useFrontendTool` pattern instead.

hitl_in_chat_agent.py
    
    
    from google.adk.agents import LlmAgent
    from ag_ui_adk import AGUIToolset
    
    from agents.shared_chat import get_model, stop_on_terminal_text
    
    # CopilotKit wires into ADK via the `AGUIToolset()` tool: pass it in the
    # `tools=` list of your `LlmAgent` to expose CopilotKit's frontend-tool
    # channel to the model. `stop_on_terminal_text` is a small ADK callback
    # that lets CopilotKit's UI know when the agent has finished its turn.
    _INSTRUCTION = (
        "You are a planning assistant. When the user asks you to plan something, "
        "always call generate_task_steps with the proposed list of steps (each "
        "with description + status='enabled'). The frontend will render the "
        "steps inline and the user will confirm or reject — your job is to plan "
        "and call the tool, then summarise the user's decision once they "
        "respond."
    )
    
    hitl_in_chat_agent = LlmAgent(
        name="HitlInChatAgent",
        model=get_model(),
        instruction=_INSTRUCTION,
        tools=[AGUIToolset()],
        after_model_callback=stop_on_terminal_text,
    )

CopilotKit ships two complementary ways to pause an agent turn and ask the human something. They look similar from the outside (the chat pauses, a custom component appears, the user answers, the run resumes) but they're wired differently on the backend, and each has its own niche.

Pattern| Who decides to pause?| Backend surface  
---|---|---  
`useHumanInTheLoop`| The **LLM** , by calling a registered client-side tool| A frontend-only tool description (Zod schema + `render`)  
`useInterrupt`| The **graph** , by calling `interrupt(...)` during a node| A server-side `interrupt()` call in your LangGraph agent  
  
**Pick`useHumanInTheLoop`** when the pause is an _agent-initiated_ decision — the model chose to ask the user — and you want the picker UI inlined into the normal tool-call flow.

**Pick`useInterrupt`** when the pause is a _graph-enforced_ checkpoint — the code path deterministically requires a human answer — and you want `langgraph.interrupt()` as the server-side contract.

## Pattern 1 — `useHumanInTheLoop` (tool-based)#

The agent registers a HITL tool on the client with `useHumanInTheLoop`. When the LLM calls that tool, CopilotKit routes the call through your `render` function, which shows a custom component and calls `respond` with the user's answer. The agent sees the answer as the tool result and continues from there.

page.tsx
    
    
    import React from "react";import {  CopilotKit,  CopilotChat,  useHumanInTheLoop,  useConfigureSuggestions,} from "@copilotkit/react-core/v2";import { z } from "zod";import { TimePickerCard, TimeSlot } from "./time-picker-card";const DEFAULT_SLOTS: TimeSlot[] = [  { label: "Tomorrow 10:00 AM", iso: "2026-04-19T10:00:00-07:00" },  { label: "Tomorrow 2:00 PM", iso: "2026-04-19T14:00:00-07:00" },  { label: "Monday 9:00 AM", iso: "2026-04-21T09:00:00-07:00" },  { label: "Monday 3:30 PM", iso: "2026-04-21T15:30:00-07:00" },];export default function HitlInChatDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent="hitl-in-chat">      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  useConfigureSuggestions({    suggestions: [      {        title: "Book a call with sales",        message:          "Please book an intro call with the sales team to discuss pricing.",      },      {        title: "Schedule a 1:1 with Alice",        message: "Schedule a 1:1 with Alice next week to review Q2 goals.",      },    ],    available: "always",  });  useHumanInTheLoop({    agentId: "hitl-in-chat",    name: "book_call",    description:      "Ask the user to pick a time slot for a call. The picker UI presents fixed candidate slots; the user's choice is returned to the agent.",    parameters: z.object({      topic: z        .string()        .describe("What the call is about (e.g. 'Intro with sales')"),      attendee: z        .string()        .describe("Who the call is with (e.g. 'Alice from Sales')"),    }),    render: ({ args, status, respond }: any) => (      <TimePickerCard        topic={args?.topic ?? "a call"}        attendee={args?.attendee}        slots={DEFAULT_SLOTS}        status={status}        onSubmit={(result) => respond?.(result)}      />    ),  });

The picker UI is fed a static list of candidate slots — this is just data the demo page owns, so you can swap in real availability, a calendar API, or anything else:

page.tsx
    
    
    import React from "react";import {  CopilotKit,  CopilotChat,  useHumanInTheLoop,  useConfigureSuggestions,} from "@copilotkit/react-core/v2";import { z } from "zod";import { TimePickerCard, TimeSlot } from "./time-picker-card";const DEFAULT_SLOTS: TimeSlot[] = [  { label: "Tomorrow 10:00 AM", iso: "2026-04-19T10:00:00-07:00" },  { label: "Tomorrow 2:00 PM", iso: "2026-04-19T14:00:00-07:00" },  { label: "Monday 9:00 AM", iso: "2026-04-21T09:00:00-07:00" },  { label: "Monday 3:30 PM", iso: "2026-04-21T15:30:00-07:00" },];

## Pattern 2 — `useInterrupt` (graph-paused)#

With LangGraph's `interrupt()` the pause is enforced by the graph itself: a node calls `interrupt({...})`, the run suspends, the client receives the payload, renders a UI, and resumes the run with the user's answer. CopilotKit's `useInterrupt` hook is the render contract.

See the [`useInterrupt` deep dive](https://docs.copilotkit.ai/slack/google-adk/human-in-the-loop/useInterrupt) for the full walkthrough, including the backend tool and render-prop wiring.

DemoCode

interrupt_agent.py

page.tsx

time-picker-card.tsx

route.ts
    
    
    """ADK scheduling agent backing the gen-ui-interrupt demo (Strategy-B).In langgraph-python the gen-ui-interrupt demo relies on the native`interrupt()` primitive with checkpoint/resume. ADK has no such primitive,so we adapt with the same "Strategy B" pattern used by the agno andms-agent-framework ports: the agent's instruction tells Gemini to call the`schedule_meeting` tool, but NO backend tool is registered. CopilotKit's`AGUIToolset()` injects the frontend-registered `schedule_meeting`(`useHumanInTheLoop` in src/app/demos/gen-ui-interrupt/page.tsx) into themodel's tool list; the model's call is routed to the frontend, which rendersthe time-picker inline and resolves the call once the user picks a slot —equivalent to `interrupt()` in the LangGraph reference.`after_model_callback=stop_on_terminal_text` is the canonical ADK terminalguard (see shared_chat.py): without it the configured Gemini model(from `get_model()`) re-issues the same tool call indefinitely after thefrontend tool resolves."""from __future__ import annotations# region: setupfrom google.adk.agents import LlmAgentfrom ag_ui_adk import AGUIToolsetfrom agents.shared_chat import get_model, stop_on_terminal_text_INSTRUCTION = (    "You are a scheduling assistant. Whenever the user asks you to book a "    "call or schedule a meeting, you MUST call the `schedule_meeting` tool. "    "Pass a short `topic` describing the purpose of the meeting and, if "    "known, an `attendee` describing who the meeting is with.\n\n"    "The `schedule_meeting` tool is implemented on the client: it surfaces a "    "time-picker UI and returns the user's selection. After the tool "    "returns, briefly confirm whether the meeting was scheduled and at what "    "time, or note that the user cancelled. Do NOT ask for approval "    "yourself — always call the tool and let the picker handle the decision. "    "Keep responses short and friendly, and always send a brief final "    "assistant message summarising what happened so it persists.")interrupt_agent = LlmAgent(    name="InterruptAgent",    model=get_model(),    instruction=_INSTRUCTION,    # No backend tools. `schedule_meeting` is registered on the frontend via    # useHumanInTheLoop; AGUIToolset() exposes CopilotKit's frontend-tool    # channel to the model.    tools=[AGUIToolset()],    after_model_callback=stop_on_terminal_text,)# endregion

## Going headless#

Both patterns above ship with a `render` prop — CopilotKit handles the "when to show the picker" logic for you. If you want to drive interrupt resolution from a custom UI that lives anywhere in the tree (not necessarily inside a chat), see the [headless interrupts guide](https://docs.copilotkit.ai/slack/google-adk/human-in-the-loop/headless) — it shows how to compose `useAgent`, `agent.subscribe`, and `copilotkit.runAgent` to build your own `useInterrupt` equivalent.

### On this page

What is this?When should I use this?Two patterns for HITL in CopilotKitPattern 1 — useHumanInTheLoop (tool-based)Pattern 2 — useInterrupt (graph-paused)Going headless
