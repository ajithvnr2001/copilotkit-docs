---
url: https://docs.copilotkit.ai/langgraph-fastapi/generative-ui/your-components/interactive/
title: Interactive
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:05:17.533352+00:00
---

# Interactive

> Source: https://docs.copilotkit.ai/langgraph-fastapi/generative-ui/your-components/interactive/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (FastAPI)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-fastapi)[Quickstart](https://docs.copilotkit.ai/langgraph-fastapi/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-fastapi/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-fastapi/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/langgraph-fastapi/webmcp)

Agent capabilities

LangGraph (FastAPI)

[Sub-agents](https://docs.copilotkit.ai/langgraph-fastapi/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/langgraph-fastapi/learning)

[User Memories](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/analytics)[Channels](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/langgraph-fastapi/telemetry)[Community frameworks](https://docs.copilotkit.ai/langgraph-fastapi/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[LangGraph (FastAPI)](https://docs.copilotkit.ai/langgraph-fastapi)[Build Generative UI](https://docs.copilotkit.ai/langgraph-fastapi/generative-ui)Your Components

# Interactive

Create components that your agent can use to interact with the user.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

## What is this?#

Frontend tools enable you to define client-side functions that your LangGraph agent can invoke, with execution happening entirely in the user's browser. When your agent calls a frontend tool, the logic runs on the client side, giving you direct access to the frontend environment.

This can be utilized for to let [your agent control the UI](https://docs.copilotkit.ai/langgraph/frontend-tools), [generative UI](https://docs.copilotkit.ai/langgraph/frontend-tools), or for Human-in-the-loop interactions.

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

In this example we will simulate a "approval" flow for executing a command. First, use the `useHumanInTheLoop` hook to create a tool that prompts the user for approval.

page.tsx
    
    
    import { useHumanInTheLoop } from "@copilotkit/react-core/v2"
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
              <button onClick={() => respond?.(`Command is APPROVED`)}>Approve</button>
              <button onClick={() => respond?.(`Command is DENIED`)}>Deny</button>
            </div>
          );
        },
      });
    
      // ...
    }

### Install the CopilotKit SDK#

Now, we'll need to modify the agent to access these frontend tools. In your terminal, navigate to your agent's folder and continue from there!

Any LangGraph agent can be used with CopilotKit. However, creating deep agentic experiences with CopilotKit requires our LangGraph SDK.

PythonTypeScript

uvpoetrypipconda
    
    
    uv add copilotkit
    
    
    poetry add copilotkit
    
    
    pip install copilotkit --extra-index-url https://copilotkit.gateway.scarf.sh/simple/
    
    
    conda install copilotkit -c copilotkit-channel

`npm npm install @copilotkit/sdk-js `

### Inheriting from CopilotKitState#

To access the frontend tools provided by CopilotKit, you can inherit from CopilotKitState in your agent's state definition:

PythonTypeScript

agent.py
    
    
    from copilotkit import CopilotKitState 
    
    class YourAgentState(CopilotKitState): 
        your_additional_properties: str

agent-js/src/agent.ts
    
    
    import { StateSchema } from "@langchain/langgraph";
    import { CopilotKitStateSchema } from "@copilotkit/sdk-js/langgraph"; 
    import { z } from "zod";
    
    export const YourAgentStateSchema = new StateSchema({
        yourAdditionalProperty: z.string(),
        ...CopilotKitStateSchema.fields, 
    });
    export type YourAgentState = typeof YourAgentStateSchema.State;

By doing this, your agent's state will include the `copilotkit` property, which contains the frontend tools that can be accessed and invoked.

### Accessing Frontend Tools#

Once your agent's state includes the `copilotkit` property, you can access the frontend tools and utilize them within your agent's logic.

Here's how you can call a frontend tool from your agent:

DemoCode

## What is this?#

Frontend tools enable you to define client-side functions that your agent can invoke, with execution happening entirely in the user's browser. When your agent calls a frontend tool, the logic runs on the client side, giving you direct access to the frontend environment.

This can be utilized to let your agent control the UI, for generative UI, or for Human-in-the-loop interactions. In this guide, we cover the use of frontend tools driving and interacting with the UI.

## When should I use this?#

Use frontend tools when you need your agent to interact with client-side primitives such as:

  * Reading or modifying React component state
  * Accessing browser APIs like localStorage, sessionStorage, or cookies
  * Triggering UI updates or animations
  * Interacting with third-party frontend libraries
  * Performing actions that require the user's immediate browser context



## Create a frontend tool#

Use the `useFrontendTool` hook to create a tool that your agent can call from the client side:

page.tsx
    
    
    import { z } from "zod";
    import { useFrontendTool } from "@copilotkit/react-core/v2"; 
    
    export function Page() {
      // ...
    
      useFrontendTool({
        name: "sayHello",
        description: "Say hello to the user",
        parameters: z.object({
          name: z.string().describe("The name of the user to say hello to"),
        }),
        handler: async ({ name }) => {
          alert(`Hello, ${name}!`);
          return `Said hello to ${name}!`;
        },
      });
    
      // ...
    }

These tools are automatically populated by CopilotKit and are compatible with LangChain's tool call definitions, making it straightforward to integrate them into your agent's workflow.

### Give it a try!#

You've now given your agent the ability to directly call any frontend tools you've defined. These tools will be available to the agent where they can be used as needed.

### On this page

What is this?When should I use this?Implementation
