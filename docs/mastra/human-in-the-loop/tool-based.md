---
url: https://docs.copilotkit.ai/mastra/human-in-the-loop/tool-based/
title: Tool-based
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:16:38.372588+00:00
---

# Tool-based

> Source: https://docs.copilotkit.ai/mastra/human-in-the-loop/tool-based/

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

# Tool-based

Implement HITL with Mastra using frontend tools that render UI and collect user input.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

## What is this?#

CopilotKit lets you add custom UI to take user input and then pass it back to the agent upon completion. This approach uses `useHumanInTheLoop` to register a frontend tool that renders a UI component and waits for the user's response.

Looking for an approach where tools can pause mid-execution and wait for user input? See the [interrupt-based approach](https://docs.copilotkit.ai/mastra/human-in-the-loop/interrupt-flow).

## Why should I use this?#

Human-in-the-loop is a powerful way to implement complex workflows that are production ready. By having a human in the loop, you can ensure that the agent is always making the right decisions and ultimately is being steered in the right direction.

## Implementation#

### Run and connect your agent#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/langgraph/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point as this guide uses it as a starting point.

### Add a human-in-the-loop tool to your Frontend#

First, we'll create a component that offers the user options and waits for their selection.

ui/app/page.tsx
    
    
    import { useHumanInTheLoop } from "@copilotkit/react-core/v2"
    import { z } from "zod"
    
    function YourMainContent() {
      // ...
    
      useHumanInTheLoop({
        name: "offerOptions",
        description: "Give the user a choice between two options and have them select one.",
        parameters: z.object({
          option_1: z.string().describe("The first option"),
          option_2: z.string().describe("The second option"),
        }),
        render: ({ args, respond }) => {
          if (!respond) return <></>;
          return (
            <div>
              <button onClick={() => respond(`${args.option_1} was selected`)}>{args.option_1}</button>
              <button onClick={() => respond(`${args.option_2} was selected`)}>{args.option_2}</button>
            </div>
          );
        },
      });
    
      // ...
    }

### Setup the Mastra Agent#

On the agent side, we are already done! Mastra natively supports the AG-UI protocol and will automatically pass control back to the frontend when the `offerOptions` tool is called by the agent.

### Give it a try!#

Try asking your agent something that requires a choice.
    
    
    Can you show me two good options for a restaurant name?"

You'll see that the agent will present two options and wait for you to select one before continuing.

### On this page

What is this?Why should I use this?Implementation
