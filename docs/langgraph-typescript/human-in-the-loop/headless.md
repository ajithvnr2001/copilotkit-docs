---
url: https://docs.copilotkit.ai/langgraph-typescript/human-in-the-loop/headless/
title: Headless Interrupts
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:11:30.678305+00:00
---

# Headless Interrupts

> Source: https://docs.copilotkit.ai/langgraph-typescript/human-in-the-loop/headless/

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

# Headless Interrupts

Resolve agent interrupts from any UI, without a useInterrupt render slot.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Not supported on LangGraph (TypeScript)

LangGraph (TypeScript) doesn't support Human in the Loop: Headless Interrupts. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.

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



If you just want "a picker in chat", just use [`useInterrupt`](https://docs.copilotkit.ai/langgraph-typescript/human-in-the-loop/headless/useInterrupt).

## The primitives#

### Install the CopilotKit LangGraph SDK
    
    
    npm install @copilotkit/sdk-js

### Wire CopilotKit state + tools into your graph

Programmatic control (`copilotkit.runAgent`, `agent.subscribe`, `agent.addMessage`) drives runs through the same agent your chat UI uses, so the backend wiring is the same `CopilotKitStateAnnotation` setup.

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

Not supported on LangGraph (TypeScript)

LangGraph (TypeScript) doesn't support Human in the Loop: Headless Interrupts. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.

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

  * [Tool-based HITL with `useHumanInTheLoop`](https://docs.copilotkit.ai/langgraph-typescript/human-in-the-loop/human-in-the-loop) — for LLM-initiated pauses where the model decides on the fly to ask the user, rather than the runtime forcing the pause itself.
  * [`useInterrupt`](https://docs.copilotkit.ai/langgraph-typescript/human-in-the-loop/headless/useInterrupt) — the render-prop version of this page, with `enabled` gating and `handler` preprocessing.


