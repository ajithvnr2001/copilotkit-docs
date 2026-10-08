---
url: https://docs.copilotkit.ai/strands-typescript/human-in-the-loop/headless/
title: Headless Interrupts
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:29:49.701420+00:00
---

# Headless Interrupts

> Source: https://docs.copilotkit.ai/strands-typescript/human-in-the-loop/headless/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAWS Strands (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/strands-typescript)[Quickstart](https://docs.copilotkit.ai/strands-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/strands-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/strands-typescript/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/strands-typescript/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[HITL Overview](https://docs.copilotkit.ai/strands-typescript/human-in-the-loop/index)[Pausing the Agent for Input](https://docs.copilotkit.ai/strands-typescript/human-in-the-loop/useInterrupt)[Headless Interrupts](https://docs.copilotkit.ai/strands-typescript/human-in-the-loop/headless)[Governed Action Approval UI](https://docs.copilotkit.ai/strands-typescript/human-in-the-loop/governed-actions)

[WebMCP](https://docs.copilotkit.ai/strands-typescript/webmcp)

Agent capabilities

AWS Strands (TypeScript)

[Sub-agents](https://docs.copilotkit.ai/strands-typescript/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/strands-typescript/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/strands-typescript/learning)

[User Memories](https://docs.copilotkit.ai/strands-typescript/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/strands-typescript/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/strands-typescript/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/strands-typescript/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/strands-typescript/intelligence/analytics)[Channels](https://docs.copilotkit.ai/strands-typescript/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/strands-typescript/telemetry)[Community frameworks](https://docs.copilotkit.ai/strands-typescript/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

InteractivityHuman-in-the-loop

# Headless Interrupts

Resolve agent interrupts from any UI, without a useInterrupt render slot.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

interrupt-agent.ts

page.tsx

route.ts
    
    
    /** * Dedicated Strands agent for the two interrupt demos. * * Mirrors the Python sibling's `agents/interrupt_agent.py`. * * `schedule_meeting` pauses itself through Strands' native interrupt system: * `context.interrupt(...)` halts the agent loop and the AG-UI bridge finishes * the run with `RUN_FINISHED` carrying `outcome.type === "interrupt"`. The * frontend renders the time picker from the interrupt payload, and resuming on * the same `threadId` returns the user's choice to that same `interrupt()` * call, so the tool body continues where it left off. * * How the resume payload arrives depends on the bridge, so the tool normalises * both shapes (see `readResume`): the pinned `@ag-ui/aws-strands` 0.2.3 passes * the client's payload through and cancels with `{ status: "cancelled" }`, * while the Python bridge wraps a resolved answer as `{ response: ... }` and * cancels with `{ cancelled: true }`. * * This is a dedicated agent rather than a tool on the shared showcase agent * because the shared agent already owns a `schedule_meeting` that answers * straight away. One tool name cannot both answer immediately for the other * demos and pause for these two, so the pausing version gets its own mount. * * Pause and resume happen in the same process here, so no `SessionManager` is * needed. Durable resume across a restart requires one. * * Docs: https://strandsagents.com/docs/user-guide/concepts/interrupts/ */import { Agent, tool } from "@strands-agents/sdk";import { z } from "zod";import { StrandsAgent } from "@ag-ui/aws-strands";import { createModel } from "./model-factory";/** What the picker sends back. */interface MeetingChoice {  chosen_time?: string;  chosen_label?: string;  cancelled?: boolean;  status?: string;}/** * What the bridge hands a resumed tool. Two shapes are in circulation: * * - `@ag-ui/aws-strands` 0.2.3 (the pinned release) passes the client's payload *   through untouched, and signals a cancel as `{ status: "cancelled" }`. * - `ag_ui_strands` (Python) wraps it as `{ response: payload }`, and signals a *   cancel as `{ cancelled: true }`. * * Reading only one of them silently mis-reports the other: a resolved pick * arrives with no recognised answer and the tool tells the model the user never * picked a time. */interface ResumeEnvelope {  /** `null` when the client answered with no payload at all. */  response?: MeetingChoice | null;  cancelled?: boolean;  status?: string;}/** Normalise both envelope shapes to `{ choice, cancelled }`. */export function readResume(  answer: ResumeEnvelope | MeetingChoice | null | undefined,): {  choice: MeetingChoice;  cancelled: boolean;} {  const envelope: ResumeEnvelope =    answer && typeof answer === "object" ? answer : {};  const inner =    "response" in envelope      ? envelope.response      : (answer as MeetingChoice | null | undefined);  const choice: MeetingChoice = inner && typeof inner === "object" ? inner : {};  const cancelled = Boolean(    envelope.cancelled ||    envelope.status === "cancelled" ||    choice.cancelled ||    choice.status === "cancelled",  );  return { choice, cancelled };}export const scheduleMeeting = tool({  name: "schedule_meeting",  description:    "Ask the user to pick a meeting time, then confirm what was scheduled.",  inputSchema: z.object({    topic: z.string().describe("Short description of the meeting purpose."),    attendee: z.string().optional().describe("Who the meeting is with."),  }),  callback: ({ topic, attendee }, context) => {    // Typed optional by the SDK, so this is checked rather than asserted: with    // no context there is nothing to pause on, and pretending otherwise would    // schedule a meeting the user never saw.    if (!context) {      throw new Error("schedule_meeting needs a tool context to pause on");    }    // `attendee` is optional and the reason has to be JSON, which has no    // `undefined`, so it is omitted rather than sent as undefined.    const answer = context.interrupt<ResumeEnvelope>({      name: "schedule_meeting",      reason: attendee === undefined ? { topic } : { topic, attendee },    });    // Three cancel shapes reach here: each bridge's own sentinel for a    // cancelled resume entry, and the picker's Cancel button, which resolves    // with a `cancelled` flag inside the payload.    const { choice, cancelled } = readResume(answer);    if (cancelled) {      return `User cancelled. Meeting NOT scheduled: ${topic}`;    }    const label = choice.chosen_label || choice.chosen_time;    return label      ? `Meeting scheduled for ${label}: ${topic}`      : `User did not pick a time. Meeting NOT scheduled: ${topic}`;  },});const SYSTEM_PROMPT = `You are a scheduling assistant.Whenever the user asks you to book a call or schedule a meeting, you MUST callthe \`schedule_meeting\` tool. Pass a short \`topic\` describing the purpose and,if known, an \`attendee\` describing who the meeting is with.The tool pauses execution and shows the user a time picker. Once it resumes withtheir choice, briefly confirm whether the meeting was scheduled and at whattime, or note that the user cancelled. Do not ask for approval yourself: alwayscall the tool and let the picker handle the decision. Keep responses short andfriendly.Never claim a meeting is scheduled unless the tool result says so.`;/** Build the agent backing gen-ui-interrupt and interrupt-headless. */export async function buildInterruptAgent(): Promise<StrandsAgent> {  return new StrandsAgent({    agent: new Agent({      model: await createModel(),      systemPrompt: SYSTEM_PROMPT,      tools: [scheduleMeeting],    }),    name: "interrupt",    description:      "Strands agent whose scheduling tool pauses natively for the user to pick a time",  });}

## What is this?#

`useInterrupt`'s `render` callback is the 80% path: it keeps the UI glued to a `<CopilotChat>` transcript and handles "when to show the picker" logic for you. This page covers the escape hatch: a **render-less** interrupt resolver you assemble from the same primitives `useInterrupt` uses internally — a pattern that lives anywhere in your React tree, takes any shape you like (button grid, form, modal, keyboard shortcut), and resolves the interrupt without mounting a chat at all.

The underlying primitive is the framework's own interrupt call. How it reaches the client depends on the bridge, and there are two headless shapes to match:

  * A bridge that surfaces the pause as an `on_interrupt` custom event (LangGraph): subscribe to that event and resume the run by calling `copilotkit.runAgent({...})` with the matching `resume` payload.
  * A bridge that finishes the run with a standard AG-UI interrupt outcome (AWS Strands): the run's final `RUN_FINISHED` carries `outcome: { type: "interrupt", interrupts: [...] }`. Call `useInterrupt` with `renderInChat: false` and place the element it returns wherever you like; `resolve(...)` resumes the run.



Either way, no chat surface is required.

## When should I use this?#

  * **Testing / Playwright fixtures** — a deterministic, chat-less button grid is easier to drive than a chat surface where the picker only appears after an LLM call.
  * **Non-chat UIs** — dashboards, side panels, inspector surfaces, or any place where you want the _agent's interrupt_ without the _chat transcript_.
  * **Custom flow control** — when you need to know exactly when the interrupt arrived (e.g. to gate other UI) and when it was resolved.
  * **Research / debugging** — when you want to observe the raw AG-UI custom events without the abstraction layer.



If you just want "a picker in chat", just use [`useInterrupt`](https://docs.copilotkit.ai/strands-typescript/human-in-the-loop/headless/useInterrupt).

## The primitives#

The simplest headless pattern uses `useInterrupt` with `renderInChat: false`. Instead of publishing the element into `<CopilotChat>`, the hook returns the interrupt element directly so you can place it anywhere in your tree:
    
    
    function ApprovalPanel() {
      const element = useInterrupt({
        renderInChat: false,
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
    
      // `element` is null while no interrupt is active; render it wherever you like.
      return <div className="approval-panel">{element}</div>;
    }

`interrupt` carries the primary AG-UI `Interrupt` object (`{ id, reason, message?, responseSchema?, expiresAt?, ... }`). `resolve(payload)` submits the user's response and resumes the agent. `cancel()` cancels the interrupt and resumes. Both return a `Promise<RunAgentResult | void>` — void while waiting on further interrupts when more than one is open.

Under the hood, `useInterrupt` composes two public APIs:

  1. **`agent.subscribe({ onCustomEvent, onRunStartedEvent, onRunFinishedEvent, onRunFinalized, onRunFailed })`** — every `AbstractAgent` exposes an AG-UI event subscription. Standard interrupts arrive on `onRunFinishedEvent` with `{ outcome: { type: "interrupt", interrupts: [...] } }`; legacy LangGraph interrupts arrive as a custom event named `on_interrupt`.
  2. **`copilotkit.runAgent({ agent, resume })`** (standard) or **`copilotkit.runAgent({ agent, forwardedProps: { command: { resume, interruptEvent } } })`** (legacy) — the same call `useInterrupt`'s `resolve()` / `cancel()` makes to resume a paused run.



What that region shows depends on the framework. Where the framework pauses with a legacy custom event, it is a hand-rolled hook over the raw subscription; where it pauses with a standard AG-UI interrupt, the same `useInterrupt` call with `renderInChat: false` is all that is needed, and the snippet shows that instead. Either way, the raw primitives remain available when you want full control (testing fixtures, custom accumulation logic):

page.tsx
    
    
    import React, { useEffect, useState } from "react";import {  CopilotKit,  CopilotChat,  useConfigureSuggestions,  useInterrupt,} from "@copilotkit/react-core/v2";import { generateFallbackSlots } from "../_shared/interrupt-fallback-slots";import type { TimeSlot } from "../_shared/interrupt-fallback-slots";type InterruptPayload = {  topic?: string;  attendee?: string;  slots?: TimeSlot[];};// Read the tool's `interrupt()` reason off an AG-UI interrupt.//// The two bridges expose it on different channels: `ag_ui_strands` (Python)// carries the reason object under `metadata.reason`, while the published// `@ag-ui/aws-strands` 0.2.3 JSON-encodes it into `message` instead. Both are// read so one page serves both, and the legacy event value is read last for// adapters that pass the payload through unwrapped./** * JSON.parse that never throws and never returns a primitive. Both readers run * inside a React render callback, where a throw takes the whole pane down. */function parseObject(raw: string | undefined): Record<string, unknown> | null {  if (!raw) return null;  try {    const parsed: unknown = JSON.parse(raw);    return parsed && typeof parsed === "object"      ? (parsed as Record<string, unknown>)      : null;  } catch {    return null;  }}function readInterruptPayload(  interrupt: { metadata?: unknown; message?: string } | null | undefined,  eventValue: unknown,): InterruptPayload {  const metadata = interrupt?.metadata as    | { reason?: InterruptPayload }    | undefined;  if (metadata?.reason && typeof metadata.reason === "object") {    return metadata.reason;  }  // The published TypeScript bridge JSON-encodes the reason into `message`  // instead of carrying it on metadata.  const decoded = parseObject(interrupt?.message);  if (decoded) {    const nested = (decoded as { reason?: InterruptPayload }).reason;    return nested && typeof nested === "object"      ? nested      : (decoded as InterruptPayload);  }  // Legacy channel: some adapters pass the payload through as the event value,  // JSON-encoded or not.  const legacy =    typeof eventValue === "string" ? parseObject(eventValue) : eventValue;  if (!legacy || typeof legacy !== "object") return {};  const wrapped = (legacy as { metadata?: { reason?: InterruptPayload } })    .metadata?.reason;  if (wrapped && typeof wrapped === "object") return wrapped;  return legacy as InterruptPayload;}export default function InterruptHeadlessDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent="interrupt-headless">      <Layout />    </CopilotKit>  );}function Layout() {  const [resolving, setResolving] = useState(false);  const interruptElement = useInterrupt({    agentId: "interrupt-headless",    renderInChat: false,    render: ({ event, interrupt, resolve }) => {      const payload = readInterruptPayload(interrupt, event.value);      const resumeAfterPaint = (response: unknown) => {        setResolving(true);        // A frame boundary lets React paint before resume unmounts the        // interrupt, but `requestAnimationFrame` never fires in a background        // tab, so a timer runs whichever comes first and the resume cannot be        // stranded. Fire-and-forget by design: a rejected resume is re-surfaced        // globally instead of disappearing.        let fired = false;        const resumeOnce = () => {          if (fired) return;          fired = true;          void resolve(response).then(            () => setResolving(false),            (error) => {              setResolving(false);              queueMicrotask(() => {                throw error;              });            },          );        };        requestAnimationFrame(resumeOnce);        window.setTimeout(resumeOnce, 100);      };      return (        <TimeSlotPopup          payload={payload}          onPick={(slot) => {            resumeAfterPaint({              chosen_time: slot.iso,              chosen_label: slot.label,            });          }}          onCancel={() => {            resumeAfterPaint({ cancelled: true });          }}        />      );    },  });  useEffect(() => {    if (interruptElement) {      setResolving(false);    }  }, [interruptElement]);  useConfigureSuggestions({    suggestions: [      {        title: "Book a call with sales",        message: "Book an intro call with the sales team to discuss pricing.",      },      {        title: "Schedule a 1:1 with Alice",        message: "Schedule a 1:1 with Alice next week to review Q2 goals.",      },    ],    available: "always",  });  return (    <div className="grid h-screen grid-cols-[1fr_420px] bg-[#FAFAFC]">      <AppSurface interruptElement={interruptElement} resolving={resolving} />      <div className="border-l border-[#DBDBE5] bg-white">        <CopilotChat agentId="interrupt-headless" className="h-full" />      </div>    </div>  );}

A few things the hand-rolled variant is careful about:

  * It stages the incoming event in a local ref and only commits it to React state on `onRunFinalized`, mirroring `useInterrupt`, which doesn't surface the interrupt until the run has actually paused (not just when the event fires mid-stream).
  * `onRunStartedEvent` clears any stale pending state, so kicking off a new turn always starts from a clean slate.
  * `onRunFailed` drops the staged event so a transport hiccup doesn't leave the UI stuck showing a picker for a run that never paused.



## Driving it from plain UI#

The preferred approach uses `useInterrupt` with `renderInChat: false` — no hand-rolled subscription, no `<CopilotChat>`, no render prop:
    
    
    function HeadlessInterruptPanel() {
      const { copilotkit } = useCopilotKit();
      const { agent } = useAgent({ agentId: "interrupt-headless" });
    
      const kickOff = (prompt: string) => {
        agent.addMessage({ id: crypto.randomUUID(), role: "user", content: prompt });
        void copilotkit.runAgent({ agent });
      };
    
      const interruptElement = useInterrupt({
        renderInChat: false,
        render: ({ interrupt, resolve, cancel }) => (
          <div>
            <p>Pick a slot for {interrupt?.message ?? "a call"}:</p>
            {SLOTS.map((s) => (
              <button key={s.iso} onClick={() => resolve({ chosen_time: s.iso, chosen_label: s.label })}>
                {s.label}
              </button>
            ))}
            <button onClick={() => cancel()}>Cancel</button>
          </div>
        ),
      });
    
      if (interruptElement) {
        return interruptElement;
      }
    
      return <button onClick={() => kickOff("Book a call with sales.")}>Book call</button>;
    }

If you need full control over the subscription (e.g. for a custom `useHeadlessInterrupt` fixture used in Playwright tests), you can still use the raw primitives from `useHeadlessInterrupt` defined above:
    
    
    function HeadlessInterruptPanelRaw() {
      const { copilotkit } = useCopilotKit();
      const { agent } = useAgent({ agentId: "interrupt-headless" });
      const { pending, resolve } = useHeadlessInterrupt("interrupt-headless");
    
      const kickOff = (prompt: string) => {
        agent.addMessage({ id: crypto.randomUUID(), role: "user", content: prompt });
        void copilotkit.runAgent({ agent });
      };
    
      if (pending) {
        return (
          <div>
            <p>Pick a slot for {pending.value.topic ?? "a call"}:</p>
            {SLOTS.map((s) => (
              <button key={s.iso} onClick={() => resolve({ chosen_time: s.iso, chosen_label: s.label })}>
                {s.label}
              </button>
            ))}
            <button onClick={() => resolve({ cancelled: true })}>Cancel</button>
          </div>
        );
      }
    
      return <button onClick={() => kickOff("Book a call with sales.")}>Book call</button>;
    }

## Going further#

  * [Tool-based HITL with `useHumanInTheLoop`](https://docs.copilotkit.ai/strands-typescript/human-in-the-loop/human-in-the-loop) — for LLM-initiated pauses where the model decides on the fly to ask the user, rather than the runtime forcing the pause itself.
  * [`useInterrupt`](https://docs.copilotkit.ai/strands-typescript/human-in-the-loop/headless/useInterrupt) — the render-prop version of this page, with `enabled` gating and `handler` preprocessing.


