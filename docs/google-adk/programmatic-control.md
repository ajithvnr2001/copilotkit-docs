---
url: https://docs.copilotkit.ai/google-adk/programmatic-control/
title: Programmatic Control
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:03:31.000102+00:00
---

# Programmatic Control

> Source: https://docs.copilotkit.ai/google-adk/programmatic-control/

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

[Google ADK](https://docs.copilotkit.ai/google-adk)

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

### Install the ADK + AG-UI bridge
    
    
    pip install ag-ui-adk

### Add `AGUIToolset()` to your agent

Programmatic control (`copilotkit.runAgent`, `agent.subscribe`, `agent.addMessage`) drives runs through the same agent your chat UI uses, so the backend wiring is the same — wire `AGUIToolset()` once and every entry point sees the same forwarded tools and state.

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

ADK doesn't ship a native `interrupt(...)` primitive — for the headless interrupt-resolver pattern, use the frontend `useFrontendTool` Promise-based handler instead.

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

## Resolving a pause from a button#

> **Interrupt-style pause/resume isn't available on this framework.** The headless interrupt pattern shown above requires the underlying runtime to expose either a native `interrupt(...)` primitive (LangGraph) or a Promise-resolving frontend-tool path. For all other integrations, drive pauses through [`useHumanInTheLoop`](https://docs.copilotkit.ai/google-adk/programmatic-control/human-in-the-loop) instead — it's the standard hook for tool-call-based pause/resume flows and works on every framework that supports tool calls. The `agent.addMessage`, `copilotkit.runAgent`, and `agent.subscribe` primitives above still apply — only the interrupt-resolution path is framework-specific.

## See also#

  * [Headless UI](https://docs.copilotkit.ai/google-adk/programmatic-control/headless) — the full `useRenderedMessages` composition that mirrors `<CopilotChatMessageView>` line-for-line.
  * [Human-in-the-Loop](https://docs.copilotkit.ai/google-adk/programmatic-control/human-in-the-loop) — the `useHumanInTheLoop` and `useInterrupt` hooks with their render-prop contracts, for the "paused mid-chat" pattern this page's headless variant replaces.


