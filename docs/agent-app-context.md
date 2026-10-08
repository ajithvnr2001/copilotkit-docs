---
url: https://docs.copilotkit.ai/agent-app-context/
title: Agent Context
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:45:39.356941+00:00
---

# Agent Context

> Source: https://docs.copilotkit.ai/agent-app-context/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/)[Quickstart](https://docs.copilotkit.ai/quickstart)[Build with agents](https://docs.copilotkit.ai/build-with-agents)[Intelligence](https://docs.copilotkit.ai/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/webmcp)

Agent capabilities

Built-in Agent

[Sub-agents](https://docs.copilotkit.ai/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/learning)

[User Memories](https://docs.copilotkit.ai/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/intelligence/analytics)[Channels](https://docs.copilotkit.ai/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/telemetry)[Community frameworks](https://docs.copilotkit.ai/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[CopilotKit's Built-in Agent](https://docs.copilotkit.ai/)

# Agent Context

Share app-specific context with your Built-in Agent.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Share your application's state and context with the Built-in Agent using the `useAgentContext` hook. The Built-in Agent receives this context automatically, with no backend configuration.

That last part is specific to the Built-in Agent. An agent you host yourself receives the same entries on the AG-UI run input, and each framework decides what reaches the model from there — see your framework's own Agent App Context page, such as [ADK](https://docs.copilotkit.ai/adk/agent-app-context), [LangGraph](https://docs.copilotkit.ai/langgraph/agent-app-context) or [Mastra](https://docs.copilotkit.ai/mastra/agent-app-context).

## What is this?#

The `useAgentContext` hook lets you register app-specific data that gets included in the agent's context. This could be the current user, page content, shopping cart items, or any data that helps the agent provide relevant responses.

## When should I use this?#

  * You want the agent to know about the current state of your app
  * You need the agent to reference user-specific data (name, preferences, role)
  * The agent should be aware of what page or view the user is on
  * You want to provide domain-specific data without hardcoding it into the system prompt



## Implementation#

Context values arrive as JSON strings

The AG-UI protocol defines a context value as a string. Therefore `useAgentContext` calls `JSON.stringify` on any `value` that is not already a string, and your agent receives the JSON text instead of the object or the array.

Parse the value before you read a field from it. Use `json.loads(item["value"])` in Python, or `JSON.parse(item.value)` in TypeScript. If you skip the parse step, an index such as `colleagues[0]` returns a single character, and a shape check such as `isinstance(value, list)` can never pass.

Do not stringify the value again, because that produces double encoding. A `value` that is already a string is sent unchanged, so no parse step is needed for it.

### Register context in your component#

Use `useAgentContext` to share any data with the agent:

components/Dashboard.tsx
    
    
    "use client"; // only necessary for Next.js App Router
    import { useAgentContext } from "@copilotkit/react-core/v2"; 
    import { useState } from "react";
    
    export function Dashboard() {
      const [user] = useState({
        name: "Jane Smith",
        role: "Engineering Manager",
        team: "Platform",
      });
    
      const [projects] = useState([
        { id: 1, name: "Auth Redesign", status: "in-progress" },
        { id: 2, name: "API v2", status: "planning" },
      ]);
    
      // Share user info with the agent
      useAgentContext({
        description: "The currently logged-in user",
        value: user,
      });
    
      // Share project data with the agent
      useAgentContext({
        description: "The user's active projects",
        value: projects,
      });
    
      return <div>{/* Your dashboard UI */}</div>;
    }

### That's it — no backend setup needed#

Unlike LangGraph where you need to configure agent state to receive context, the Built-in Agent handles this automatically. The context you register is included in the agent's system prompt, so it can reference your app data immediately.
    
    
    User: "What projects am I working on?"
    Agent: "You're working on two projects:
      1. Auth Redesign (in progress)
      2. API v2 (planning)"

## Multiple contexts#

You can call `useAgentContext` multiple times across different components. All registered contexts are combined and sent to the agent:

components/UserInfo.tsx
    
    
    useAgentContext({
      description: "Current user profile",
      value: { name: "Jane", role: "Manager" },
    });

components/PageContext.tsx
    
    
    useAgentContext({
      description: "The page the user is currently viewing",
      value: { page: "settings", section: "notifications" },
    });

The agent sees both contexts and can reference either when responding.

## Dynamic context#

Context updates automatically when the underlying data changes:
    
    
    export function TaskList() {
      const [tasks, setTasks] = useState([]);
    
      // Context updates whenever tasks change
      useAgentContext({
        description: "The user's current task list",
        value: tasks,
      });
    
      return (
        <div>
          {/* When tasks are added/removed, the agent sees the updated list */}
        </div>
      );
    }

### On this page

What is this?When should I use this?ImplementationRegister context in your componentThat's it — no backend setup neededMultiple contextsDynamic context
