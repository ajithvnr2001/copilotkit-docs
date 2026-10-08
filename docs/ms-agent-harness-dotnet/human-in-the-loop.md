---
url: https://docs.copilotkit.ai/ms-agent-harness-dotnet/human-in-the-loop/
title: HITL Overview
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:20:37.244467+00:00
---

# HITL Overview

> Source: https://docs.copilotkit.ai/ms-agent-harness-dotnet/human-in-the-loop/

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

On this page

InteractivityHuman-in-the-loop

# HITL Overview

Allow your agent and users to collaborate on complex tasks.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

HitlInChatAgent.cs

page.tsx

time-picker-card.tsx

route.ts
    
    
    using Microsoft.Agents.AI;using Microsoft.Extensions.AI;using OpenAI;// In-Chat HITL (useHumanInTheLoop — ergonomic API) agent.//// The `book_call` tool is defined entirely on the frontend via the// `useHumanInTheLoop` hook (see src/app/demos/hitl-in-chat/page.tsx).// The .NET agent owns no tools — it just has a system prompt that nudges// the model to call the frontend-provided tool when the user asks to book// a call. The picker UI is rendered inline in the chat by the hook's// `render` callback, and the user's choice is returned to the agent as the// tool result.//// Harness column: the inner ChatClientAgent is built through the// `chatClient.AsHarnessAgent(...)` wrapper (Microsoft Agent Harness over// Microsoft Agent Framework) and the credential comes from the single shared// `OpenAIClient` threaded in from Program.cs (built via the harness// ApiKeyResolver). See the W0 contract §1.//// Reference parity with:// showcase/integrations/langgraph-python/src/agents/hitl_in_chat_agent.pypublic sealed class HitlInChatAgentFactory{    private const int HarnessMaxContextWindowTokens = 128_000;    private const int HarnessMaxOutputTokens = 8_192;    private const string SystemPrompt =        "You help users book an onboarding call with the sales team. " +        "When they ask to book a call, call the frontend-provided " +        "`book_call` tool with a short topic and the user's name. " +        "Keep any chat reply to one short sentence.";    private readonly OpenAIClient _openAiClient;    private readonly ILogger _logger;    public HitlInChatAgentFactory(OpenAIClient openAiClient, ILoggerFactory loggerFactory)    {        ArgumentNullException.ThrowIfNull(openAiClient);        ArgumentNullException.ThrowIfNull(loggerFactory);        _openAiClient = openAiClient;        _logger = loggerFactory.CreateLogger<HitlInChatAgentFactory>();    }    public AIAgent CreateHitlInChatAgent()    {        var chatClient = _openAiClient.GetChatClient("gpt-5-mini").AsIChatClient();        return chatClient.AsHarnessAgent(            HarnessMaxContextWindowTokens,            HarnessMaxOutputTokens,            new HarnessAgentOptions            {                Name = "HitlInChatAgent",                Description = "In-Chat HITL onboarding-call booking assistant powered by Microsoft Agent Harness over Microsoft Agent Framework.",                ChatOptions = new ChatOptions                {                    Instructions = SystemPrompt,                    MaxOutputTokens = HarnessMaxOutputTokens,                    Tools = [],                },            });    }}

See this in Inspector

Open Inspector on localhost. Go to **Agents** , then **Frontend Tools**. Your tool and its schema are listed.

More detail: [Inspector](https://docs.copilotkit.ai/ms-agent-harness-dotnet/inspector).

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

page.tsx
    
    
    import React from "react";import {  CopilotKit,  CopilotChat,  useHumanInTheLoop,  useConfigureSuggestions,} from "@copilotkit/react-core/v2";import { z } from "zod";import type { TimeSlot } from "./time-picker-card";import { TimePickerCard } from "./time-picker-card";const DEFAULT_SLOTS: TimeSlot[] = [  { label: "Tomorrow 10:00 AM", iso: "2026-04-19T10:00:00-07:00" },  { label: "Tomorrow 2:00 PM", iso: "2026-04-19T14:00:00-07:00" },  { label: "Monday 9:00 AM", iso: "2026-04-21T09:00:00-07:00" },  { label: "Monday 3:30 PM", iso: "2026-04-21T15:30:00-07:00" },];export default function HitlInChatDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent="hitl-in-chat">      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  useConfigureSuggestions({    suggestions: [      {        title: "Book a call with sales",        message:          "Please book an intro call with the sales team to discuss pricing.",      },      {        title: "Schedule a 1:1 with Alice",        message: "Schedule a 1:1 with Alice next week to review Q2 goals.",      },    ],    available: "always",  });  useHumanInTheLoop({    agentId: "hitl-in-chat",    name: "book_call",    description:      "Ask the user to pick a time slot for a call. The picker UI presents fixed candidate slots; the user's choice is returned to the agent.",    parameters: z.object({      topic: z        .string()        .describe("What the call is about (e.g. 'Intro with sales')"),      attendee: z        .string()        .describe("Who the call is with (e.g. 'Alice from Sales')"),    }),    render: ({ args, status, respond }: any) => (      <TimePickerCard        topic={args?.topic ?? "a call"}        attendee={args?.attendee}        slots={DEFAULT_SLOTS}        status={status}        onSubmit={(result) => respond?.(result)}      />    ),  });

The picker UI is fed a static list of candidate slots — this is just data the demo page owns, so you can swap in real availability, a calendar API, or anything else:

page.tsx
    
    
    import React from "react";import {  CopilotKit,  CopilotChat,  useHumanInTheLoop,  useConfigureSuggestions,} from "@copilotkit/react-core/v2";import { z } from "zod";import type { TimeSlot } from "./time-picker-card";import { TimePickerCard } from "./time-picker-card";const DEFAULT_SLOTS: TimeSlot[] = [  { label: "Tomorrow 10:00 AM", iso: "2026-04-19T10:00:00-07:00" },  { label: "Tomorrow 2:00 PM", iso: "2026-04-19T14:00:00-07:00" },  { label: "Monday 9:00 AM", iso: "2026-04-21T09:00:00-07:00" },  { label: "Monday 3:30 PM", iso: "2026-04-21T15:30:00-07:00" },];

## Pattern 2 — `useInterrupt` (graph-paused)#

With LangGraph's `interrupt()` the pause is enforced by the graph itself: a node calls `interrupt({...})`, the run suspends, the client receives the payload, renders a UI, and resumes the run with the user's answer. CopilotKit's `useInterrupt` hook is the render contract.

See the [`useInterrupt` deep dive](https://docs.copilotkit.ai/ms-agent-harness-dotnet/human-in-the-loop/useInterrupt) for the full walkthrough, including the backend tool and render-prop wiring.

Not supported on MS Agent Harness (.NET)

MS Agent Harness (.NET) doesn't support Human in the Loop: Interrupts. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.

## Going headless#

Both patterns above ship with a `render` prop — CopilotKit handles the "when to show the picker" logic for you. If you want to drive interrupt resolution from a custom UI that lives anywhere in the tree (not necessarily inside a chat), see the [headless interrupts guide](https://docs.copilotkit.ai/ms-agent-harness-dotnet/human-in-the-loop/headless) — it shows how to compose `useAgent`, `agent.subscribe`, and `copilotkit.runAgent` to build your own `useInterrupt` equivalent.

### On this page

What is this?When should I use this?Two patterns for HITL in CopilotKitPattern 1 — useHumanInTheLoop (tool-based)Pattern 2 — useInterrupt (graph-paused)Going headless
