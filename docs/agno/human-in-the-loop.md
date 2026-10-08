---
url: https://docs.copilotkit.ai/agno/human-in-the-loop/
title: Human-in-the-Loop
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:47:07.175979+00:00
---

# Human-in-the-Loop

> Source: https://docs.copilotkit.ai/agno/human-in-the-loop/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAgno

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/agno)[Quickstart](https://docs.copilotkit.ai/agno/quickstart)[Build with agents](https://docs.copilotkit.ai/agno/build-with-agents)[Intelligence](https://docs.copilotkit.ai/agno/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/agno/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/agno/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/agno/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/agno/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/agno/learning)

[User Memories](https://docs.copilotkit.ai/agno/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/agno/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/agno/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/agno/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/agno/intelligence/analytics)[Channels](https://docs.copilotkit.ai/agno/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/agno/telemetry)[Community frameworks](https://docs.copilotkit.ai/agno/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

InteractivityHuman-in-the-loop

# Human-in-the-Loop

Create frontend tools and use them within your Agno agent for human-in-the-loop interactions.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

## What is this?#

Frontend tools enable you to define client-side functions that your Agno agent can invoke, with execution happening entirely in the user's browser. When your agent calls a frontend tool, the logic runs on the client side, giving you direct access to the frontend environment.

This can be utilized to let [your agent control the UI](https://docs.copilotkit.ai/agno/frontend-tools), [generative UI](https://docs.copilotkit.ai/agno/frontend-tools), or for Human-in-the-loop interactions.

In this guide, we cover the use of frontend tools for Human-in-the-loop.

## When should I use this?#

Use frontend tools when you need your agent to interact with client-side primitives such as:

  * Reading or modifying React component state
  * Accessing browser APIs like localStorage, sessionStorage, or cookies
  * Triggering UI updates or animations
  * Interacting with third-party frontend libraries
  * Performing actions that require the user's immediate browser context



## Implementation#

Configure session storage

Agno must store the paused run before a frontend tool can return its result. Configure a database on the `Agent` that owns the external tool.

Install the SQLite dependency:
    
    
    pip install sqlalchemy

Use a project-relative SQLite file for local development:
    
    
    from agno.agent import Agent
    from agno.db.sqlite import SqliteDb
    
    db = SqliteDb(db_file="tmp/agno.db")
    
    agent = Agent(
        # ...
        db=db,
    )

The deployed showcase uses `/tmp/agno.db` because its application directory is read-only to the runtime user.

For production, use durable shared storage such as `PgDb`. An ephemeral container file cannot resume a run on another instance.

### Define the frontend tool in your Agno agent#

In your Agno agent, define a tool with the `@tool(external_execution=True)` decorator:

tools/frontend.py
    
    
    from agno.tools import tool
    
    @tool(external_execution=True)
    def offerOptions(option_1: str, option_2: str):
        """
        Give the user a choice between two options and have them select one.
    
        Args:
            option_1: str: The first option
            option_2: str: The second option
        """

Register the tool with your agent:

agent.py
    
    
    from agno.agent import Agent
    from agno.db.sqlite import SqliteDb
    from agno.models.openai import OpenAIChat
    from agno.os import AgentOS
    from agno.os.interfaces.agui import AGUI
    from tools.frontend import offerOptions
    
    db = SqliteDb(db_file="tmp/agno.db")
    
    agent = Agent(
        model=OpenAIChat(id="gpt-5.4"),
        tools=[offerOptions],
        db=db,
        description="A helpful assistant that can answer questions and provide information.",
        instructions="Be helpful and friendly. Format your responses using markdown where appropriate.",
    )
    
    agent_os = AgentOS(agents=[agent], interfaces=[AGUI(agent=agent)])
    app = agent_os.get_app()
    
    if __name__ == "__main__":
        agent_os.serve(app="main:app", port=8000, reload=True)

### Create a frontend human-in-the-loop tool#

Frontend tools can be leveraged in a variety of ways. One of those ways is to have a human-in-the-loop flow where the response of the tool is gated by a user's decision.

In this example we will simulate an "approval" flow for executing a command. Use the `useHumanInTheLoop` hook to create a tool that prompts the user for approval.

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

### Try it out!#

You've now given your agent the ability to show the user two options and have them select one. The agent will then be aware of the user's choice and can use it in subsequent steps.
    
    
    Can you show me two good options for a restaurant name?

### On this page

What is this?When should I use this?Implementation
