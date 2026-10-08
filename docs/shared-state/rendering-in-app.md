---
url: https://docs.copilotkit.ai/shared-state/rendering-in-app/
title: Render agent state in your app
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:29.795927+00:00
---

# Render agent state in your app

> Source: https://docs.copilotkit.ai/shared-state/rendering-in-app/

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

Render agent state in your app

InteractivityShared state

# Render agent state in your app

Read agent.state with useAgent and render it in your main view or canvas.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

[Shared state](https://docs.copilotkit.ai/shared-state) is most powerful when the agent's state shows up in your application UI, such as a dashboard, document canvas, map, or table. Because `agent.state` is plain React data, you can subscribe to it from any component in your tree and render it however you like.

## The pattern#

`useAgent` works in any component under `<CopilotKit>`. It doesn't have to be near the chat. Call it in your main-view component, read `agent.state`, and render:

components/Canvas.tsx
    
    
    import { useEffect } from "react";
    import { useAgent } from "@copilotkit/react-core/v2";
    
    type CanvasState = {
      title: string;
      items: { id: string; label: string; done: boolean }[];
    };
    
    const INITIAL_CANVAS_STATE: CanvasState = {
      title: "Project launch",
      items: [
        { id: "research", label: "Research user needs", done: true },
        { id: "prototype", label: "Build a prototype", done: false },
      ],
    };
    
    export function Canvas() {
      // No agentId means the "default" agent. Pass { agentId } to target another.
      const { agent, isReady } = useAgent();
      const state = (agent.state ?? {}) as Partial<CanvasState>;
    
      useEffect(() => {
        if (!isReady) return;
    
        const current = (agent.state ?? {}) as Partial<CanvasState>;
        const updates: Partial<CanvasState> = {};
    
        if (current.title === undefined) {
          updates.title = INITIAL_CANVAS_STATE.title;
        }
        if (current.items === undefined) {
          updates.items = INITIAL_CANVAS_STATE.items;
        }
    
        if (Object.keys(updates).length > 0) {
          agent.setState({ ...(agent.state ?? {}), ...updates });
        }
      }, [agent, isReady, state.title, state.items]);
    
      return (
        <main className="canvas">
          <h1>{state.title ?? "Untitled"}</h1>
          <ul>
            {(state.items ?? []).map((item) => (
              <li key={item.id} data-done={item.done}>
                {item.label}
              </li>
            ))}
          </ul>
        </main>
      );
    }

The `INITIAL_CANVAS_STATE` value is UI-owned initial state for this example. It makes the canvas visible before the agent writes state. The effect sets only `undefined` fields and preserves all other state. If the backend owns the initial state, define it in the shared-state setup for that framework.

Every time the agent mutates its state, whether from a tool call, node transition, or [streamed update](https://docs.copilotkit.ai/shared-state/streaming), `useAgent` re-renders this component with the new values. The chat can be in a sidebar, a popup, or absent entirely; your canvas updates the same way.

## Put it anywhere in your layout#

The agent lives on the `<CopilotKit>` provider, so the chat surface and your main-view components are just two consumers of the same agent. A typical layout renders the canvas as the primary content and the chat as a docked sidebar:

app/page.tsx
    
    
    import { CopilotKit, CopilotSidebar } from "@copilotkit/react-core/v2";
    import { Canvas } from "../components/Canvas";
    
    export default function Page() {
      return (
        <CopilotKit runtimeUrl="/api/copilotkit">
          <div className="app-shell">
            {/* Your app UI, driven by agent.state */}
            <Canvas />
            {/* Chat is just another consumer of the same agent */}
            <CopilotSidebar />
          </div>
        </CopilotKit>
      );
    }

`<Canvas>` and `<CopilotSidebar>` both call `useAgent()` for the same `agentId`, so they share one agent instance and one state object. There's nothing chat-specific about reading `agent.state`. The sidebar is not special.

## Writing back from the main view#

The same `agent` exposes `setState`, so your canvas can be interactive, not just a read-only mirror. A click handler in the main view can push a new value that the agent reads on its next turn:
    
    
    function toggleItem(id: string) {
      agent.setState({
        ...agent.state,
        items: (agent.state?.items ?? []).map((it) =>
          it.id === id ? { ...it, done: !it.done } : it,
        ),
      });
    }

This is the same two-way channel described in [Shared State](https://docs.copilotkit.ai/shared-state). The only difference here is that the reads and writes happen in your application's main surface rather than in the chat.

## Tips#

  * **Target a specific agent** with `useAgent({ agentId: "research-agent" })` when you have more than one. The default is the agent named `"default"`.
  * **Throttle high-frequency updates** with `useAgent({ throttleMs })` if a streaming run re-renders a heavy canvas too often.
  * **Treat`agent.state` as possibly partial** while a run is in progress. Guard with defaults (as above) so half-streamed state doesn't crash your render.



## Related#

  * [Shared State](https://docs.copilotkit.ai/shared-state): the full read/write model and the underlying `useAgent` subscription.
  * [State streaming](https://docs.copilotkit.ai/shared-state/streaming): stream a tool argument into a state key so the canvas fills in token-by-token.
  * [Agent read-only context](https://docs.copilotkit.ai/shared-state/agent-readonly): push UI values _to_ the agent without letting it write back.
  * [`useAgent` reference](https://docs.copilotkit.ai/reference/v2/hooks/useAgent): full hook signature and options.



### On this page

The patternPut it anywhere in your layoutWriting back from the main viewTipsRelated
