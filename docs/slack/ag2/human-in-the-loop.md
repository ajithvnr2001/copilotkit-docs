---
url: https://docs.copilotkit.ai/slack/ag2/human-in-the-loop/
title: Human-in-the-Loop
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:39:18.670707+00:00
---

# Human-in-the-Loop

> Source: https://docs.copilotkit.ai/slack/ag2/human-in-the-loop/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

ChannelSlackAgent backendAG2

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Getting Started

[Overview](https://docs.copilotkit.ai/slack/ag2)[Configure the Channel in Intelligence](https://docs.copilotkit.ai/slack/ag2/intelligence)[Connect and run your agent](https://docs.copilotkit.ai/slack/ag2/connect)

Build

[Tools and context](https://docs.copilotkit.ai/slack/ag2/tools)[Identity and Memory](https://docs.copilotkit.ai/slack/ag2/identity-and-memory)[Rich messages and components](https://docs.copilotkit.ai/slack/ag2/rich-messages)[Interactive messages and approvals](https://docs.copilotkit.ai/slack/ag2/interactive)[Commands and reactions](https://docs.copilotkit.ai/slack/ag2/commands-and-reactions)[Files and multimodal input](https://docs.copilotkit.ai/slack/ag2/files-and-multimodality)[Threads and state](https://docs.copilotkit.ai/slack/ag2/threads-and-state)

Production

[Persistence and scaling](https://docs.copilotkit.ai/slack/ag2/persistence-and-scaling)[History and transcripts](https://docs.copilotkit.ai/slack/ag2/history-and-transcripts)[Deploy and operate](https://docs.copilotkit.ai/slack/ag2/deploy-and-operate)[API reference](https://docs.copilotkit.ai/reference/channels)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[AG2](https://docs.copilotkit.ai/slack/ag2)

# Human-in-the-Loop

Create frontend tools and use them within your AG2 agent for human-in-the-loop interactions.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

This video shows the result of `npx copilotkit@latest init` with the implementation section applied to it.

## What is this?#

Frontend tools enable you to define client-side functions that your AG2 agent can invoke, with execution happening entirely in the user's browser. When your agent calls a frontend tool, the logic runs on the client side, giving you direct access to the frontend environment.

This can be utilized to let [your agent control the UI](https://docs.copilotkit.ai/ag2/frontend-tools), [generative UI](https://docs.copilotkit.ai/ag2/frontend-tools), or for Human-in-the-loop interactions.

In this guide, we cover the use of frontend tools for Human-in-the-loop.

CopilotKit consumes AG-UI protocol events streamed by AG2 over `/chat`. See the [AG2 AG-UI integration docs](https://docs.ag2.ai/docs/user-guide/ag-ui/).

## When should I use this?#

Use frontend tools when you need your agent to interact with client-side primitives such as:

  * Reading or modifying React component state
  * Accessing browser APIs like localStorage, sessionStorage, or cookies
  * Triggering UI updates or animations
  * Interacting with third-party frontend libraries
  * Performing actions that require the user's immediate browser context



## Implementation#

### Run and connect your agent#

Start your AG2 backend on a `/chat` endpoint and connect your frontend to it with CopilotKit.

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

### Set up your AG2 backend#

The frontend tool emits AG-UI tool events. AG2 can consume those events, then persist the user decision to shared state:

agent.py
    
    
    from typing import Annotated
    
    from fastapi import FastAPI, Header
    from fastapi.responses import StreamingResponse
    from pydantic import Field
    
    from ag2 import Agent, Context, tool
    from ag2.ag_ui import AGUIStream, RunAgentInput
    from ag2.config import OpenAIResponsesConfig
    
    @tool
    def store_user_choice(
        choice: Annotated[str, Field(description="The option selected by the user")],
        context: Context,
    ) -> str:
        """Store the latest user choice in shared state."""
        context.variables["hitl"] = {"latest_choice": choice}
        return f"Stored choice: {choice}"
    
    agent = Agent(
        name="assistant",
        prompt=(
            "When you need the user to choose, call the frontend tool `offerOptions`. "
            "After it returns, call `store_user_choice` with the selected value."
        ),
        config=OpenAIResponsesConfig(model="gpt-5.5"),
        tools=[store_user_choice],
    )
    
    stream = AGUIStream(agent)
    app = FastAPI()
    
    @app.post("/chat")
    async def run_agent(
        message: RunAgentInput,
    accept: str | None = Header(None),
    ) -> StreamingResponse:
        return StreamingResponse(
            stream.dispatch(message, accept=accept),
            media_type=accept or "text/event-stream",
        )

The frontend tools are automatically populated by CopilotKit through the AG-UI protocol and are available to your AG2 backend. When a tool updates `context.variables`, `AGUIStream` automatically emits a `STATE_SNAPSHOT` event at the end of the run — no manual event construction needed.

### Try it out#

You've now given your agent the ability to show the user two options and have them select one. The agent will then be aware of the user's choice and can use it in subsequent steps.
    
    
    Can you show me two good options for a restaurant name?

## Approve a tool call with interrupts#

Frontend tools put the decision in the browser. AG-UI 1.0 also lets the **backend** pause a run and ask: a tool wrapped in `ApprovalRequired` is held until the user approves or rejects the call. AG2 sends the held call to the client as an AG-UI interrupt, and CopilotKit's `useInterrupt` renders it.

### Gate the tool in AG2#

tools.py
    
    
    from typing import Annotated
    
    from pydantic import Field
    
    from ag2 import Context, tool
    from ag2.middleware.builtin.tools.approval import ApprovalRequired
    
    @tool(
        description="Save a city to the user's favorites. The user confirms before anything is saved.",
        middleware=[
            ApprovalRequired("Save this city to your favorites?\n{tool_arguments}", allow_always=False)
        ],
    )
    async def save_favorite_city(
        context: Context,
        city: Annotated[str, Field(description="The city name to save, e.g. 'Lisbon'")],
    ) -> list[str]:
        favorites = list(context.variables.get("favorites", []))
        if city not in favorites:
            favorites.append(city)
        context.variables["favorites"] = favorites
        return favorites

Serve the agent with `AGUIStream` as usual. Don't set a `hitl_hook` on the agent: with one, AG2 asks in-process and no interrupt reaches the browser.

### Answer it with `useInterrupt`#

The run ends with an interrupt of reason `tool_call`. The backend reads the answer as a boolean, so `resolve(true)` approves the call and `resolve(false)` refuses it. A refusal does not fail the run: the model is told the call was refused and carries on.

page.tsx
    
    
    import { useInterrupt } from "@copilotkit/react-core/v2"; 
    
    export function Page() {
      useInterrupt({
        agentId: "agenticChatAgent",
        render: ({ interrupt, resolve }) => (
          <div>
            <p>{interrupt?.message ?? "The assistant needs your confirmation."}</p>
            <button onClick={() => resolve(true)}>Approve</button>
            <button onClick={() => resolve(false)}>Reject</button>
          </div>
        ),
      });
    
      // ...
    }

### Try it out#
    
    
    Save Lisbon to my favorites

The approval card appears in the chat. Approve it and the city shows up in the [shared state](https://docs.copilotkit.ai/ag2/shared-state).

`useInterrupt().resolve()` and `.cancel()` send no `metadata` in the resume entry. That is enough for a gated tool call like the one above, but not for an AG2 server built with `require_resume_proof=True`, which needs the interrupt's `metadata` copied into the resume entry. See [Asking the human a question](https://docs.ag2.ai/docs/user-guide/ag-ui/overview#asking-the-human-a-question) in the AG2 docs.

A held turn lives in the AG2 process that served the run, so the resuming run must reach that same process. See [the AG2 deployment notes](https://docs.ag2.ai/docs/user-guide/ag-ui/overview#deployment-a-held-turn-lives-in-one-process) before running several replicas.

### On this page

What is this?When should I use this?ImplementationApprove a tool call with interrupts
