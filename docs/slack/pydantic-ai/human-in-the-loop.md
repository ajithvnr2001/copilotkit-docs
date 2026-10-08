---
url: https://docs.copilotkit.ai/slack/pydantic-ai/human-in-the-loop/
title: Human-in-the-Loop
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:39:48.908580+00:00
---

# Human-in-the-Loop

> Source: https://docs.copilotkit.ai/slack/pydantic-ai/human-in-the-loop/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

ChannelSlackAgent backendPydanticAI

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Getting Started

[Overview](https://docs.copilotkit.ai/slack/pydantic-ai)[Configure the Channel in Intelligence](https://docs.copilotkit.ai/slack/pydantic-ai/intelligence)[Connect and run your agent](https://docs.copilotkit.ai/slack/pydantic-ai/connect)

Build

[Tools and context](https://docs.copilotkit.ai/slack/pydantic-ai/tools)[Identity and Memory](https://docs.copilotkit.ai/slack/pydantic-ai/identity-and-memory)[Rich messages and components](https://docs.copilotkit.ai/slack/pydantic-ai/rich-messages)[Interactive messages and approvals](https://docs.copilotkit.ai/slack/pydantic-ai/interactive)[Commands and reactions](https://docs.copilotkit.ai/slack/pydantic-ai/commands-and-reactions)[Files and multimodal input](https://docs.copilotkit.ai/slack/pydantic-ai/files-and-multimodality)[Threads and state](https://docs.copilotkit.ai/slack/pydantic-ai/threads-and-state)

Production

[Persistence and scaling](https://docs.copilotkit.ai/slack/pydantic-ai/persistence-and-scaling)[History and transcripts](https://docs.copilotkit.ai/slack/pydantic-ai/history-and-transcripts)[Deploy and operate](https://docs.copilotkit.ai/slack/pydantic-ai/deploy-and-operate)[API reference](https://docs.copilotkit.ai/reference/channels)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[PydanticAI](https://docs.copilotkit.ai/slack/pydantic-ai)

# Human-in-the-Loop

Create frontend tools and use them within your Pydantic AI agent for human-in-the-loop interactions.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

## What is this?#

Frontend tools enable you to define client-side functions that your Pydantic AI agent can invoke, with execution happening entirely in the user's browser. When your agent calls a frontend tool, the logic runs on the client side, giving you direct access to the frontend environment.

This can be utilized to let [your agent control the UI](https://docs.copilotkit.ai/pydantic-ai/frontend-tools), [generative UI](https://docs.copilotkit.ai/pydantic-ai/frontend-tools), or for Human-in-the-loop interactions.

In this guide, we cover the use of frontend tools for Human-in-the-loop.

## When should I use this?#

Use frontend tools when you need your agent to interact with client-side primitives such as:

  * Reading or modifying React component state
  * Accessing browser APIs like localStorage, sessionStorage, or cookies
  * Triggering UI updates or animations
  * Interacting with third-party frontend libraries
  * Performing actions that require the user's immediate browser context



## Implementation#

### Run and connect your agent#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/langgraph/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point as this guide uses it as a starting point.

### Create a frontend human-in-the-loop tool#

Frontend tools can be leveraged in a variety of ways. One of those ways is to have a human-in-the-loop flow where the response of the tool is gated by a user's decision.

In this example we will simulate an "approval" flow for executing a command. First, use the `useHumanInTheLoop` hook to create a tool that prompts the user for approval.

page.tsx
    
    
    import { useHumanInTheLoop } from "@copilotkit/react-core/v2"
    import { z } from "zod"
    
    export function Page() {
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

### Set up your agent#

Pydantic AI automatically picks up human-in-the-loop tools when you create your agent. No special configuration is needed:

agent.py
    
    
    from pydantic_ai import Agent
    from pydantic_ai.ui.ag_ui import AGUIAdapter
    from starlette.applications import Starlette
    from starlette.requests import Request
    from starlette.responses import Response
    from starlette.routing import Route
    
    agent = Agent('openai:gpt-5.4-mini')
    
    
    async def run_agent(request: Request) -> Response:
        return await AGUIAdapter.dispatch_request(request, agent=agent)
    
    
    app = Starlette(routes=[Route("/", run_agent, methods=["POST"])])

The frontend tools are automatically populated by CopilotKit through the AG-UI protocol and are available to your agent.

### Try it out!#

You've now given your agent the ability to show the user two options and have them select one. The agent will then be aware of the user's choice and can use it in subsequent steps.
    
    
    Can you show me two good options for a restaurant name?

### On this page

What is this?When should I use this?Implementation
