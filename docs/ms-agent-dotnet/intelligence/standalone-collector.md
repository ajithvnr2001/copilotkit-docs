---
url: https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/standalone-collector/
title: Standalone collector
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:18:55.948553+00:00
---

# Standalone collector

> Source: https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/standalone-collector/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMS Agent Framework (.NET)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ms-agent-dotnet)[Quickstart](https://docs.copilotkit.ai/ms-agent-dotnet/quickstart)[Build with agents](https://docs.copilotkit.ai/ms-agent-dotnet/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ms-agent-dotnet/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ms-agent-dotnet/webmcp)

Agent capabilities

Microsoft Agent Framework

[Sub-agents](https://docs.copilotkit.ai/ms-agent-dotnet/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ms-agent-dotnet/learning)

[User Memories](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ms-agent-dotnet/telemetry)[Community frameworks](https://docs.copilotkit.ai/ms-agent-dotnet/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Standalone collector

IntelligenceFeatures

# Standalone collector

Capture clicks, form edits, page changes, and network requests as AG-UI events in any web app, without CopilotKit.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview#

`@copilotkit/learning` captures clicks, form edits, page changes, and network requests as AG-UI `CUSTOM` events. It sends batches to a sink you provide. This standalone integration is experimental and self-hosted.

Capture retains browser-visible text, values, headers, bounded body snapshots, and full URLs by default. See [Captured data](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/captured-data) for fields, limits, and explicit exclusions.

When you are done, your app sends batches of events to your own endpoint. You can also add events for the outcomes that matter to you.

## Capture events#

### Install the package#
    
    
    npm install @copilotkit/learning

### Create a collector and start it#

src/capture.ts
    
    
    import { createCollector, httpSink } from "@copilotkit/learning";
    
    export const collector = createCollector({
      sink: httpSink("/api/learning-events"),
    });
    
    collector.start({ trajectoryId: crypto.randomUUID() });

Before `start()`, the collector installs nothing. Call `start()` only after the person allows capture.

### Add events for outcomes#

Clicks show what a person did. They do not show whether it worked. Emit an event when the outcome is known:
    
    
    collector.emit("report.exported", { format: "csv", rows: 120 });

Use your own names. Built-in names such as `click` are reserved.

### Stop when the session ends#
    
    
    collector.stop();

`stop()` removes every listener and patch, then sends queued events once. It does not wait for delivery or retry a failed send.

Your endpoint now receives batches such as `{ "trajectoryId": "...", "events": [...], "dropped": 0 }`.

## Send events somewhere else#

A sink is a function that receives each batch. Use it to forward events to your own service:
    
    
    import { createCollector } from "@copilotkit/learning";
    import type { LearningBatch } from "@copilotkit/learning";
    
    const collector = createCollector({
      sink: async (batch: LearningBatch) => {
        const response = await fetch("https://events.example.com/ingest", {
          method: "POST",
          headers: { "content-type": "application/json" },
          body: JSON.stringify(batch),
        });
        if (!response.ok) throw new Error(`Capture endpoint returned ${response.status}`);
      },
      ignoreUrls: ["https://events.example.com/"],
    });

Add your sink's URL to `ignoreUrls`, so the collector does not record its own requests. `httpSink` does this for you.

## Add context to clicks#

`enrich` adds fields to each click from the element that was clicked:
    
    
    const collector = createCollector({
      sink: httpSink("/api/learning-events"),
      enrich: (element) => ({
        section: element.closest("[data-section]")?.getAttribute("data-section") ?? null,
      }),
    });

Capture already includes element text, attributes, and live control values. Use `enrich` for additional app context. Use `beforeSend`, capture flags, or `data-copilotkit-ignore` to exclude data.

For every field and control, see [Captured data](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/captured-data). With CopilotKit, use the [`learning` prop](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/capture-interactions) instead.

### On this page

OverviewCapture eventsSend events somewhere elseAdd context to clicks
