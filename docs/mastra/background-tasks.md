---
url: https://docs.copilotkit.ai/mastra/background-tasks/
title: Background Tasks
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:16:03.482947+00:00
---

# Background Tasks

> Source: https://docs.copilotkit.ai/mastra/background-tasks/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMastra

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/mastra)[Quickstart](https://docs.copilotkit.ai/mastra/quickstart)[Build with agents](https://docs.copilotkit.ai/mastra/build-with-agents)[Intelligence](https://docs.copilotkit.ai/mastra/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/mastra/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/mastra/webmcp)

Agent capabilities

Mastra

[Background Tasks](https://docs.copilotkit.ai/mastra/background-tasks)

[Sub-agents](https://docs.copilotkit.ai/mastra/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/mastra/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/mastra/learning)

[User Memories](https://docs.copilotkit.ai/mastra/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/mastra/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/mastra/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/mastra/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/mastra/intelligence/analytics)[Channels](https://docs.copilotkit.ai/mastra/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/mastra/telemetry)[Community frameworks](https://docs.copilotkit.ai/mastra/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Background Tasks

Agent capabilitiesMastra

# Background Tasks

Dispatch long-running work to Mastra's BackgroundTaskManager and surface it as a live activity card in the chat.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

Mastra's [background tasks](https://mastra.ai/docs/agents/background-tasks) let a tool run outside the agentic loop instead of blocking it. When a tool is flagged `background: { enabled: true }`, Mastra dispatches it to its `BackgroundTaskManager`, emits a `background-task-started` lifecycle chunk, and returns a placeholder result so the conversation keeps flowing.

`MastraAgent` (the AG-UI adapter) maps that lifecycle to an AG-UI **activity event** (activity type `mastra-background-task`) and **suppresses the normal tool pill** — so the work surfaces only as a live "working" card, never as an orphan tool call. A registered CopilotKit activity renderer paints that card inline in the transcript.

## When should I use this?#

Background tasks fit any work that is too slow to hold the chat hostage:

  * **Deep research / long lookups** — kick off a multi-step investigation and let the user keep chatting
  * **Report or artifact generation** — build something in the background and surface progress
  * **Batch or fan-out work** — dispatch several jobs without serializing the conversation



Completion is delivered **out of band**. On the dispatching turn Mastra emits only the `started` lifecycle plus a placeholder result, so within that turn the card stays in the "working" state; the finished result is delivered on a later turn (or retrieved from the task manager). See Completion is out of band below.

## Implementation#

### Run and connect your agent#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/langgraph/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point as this guide uses it as a starting point.

### Define a backgroundable tool#

Flag the tool with `background: { enabled: true }`. Mastra dispatches it to the `BackgroundTaskManager` instead of running it inline.

src/mastra/tools/background-research.ts
    
    
    import { createTool } from "@mastra/core/tools";
    import { z } from "zod";
    
    export const runDeepResearchTool = createTool({
      id: "run_deep_research",
      description:
        "Kick off a long-running deep-research task on a topic. This runs in " +
        "the background while the conversation continues.",
      inputSchema: z.object({
        topic: z.string().describe("The topic to research in depth."),
      }),
      background: { enabled: true }, 
      execute: async ({ topic }) => {
        // Runs when the background worker executes the task.
        return JSON.stringify({
          topic,
          summary: `Deep research on "${topic}" completed.`,
        });
      },
    });

### Enable the BackgroundTaskManager on the Mastra instance#

Backgroundable tools only dispatch when the manager is enabled on the instance. A configured `storage` is also required so tasks can be tracked.

src/mastra/index.ts
    
    
    import { Mastra } from "@mastra/core/mastra";
    import { LibSQLStore } from "@mastra/libsql";
    import { backgroundAgentsAgent } from "./agents";
    
    export const mastra = new Mastra({
      agents: { backgroundAgentsAgent },
      storage: new LibSQLStore({ id: "mastra-storage", url: ":memory:" }),
      backgroundTasks: { enabled: true }, 
    });

### Add the tool to your agent#

src/mastra/agents/index.ts
    
    
    import { Agent } from "@mastra/core/agent";
    import { openai } from "@ai-sdk/openai";
    import { runDeepResearchTool } from "@/mastra/tools/background-research"; 
    
    export const backgroundAgentsAgent = new Agent({
      id: "background-agents",
      name: "Background Agents Agent",
      tools: { runDeepResearchTool }, 
      model: openai("gpt-4.1"),
      instructions:
        "You are a research assistant that dispatches long-running work to the " +
        "background. When the user asks you to research a topic, call the " +
        "run_deep_research tool ONCE, then send a short message saying the work " +
        "is running in the background.",
    });

### Render the activity card in your frontend#

Write an activity renderer for the `mastra-background-task` activity type. The standard chat surface renders registered activity messages inline, so no custom message list is needed.

Register the renderer on `<CopilotKit>` via `renderActivityMessages`.

ui/app/activity-card.tsx
    
    
    import { z } from "zod";
    import type { ReactActivityMessageRenderer } from "@copilotkit/react-core/v2";
    
    const contentSchema = z
      .object({ status: z.string().optional(), args: z.record(z.unknown()).optional() })
      .passthrough();
    
    export const backgroundTaskActivityRenderer: ReactActivityMessageRenderer<
      z.infer<typeof contentSchema>
    > = {
      activityType: "mastra-background-task", 
      content: contentSchema,
      render: ({ content }) => {
        const working = content.status !== "completed" && content.status !== "failed";
    const topic = (content.args?.topic as string | undefined) ?? "task";
        return (
          <div data-status={content.status ?? "running"}>
            <strong>Deep research</strong> — {topic}
            <span>{working ? "Working…" : content.status}</span>
          </div>
        );
      },
    };

ui/app/page.tsx
    
    
    import { CopilotKit, CopilotChat } from "@copilotkit/react-core/v2";
    import { backgroundTaskActivityRenderer } from "./activity-card";
    
    export default function Page() {
      return (
        <CopilotKit
          runtimeUrl="/api/copilotkit"
          agent="backgroundAgentsAgent"
          renderActivityMessages={[backgroundTaskActivityRenderer]} 
        >
          <CopilotChat />
        </CopilotKit>
      );
    }

### Give it a try!#

Ask the agent to research something.
    
    
    Kick off deep research on the current landscape of AI agent frameworks.

The agent calls `run_deep_research`, Mastra dispatches it in the background, and a live "working" activity card appears inline — with no blocking tool pill — while the conversation stays responsive.

## Completion is out of band#

By design, the dispatching run's stream carries only the `started` lifecycle plus a placeholder result — the tool's `execute` has not finished by the time the stream closes. So within that turn the card stays "working"; the finished result is delivered out of band.

Mastra exposes `untilIdle: true` (via `getLocalAgents`) to hold the run open and pipe the manager pubsub chunks — including `background-task-completed` — into the same stream so the card could flip to "Completed" in-turn. That only works when a **background worker actually executes the dispatched task before the idle window closes**. In a single-process app with no such worker the task is never executed within the run, so no completion chunk is produced and `untilIdle` only holds the stream open with no benefit. When you run a deployment with a real background worker, enable `untilIdle` and the adapter's lifecycle mapping (`running` → `completed`/`failed`/`cancelled`) flips the card automatically. Otherwise, retrieve results out of band via the task manager (`backgroundTaskManager.stream()` / `getTask(taskId)`).

## Observational Memory as background activity#

If your agent uses Mastra's [Observational Memory](https://mastra.ai/docs/memory/observational-memory), you can surface its observation/buffering/activation cycles the same way — as a live activity card instead of invisible background work. This is opt-in and OFF by default.

Two switches, both required:

  1. **The agent's`Memory` must have Observational Memory enabled** (that's what makes Mastra stream the OM lifecycle in the first place):

src/mastra/agents/index.ts
         
         memory: new Memory({
           storage,
           options: {
             observationalMemory: {
               scope: "thread",
               observation: { messageTokens: 600, bufferTokens: 300 },
               model: openai("gpt-4.1"),
             },
           },
         }),

  2. **The adapter must be told to forward it** — pass `observationalMemory: true` (or an array of agent ids) to `getLocalAgents`:

app/api/copilotkit/route.ts
         
         const localAgents = getLocalAgents({
           mastra,
           resourceId: "user-1",
           observationalMemory: true, 
         });




With both on, `MastraAgent` maps the OM lifecycle to AG-UI activity events under activity type `mastra-observational-memory`. Render them exactly like the background-task card — register a renderer for that activity type:

app/page.tsx
    
    
    const observationalMemoryActivityRenderer = {
      activityType: "mastra-observational-memory", 
      render: ({ content }) => <OMActivityCard content={content} />,
    };
    
    <CopilotKit
      runtimeUrl="/api/copilotkit"
      renderActivityMessages={[observationalMemoryActivityRenderer]} 
    >

The activity content carries the cycle (`cycleId`, `phase: "observation" | "buffering" | "activation"`, `status`, token counts) and advances in place as the cycle progresses, so one card tracks each OM cycle from start to completion.

OM cycles trigger on **unobserved message-token size** , not turn count — short chats may never trip one. If you're testing the card, drive a few sizable messages.

### On this page

What is this?When should I use this?ImplementationCompletion is out of bandObservational Memory as background activity
