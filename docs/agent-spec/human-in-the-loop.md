---
url: https://docs.copilotkit.ai/agent-spec/human-in-the-loop/
title: HITL Overview
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:45:39.850332+00:00
---

# HITL Overview

> Source: https://docs.copilotkit.ai/agent-spec/human-in-the-loop/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/agent-spec)[Quickstart](https://docs.copilotkit.ai/agent-spec/quickstart)[Build with agents](https://docs.copilotkit.ai/agent-spec/build-with-agents)[Intelligence](https://docs.copilotkit.ai/agent-spec/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/agent-spec/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/agent-spec/webmcp)

Agent capabilities

Open Agent Spec

[Sub-agents](https://docs.copilotkit.ai/agent-spec/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/agent-spec/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/agent-spec/learning)

[User Memories](https://docs.copilotkit.ai/agent-spec/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/agent-spec/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/agent-spec/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/agent-spec/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/agent-spec/intelligence/analytics)[Channels](https://docs.copilotkit.ai/agent-spec/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/agent-spec/telemetry)[Community frameworks](https://docs.copilotkit.ai/agent-spec/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

InteractivityHuman-in-the-loop

# HITL Overview

Allow your agent and users to collaborate on complex tasks.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

See this in Inspector

Open Inspector on localhost. Go to **Agents** , then **Frontend Tools**. Your tool and its schema are listed.

More detail: [Inspector](https://docs.copilotkit.ai/agent-spec/inspector).

## What is this?#

Human-in-the-loop (HITL) lets an agent pause mid-run to collect input, confirmation, or a choice from the user, then resume with that answer folded back into its reasoning. It's what turns an autonomous workflow into a collaborative one: the agent keeps its context, the user keeps the steering wheel.

## When should I use this?#

Use HITL when you need:

  * **Quality control** — a human gate at high-stakes decision points
  * **Edge cases** — graceful fallbacks when the agent's confidence is low
  * **Expert input** — lean on the user for domain knowledge the model lacks
  * **Reliability** — a more robust loop for real-world, production traffic



## Two patterns for HITL in CopilotKit#

CopilotKit ships two complementary ways to pause an agent turn and ask the human something. They look similar from the outside (the chat pauses, a custom component appears, the user answers, the run resumes) but they're wired differently on the backend, and each has its own niche.

Pattern| Who decides to pause?| Backend surface  
---|---|---  
`useHumanInTheLoop`| The **LLM** , by calling a registered client-side tool| A frontend-only tool description (Zod schema + `render`)  
`useInterrupt`| The **graph** , by calling `interrupt(...)` during a node| A server-side `interrupt()` call in your LangGraph agent  
  
**Pick`useHumanInTheLoop`** when the pause is an _agent-initiated_ decision — the model chose to ask the user — and you want the picker UI inlined into the normal tool-call flow.

**Pick`useInterrupt`** when the pause is a _graph-enforced_ checkpoint — the code path deterministically requires a human answer — and you want `langgraph.interrupt()` as the server-side contract.

## Pattern 1 — `useHumanInTheLoop` (tool-based)#

The agent registers a HITL tool on the client with `useHumanInTheLoop`. When the LLM calls that tool, CopilotKit routes the call through your `render` function, which shows a custom component and calls `respond` with the user's answer. The agent sees the answer as the tool result and continues from there.

Missing snippet

No demo found for `agent-spec::hitl-in-chat`. Known demos are bundled from manifest `demos[i]`; check the cell id and framework slug.

The picker UI is fed a static list of candidate slots — this is just data the demo page owns, so you can swap in real availability, a calendar API, or anything else:

Missing snippet

No demo found for `agent-spec::hitl-in-chat`. Known demos are bundled from manifest `demos[i]`; check the cell id and framework slug.

## Pattern 2 — `useInterrupt` (graph-paused)#

With LangGraph's `interrupt()` the pause is enforced by the graph itself: a node calls `interrupt({...})`, the run suspends, the client receives the payload, renders a UI, and resumes the run with the user's answer. CopilotKit's `useInterrupt` hook is the render contract.

See the [`useInterrupt` deep dive](https://docs.copilotkit.ai/agent-spec/human-in-the-loop/useInterrupt) for the full walkthrough, including the backend tool and render-prop wiring.

## Going headless#

Both patterns above ship with a `render` prop — CopilotKit handles the "when to show the picker" logic for you. If you want to drive interrupt resolution from a custom UI that lives anywhere in the tree (not necessarily inside a chat), see the [headless interrupts guide](https://docs.copilotkit.ai/agent-spec/human-in-the-loop/headless) — it shows how to compose `useAgent`, `agent.subscribe`, and `copilotkit.runAgent` to build your own `useInterrupt` equivalent.

## Choose your AI backend

See [Integrations](https://ssr-placeholder.invalid//integrations) for all available frameworks (human-in-the-loop).

### On this page

What is this?When should I use this?Two patterns for HITL in CopilotKitPattern 1 — useHumanInTheLoop (tool-based)Pattern 2 — useInterrupt (graph-paused)Going headless
