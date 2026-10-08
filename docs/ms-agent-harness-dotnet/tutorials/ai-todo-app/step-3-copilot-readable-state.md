---
url: https://docs.copilotkit.ai/ms-agent-harness-dotnet/tutorials/ai-todo-app/step-3-copilot-readable-state/
title: Step 3: Copilot Readable State
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:21:15.692566+00:00
---

# Step 3: Copilot Readable State

> Source: https://docs.copilotkit.ai/ms-agent-harness-dotnet/tutorials/ai-todo-app/step-3-copilot-readable-state/

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

On this page

[MS Agent Harness (.NET)](https://docs.copilotkit.ai/ms-agent-harness-dotnet)TutorialsTutorial: AI Todo App

# Step 3: Copilot Readable State

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

At this point, we have a chat popup in our app and we're able to chat directly with our copilot. This is great, but our copilot doesn't know anything about our app. In this step, we'll provide our copilot with the state of our todos.

In this step, you'll learn how to provide knowledge to the copilot. In our case, we want the copilot to know about the tasks in our app.

## Our App's State#

Let's quickly review how our app's state works. Open up the [`lib/hooks/use-tasks.tsx`](https://github.com/CopilotKit/CopilotKit/tree/main/examples/starters/todos-app/start/lib/hooks/use-tasks.tsx) file.

At a glance, we can see that the file exposes a provider (`TasksProvider`), which defines a useful things:

  * The state of our tasks (`tasks`)
  * A function to add a task (`addTask`)
  * A function to update a task (`updateTask`)
  * A function to delete a task (`deleteTask`)



All of this is consumable by a `useTasks` hook, which we use in the rest of our application (feel free to check out the `TasksList`, `AddTask` and `Task` components).

This resembles the majority of React apps, where frontend state, either for a feature or the entire app, is managed by a context or state management library.

## The `useAgentContext` hook#

Our goal is to make our copilot aware of this state, so that it can provide more accurate and helpful responses. We can easily achieve this by using the [`useAgentContext`](https://docs.copilotkit.ai/reference/hooks/useAgentContext) hook.

lib/hooks/use-tasks.tsx
    
    
    // ... the rest of the file
    
    export const TasksProvider = ({ children }: { children: ReactNode }) => {
      const [tasks, setTasks] = useState<Task[]>(defaultTasks);
    
      useAgentContext({
        description: "The state of the todo list",
        value: JSON.stringify(tasks),
      });
    
      // ... the rest of the file
    };

In this example, we use the `useAgentContext` hook to provide the copilot with the state of our tasks.

  * For the `description` property, we provide a concise description that tells the copilot what this piece of readable data means.
  * For the `value` property, we pass the entire state as a JSON string.



## Try it out!#

Now, try it out! Ask your Copilot a question about the state of the todo list. For example:

> How many tasks do I still need to get done?

Magical, isn't it? ✨

### [← Previous: Set up CopilotKitWire the CopilotKit provider and chat UI into the app.](https://docs.copilotkit.ai/tutorials/ai-todo-app/step-2-setup-copilotkit)### [Next: Frontend tools →Let the copilot take actions on the todo list with useFrontendTool.](https://docs.copilotkit.ai/tutorials/ai-todo-app/step-4-frontend-tools)

### On this page

Our App's StateThe useAgentContext hookTry it out!
