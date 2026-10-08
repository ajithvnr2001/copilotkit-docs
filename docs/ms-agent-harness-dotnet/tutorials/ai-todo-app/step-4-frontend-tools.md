---
url: https://docs.copilotkit.ai/ms-agent-harness-dotnet/tutorials/ai-todo-app/step-4-frontend-tools/
title: Step 4: Frontend Tools
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:21:15.804169+00:00
---

# Step 4: Frontend Tools

> Source: https://docs.copilotkit.ai/ms-agent-harness-dotnet/tutorials/ai-todo-app/step-4-frontend-tools/

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

# Step 4: Frontend Tools

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Now it's time to make our copilot even more useful by enabling it to execute tools.

## Available Tools#

Once again, let's take a look at our app's state in the [`lib/hooks/use-tasks.tsx`](https://github.com/CopilotKit/CopilotKit/tree/main/examples/starters/todos-app/start/lib/hooks/use-tasks.tsx#L19-L33) file.

Essentially, we want our copilot to be able to call the `addTask`, `setTaskStatus` and `deleteTask` functions.

## The `useFrontendTool` hook#

The [`useFrontendTool`](https://docs.copilotkit.ai/reference/v1/hooks/useFrontendTool) hook makes tools available to our copilot. Let's implement it in the [`lib/hooks/use-tasks.tsx`](https://github.com/CopilotKit/CopilotKit/tree/main/examples/starters/todos-app/start/lib/hooks/use-tasks.tsx) file.
    
    
    // ... the rest of the file
    
    export const TasksProvider = ({ children }: { children: ReactNode }) => {
      const [tasks, setTasks] = useState<Task[]>(defaultTasks);
    
      useFrontendTool({
        name: "addTask",
        description: "Adds a task to the todo list",
        parameters: z.object({
          title: z.string().describe("The title of the task"),
        }),
        handler: async ({ title }) => {
          addTask(title);
          return `Added task: ${title}`;
        },
      });
    
      useFrontendTool({
        name: "deleteTask",
        description: "Deletes a task from the todo list",
        parameters: z.object({
          id: z.number().describe("The id of the task"),
        }),
        handler: async ({ id }) => {
          deleteTask(id);
          return `Deleted task ${id}`;
        },
      });
    
      useFrontendTool({
        name: "setTaskStatus",
        description: "Sets the status of a task",
        parameters: z.object({
          id: z.number().describe("The id of the task"),
          status: z
            .enum(Object.values(TaskStatus) as [string, ...string[]])
            .describe("The status of the task"),
        }),
        handler: async ({ id, status }) => {
          setTaskStatus(id, status);
          return `Set task ${id} status to ${status}`;
        },
      });
    
      // ... the rest of the file
    };

The `useFrontendTool` hook is a powerful hook that allows us to register tools with our copilot. It takes an object with the following properties:

  * `name` is the name of the tool.
  * `description` is a description of the tool. It's important to choose a good description so that our copilot can choose the right tool.
  * `parameters` is a Zod schema that defines the parameters the tool accepts. This provides runtime validation and TypeScript type inference.
  * `handler` is a function that will be called when the tool is triggered. It's type safe thanks to Zod!



You can check out the full reference for the `useFrontendTool` hook [here](https://docs.copilotkit.ai/reference/hooks/useFrontendTool).

## Try it out!#

Now, head back to the app and ask your pilot to do any of the following:

  * "Create a task about inviting Daniel to my birthday"
  * "Delete all outstanding tasks"
  * "Mark task with ID 2 as done"
  * etc.



Your copilot is now more helpful than ever 💪

### [← Previous: Read app stateUse useAgentContext so the copilot can answer questions about your todos.](https://docs.copilotkit.ai/tutorials/ai-todo-app/step-3-copilot-readable-state)### [Next: Wrap up →Find the source code, ideas for what to build next, and more tutorials.](https://docs.copilotkit.ai/tutorials/ai-todo-app/next-steps)

### On this page

Available ToolsThe useFrontendTool hookTry it out!
