---
url: https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/your-components/interactive/
title: Interactive
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:20:37.364801+00:00
---

# Interactive

> Source: https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/your-components/interactive/

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

Your Components

[Display-only](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/your-components/display-only)[Interactive](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/your-components/interactive)

Declarative Generative UI (A2UI)

[Readables](https://docs.copilotkit.ai/ms-agent-harness-dotnet/agent-app-context)[Copilot Runtime](https://docs.copilotkit.ai/ms-agent-harness-dotnet/copilot-runtime)[AG-UI](https://docs.copilotkit.ai/ms-agent-harness-dotnet/ag-ui)

Troubleshooting Copilots

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

Agent capabilitiesMS Agent Harness (.NET)Your Components

# Interactive

Create components that your agent can use to interact with the user.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

## What is this?

Frontend tools enable you to define client-side functions that your agent can invoke, with execution happening entirely in the user's browser. When your agent calls a frontend tool, the logic runs on the client side, giving you direct access to the frontend environment.

This can be utilized for UI control, generative UI, or Human-in-the-loop interactions. In this guide, we cover the use of frontend tools for Human-in-the-loop.

## When should I use this?

Use frontend tools when you need your agent to interact with client-side primitives such as:

  * Reading or modifying React component state
  * Accessing browser APIs like localStorage, sessionStorage, or cookies
  * Triggering UI updates or animations
  * Interacting with third-party frontend libraries
  * Performing actions that require the user's immediate browser context



## Create a frontend human-in-the-loop tool

Frontend tools can be leveraged in a variety of ways. One of those ways is to have a human-in-the-loop flow where the response of the tool is gated by a user's decision.

In this example we will simulate an "approval" flow for executing a command. Use the `useHumanInTheLoop` hook to create a tool that prompts the user for approval.

page.tsx
    
    
    import { useHumanInTheLoop } from "@copilotkit/react-core/v2"; 
    import { z } from "zod";
    
    export function Page() {
      // ...
    
      useHumanInTheLoop({
        name: "humanApprovedCommand",
        description: "Ask human for approval to run a command.",
        parameters: z.object({
          command: z.string().describe("The command to run"),
        }),
        render: ({ args, respond, status }) => {
          if (status !== "executing") return <></>;
          return (
            <div>
              <pre>{args.command}</pre>
              <button onClick={() => respond?.(`Tell the user the command ran`)}>
                Approve
              </button>
              <button
                onClick={() => respond?.(`Tell the user the command wasn't run`)}
              >
                Deny
              </button>
            </div>
          );
        },
      });
    
      // ...
    }
