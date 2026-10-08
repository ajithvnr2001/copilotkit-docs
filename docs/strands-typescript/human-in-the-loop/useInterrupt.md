---
url: https://docs.copilotkit.ai/strands-typescript/human-in-the-loop/useInterrupt/
title: Pausing the Agent for Input
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:29:49.882618+00:00
---

# Pausing the Agent for Input

> Source: https://docs.copilotkit.ai/strands-typescript/human-in-the-loop/useInterrupt/

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

# Pausing the Agent for Input

Pause an agent run mid-tool, hand control to a custom React component, and resume with the user's answer.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

interrupt-agent.ts

page.tsx

time-picker-card.tsx

route.ts
    
    
    /** * Dedicated Strands agent for the two interrupt demos. * * Mirrors the Python sibling's `agents/interrupt_agent.py`. * * `schedule_meeting` pauses itself through Strands' native interrupt system: * `context.interrupt(...)` halts the agent loop and the AG-UI bridge finishes * the run with `RUN_FINISHED` carrying `outcome.type === "interrupt"`. The * frontend renders the time picker from the interrupt payload, and resuming on * the same `threadId` returns the user's choice to that same `interrupt()` * call, so the tool body continues where it left off. * * How the resume payload arrives depends on the bridge, so the tool normalises * both shapes (see `readResume`): the pinned `@ag-ui/aws-strands` 0.2.3 passes * the client's payload through and cancels with `{ status: "cancelled" }`, * while the Python bridge wraps a resolved answer as `{ response: ... }` and * cancels with `{ cancelled: true }`. * * This is a dedicated agent rather than a tool on the shared showcase agent * because the shared agent already owns a `schedule_meeting` that answers * straight away. One tool name cannot both answer immediately for the other * demos and pause for these two, so the pausing version gets its own mount. * * Pause and resume happen in the same process here, so no `SessionManager` is * needed. Durable resume across a restart requires one. * * Docs: https://strandsagents.com/docs/user-guide/concepts/interrupts/ */import { Agent, tool } from "@strands-agents/sdk";import { z } from "zod";import { StrandsAgent } from "@ag-ui/aws-strands";import { createModel } from "./model-factory";/** What the picker sends back. */interface MeetingChoice {  chosen_time?: string;  chosen_label?: string;  cancelled?: boolean;  status?: string;}/** * What the bridge hands a resumed tool. Two shapes are in circulation: * * - `@ag-ui/aws-strands` 0.2.3 (the pinned release) passes the client's payload *   through untouched, and signals a cancel as `{ status: "cancelled" }`. * - `ag_ui_strands` (Python) wraps it as `{ response: payload }`, and signals a *   cancel as `{ cancelled: true }`. * * Reading only one of them silently mis-reports the other: a resolved pick * arrives with no recognised answer and the tool tells the model the user never * picked a time. */interface ResumeEnvelope {  /** `null` when the client answered with no payload at all. */  response?: MeetingChoice | null;  cancelled?: boolean;  status?: string;}/** Normalise both envelope shapes to `{ choice, cancelled }`. */export function readResume(  answer: ResumeEnvelope | MeetingChoice | null | undefined,): {  choice: MeetingChoice;  cancelled: boolean;} {  const envelope: ResumeEnvelope =    answer && typeof answer === "object" ? answer : {};  const inner =    "response" in envelope      ? envelope.response      : (answer as MeetingChoice | null | undefined);  const choice: MeetingChoice = inner && typeof inner === "object" ? inner : {};  const cancelled = Boolean(    envelope.cancelled ||    envelope.status === "cancelled" ||    choice.cancelled ||    choice.status === "cancelled",  );  return { choice, cancelled };}export const scheduleMeeting = tool({  name: "schedule_meeting",  description:    "Ask the user to pick a meeting time, then confirm what was scheduled.",  inputSchema: z.object({    topic: z.string().describe("Short description of the meeting purpose."),    attendee: z.string().optional().describe("Who the meeting is with."),  }),  callback: ({ topic, attendee }, context) => {    // Typed optional by the SDK, so this is checked rather than asserted: with    // no context there is nothing to pause on, and pretending otherwise would    // schedule a meeting the user never saw.    if (!context) {      throw new Error("schedule_meeting needs a tool context to pause on");    }    // `attendee` is optional and the reason has to be JSON, which has no    // `undefined`, so it is omitted rather than sent as undefined.    const answer = context.interrupt<ResumeEnvelope>({      name: "schedule_meeting",      reason: attendee === undefined ? { topic } : { topic, attendee },    });    // Three cancel shapes reach here: each bridge's own sentinel for a    // cancelled resume entry, and the picker's Cancel button, which resolves    // with a `cancelled` flag inside the payload.    const { choice, cancelled } = readResume(answer);    if (cancelled) {      return `User cancelled. Meeting NOT scheduled: ${topic}`;    }    const label = choice.chosen_label || choice.chosen_time;    return label      ? `Meeting scheduled for ${label}: ${topic}`      : `User did not pick a time. Meeting NOT scheduled: ${topic}`;  },});const SYSTEM_PROMPT = `You are a scheduling assistant.Whenever the user asks you to book a call or schedule a meeting, you MUST callthe \`schedule_meeting\` tool. Pass a short \`topic\` describing the purpose and,if known, an \`attendee\` describing who the meeting is with.The tool pauses execution and shows the user a time picker. Once it resumes withtheir choice, briefly confirm whether the meeting was scheduled and at whattime, or note that the user cancelled. Do not ask for approval yourself: alwayscall the tool and let the picker handle the decision. Keep responses short andfriendly.Never claim a meeting is scheduled unless the tool result says so.`;/** Build the agent backing gen-ui-interrupt and interrupt-headless. */export async function buildInterruptAgent(): Promise<StrandsAgent> {  return new StrandsAgent({    agent: new Agent({      model: await createModel(),      systemPrompt: SYSTEM_PROMPT,      tools: [scheduleMeeting],    }),    name: "interrupt",    description:      "Strands agent whose scheduling tool pauses natively for the user to pick a time",  });}

## What is this?#

`useInterrupt` lets your agent pause mid-run, hand control to the user through a custom React component, and resume with whatever the user returns. How that pause is implemented depends on the framework's runtime.

This framework ships a first-class interrupt primitive that lets running work suspend itself and hand control to the client ([LangGraph](https://docs.langchain.com/oss/python/langgraph/interrupts), [AWS Strands](https://strandsagents.com/docs/user-guide/concepts/interrupts/)). The run is frozen server-side until the client resolves the interrupt with a payload, at which point execution resumes as if the interrupt call had simply returned that payload.

CopilotKit's `useInterrupt` is the frontend half of that contract: it subscribes to the paused run, renders whatever component you give it, and calls the agent back with the user's answer.

## When should I use this?#

Reach for `useInterrupt` when the pause is a **graph-enforced checkpoint** where the code path _must_ stop and wait for a human, not an LLM-initiated tool call. Typical cases:

  * A sensitive action (payments, irreversible writes) must be approved
  * A required piece of state isn't known and can only be collected from the user
  * The agent explicitly reaches an approval node in a longer workflow
  * You want the server-side contract to be `interrupt(...)` and resume with a payload



For LLM-initiated pauses where the model decides on the fly to ask the user, prefer [`useHumanInTheLoop`](https://docs.copilotkit.ai/strands-typescript/human-in-the-loop/human-in-the-loop).

## The backend: `interrupt()` inside a tool#

### Pause a tool with Strands' native interrupt

AWS Strands ships a first-class [interrupt primitive](https://strandsagents.com/docs/user-guide/concepts/interrupts/). A tool's callback receives a context whose `interrupt({ name, reason })` call halts the agent loop and hands `reason` to the client as the interrupt payload. The AG-UI adapter finishes the run with `RUN_FINISHED` carrying `outcome.type === "interrupt"`.

src/agent/interrupt-agent.ts
    
    
    export const scheduleMeeting = tool({
      name: "schedule_meeting",
      description:
        "Ask the user to pick a meeting time, then confirm what was scheduled.",
      inputSchema: z.object({
        topic: z.string().describe("Short description of the meeting purpose."),
        attendee: z.string().optional().describe("Who the meeting is with."),
      }),
      callback: ({ topic, attendee }, context) => {
        // Typed optional by the SDK, so this is checked rather than asserted: with
        // no context there is nothing to pause on, and pretending otherwise would
        // schedule a meeting the user never saw.
        if (!context) {
          throw new Error("schedule_meeting needs a tool context to pause on");
        }
    
        // `attendee` is optional and the reason has to be JSON, which has no
        // `undefined`, so it is omitted rather than sent as undefined.
        const answer = context.interrupt<ResumeEnvelope>({
          name: "schedule_meeting",
          reason: attendee === undefined ? { topic } : { topic, attendee },
        });
    
        // Three cancel shapes reach here: each bridge's own sentinel for a
        // cancelled resume entry, and the picker's Cancel button, which resolves
        // with a `cancelled` flag inside the payload.
        const { choice, cancelled } = readResume(answer);
        if (cancelled) {
          return `User cancelled. Meeting NOT scheduled: ${topic}`;
        }
    
        const label = choice.chosen_label || choice.chosen_time;
        return label
          ? `Meeting scheduled for ${label}: ${topic}`
          : `User did not pick a time. Meeting NOT scheduled: ${topic}`;
      },
    });

How the answer reaches the tool depends on the adapter version. The pinned `@ag-ui/aws-strands` 0.2.3 hands the client's payload through untouched and signals a cancel as `{ status: "cancelled" }`; the Python adapter wraps an answer as `{ response: ... }` and cancels with `{ cancelled: true }`. Read both shapes, or a picked slot comes back to the model as though the user never picked one.

### Keep the pausing tool off a client-executed name

`useHumanInTheLoop` registers its tool on the FRONTEND, so a name used there cannot also be a pausing backend tool. This showcase mounts a dedicated interrupt agent and points the interrupt demos' agent names at it, leaving `schedule_meeting` on the shared agent free for the frontend-tool flow.

### Resume in the same process, or across a restart

Pause and resume on the same running process need no extra wiring. For a resume that survives a restart, give the agent a Strands `SessionManager` through `StrandsAgentConfig.sessionManagerProvider`; the adapter persists its interrupt checkpoint into that session.

The example agent exposes a `schedule_meeting` tool. When the model calls it, the tool interrupts itself with the meeting context. The run freezes here until the client resolves; the resolution becomes the return value of the interrupt call, which the tool then turns into a final string for the model:

interrupt-agent.ts
    
    
    export const scheduleMeeting = tool({  name: "schedule_meeting",  description:    "Ask the user to pick a meeting time, then confirm what was scheduled.",  inputSchema: z.object({    topic: z.string().describe("Short description of the meeting purpose."),    attendee: z.string().optional().describe("Who the meeting is with."),  }),  callback: ({ topic, attendee }, context) => {    // Typed optional by the SDK, so this is checked rather than asserted: with    // no context there is nothing to pause on, and pretending otherwise would    // schedule a meeting the user never saw.    if (!context) {      throw new Error("schedule_meeting needs a tool context to pause on");    }    // `attendee` is optional and the reason has to be JSON, which has no    // `undefined`, so it is omitted rather than sent as undefined.    const answer = context.interrupt<ResumeEnvelope>({      name: "schedule_meeting",      reason: attendee === undefined ? { topic } : { topic, attendee },    });    // Three cancel shapes reach here: each bridge's own sentinel for a    // cancelled resume entry, and the picker's Cancel button, which resolves    // with a `cancelled` flag inside the payload.    const { choice, cancelled } = readResume(answer);    if (cancelled) {      return `User cancelled. Meeting NOT scheduled: ${topic}`;    }    const label = choice.chosen_label || choice.chosen_time;    return label      ? `Meeting scheduled for ${label}: ${topic}`      : `User did not pick a time. Meeting NOT scheduled: ${topic}`;  },});

Two things to note:

  * The payload (`{"topic": topic, "attendee": attendee}`) is what the frontend reads off the interrupt. Keep it a plain, serializable object. It's the "pause-time context" the UI needs to render. Where it lands depends on the bridge: LangGraph hands it to `render` as `event.value`, while a standard AG-UI interrupt carries it on the interrupt itself, either under `metadata` or JSON-encoded into `message`. Read the channels your bridge uses rather than assuming one.
  * The return-side contract (`{chosen_label, chosen_time}` or `{cancelled: true}`) is entirely yours. The client can send anything as the resolve payload; the tool is the one that gives it meaning.



## The frontend: `useInterrupt` render prop#

On the client you register a `useInterrupt` hook per agent. When the paused run arrives, `render` receives both the raw `event` and the `interrupt` itself, and `resolve(...)` is how you resume the run. Where the payload sits depends on how the framework pauses: a legacy custom-event interrupt carries it on `event.value`, while a standard AG-UI interrupt carries it on the `interrupt` (its `metadata`, or a JSON-encoded `message`, depending on the bridge). Read the channel your framework uses:

page.tsx
    
    
    import {  CopilotKit,  CopilotChat,  useInterrupt,} from "@copilotkit/react-core/v2";import type { TimeSlot } from "./_components/time-picker-card";import { TimePickerCard } from "./_components/time-picker-card";import { generateFallbackSlots } from "../_shared/interrupt-fallback-slots";import { useGenUiInterruptSuggestions } from "./suggestions";// Shape the backend `schedule_meeting` tool pauses with: its `interrupt()`// `reason` payload. `slots` is absent on the Strands path (the tool passes only// topic and attendee), so the picker falls back to generated slots.type SchedulingPayload = {  topic?: string;  attendee?: string;  slots?: TimeSlot[];};// Read the tool's `interrupt()` reason off an AG-UI interrupt.//// The two bridges expose it on different channels: `ag_ui_strands` (Python)// carries the reason object under `metadata.reason`, while the published// `@ag-ui/aws-strands` 0.2.3 JSON-encodes it into `message` instead. Both are// read so one page serves both, and the legacy event value is read last for// adapters that pass the payload through unwrapped./** * JSON.parse that never throws and never returns a primitive. Both readers run * inside a React render callback, where a throw takes the whole pane down. */function parseObject(raw: string | undefined): Record<string, unknown> | null {  if (!raw) return null;  try {    const parsed: unknown = JSON.parse(raw);    return parsed && typeof parsed === "object"      ? (parsed as Record<string, unknown>)      : null;  } catch {    return null;  }}function readSchedulingPayload(  interrupt: { metadata?: unknown; message?: string } | null | undefined,  eventValue: unknown,): SchedulingPayload {  const metadata = interrupt?.metadata as    | { reason?: SchedulingPayload }    | undefined;  if (metadata?.reason && typeof metadata.reason === "object") {    return metadata.reason;  }  // The published TypeScript bridge JSON-encodes the reason into `message`  // instead of carrying it on metadata.  const decoded = parseObject(interrupt?.message);  if (decoded) {    const nested = (decoded as { reason?: SchedulingPayload }).reason;    return nested && typeof nested === "object"      ? nested      : (decoded as SchedulingPayload);  }  // Legacy channel: some adapters pass the payload through as the event value,  // JSON-encoded or not.  const legacy =    typeof eventValue === "string" ? parseObject(eventValue) : eventValue;  if (!legacy || typeof legacy !== "object") return {};  const wrapped = (legacy as { metadata?: { reason?: SchedulingPayload } })    .metadata?.reason;  if (wrapped && typeof wrapped === "object") return wrapped;  return legacy as SchedulingPayload;}export default function GenUiInterruptDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent="gen-ui-interrupt">      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  // The failure banner lives OUTSIDE the interrupt element on purpose. The hook  // caches the element it rendered, so a picker already on screen never sees an  // updated prop: a flag threaded into the card would keep showing a stale  // failure on the NEXT booking, before that booking's resume has even started.  const [resumeFailed, setResumeFailed] = useState(false);  return (    <div className="flex h-full flex-col">      {resumeFailed && (        <div          role="alert"          data-testid="time-picker-resume-error"          className="m-4 rounded-lg border border-red-200 bg-red-50 p-3 text-sm text-red-800"        >          Your previous selection could not be sent. Please try booking again.        </div>      )}      <div className="min-h-0 flex-1">        <InterruptChat setResumeFailed={setResumeFailed} />      </div>    </div>  );}function InterruptChat({  setResumeFailed,}: {  setResumeFailed: (failed: boolean) => void;}) {  useGenUiInterruptSuggestions();  // Native interrupt path. The backend `schedule_meeting` tool calls Strands'  // `context.interrupt(...)`; the @ag-ui/aws-strands bridge finishes the run  // with `outcome.type === "interrupt"`. Where the tool's `reason` travels  // depends on the bridge version, so the reader below accepts both channels.  // `resolve(...)` resumes the same Strands run, handing the selection back to  // that `interrupt()` call.  useInterrupt({    agentId: "gen-ui-interrupt",    renderInChat: true,    render: ({ event, interrupt, resolve }) => {      const payload = readSchedulingPayload(interrupt, event.value);      const slots =        payload.slots && payload.slots.length > 0          ? payload.slots          : generateFallbackSlots();      return (        <TimePickerCard          topic={payload.topic ?? "a call"}          attendee={payload.attendee}          slots={slots}          onSubmit={(result) => {            setResumeFailed(false);            // Defer resolve so React commits the picked/cancelled badge before            // useInterrupt clears the interrupt element (a single rAF is not            // reliable: it can fire before React's commit). The rejection is            // re-surfaced rather than dropped, because the card has already            // shown a green "Booked" badge by then and a silently failed            // resume would leave the user reading a success that never            // happened.            window.setTimeout(() => {              void resolve(result).catch((error: unknown) => {                setResumeFailed(true);                queueMicrotask(() => {                  throw error;                });              });            }, 500);          }}        />      );    },  });

Whatever you pass to `resolve` is round-tripped back to the agent as the return value of the matching `interrupt(...)` call.

### Key props#

  * **`agentId`** — must match a runtime-registered agent. If omitted, the hook assumes `"default"`. A mismatch means the interrupt never fires.
  * **`render`** — receives `{ event, interrupt, resolve }`. The payload you passed to `interrupt(...)` on the server arrives on `event.value` for a legacy custom-event interrupt and on the `interrupt` for a standard one.
  * **`renderInChat`** — when `true` (as above), the picker appears inline in the chat transcript, between the paused assistant turn and the still-pending continuation.



## Multiple interrupts? Add a type and gate with `enabled`#

If your graph issues more than one kind of interrupt (e.g. `"ask"` vs `"approval"`), tag each with a `type` field on the payload and install one `useInterrupt` per shape, each gated by an `enabled` predicate:
    
    
    useInterrupt({
      agentId: "gen-ui-interrupt",
      enabled: (event) => event.value.type === "ask",
      render: ({ event, resolve }) => (
        <AskCard question={event.value.content} onAnswer={resolve} />
      ),
    });
    
    useInterrupt({
      agentId: "gen-ui-interrupt",
      enabled: (event) => event.value.type === "approval",
      render: ({ event, resolve }) => (
        <ApproveCard content={event.value.content} onAnswer={resolve} />
      ),
    });

## Preprocess with `handler`#

For cases where the interrupt can sometimes be resolved _without_ user input (e.g. the current user already has permission), pass a `handler` that runs before `render`. The handler can call `resolve(...)` itself to resume the agent early — the interrupt card unmounts when the resume run starts. Or return a value that `render` receives as `result`:
    
    
    useInterrupt({
      agentId: "gen-ui-interrupt",
      handler: async ({ event, resolve }) => {
        const dept = await lookupUserDepartment();
        if (event.value.accessDepartment === dept || dept === "admin") {
          resolve({ code: "AUTH_BY_DEPARTMENT" });
          return; // agent will resume; card unmounts when the run starts
        }
        return { dept };
      },
      render: ({ result, event, resolve }) => (
        <RequestAccessCard
          dept={result?.dept}
          onRequest={() => resolve({ code: "REQUEST_AUTH" })}
          onCancel={() => resolve({ code: "CANCEL" })}
        />
      ),
    });

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

  * [Tool-based HITL with `useHumanInTheLoop`](https://docs.copilotkit.ai/strands-typescript/human-in-the-loop/human-in-the-loop) — for LLM-initiated pauses.
  * [Headless interrupts](https://docs.copilotkit.ai/strands-typescript/human-in-the-loop/useInterrupt/headless) — compose the lower-level primitives (`useAgent`, `agent.subscribe`, `copilotkit.runAgent`) to resolve interrupts outside a chat surface.


