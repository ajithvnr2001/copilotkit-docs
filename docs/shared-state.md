---
url: https://docs.copilotkit.ai/shared-state/
title: Shared State
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:29.715821+00:00
---

# Shared State

> Source: https://docs.copilotkit.ai/shared-state/

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

[Shared State](https://docs.copilotkit.ai/shared-state)[Render agent state in your app](https://docs.copilotkit.ai/shared-state/rendering-in-app)[State Streaming](https://docs.copilotkit.ai/shared-state/streaming)[Agent Read-Only Context](https://docs.copilotkit.ai/shared-state/agent-readonly)

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

Shared State

InteractivityShared state

# Shared State

Bidirectional state sharing between your app and the Built-in Agent.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Share state bidirectionally between your React app and the Built-in Agent. Your app can read and write agent state, and the agent can update state that your UI reacts to in real time.

## What is this?#

Shared state lets your frontend and agent stay in sync. The agent can update state (like adding items to a list or changing a setting), and your React components re-render automatically. Your app can also write state that the agent can read.

## When should I use this?#

  * The agent should be able to modify your app's UI (add items, update fields, toggle settings)
  * You want real-time UI updates as the agent works
  * Your app needs to read what the agent is doing (progress indicators, intermediate results)



For a complete example of selecting a prepared control with structured AI judgments and returning user actions to the agent, follow the [CopilotKit + Jev cookbook](https://docs.copilotkit.ai/cookbook/jev-generative-ui).

## Reading agent state#

Use the `useAgent` hook to access the agent's current state:

app/page.tsx
    
    
    import { useAgent } from "@copilotkit/react-core/v2"; 
    
    function TaskBoard() {
      const { agent } = useAgent();
    
      // Read state set by the agent
      const tasks = (agent.state.tasks as any[]) ?? [];
    
      return (
        <div>
          <h2>Tasks</h2>
          <ul>
            {tasks.map((task, i) => (
              <li key={i}>
                {task.title} — {task.status}
              </li>
            ))}
          </ul>
        </div>
      );
    }

`agent.state` is reactive — your component re-renders automatically when the agent updates state.

## Writing state from the frontend#

You can also push state from the frontend to the agent:

app/page.tsx
    
    
    import { useAgent } from "@copilotkit/react-core/v2";
    
    function SettingsPanel() {
      const { agent } = useAgent();
    
      const handleThemeChange = (theme: string) => {
        agent.setState({ 
          ...agent.state, 
          userPreferences: { theme }, 
        }); 
      };
    
      return (
        <div>
          <button onClick={() => handleThemeChange("dark")}>Dark Mode</button>
          <button onClick={() => handleThemeChange("light")}>Light Mode</button>
        </div>
      );
    }

## How it works#

The Built-in Agent automatically has access to state tools (`AGUISendStateSnapshot` and `AGUISendStateDelta`) through the AG-UI protocol. When the agent calls these tools:

  1. The agent sends a state update (full snapshot or delta)
  2. The CopilotKit runtime delivers the update to the frontend via SSE
  3. Your `useAgent` hook receives the update and triggers a re-render



No additional backend configuration is required — state tools are available to the Built-in Agent by default.

## Example: collaborative todo list#

Here's a complete example where the agent can add and manage tasks:

app/page.tsx
    
    
    import { CopilotChat } from "@copilotkit/react-core/v2";
    import { useAgent } from "@copilotkit/react-core/v2";
    
    function TodoApp() {
      const { agent } = useAgent();
    
      const todos = (agent.state.todos as any[]) ?? [];
    
      return (
        <div style={{ display: "flex", gap: "1rem" }}>
          <div>
            <h2>My Todos</h2>
            <ul>
              {todos.map((todo, i) => (
                <li key={i} style={{ textDecoration: todo.done ? "line-through" : "none" }}>
                  {todo.text}
                </li>
              ))}
            </ul>
          </div>
          <CopilotChat
            labels={{
              welcomeMessageText: "I can help manage your todos. Try 'Add a task to buy groceries'.",
            }}
          />
        </div>
      );
    }

When you tell the agent "Add a task to buy groceries", it updates the shared state and your todo list renders the new item immediately.

### On this page

What is this?When should I use this?Reading agent stateWriting state from the frontendHow it worksExample: collaborative todo list
