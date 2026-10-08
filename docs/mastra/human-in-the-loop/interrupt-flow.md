---
url: https://docs.copilotkit.ai/mastra/human-in-the-loop/interrupt-flow/
title: Interrupts (Not Supported)
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:16:38.428528+00:00
---

# Interrupts (Not Supported)

> Source: https://docs.copilotkit.ai/mastra/human-in-the-loop/interrupt-flow/

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

On this page

[Mastra](https://docs.copilotkit.ai/mastra)[Human-in-the-Loop](https://docs.copilotkit.ai/mastra/human-in-the-loop)

# Interrupts (Not Supported)

Mastra does not support native interrupt flow. Use the tool-based HITL approach instead.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

**Mastra does not support native interrupt flow.** The framework lacks LangGraph-style `interrupt()` primitives that pause execution mid-tool and emit AG-UI interrupt events. This page documents the interrupt pattern for reference, but it **will not work** with Mastra.

For working Human-in-the-Loop functionality with Mastra, use the [tool-based approach](https://docs.copilotkit.ai/mastra/human-in-the-loop/tool-based) with `useHumanInTheLoop` instead.

## What are interrupts?#

Some frameworks (like LangGraph) provide native interrupt capabilities where tools can pause their own execution mid-stream via an `interrupt()` or `suspend()` call, emit an AG-UI interrupt event to the frontend, and wait for the user's response before resuming. CopilotKit's `useInterrupt` hook captures these events and renders custom UI.

## Why doesn't Mastra support this?#

Mastra does not emit AG-UI interrupt events. While Mastra has a `suspend()` API for tool approval workflows, it operates within Mastra's own execution model and does not integrate with CopilotKit's interrupt handling via the AG-UI protocol. Any `useInterrupt` hook in a Mastra application will listen for events that never arrive, leaving the UI stuck on tool-call placeholders.

## What should I use instead?#

**Use the tool-based approach with`useHumanInTheLoop`.** This is the supported and working pattern for Mastra:

### Register a frontend tool#

Define a frontend tool that renders UI and waits for the user's response:

ui/app/page.tsx
    
    
    import { useHumanInTheLoop } from "@copilotkit/react-core/v2";
    import { z } from "zod";
    
    function YourMainContent() {
      useHumanInTheLoop({
        agentId: "my-agent",
        name: "confirm_action",
        description: "Ask the user to confirm before performing a critical action",
        parameters: z.object({
          action: z.string().describe("Description of the action to confirm"),
        }),
        render: ({ args, respond }) => {
          if (!respond) return null;
          return (
            <div>
              <p>{args.action}</p>
              <button onClick={() => respond({ confirmed: true })}>
                Approve
              </button>
              <button onClick={() => respond({ confirmed: false })}>
                Reject
              </button>
            </div>
          );
        },
      });
    
      return <div>{/* Your UI */}</div>;
    }

### Agent automatically uses the tool#

Mastra natively supports the AG-UI protocol. When your agent calls the `confirm_action` tool (defined on the frontend), CopilotKit automatically routes the call to your `useHumanInTheLoop` handler, renders the UI, and waits for the user's response.

No backend tool definition is needed—the frontend tool registration is sufficient.

### Give it a try#

Ask your agent something that requires confirmation:
    
    
    Can you delete all inactive user accounts?

The agent will call the `confirm_action` tool, render your approval UI, and wait for the user's response before continuing.

## Full working example#

For a complete implementation, see the [tool-based Human-in-the-Loop guide](https://docs.copilotkit.ai/mastra/human-in-the-loop/tool-based), which includes:

  * Multiple frontend tools with different UI patterns
  * Parameter validation with Zod schemas
  * Error handling and loading states
  * Production-ready examples



## Comparison: Interrupts vs. Tool-based#

Feature| Interrupts (LangGraph)| Tool-based (Mastra)  
---|---|---  
**Backend support**|  ✅ Native `interrupt()`| ❌ No interrupt events  
**Frontend hook**| `useInterrupt`| `useHumanInTheLoop`  
**Execution model**|  Tool pauses mid-execution| Agent calls frontend tool  
**When to use**|  LangGraph, frameworks with native interrupt support| Mastra, frameworks without interrupt primitives  
**Works with Mastra?**|  ❌ No| ✅ Yes  
  
* * *

**Ready to implement HITL with Mastra?** Head to the [tool-based approach guide](https://docs.copilotkit.ai/mastra/human-in-the-loop/tool-based) for working examples and best practices.

### On this page

What are interrupts?Why doesn't Mastra support this?What should I use instead?Full working exampleComparison: Interrupts vs. Tool-based
