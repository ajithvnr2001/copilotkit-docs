---
url: https://docs.copilotkit.ai/langgraph-typescript/advanced/emit-api-hook-mapping/
title: Connecting Backend Emit APIs to Frontend Hooks
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:09:59.278121+00:00
---

# Connecting Backend Emit APIs to Frontend Hooks

> Source: https://docs.copilotkit.ai/langgraph-typescript/advanced/emit-api-hook-mapping/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-typescript)[Quickstart](https://docs.copilotkit.ai/langgraph-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-typescript/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-typescript/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/langgraph-typescript/webmcp)

Agent capabilities

LangGraph (TypeScript)

[Sub-agents](https://docs.copilotkit.ai/langgraph-typescript/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/langgraph-typescript/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/langgraph-typescript/learning)

[User Memories](https://docs.copilotkit.ai/langgraph-typescript/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/langgraph-typescript/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/langgraph-typescript/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/langgraph-typescript/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/langgraph-typescript/intelligence/analytics)[Channels](https://docs.copilotkit.ai/langgraph-typescript/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/langgraph-typescript/telemetry)[Community frameworks](https://docs.copilotkit.ai/langgraph-typescript/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[LangGraph (TypeScript)](https://docs.copilotkit.ai/langgraph-typescript)Advanced

# Connecting Backend Emit APIs to Frontend Hooks

End-to-end guide: how LangGraph SDK emit functions map to React v2 frontend hooks.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

CopilotKit's Python SDK provides **emit functions** that your LangGraph nodes can call to push tool calls and control streaming behavior. On the frontend, React v2 provides **hooks** that register handlers and renderers for those emitted events.

This page shows exactly how the two sides connect so you can build predictable, end-to-end integrations without guessing.

## The mapping at a glance#

Backend (Python SDK)| Frontend (React v2)| What it does  
---|---|---  
`copilotkit_emit_tool_call(config, name, args)`| `useFrontendTool`| Agent manually fires a tool call; the registered handler runs in the browser  
LLM calls a frontend tool normally (via `bind_tools`)| `useFrontendTool`| Agent lets the LLM decide when to call the tool; same handler, same result  
LLM calls a frontend tool (via `bind_tools`)| `useComponent`| Agent calls a tool and the registered component is rendered inline in the chat  
`copilotkit_customize_config(config, emit_tool_calls=["ToolName"])`| `useFrontendTool` / `useComponent`| Controls which tool calls are streamed to the frontend; use this to filter noise  
`copilotkit_customize_config(config, emit_tool_calls=False)`| —| Suppresses all tool call streaming for that LLM invocation  
  
### Persisted vs. emitted tool calls#

Key concept: persisted vs. transient

  * **Persisted tool calls** are LLM-generated tool call messages stored in `state["messages"]`. They appear in chat history and are replayed on page refresh.
  * **Emitted tool calls** (`copilotkit_emit_tool_call`) are transient events that fire a frontend handler immediately. They are **not** stored in chat history unless you explicitly add a message to state.



`useComponent` and `useFrontendTool` both respond to persisted tool calls triggered by the LLM. `copilotkit_emit_tool_call` lets you fire the same frontend mechanism imperatively, without waiting for the LLM.

## End-to-end example: `copilotkit_emit_tool_call` → `useFrontendTool`#

This pattern lets a LangGraph node **directly invoke** a frontend function — for example, to update React state, show a toast, or trigger a browser API — without the LLM needing to decide when to call it.

### Step 1: Register the frontend tool#

app/page.tsx
    
    
    import { z } from "zod";
    import { useFrontendTool } from "@copilotkit/react-core/v2"; 
    
    export function Page() {
      const [status, setStatus] = React.useState("");
    
      useFrontendTool({
        name: "updateStatus",
        description: "Update the status displayed in the UI.",
        parameters: z.object({
          message: z.string().describe("The status message to display"),
        }),
        handler: async ({ message }) => {
          setStatus(message);
          return `Status updated to: ${message}`;
        },
      });
    
      return <div>Agent says: {status}</div>;
    }

### Step 2: Emit the tool call from your LangGraph node#

agent.py
    
    
    from langchain_core.runnables import RunnableConfig
    from copilotkit import CopilotKitState
    from copilotkit.langgraph import copilotkit_emit_tool_call 
    
    class AgentState(CopilotKitState):
        pass
    
    async def my_node(state: AgentState, config: RunnableConfig):
        # Imperatively fires the frontend tool handler without the LLM
        await copilotkit_emit_tool_call( 
            config,                      
            name="updateStatus",         
            args={"message": "Processing your request..."}, 
        )                                
    
        # ... do other work ...
    
        await copilotkit_emit_tool_call(
            config,
            name="updateStatus",
            args={"message": "Done!"},
        )
    
        return state

When `copilotkit_emit_tool_call` is called:

  1. CopilotKit sends the tool call event to the frontend over SSE.
  2. The `useFrontendTool` handler matching `"updateStatus"` runs in the browser immediately.
  3. The return value of the handler is sent back to the agent as the tool result.
  4. The call is **not** saved to `state["messages"]` unless you add it yourself.



## End-to-end example: LLM tool call → `useComponent`#

This pattern lets the LLM decide when to render a custom React component in the chat, passing its parameters as props.

### Step 1: Register the component#

app/page.tsx
    
    
    import { useComponent } from "@copilotkit/react-core/v2"; 
    import { z } from "zod";
    
    function WeatherCard({ city, temperature, condition }: {
      city: string;
      temperature: number;
      condition: string;
    }) {
      return (
        <div className="rounded-lg border p-4">
          <h3 className="font-semibold">{city}</h3>
          <p className="text-2xl">{temperature}°F</p>
          <p className="text-sm text-gray-500">{condition}</p>
        </div>
      );
    }
    
    export function Page() {
      useComponent({
        name: "showWeather",
        description: "Display a weather card for a city.",
        parameters: z.object({
          city: z.string(),
          temperature: z.number(),
          condition: z.string(),
        }),
        render: WeatherCard,
      });
    
      return <div>{/* your app */}</div>;
    }

### Step 2: Expose it to the LLM via `bind_tools`#

agent.py
    
    
    from langchain_openai import ChatOpenAI
    from langchain_core.runnables import RunnableConfig
    from copilotkit import CopilotKitState
    
    class AgentState(CopilotKitState):
        pass
    
    async def chat_node(state: AgentState, config: RunnableConfig):
        model = ChatOpenAI(model="gpt-4o").bind_tools(
            state["copilotkit"]["actions"]  # includes all registered frontend tools/components 
        )
        response = await model.ainvoke(state["messages"], config)
        return {"messages": response}

When the LLM calls `showWeather`:

  1. The tool call is stored as a message in `state["messages"]` (persisted).
  2. CopilotKit streams the tool call to the frontend.
  3. `useComponent` renders `WeatherCard` inline in the chat with the tool arguments as props.
  4. The component remains visible in the chat on replay/refresh because the message is persisted.



## Controlling which tool calls are streamed with `copilotkit_customize_config`#

By default, CopilotKit streams all LLM tool calls to the frontend. Use `copilotkit_customize_config` to filter them.

agent.py
    
    
    from copilotkit.langgraph import copilotkit_customize_config 
    
    async def chat_node(state: AgentState, config: RunnableConfig):
        # Only stream "showWeather" to the frontend; suppress all others
        streaming_config = copilotkit_customize_config( 
            config,                                      
            emit_tool_calls=["showWeather"],             
        )                                                
    
        model = ChatOpenAI(model="gpt-4o").bind_tools(
            state["copilotkit"]["actions"]
        )
        response = await model.ainvoke(state["messages"], streaming_config) 
        return {"messages": response}

Use a new variable

Always assign the result to a **new variable** (e.g. `streaming_config`) rather than overwriting `config`. In LangGraph Python, `config` is implicitly passed to all LangChain LLM calls in scope — overwriting it changes the behavior of every subsequent call unexpectedly.

### `emit_tool_calls` options at a glance#

Value| Effect  
---|---  
`True` (default)| Stream all tool calls to the frontend  
`False`| Suppress all tool call streaming for this LLM call  
`"ToolName"`| Stream only the named tool call  
`["Tool1", "Tool2"]`| Stream only the listed tool calls  
  
## Choosing the right pattern#

Goal| Recommended pattern  
---|---  
Agent imperatively triggers a browser action (toast, state update)| `copilotkit_emit_tool_call` → `useFrontendTool`  
LLM decides when to trigger a browser action| `bind_tools(state["copilotkit"]["actions"])` → `useFrontendTool`  
LLM renders a rich component in chat (persisted in history)| `bind_tools(state["copilotkit"]["actions"])` → `useComponent`  
Hide certain LLM tool calls from the frontend| `copilotkit_customize_config(emit_tool_calls=[...])`  
Hide all tool calls from the frontend for a sensitive LLM call| `copilotkit_customize_config(emit_tool_calls=False)`  
  
## See also#

  * [Frontend Tools](https://docs.copilotkit.ai/integrations/langgraph/frontend-tools) — full guide to `useFrontendTool`
  * [Display-only components](https://docs.copilotkit.ai/integrations/langgraph/generative-ui/your-components/display-only) — full guide to `useComponent`
  * [Disabling state streaming](https://docs.copilotkit.ai/integrations/langgraph/advanced/disabling-state-streaming) — `copilotkit_customize_config` reference



### On this page

What is this?The mapping at a glancePersisted vs. emitted tool callsEnd-to-end example: copilotkitemittool_call → useFrontendToolStep 1: Register the frontend toolStep 2: Emit the tool call from your LangGraph nodeEnd-to-end example: LLM tool call → useComponentStep 1: Register the componentStep 2: Expose it to the LLM via bind_toolsControlling which tool calls are streamed with copilotkitcustomizeconfigemittoolcalls options at a glanceChoosing the right patternSee also
