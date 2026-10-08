---
url: https://docs.copilotkit.ai/langgraph-fastapi/shared-state/
title: Shared State
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:05:52.383975+00:00
---

# Shared State

> Source: https://docs.copilotkit.ai/langgraph-fastapi/shared-state/

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

[Shared State](https://docs.copilotkit.ai/langgraph-fastapi/shared-state)[Render agent state in your app](https://docs.copilotkit.ai/langgraph-fastapi/shared-state/rendering-in-app)[State Streaming](https://docs.copilotkit.ai/langgraph-fastapi/shared-state/streaming)[Agent Read-Only Context](https://docs.copilotkit.ai/langgraph-fastapi/shared-state/agent-readonly)

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

Shared State

InteractivityShared state

# Shared State

Create a two-way connection between your UI and agent state.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is shared state?#

Agentic Copilots maintain a shared state that seamlessly connects your UI with the agent's execution. This shared state system allows you to:

  * Display the agent's current progress and intermediate results
  * Update the agent's state through UI interactions
  * React to state changes in real-time across your application

![Shared State Demo](https://cdn.copilotkit.ai/docs/copilotkit/images/coagents/SharedStateCoAgents.gif)

See this in Inspector

Open Inspector on localhost. Open a thread, then click **State**. Agent state updates here as the run proceeds.

More detail: [Inspector](https://docs.copilotkit.ai/langgraph-fastapi/inspector).

## When should I use this?#

Use shared state when you want the agent and the user to collaborate through the same application state. The agent's outputs are reflected in the UI, and user updates in the UI are reflected in the agent's execution.

[Building stateful agents?Persistent threads ship with CopilotKit Intelligence on the free Developer tier.Get CopilotKit Intelligence free](https://ssr-placeholder.invalid/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_shared_state&utm_frontend=react&utm_backend=langgraph-fastapi)

## Reading agent state#

### Install the LangGraph Python SDK

uvpoetrypipconda
    
    
    uv add copilotkit
    
    
    poetry add copilotkit
    
    
    pip install copilotkit --extra-index-url https://copilotkit.gateway.scarf.sh/simple/
    
    
    conda install copilotkit -c copilotkit-channel

### Wire CopilotKit middleware into your graph

Shared state flows between your UI and your agent through `agent.setState` on the frontend and `state.get(...)` in your graph nodes. Attach `CopilotKitMiddleware` to your `create_agent` call so CopilotKit-specific state is picked up alongside your own.

shared_state_read_write.py
    
    
    graph = create_agent(
        model=ChatOpenAI(model="gpt-5.4"),
        tools=[set_notes],
        middleware=[CopilotKitMiddleware(), PreferencesInjectorMiddleware()],
        state_schema=AgentState,
        system_prompt=(
            "You are a helpful, concise assistant. "
            "The user's preferences are supplied via shared state and will be "
            "added as a system message at the start of every turn. Always "
            "respect them. "
            "When the user asks you to remember something, or when you observe "
            "something worth surfacing in the UI, call `set_notes` with the "
            "FULL updated list of short note strings (existing notes + new)."
        ),
    )

Subscribe a component to the agent's state with `useAgent`. Any time the agent mutates its state, for example via a tool call, the hook fires and your UI re-renders with the new values.

page.tsx
    
    
      // Subscribe the component to agent state changes. Any time the agent  // mutates its state (e.g. via its `set_notes` tool) this hook fires,  // we re-render, and the sidebar panels reflect the new values.  const { agent } = useAgent({    agentId: "shared-state-read-write",    updates: [UseAgentUpdate.OnStateChanged],  });

The returned `agent.state` is just a plain object. Read it like any other piece of React state and render the parts you care about: agent-written notes, structured outputs, progress indicators, anything the agent has put there.

## Writing agent state#

The same `agent` object exposes a `setState` setter. Calling it from a UI event handler pushes the new value into shared state, and the agent reads it back on its next turn. The UI's writes visibly steer the model.

page.tsx
    
    
      // WRITE: every edit in the sidebar goes straight into agent state.  // On the agent's next turn, `PreferencesInjectorMiddleware` reads this  // back out of state and adds it to the system prompt — so the UI's  // writes visibly steer the model.  const handlePreferencesChange = (next: Preferences) => {    agent.setState({      preferences: next,      notes, // preserve what the agent has written    } as RWAgentState);  };

This is what makes the channel two-way: the UI doesn't just observe the agent, it can hand the agent fresh inputs (preferences, selections, partial work) without going through the chat thread.

## Rendering shared state in the UI#

Because `agent.state` is plain React data, the UI layer is whatever you'd normally build. The demo on this page wires the agent's outputs into a small card component and feeds user edits back through `setState`.

notes-card.tsx
    
    
    // Read-side render: this card reflects the agent-authored `notes` slice// of shared state. The parent page passes `state.notes` in; we never// touch agent state ourselves — we just render it. The Clear button is// a small write-back, exposed as an `onClear` prop.export function NotesCard({ notes, onClear }: NotesCardProps) {  return (    <Card data-testid="notes-card" className="w-full">      <CardHeader>        <div className="flex items-start justify-between gap-3">          <div className="space-y-1.5">            <CardTitle>Agent Scratch pad</CardTitle>            <CardDescription>              The agent writes here via its{" "}              <code className="font-mono text-[11px] text-[#010507]">                set_notes              </code>{" "}              tool. The UI re-renders from shared state.            </CardDescription>          </div>          {notes.length > 0 && (            <Button              type="button"              onClick={onClear}              data-testid="notes-clear-button"              variant="destructive"              size="sm"              className="uppercase tracking-[0.14em] text-[10px]"            >              Clear            </Button>          )}        </div>      </CardHeader>      <CardContent>        {notes.length === 0 ? (          <div            data-testid="notes-empty"            className="text-sm text-[#838389] italic min-h-[160px] flex items-center justify-center text-center px-4 border border-dashed border-[#E9E9EF] rounded-xl bg-[#FAFAFC]"          >            the agent will make observations about you and note them here!          </div>        ) : (          <ul            data-testid="notes-list"            className="space-y-2 text-sm text-[#010507]"          >            {notes.map((note, i) => (              <li                key={i}                data-testid="note-item"                className="flex gap-2 rounded-lg border border-[#E9E9EF] bg-[#FAFAFC] px-3 py-2"              >                <span className="text-[#838389] font-mono text-xs leading-5 select-none">                  {String(i + 1).padStart(2, "0")}                </span>                <span className="flex-1">{note}</span>              </li>            ))}          </ul>        )}      </CardContent>    </Card>  );}

Nothing about this is chat-specific: `useAgent` works in any component under `<CopilotKit>`, so you can render `agent.state` in your main view or canvas, not just inside the chat panel. See **[Render agent state in your app](https://docs.copilotkit.ai/langgraph-fastapi/shared-state/rendering-in-app)** for the full main-view pattern.

## Streaming partial state updates#

By default, agent state only updates _between_ backend checkpoints, so a long-running tool call appears as one big burst at the end. State streaming forwards a specific tool argument straight into a state key _as it's being generated_ , so the UI can watch the answer assemble token-by-token.

Missing snippet

Region `state-streaming-middleware` not found in `langgraph-fastapi::shared-state-streaming`. Tag the relevant source lines with `// @region[state-streaming-middleware]` / `// @endregion[state-streaming-middleware]`.

Available: frontend-use-coagent-state

See **[State streaming](https://docs.copilotkit.ai/langgraph-fastapi/shared-state/streaming)** for the full walkthrough, including the corresponding `useAgent` subscription on the frontend.

## Read-only context#

When the value is **UI-owned** and the agent should read it but never write it back, such as current user, selected record, or scroll position, reach for `useAgentContext` instead of full shared state. It publishes values as a one-way UI-to-agent channel that auto-unregisters on unmount.

See **[Agent read-only context](https://docs.copilotkit.ai/langgraph-fastapi/shared-state/agent-readonly)** for the full pattern.

### On this page

What is shared state?When should I use this?Reading agent stateWriting agent stateRendering shared state in the UIStreaming partial state updatesRead-only context
