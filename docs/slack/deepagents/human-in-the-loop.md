---
url: https://docs.copilotkit.ai/slack/deepagents/human-in-the-loop/
title: HITL Overview
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:39:34.703896+00:00
---

# HITL Overview

> Source: https://docs.copilotkit.ai/slack/deepagents/human-in-the-loop/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

ChannelSlackAgent backendDeep Agents

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Getting Started

[Overview](https://docs.copilotkit.ai/slack/deepagents)[Configure the Channel in Intelligence](https://docs.copilotkit.ai/slack/deepagents/intelligence)[Connect and run your agent](https://docs.copilotkit.ai/slack/deepagents/connect)

Build

[Tools and context](https://docs.copilotkit.ai/slack/deepagents/tools)[Identity and Memory](https://docs.copilotkit.ai/slack/deepagents/identity-and-memory)[Rich messages and components](https://docs.copilotkit.ai/slack/deepagents/rich-messages)[Interactive messages and approvals](https://docs.copilotkit.ai/slack/deepagents/interactive)[Commands and reactions](https://docs.copilotkit.ai/slack/deepagents/commands-and-reactions)[Files and multimodal input](https://docs.copilotkit.ai/slack/deepagents/files-and-multimodality)[Threads and state](https://docs.copilotkit.ai/slack/deepagents/threads-and-state)

Production

[Persistence and scaling](https://docs.copilotkit.ai/slack/deepagents/persistence-and-scaling)[History and transcripts](https://docs.copilotkit.ai/slack/deepagents/history-and-transcripts)[Deploy and operate](https://docs.copilotkit.ai/slack/deepagents/deploy-and-operate)[API reference](https://docs.copilotkit.ai/reference/channels)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[Deep Agents](https://docs.copilotkit.ai/slack/deepagents)

# HITL Overview

Allow your agent and users to collaborate on complex tasks.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Not available for Deep Agents yet

This feature (`hitl-in-chat`) hasn't been tagged in any Deep Agents cell yet. Try [CopilotKit's Built-in Agent](https://docs.copilotkit.ai/slack/built-in-agent/human-in-the-loop), [LangGraph (Python)](https://docs.copilotkit.ai/slack/langgraph-python/human-in-the-loop), [LangGraph (TypeScript)](https://docs.copilotkit.ai/slack/langgraph-typescript/human-in-the-loop).

See this in Inspector

Open Inspector on localhost. Go to **Agents** , then **Frontend Tools**. Your tool and its schema are listed.

More detail: [Inspector](https://docs.copilotkit.ai/slack/deepagents/inspector).

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

No demo found for `deepagents::hitl-in-chat`. Known demos are bundled from manifest `demos[i]`; check the cell id and framework slug.

The picker UI is fed a static list of candidate slots — this is just data the demo page owns, so you can swap in real availability, a calendar API, or anything else:

Missing snippet

No demo found for `deepagents::hitl-in-chat`. Known demos are bundled from manifest `demos[i]`; check the cell id and framework slug.

## Pattern 2 — `useInterrupt` (graph-paused)#

With LangGraph's `interrupt()` the pause is enforced by the graph itself: a node calls `interrupt({...})`, the run suspends, the client receives the payload, renders a UI, and resumes the run with the user's answer. CopilotKit's `useInterrupt` hook is the render contract.

See the [`useInterrupt` deep dive](https://docs.copilotkit.ai/slack/deepagents/human-in-the-loop/useInterrupt) for the full walkthrough, including the backend tool and render-prop wiring.

## Going headless#

Both patterns above ship with a `render` prop — CopilotKit handles the "when to show the picker" logic for you. If you want to drive interrupt resolution from a custom UI that lives anywhere in the tree (not necessarily inside a chat), see the [headless interrupts guide](https://docs.copilotkit.ai/slack/deepagents/human-in-the-loop/headless) — it shows how to compose `useAgent`, `agent.subscribe`, and `copilotkit.runAgent` to build your own `useInterrupt` equivalent.

### On this page

What is this?When should I use this?Two patterns for HITL in CopilotKitPattern 1 — useHumanInTheLoop (tool-based)Pattern 2 — useInterrupt (graph-paused)Going headless
