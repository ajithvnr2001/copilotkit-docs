---
url: https://docs.copilotkit.ai/ms-agent-harness-dotnet/programmatic-control/
title: Programmatic Control
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:21:00.171014+00:00
---

# Programmatic Control

> Source: https://docs.copilotkit.ai/ms-agent-harness-dotnet/programmatic-control/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMS Agent Harness (.NET)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ms-agent-harness-dotnet)[Quickstart](https://docs.copilotkit.ai/ms-agent-harness-dotnet/quickstart)[Build with agents](https://docs.copilotkit.ai/ms-agent-harness-dotnet/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ms-agent-harness-dotnet/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ms-agent-harness-dotnet/webmcp)

Agent capabilities

MS Agent Harness (.NET)

[Sub-agents](https://docs.copilotkit.ai/ms-agent-harness-dotnet/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ms-agent-harness-dotnet/learning)

[User Memories](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/ms-agent-harness-dotnet/telemetry)[Community frameworks](https://docs.copilotkit.ai/ms-agent-harness-dotnet/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[MS Agent Harness (.NET)](https://docs.copilotkit.ai/ms-agent-harness-dotnet)

# Programmatic Control

Drive agent runs directly from code — no chat UI required.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

Programmatic control is what you reach for when you want to drive an agent run from code rather than from a chat composer: a button, a form, a cron job, a keyboard shortcut, a graph callback. CopilotKit exposes three primitives that cover every triggering pattern:

  * `agent.addMessage(...)` — append a message to the conversation without running the agent. Pair with `copilotkit.runAgent({ agent })` when you want the appended message to kick off a turn.
  * `copilotkit.runAgent({ agent })` — the same entry point `<CopilotChat />` calls under the hood. Orchestrates frontend tools, follow-up runs, and the subscriber lifecycle.
  * `agent.subscribe(subscriber)` — low-level AG-UI event subscription (`onCustomEvent`, `onRunStartedEvent`, `onRunFinalized`, `onRunFailed`, …). Pairs with `copilotkit.runAgent({ agent, resume })` for standard AG-UI interrupts, or `copilotkit.runAgent({ agent, forwardedProps: { command: { resume, interruptEvent } } })` for legacy `on_interrupt` custom events, to drive interrupt resolution from arbitrary UI.



The send-and-stop example below is intentionally self-contained. The later subscription and interrupt examples are pulled from the live `interrupt-headless` cell.

## When should I use this?#

Use programmatic control when you want to:

  * Trigger agent runs from buttons, forms, or other UI elements
  * Execute specific tools directly from UI interactions (without an LLM turn)
  * Build agent features without a chat window
  * Access agent state and results programmatically
  * Create fully custom agent-driven workflows



## Sending a message from code#

The canonical pattern is to append a user message with `agent.addMessage`, then call `copilotkit.runAgent({ agent })`. Use `copilotkit.stopAgent({ agent })` to cancel an in-flight run.

frontend/src/app/agent-trigger.tsx
    
    
    "use client";
    
    import { useAgent, useCopilotKit } from "@copilotkit/react-core/v2";
    
    export function AgentTrigger({ agentId }: { agentId: string }) {
      const { agent } = useAgent({ agentId });
      const { copilotkit } = useCopilotKit();
    
      const run = async () => {
        if (agent.isRunning) return;
    
        agent.addMessage({
          id: crypto.randomUUID(),
          role: "user",
          content: "Summarize the latest sales data",
        });
    
        try {
          await copilotkit.runAgent({ agent });
        } catch (error) {
          console.error("CopilotKit runAgent failed:", error);
        }
      };
    
      return (
        <>
          <button onClick={run} disabled={agent.isRunning}>
            Run agent
          </button>
          <button
            onClick={() => copilotkit.stopAgent({ agent })}
            disabled={!agent.isRunning}
          >
            Stop
          </button>
        </>
      );
    }

### `copilotkit.runAgent()` vs `agent.runAgent()`#

Both methods trigger the agent, but they operate at different levels:

  * **`copilotkit.runAgent({ agent })`** — the recommended default. Orchestrates the full lifecycle: executes frontend tools, handles follow-up runs, and routes errors through the subscriber system.
  * **`agent.runAgent(options)`** — low-level method on the agent instance. Sends the request to the runtime but does **not** execute frontend tools or chain follow-ups. Reach for this only when you need direct control. (For the interrupt-resume case, use `copilotkit.runAgent({ agent, resume })` for standard AG-UI interrupts, or `copilotkit.runAgent({ agent, forwardedProps: { command: { resume, interruptEvent } } })` for legacy `on_interrupt` custom events — the snippet below shows the legacy form — so the subscriber lifecycle still wraps the resumed run.)



## Subscribing to agent events#

`agent.subscribe(subscriber)` returns `{ unsubscribe }`. The subscriber object accepts every AG-UI lifecycle callback: `onCustomEvent`, `onRunStartedEvent`, `onRunFinalized`, `onRunFailed`, and the streaming deltas. Use it to drive custom progress UI, forward events to analytics, or catch framework pause/resume events and resolve them with a payload (the pattern below).

## Resolving a frontend tool call from a button#

For promise-based integrations there is no native interrupt primitive — the demo uses `useFrontendTool` with a Promise-based handler instead. The handler stages its `resolve` callback and pending payload via React state, the app surface renders the picker outside the chat, and the user's pick resolves the Promise that the agent's tool call is awaiting. Same UX, different mechanism — the agent never knows it's talking to a button grid instead of a chat picker:

Not supported on MS Agent Harness (.NET)

MS Agent Harness (.NET) doesn't support Human in the Loop: Headless Interrupts. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.

The resulting `{ pending, resolveActive }` pair is pure data; any UI can drive it. The cell itself renders a simple button grid, but the same pattern would power a modal, a toast, a sidebar form, or a voice UI.

## See also#

  * [Headless UI](https://docs.copilotkit.ai/ms-agent-harness-dotnet/programmatic-control/headless) — the full `useRenderedMessages` composition that mirrors `<CopilotChatMessageView>` line-for-line.
  * [Human-in-the-Loop](https://docs.copilotkit.ai/ms-agent-harness-dotnet/programmatic-control/human-in-the-loop) — the `useHumanInTheLoop` and `useInterrupt` hooks with their render-prop contracts, for the "paused mid-chat" pattern this page's headless variant replaces.


