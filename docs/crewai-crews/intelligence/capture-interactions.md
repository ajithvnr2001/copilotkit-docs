---
url: https://docs.copilotkit.ai/crewai-crews/intelligence/capture-interactions/
title: Capture interactions
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:57:14.430124+00:00
---

# Capture interactions

> Source: https://docs.copilotkit.ai/crewai-crews/intelligence/capture-interactions/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendCrewAI Flows

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/crewai-crews)[Quickstart](https://docs.copilotkit.ai/crewai-crews/quickstart)[Build with agents](https://docs.copilotkit.ai/crewai-crews/build-with-agents)[Intelligence](https://docs.copilotkit.ai/crewai-crews/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/crewai-crews/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/crewai-crews/webmcp)

Agent capabilities

CrewAI Flows

[Sub-agents](https://docs.copilotkit.ai/crewai-crews/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/crewai-crews/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/crewai-crews/learning)

[User Memories](https://docs.copilotkit.ai/crewai-crews/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/crewai-crews/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/crewai-crews/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/crewai-crews/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/crewai-crews/intelligence/analytics)[Channels](https://docs.copilotkit.ai/crewai-crews/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/crewai-crews/telemetry)[Community frameworks](https://docs.copilotkit.ai/crewai-crews/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Capture interactions

IntelligenceFeatures

# Capture interactions

Use the experimental custom-sink integration to capture browser interactions and CopilotKit context as AG-UI events.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview#

This guide covers the experimental self-hosted integration that sends captured events to your own sink. It records browser interactions as AG-UI `CUSTOM` events. Core adds Thread, message, and tool context where available. These chat events and links belong to this custom-sink integration.

When you are done, your app sends batches of events to a route you own. Each click inside the chat carries its `threadId`, `messageId`, and `toolCallId`.

Capture retains full URLs, page titles, referrers, element text, attributes, control values, browser-visible headers, and bounded body snapshots by default. It also records form edits and full agent message text. Passwords and credentials are replaced with `[redacted]` in the browser. See [Captured data](https://docs.copilotkit.ai/crewai-crews/intelligence/captured-data) for fields, limits, redaction, and explicit exclusions.

## Turn on capture#

### Install the package#
    
    
    npm install @copilotkit/learning

### Add a route that receives the events#

The sink posts JSON batches to this route. This example only logs them. Store them where you want.

app/api/learning-events/route.ts
    
    
    export async function POST(request: Request) {
      const batch = await request.json();
      console.log(batch.trajectoryId, batch.events.length, "events");
      return Response.json({ ok: true });
    }

### Pass `learning` to the provider#

A Trajectory groups the events of one session. Your app decides where a Trajectory starts. Here, each page load starts one.

app/providers.tsx
    
    
    "use client";
    
    import { httpSink } from "@copilotkit/learning";
    import { CopilotKitProvider } from "@copilotkit/react-core/v2";
    import { useState } from "react";
    
    const sink = httpSink("/api/learning-events");
    
    export function Providers({ children }: { children: React.ReactNode }) {
      const [trajectoryId] = useState(() => crypto.randomUUID());
    
      return (
        <CopilotKitProvider
          runtimeUrl="/api/copilotkit"
          learning={{ sink, trajectoryId }}
        >
          {children}
        </CopilotKitProvider>
      );
    }

Capture starts after the provider mounts and stops when it unmounts. CopilotKit's own runtime requests are never captured.

### Name the actions that matter#

Click events include the element's text, attributes, and control values. Add `data-copilotkit-action` for a stable action name:
    
    
    <button data-copilotkit-action="deal.approve" onClick={approve}>
      Approve
    </button>

Click **Approve** inside a tool's UI in the chat. Your route logs a batch with a click like this:
    
    
    {
      "type": "CUSTOM",
      "name": "click",
      "timestamp": 1790841234567,
      "value": {
        "seq": 7,
        "target": {
          "tag": "button",
          "role": null,
          "action": "deal.approve",
          "text": "Approve",
          "attributes": { "data-copilotkit-action": "deal.approve" },
          "input": "pointer"
        },
        "route": "/deals/42",
        "url": "https://app.example.com/deals/42?source=inbox#review",
        "threadId": "5f0c6b1e-0b8f-4f6e-9a57-2f3d1c9a4e21",
        "agentId": "default",
        "messageId": "msg-42",
        "runId": "run-9",
        "toolCallId": "call-3",
        "toolName": "approveDeal",
        "toolStatus": "executing"
      }
    }

## How a click finds its Thread#

Core picks the Thread in this order:

  1. A click inside a chat message uses the Thread of that message.
  2. Otherwise, the one Thread that a chat on the page shows.
  3. Otherwise, `threadId` is `null`.



When two chats show different Threads, a click outside both gets `threadId: null` and a `threadAmbiguity` object with the candidates. Capture does not guess.

Core also emits `thread.linked` when a chat shows a Thread: once at start, when a new chat opens, and when a chat switches Threads. `hasMessages: false` marks a new Thread that has no messages yet.

With connected Core capture, Core emits `thread.linked` with only `threadId` when Runtime starts an agent run, once for each Thread. Runtime creates the Thread before the run starts, so Intelligence can link it.

## Record outcomes#

A click shows what a person did. It does not show whether the work succeeded. Record the outcome when your app knows it:
    
    
    import { useCopilotKit } from "@copilotkit/react-core/v2";
    
    function ApproveButton({ dealId }: { dealId: string }) {
      const { copilotkit } = useCopilotKit();
      return (
        <button onClick={() => copilotkit.emitTrajectoryEvent("deal.approved", { dealId })}>
          Approve
        </button>
      );
    }

The event carries the open Thread. Built-in names such as `click` are reserved.

## Start and stop a Trajectory yourself#

Leave out `trajectoryId` on the prop, then call Core when your app decides a session starts:
    
    
    import { useCopilotKit } from "@copilotkit/react-core/v2";
    
    function StartCaptureButton({ projectId }: { projectId: string }) {
      const { copilotkit } = useCopilotKit();
      return (
        <button onClick={() => copilotkit.startTrajectory({ trajectoryId: `${projectId}-${Date.now()}` })}>
          Start capture
        </button>
      );
    }

One Trajectory runs at a time. Starting the same ID again does nothing. `copilotkit.stopTrajectory()` removes every listener and sends queued events once. It does not wait for delivery or retry a failed send.

Sequence numbers (`seq`) increase for the lifetime of the Core instance, including across stop/start cycles. They do not start at 0: each Core instance starts from its creation time, so a page reload or second tab that reuses a Trajectory ID continues above the earlier numbers.

Need capture in an app without CopilotKit? Use the [standalone collector](https://docs.copilotkit.ai/crewai-crews/intelligence/standalone-collector).

### On this page

OverviewTurn on captureHow a click finds its ThreadRecord outcomesStart and stop a Trajectory yourself
