---
url: https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTool/
title: useFrontendTool
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:34:44.570543+00:00
---

# useFrontendTool

> Source: https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTool/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁React (V2)SDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Components

[CopilotChat](https://docs.copilotkit.ai/reference/v2/components/CopilotChat)[CopilotChatAssistantMessage](https://docs.copilotkit.ai/reference/v2/components/CopilotChatAssistantMessage)[CopilotChatInput](https://docs.copilotkit.ai/reference/v2/components/CopilotChatInput)[CopilotChatMessageView](https://docs.copilotkit.ai/reference/v2/components/CopilotChatMessageView)[CopilotChatUserMessage](https://docs.copilotkit.ai/reference/v2/components/CopilotChatUserMessage)[CopilotChatView](https://docs.copilotkit.ai/reference/v2/components/CopilotChatView)[CopilotKit](https://docs.copilotkit.ai/reference/v2/components/CopilotKit)[CopilotPopup](https://docs.copilotkit.ai/reference/v2/components/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/v2/components/CopilotSidebar)[CopilotThreadsDrawer](https://docs.copilotkit.ai/reference/v2/components/CopilotThreadsDrawer)

Hooks

[useAgent](https://docs.copilotkit.ai/reference/v2/hooks/useAgent)[useAgentContext](https://docs.copilotkit.ai/reference/v2/hooks/useAgentContext)[useCapabilities](https://docs.copilotkit.ai/reference/v2/hooks/useCapabilities)[useComponent](https://docs.copilotkit.ai/reference/v2/hooks/useComponent)[useConfigureSuggestions](https://docs.copilotkit.ai/reference/v2/hooks/useConfigureSuggestions)[useCopilotChatConfiguration](https://docs.copilotkit.ai/reference/v2/hooks/useCopilotChatConfiguration)[useCopilotKit](https://docs.copilotkit.ai/reference/v2/hooks/useCopilotKit)[useDefaultRenderTool](https://docs.copilotkit.ai/reference/v2/hooks/useDefaultRenderTool)[useFrontendTool](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTool)[useFrontendTools](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTools)[useHumanInTheLoop](https://docs.copilotkit.ai/reference/v2/hooks/useHumanInTheLoop)[useInterrupt](https://docs.copilotkit.ai/reference/v2/hooks/useInterrupt)[useRenderTool](https://docs.copilotkit.ai/reference/v2/hooks/useRenderTool)[useRenderToolCall](https://docs.copilotkit.ai/reference/v2/hooks/useRenderToolCall)[useSuggestions](https://docs.copilotkit.ai/reference/v2/hooks/useSuggestions)[useThreads](https://docs.copilotkit.ai/reference/v2/hooks/useThreads)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[v2](https://docs.copilotkit.ai/reference/v2)Hooks

# useFrontendTool

React hook for registering client-side tool handlers with optional UI rendering

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useFrontendTool` registers a client-side tool with CopilotKit at component scope. When the agent decides to call the tool, the provided `handler` function executes in the browser. Optionally, you can supply a `render` component to display custom UI in the chat showing the tool's execution progress and results.

The hook manages the full registration lifecycle: it warns if a tool with the same name already exists, registers the tool and its render component on mount, and cleans up both registrations on unmount. In v2, parameter schemas are defined using [Zod](https://zod.dev) instead of plain parameter arrays.

## Signature
    
    
    import { useFrontendTool } from "@copilotkit/react-core/v2";
    
    function useFrontendTool<T extends Record<string, unknown>>(
      tool: ReactFrontendTool<T>,
      deps?: ReadonlyArray<unknown>,
    ): void;

## Parameters

Prop

Type

`tool`ReactFrontendTool<T>

Prop

Type

`deps?`ReadonlyArray<unknown>

## Usage

### Basic Tool with Zod Parameters
    
    
    function TodoManager() {
      const [todos, setTodos] = useState<string[]>([]);
    
      useFrontendTool(
        {
          name: "addTodo",
          description: "Add a new item to the user's todo list",
          parameters: z.object({
            text: z.string().describe("The todo item text"),
            priority: z.enum(["low", "medium", "high"]).describe("Priority level"),
          }),
          handler: async ({ text, priority }) => {
            setTodos((prev) => [...prev, text]);
            return `Added "${text}" with ${priority} priority`;
          },
        },
        [],
      );
    
      return (
        <ul>
          {todos.map((t, i) => (
            <li key={i}>{t}</li>
          ))}
        </ul>
      );
    }

### Tool with Custom Render Component
    
    
    function WeatherWidget() {
      useFrontendTool(
        {
          name: "getWeather",
          description: "Fetch and display weather information for a city",
          parameters: z.object({
            city: z.string().describe("City name"),
            units: z.enum(["celsius", "fahrenheit"]).default("celsius"),
          }),
          handler: async ({ city, units }, { signal }) => {
            const response = await fetch(
              `/api/weather?city=${city}&units=${units}`,
              { signal },
            );
            const data = await response.json();
            return JSON.stringify(data);
          },
          render: ({ args, status, result }) => {
            if (status === ToolCallStatus.InProgress) {
              return (
                <div className="animate-pulse">
                  Fetching weather for {args.city}...
                </div>
              );
            }
            if (status === ToolCallStatus.Complete && result) {
              const data = JSON.parse(result);
              return (
                <div className="p-4 border rounded">
                  <h3>{data.city}</h3>
                  <p>
                    {data.temperature}&deg; {data.units}
                  </p>
                  <p>{data.conditions}</p>
                </div>
              );
            }
            return null;
          },
        },
        [],
      );
    
      return null;
    }

### Conditionally Available Tool
    
    
    function AdminPanel({ isAdmin }: { isAdmin: boolean }) {
      useFrontendTool(
        {
          name: "deleteUser",
          description: "Delete a user account by ID (admin only)",
          parameters: z.object({
            userId: z.string().describe("The ID of the user to delete"),
          }),
          handler: async ({ userId }) => {
            await fetch(`/api/users/${userId}`, { method: "DELETE" });
            return `User ${userId} deleted`;
          },
          available: isAdmin ? "enabled" : "disabled",
        },
        [isAdmin],
      );
    
      return <div>{/* admin UI */}</div>;
    }

### Expose a Tool to Browser Agents (WebMCP)

Pass `webmcp` to also register the tool on `document.modelContext`. Browser agents that support [WebMCP](https://developer.chrome.com/docs/ai/webmcp) can then discover and call the tool while the page is open.
    
    
    function OrderSearch() {
      useFrontendTool({
        name: "searchOrders",
        description: "Search the signed-in user's orders by status",
        parameters: z.object({
          status: z.enum(["open", "shipped", "delivered"]),
        }),
        handler: async ({ status }) => {
          const orders = await searchOrders(status);
          return JSON.stringify(orders);
        },
        webmcp: {
          annotations: { readOnlyHint: true },
        },
      });
    
      return null;
    }

## LangGraph agents: description vs. system_prompt

For simple UI-control tools (e.g. toggling a theme), the `description` field is usually enough for a LangGraph agent to discover and call the tool at the right time. For **mandatory** tools — ones where the agent must call the tool before answering rather than reasoning from stale context — pair a clear `description` with an explicit instruction in the agent's `system_prompt`.

agent.py — make mandatory tools explicit in system_prompt
    
    
    graph = create_agent( # create_agent supersedes the deprecated create_react_agent, which accepts neither middleware= nor system_prompt=
        model="openai:gpt-4o",
        tools=[],
        middleware=[CopilotKitMiddleware()],
        state_schema=CopilotKitState,
        system_prompt=(
            "You are a helpful assistant.\n\n"
            "IMPORTANT: When the user asks about current sales data, you MUST call "
            "the `fetch_sales_by_month_range` frontend tool first. "
            "Never answer from memory or previously seen context values."
        ),
    )

See [Ensuring your agent reliably calls frontend tools](https://docs.copilotkit.ai/integrations/langgraph/frontend-tools#ensuring-your-agent-reliably-calls-frontend-tools) for the full pattern and a TypeScript example.

## Behavior

  * **Duplicate detection** : If a tool with the same `name` is already registered, the hook logs a warning. Only one tool per name is active at a time.
  * **Mount/Unmount lifecycle** : The tool and its optional render component are registered on mount and removed on unmount.
  * **Dependency tracking** : When `deps` is provided, the tool registration is refreshed whenever any dependency value changes, similar to `useEffect`.
  * **WebMCP registration** : With `webmcp` set, the tool is also registered on `document.modelContext` and unregistered on unmount. The tool needs a `description` for this (WebMCP rejects tools without one).
  * **Render component lifecycle** : If a `render` function is provided, it is added to the internal render tool calls registry. It receives streaming `args` (partial during `InProgress`, complete during `Executing` and `Complete`).
  * **No return value** : The hook returns `void`.



## Related

  * [`useHumanInTheLoop`](https://docs.copilotkit.ai/reference/hooks/useHumanInTheLoop) \-- for tools that pause execution and wait for user input
  * [`useRenderToolCall`](https://docs.copilotkit.ai/reference/hooks/useRenderToolCall) \-- for rendering backend tool calls without a client-side handler
  * [`useComponent`](https://docs.copilotkit.ai/reference/hooks/useComponent) \-- convenience wrapper for rendering React components from tool args
  * [`useRenderTool`](https://docs.copilotkit.ai/reference/hooks/useRenderTool) \-- register renderer-only tool call UI (named or wildcard)
  * [`useCopilotAction`](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotAction) \-- v1 equivalent


