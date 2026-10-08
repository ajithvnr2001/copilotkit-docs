---
url: https://docs.copilotkit.ai/strands/generative-ui/interactive/
title: Interactive components
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:31:24.689124+00:00
---

# Interactive components

> Source: https://docs.copilotkit.ai/strands/generative-ui/interactive/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAWS Strands (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/strands)[Quickstart](https://docs.copilotkit.ai/strands/quickstart)[Build with agents](https://docs.copilotkit.ai/strands/build-with-agents)[Intelligence](https://docs.copilotkit.ai/strands/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/strands/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/strands/webmcp)

Agent capabilities

AWS Strands (Python)

[Sub-agents](https://docs.copilotkit.ai/strands/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/strands/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/strands/learning)

[User Memories](https://docs.copilotkit.ai/strands/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/strands/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/strands/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/strands/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/strands/intelligence/analytics)[Channels](https://docs.copilotkit.ai/strands/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/strands/telemetry)[Community frameworks](https://docs.copilotkit.ai/strands/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[AWS Strands (Python)](https://docs.copilotkit.ai/strands)[Build Generative UI](https://docs.copilotkit.ai/strands/generative-ui)

# Interactive components

Create approval flows where the agent pauses and waits for human input.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

interrupt_agent.py

page.tsx

time-picker-card.tsx

route.ts
    
    
    """Dedicated Strands agent for the two interrupt demos.`schedule_meeting` pauses itself through Strands' native interrupt system:`tool_context.interrupt(...)` halts the agent loop and the AG-UI bridge finishesthe run with `RUN_FINISHED` carrying `outcome.type == "interrupt"`. The frontendrenders the time picker from the interrupt payload and resuming on the same`thread_id` returns the user's choice to that same `interrupt()` call, so thetool body continues where it left off.The resume payload arrives wrapped: a resolved answer as `{"response": ...}`, aclient-side cancel as `{"cancelled": True}`. The bridge wraps it becauseStrands' resume gate is truthiness-based, and a bare falsy answer would re-raisethe same interrupt forever.This is a dedicated agent rather than a tool on the shared showcase agentbecause the shared agent already owns a `schedule_meeting` that answers straightaway. One tool name cannot both answer immediately for the other demos and pausefor these two, so the pausing version gets its own mount.Pause and resume happen in the same process here, so no `SessionManager` isneeded. Durable resume across a restart requires one.Docs: https://strandsagents.com/docs/user-guide/concepts/interrupts/"""from __future__ import annotationsfrom collections.abc import Mappingfrom strands import Agent, toolfrom strands.types.tools import ToolContextfrom ag_ui_strands import StrandsAgentfrom agents.agent import _build_modelSYSTEM_PROMPT = """You are a scheduling assistant.Whenever the user asks you to book a call or schedule a meeting, you MUST callthe `schedule_meeting` tool. Pass a short `topic` describing the purpose and, ifknown, an `attendee` describing who the meeting is with.The tool pauses execution and shows the user a time picker. Once it resumes withtheir choice, briefly confirm whether the meeting was scheduled and at whattime, or note that the user cancelled. Do not ask for approval yourself: alwayscall the tool and let the picker handle the decision. Keep responses short andfriendly.Never claim a meeting is scheduled unless the tool result says so."""@tool(context=True)def schedule_meeting(topic: str, tool_context: ToolContext, attendee: str = "") -> str:    """Ask the user to pick a meeting time, then confirm what was scheduled.    Args:        topic: Short description of the meeting purpose.        attendee: Who the meeting is with, if known.    """    answer = tool_context.interrupt(        "schedule_meeting",        reason={"topic": topic, "attendee": attendee},    )    # Neither the envelope nor the value inside it is guaranteed to be a    # mapping: `ag_ui_strands` wraps a resolved answer as `{"response": ...}`    # and a cancel as `{"cancelled": True}`, but the payload itself is whatever    # the client sent, and a client that answers with a bare value would make    # `answer.get` raise inside the tool. Both levels are checked.    envelope: Mapping = answer if isinstance(answer, Mapping) else {}    # `ag_ui_strands` wraps the answer under "response"; a bridge that passes    # the client payload through (the published TypeScript one does) hands the    # payload itself, so a mapping without that key IS the payload.    inner = envelope["response"] if "response" in envelope else envelope    payload = inner if isinstance(inner, Mapping) else {}    cancelled = (        envelope.get("cancelled")        or envelope.get("status") == "cancelled"        or payload.get("cancelled")        or payload.get("status") == "cancelled"    )    if cancelled:        return f"User cancelled. Meeting NOT scheduled: {topic}"    label = payload.get("chosen_label") or payload.get("chosen_time")    if not label:        return f"User did not pick a time. Meeting NOT scheduled: {topic}"    return f"Meeting scheduled for {label}: {topic}"def build_interrupt_agent() -> StrandsAgent:    """Construct the StrandsAgent backing gen-ui-interrupt and interrupt-headless."""    strands_agent = Agent(        model=_build_model(),        system_prompt=SYSTEM_PROMPT,        tools=[schedule_meeting],    )    return StrandsAgent(        agent=strands_agent,        name="interrupt",        description=(            "Strands agent whose scheduling tool pauses natively for the user "            "to pick a time"        ),    )

## What is this?#

Interactive generative UI creates flows where the agent pauses execution and waits for user input before continuing. This enables approval workflows, confirmation dialogs, and any scenario where human judgment is needed mid-execution.

## When should I use this?#

Use interactive generative UI when you need:

  * Approval/rejection flows (e.g. "Run this command?")
  * User decisions that the agent should know about
  * Confirmation dialogs with structured responses
  * Any flow where the agent pauses for human judgment



## How it works in code#

### Pause a tool with Strands' native interrupt

AWS Strands ships a first-class [interrupt primitive](https://strandsagents.com/docs/user-guide/concepts/interrupts/). A tool declared with `@tool(context=True)` calls `tool_context.interrupt(name, reason=...)`, which halts the agent loop and hands `reason` to the client as the interrupt payload. The AG-UI adapter finishes the run with `RUN_FINISHED` carrying `outcome.type == "interrupt"`.

src/agents/interrupt_agent.py
    
    
    @tool(context=True)
    def schedule_meeting(topic: str, tool_context: ToolContext, attendee: str = "") -> str:
        """Ask the user to pick a meeting time, then confirm what was scheduled.
    
        Args:
            topic: Short description of the meeting purpose.
            attendee: Who the meeting is with, if known.
        """
        answer = tool_context.interrupt(
            "schedule_meeting",
            reason={"topic": topic, "attendee": attendee},
        )
    
        # Neither the envelope nor the value inside it is guaranteed to be a
        # mapping: `ag_ui_strands` wraps a resolved answer as `{"response": ...}`
        # and a cancel as `{"cancelled": True}`, but the payload itself is whatever
        # the client sent, and a client that answers with a bare value would make
        # `answer.get` raise inside the tool. Both levels are checked.
        envelope: Mapping = answer if isinstance(answer, Mapping) else {}
        # `ag_ui_strands` wraps the answer under "response"; a bridge that passes
        # the client payload through (the published TypeScript one does) hands the
        # payload itself, so a mapping without that key IS the payload.
        inner = envelope["response"] if "response" in envelope else envelope
        payload = inner if isinstance(inner, Mapping) else {}
        cancelled = (
            envelope.get("cancelled")
            or envelope.get("status") == "cancelled"
            or payload.get("cancelled")
            or payload.get("status") == "cancelled"
        )
        if cancelled:
            return f"User cancelled. Meeting NOT scheduled: {topic}"
    
        label = payload.get("chosen_label") or payload.get("chosen_time")
        if not label:
            return f"User did not pick a time. Meeting NOT scheduled: {topic}"
        return f"Meeting scheduled for {label}: {topic}"
    
    

The resume payload arrives wrapped: an answer as `{"response": ...}`, a client-side cancel as `{"cancelled": True}`. The adapter wraps it because Strands' resume gate is truthiness-based, so a bare falsy answer would re-raise the same interrupt forever.

### Keep the pausing tool off a client-executed name

`useHumanInTheLoop` registers its tool on the FRONTEND, so a name used there cannot also be a pausing backend tool. This showcase mounts a dedicated interrupt agent and points the interrupt demos' agent names at it, leaving `schedule_meeting` on the shared agent free for the frontend-tool flow.

### Resume in the same process, or across a restart

Pause and resume on the same running process need no extra wiring. For a resume that survives a restart, give the agent a Strands `SessionManager` through `StrandsAgentConfig.session_manager_provider`; the adapter persists its interrupt checkpoint into that session.

On the frontend, register an interrupt renderer with `useInterrupt`. When the agent pauses, your component mounts inline in the chat, captures the user's choice, and resumes the run with that input.

page.tsx
    
    
    import {  CopilotKit,  CopilotChat,  useInterrupt,} from "@copilotkit/react-core/v2";import type { TimeSlot } from "./_components/time-picker-card";import { TimePickerCard } from "./_components/time-picker-card";import { generateFallbackSlots } from "../_shared/interrupt-fallback-slots";import { useGenUiInterruptSuggestions } from "./suggestions";// Shape the backend `schedule_meeting` tool pauses with: its `interrupt()`// `reason` payload. `slots` is absent on the Strands path (the tool passes only// topic and attendee), so the picker falls back to generated slots.type SchedulingPayload = {  topic?: string;  attendee?: string;  slots?: TimeSlot[];};// Read the tool's `interrupt()` reason off an AG-UI interrupt.//// The two bridges expose it on different channels: `ag_ui_strands` (Python)// carries the reason object under `metadata.reason`, while the published// `@ag-ui/aws-strands` 0.2.3 JSON-encodes it into `message` instead. Both are// read so one page serves both, and the legacy event value is read last for// adapters that pass the payload through unwrapped./** * JSON.parse that never throws and never returns a primitive. Both readers run * inside a React render callback, where a throw takes the whole pane down. */function parseObject(raw: string | undefined): Record<string, unknown> | null {  if (!raw) return null;  try {    const parsed: unknown = JSON.parse(raw);    return parsed && typeof parsed === "object"      ? (parsed as Record<string, unknown>)      : null;  } catch {    return null;  }}function readSchedulingPayload(  interrupt: { metadata?: unknown; message?: string } | null | undefined,  eventValue: unknown,): SchedulingPayload {  const metadata = interrupt?.metadata as    | { reason?: SchedulingPayload }    | undefined;  if (metadata?.reason && typeof metadata.reason === "object") {    return metadata.reason;  }  // The published TypeScript bridge JSON-encodes the reason into `message`  // instead of carrying it on metadata.  const decoded = parseObject(interrupt?.message);  if (decoded) {    const nested = (decoded as { reason?: SchedulingPayload }).reason;    return nested && typeof nested === "object"      ? nested      : (decoded as SchedulingPayload);  }  // Legacy channel: some adapters pass the payload through as the event value,  // JSON-encoded or not.  const legacy =    typeof eventValue === "string" ? parseObject(eventValue) : eventValue;  if (!legacy || typeof legacy !== "object") return {};  const wrapped = (legacy as { metadata?: { reason?: SchedulingPayload } })    .metadata?.reason;  if (wrapped && typeof wrapped === "object") return wrapped;  return legacy as SchedulingPayload;}export default function GenUiInterruptDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent="gen-ui-interrupt">      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  // The failure banner lives OUTSIDE the interrupt element on purpose. The hook  // caches the element it rendered, so a picker already on screen never sees an  // updated prop: a flag threaded into the card would keep showing a stale  // failure on the NEXT booking, before that booking's resume has even started.  const [resumeFailed, setResumeFailed] = useState(false);  return (    <div className="flex h-full flex-col">      {resumeFailed && (        <div          role="alert"          data-testid="time-picker-resume-error"          className="m-4 rounded-lg border border-red-200 bg-red-50 p-3 text-sm text-red-800"        >          Your previous selection could not be sent. Please try booking again.        </div>      )}      <div className="min-h-0 flex-1">        <InterruptChat setResumeFailed={setResumeFailed} />      </div>    </div>  );}function InterruptChat({  setResumeFailed,}: {  setResumeFailed: (failed: boolean) => void;}) {  useGenUiInterruptSuggestions();  // Native interrupt path. The backend `schedule_meeting` tool calls Strands'  // `tool_context.interrupt(...)`; the @ag-ui/aws-strands bridge finishes the  // run with `outcome.type === "interrupt"` and carries the tool's `reason`  // under the interrupt's `metadata.reason`. `resolve(...)` resumes the same  // Strands run, handing the selection back to that `interrupt()` call.  useInterrupt({    agentId: "gen-ui-interrupt",    renderInChat: true,    render: ({ event, interrupt, resolve }) => {      const payload = readSchedulingPayload(interrupt, event.value);      const slots =        payload.slots && payload.slots.length > 0          ? payload.slots          : generateFallbackSlots();      return (        <TimePickerCard          topic={payload.topic ?? "a call"}          attendee={payload.attendee}          slots={slots}          onSubmit={(result) => {            setResumeFailed(false);            // Defer resolve so React commits the picked/cancelled badge before            // useInterrupt clears the interrupt element (a single rAF is not            // reliable: it can fire before React's commit). The rejection is            // re-surfaced rather than dropped, because the card has already            // shown a green "Booked" badge by then and a silently failed            // resume would leave the user reading a success that never            // happened.            window.setTimeout(() => {              void resolve(result).catch((error: unknown) => {                setResumeFailed(true);                queueMicrotask(() => {                  throw error;                });              });            }, 500);          }}        />      );    },  });

On the backend, the agent calls into the interrupt primitive and waits for the resumed response before continuing the graph.

interrupt_agent.py
    
    
    @tool(context=True)def schedule_meeting(topic: str, tool_context: ToolContext, attendee: str = "") -> str:    """Ask the user to pick a meeting time, then confirm what was scheduled.    Args:        topic: Short description of the meeting purpose.        attendee: Who the meeting is with, if known.    """    answer = tool_context.interrupt(        "schedule_meeting",        reason={"topic": topic, "attendee": attendee},    )    # Neither the envelope nor the value inside it is guaranteed to be a    # mapping: `ag_ui_strands` wraps a resolved answer as `{"response": ...}`    # and a cancel as `{"cancelled": True}`, but the payload itself is whatever    # the client sent, and a client that answers with a bare value would make    # `answer.get` raise inside the tool. Both levels are checked.    envelope: Mapping = answer if isinstance(answer, Mapping) else {}    # `ag_ui_strands` wraps the answer under "response"; a bridge that passes    # the client payload through (the published TypeScript one does) hands the    # payload itself, so a mapping without that key IS the payload.    inner = envelope["response"] if "response" in envelope else envelope    payload = inner if isinstance(inner, Mapping) else {}    cancelled = (        envelope.get("cancelled")        or envelope.get("status") == "cancelled"        or payload.get("cancelled")        or payload.get("status") == "cancelled"    )    if cancelled:        return f"User cancelled. Meeting NOT scheduled: {topic}"    label = payload.get("chosen_label") or payload.get("chosen_time")    if not label:        return f"User did not pick a time. Meeting NOT scheduled: {topic}"    return f"Meeting scheduled for {label}: {topic}"
