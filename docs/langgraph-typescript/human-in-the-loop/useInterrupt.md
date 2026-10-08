---
url: https://docs.copilotkit.ai/langgraph-typescript/human-in-the-loop/useInterrupt/
title: Pausing the Agent for Input
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:11:31.187369+00:00
---

# Pausing the Agent for Input

> Source: https://docs.copilotkit.ai/langgraph-typescript/human-in-the-loop/useInterrupt/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-typescript)[Quickstart](https://docs.copilotkit.ai/langgraph-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-typescript/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-typescript/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[HITL Overview](https://docs.copilotkit.ai/langgraph-typescript/human-in-the-loop/index)[Pausing the Agent for Input](https://docs.copilotkit.ai/langgraph-typescript/human-in-the-loop/useInterrupt)[Headless Interrupts](https://docs.copilotkit.ai/langgraph-typescript/human-in-the-loop/headless)[Governed Action Approval UI](https://docs.copilotkit.ai/langgraph-typescript/human-in-the-loop/governed-actions)

[WebMCP](https://docs.copilotkit.ai/langgraph-typescript/webmcp)

Agent capabilities

LangGraph (TypeScript)

[Sub-agents](https://docs.copilotkit.ai/langgraph-typescript/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/langgraph-typescript/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/langgraph-typescript/learning)

[User Memories](https://docs.copilotkit.ai/langgraph-typescript/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/langgraph-typescript/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/langgraph-typescript/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/langgraph-typescript/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/langgraph-typescript/intelligence/analytics)[Channels](https://docs.copilotkit.ai/langgraph-typescript/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/langgraph-typescript/telemetry)[Community frameworks](https://docs.copilotkit.ai/langgraph-typescript/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

InteractivityHuman-in-the-loop

# Pausing the Agent for Input

Pause an agent run mid-tool, hand control to a custom React component, and resume with the user's answer.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Not supported on LangGraph (TypeScript)

LangGraph (TypeScript) doesn't support Human in the Loop: Interrupts. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.

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



For LLM-initiated pauses where the model decides on the fly to ask the user, prefer [`useHumanInTheLoop`](https://docs.copilotkit.ai/langgraph-typescript/human-in-the-loop/human-in-the-loop).

## The backend: `interrupt()` inside a tool#

### Install the CopilotKit LangGraph SDK
    
    
    npm install @copilotkit/sdk-js

### Wire CopilotKit state + tools into your graph

Tool-based HITL (`useHumanInTheLoop`) registers the tool on the frontend and forwards it via `state.copilotkit.actions` — the same wiring as frontend tools. The graph-paused pattern (`useInterrupt`) uses LangGraph's native `interrupt(...)` primitive inside a node.

frontend-tools.ts
    
    
    import type { RunnableConfig } from "@langchain/core/runnables";
    import { SystemMessage } from "@langchain/core/messages";
    import { MemorySaver, START, StateGraph } from "@langchain/langgraph";
    import { ChatOpenAI } from "@langchain/openai";
    import {
      convertActionsToDynamicStructuredTools,
      CopilotKitStateAnnotation,
    } from "@copilotkit/sdk-js/langgraph";
    
    // CopilotKit forwards frontend tools to the agent via
    // `state.copilotkit.actions`. `CopilotKitStateAnnotation` adds that
    // channel to your graph's state; `convertActionsToDynamicStructuredTools`
    // turns the forwarded action schemas into LangChain tools you can bind
    // at model-invocation time.
    const AgentStateAnnotation = CopilotKitStateAnnotation;
    export type AgentState = typeof AgentStateAnnotation.State;
    
    const SYSTEM_PROMPT = "You are a helpful, concise assistant.";
    
    async function runChatNode(
      state: AgentState,
      config: RunnableConfig,
      model: ChatOpenAI,
    ) {
      const modelWithTools = model.bindTools!([
        ...convertActionsToDynamicStructuredTools(state.copilotkit?.actions ?? []),
      ]);
    
      const response = await modelWithTools.invoke(
        [new SystemMessage({ content: SYSTEM_PROMPT }), ...state.messages],
        config,
      );
    
      return { messages: response };
    }
    
    async function chatNode(state: AgentState, config: RunnableConfig) {
      return runChatNode(
        state,
        config,
        new ChatOpenAI({ temperature: 0, model: "gpt-5-mini" }),
      );
    }
    
    function compileGraph(node: typeof chatNode) {
      return new StateGraph(AgentStateAnnotation)
        .addNode("chat_node", node)
        .addEdge(START, "chat_node")
        .addEdge("chat_node", "__end__")
        .compile({ checkpointer: new MemorySaver() });
    }
    
    export const graph = compileGraph(chatNode);

The example agent exposes a `schedule_meeting` tool. When the model calls it, the tool interrupts itself with the meeting context. The run freezes here until the client resolves; the resolution becomes the return value of the interrupt call, which the tool then turns into a final string for the model:

Not supported on LangGraph (TypeScript)

LangGraph (TypeScript) doesn't support Human in the Loop: Interrupts. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.

Two things to note:

  * The payload (`{"topic": topic, "attendee": attendee}`) is what the frontend reads off the interrupt. Keep it a plain, serializable object. It's the "pause-time context" the UI needs to render. Where it lands depends on the bridge: LangGraph hands it to `render` as `event.value`, while a standard AG-UI interrupt carries it on the interrupt itself, either under `metadata` or JSON-encoded into `message`. Read the channels your bridge uses rather than assuming one.
  * The return-side contract (`{chosen_label, chosen_time}` or `{cancelled: true}`) is entirely yours. The client can send anything as the resolve payload; the tool is the one that gives it meaning.



## The frontend: `useInterrupt` render prop#

On the client you register a `useInterrupt` hook per agent. When the paused run arrives, `render` receives both the raw `event` and the `interrupt` itself, and `resolve(...)` is how you resume the run. Where the payload sits depends on how the framework pauses: a legacy custom-event interrupt carries it on `event.value`, while a standard AG-UI interrupt carries it on the `interrupt` (its `metadata`, or a JSON-encoded `message`, depending on the bridge). Read the channel your framework uses:

Not supported on LangGraph (TypeScript)

LangGraph (TypeScript) doesn't support Human in the Loop: Interrupts. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.

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

  * [Tool-based HITL with `useHumanInTheLoop`](https://docs.copilotkit.ai/langgraph-typescript/human-in-the-loop/human-in-the-loop) — for LLM-initiated pauses.
  * [Headless interrupts](https://docs.copilotkit.ai/langgraph-typescript/human-in-the-loop/useInterrupt/headless) — compose the lower-level primitives (`useAgent`, `agent.subscribe`, `copilotkit.runAgent`) to resolve interrupts outside a chat surface.


