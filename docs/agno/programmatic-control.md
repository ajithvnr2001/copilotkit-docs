---
url: https://docs.copilotkit.ai/agno/programmatic-control/
title: Programmatic Control
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:47:48.651951+00:00
---

# Programmatic Control

> Source: https://docs.copilotkit.ai/agno/programmatic-control/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAgno

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/agno)[Quickstart](https://docs.copilotkit.ai/agno/quickstart)[Build with agents](https://docs.copilotkit.ai/agno/build-with-agents)[Intelligence](https://docs.copilotkit.ai/agno/intelligence/overview)

Basics

Chat

[Prebuilt Components](https://docs.copilotkit.ai/agno/prebuilt-components)

Custom Look and Feel

[Programmatic Control](https://docs.copilotkit.ai/agno/programmatic-control)

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

Programmatic Control

BasicsChat

# Programmatic Control

Control your Agno agent programmatically with useAgent and copilotkit.runAgent().

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview#

The `useAgent` hook provides direct access to your agent from any React component. It gives you real-time access to the agent's state, messages, execution status, and allows you to subscribe to custom events.

This enables you to build custom agent dashboards, monitoring tools, and interactive features that respond to your agent's behavior.

▶️Running the AgentTrigger your agent programmatically with copilotkit.runAgent().[⚙️Headless UIBuild a completely custom chat interface from the ground up using CopilotKit's headless hooks.](https://docs.copilotkit.ai/agno/programmatic-control/custom-look-and-feel/headless-ui)

### Import the hook#

First, import `useAgent` from the v2 package:

page.tsx
    
    
    import { useAgent } from "@copilotkit/react-core/v2"; 

### Access your agent#

Call the hook to get a reference to your agent:

page.tsx
    
    
    export function AgentInfo() {
      const { agent } = useAgent(); 
    
      return (
        <div>
          <p>Agent ID: {agent.agentId}</p>
          <p>Thread ID: {agent.threadId}</p>
          <p>Status: {agent.isRunning ? "Running" : "Idle"}</p>
          <p>Messages: {agent.messages.length}</p>
        </div>
      );
    }

If you are not using CopilotKit Cloud's public access/license key, pass your agentId to the `useAgent()` hook:
    
    
    const { agent } = useAgent({ agentId: "myAgent" });

The hook will throw an error if no agent is configured, so you can safely use `agent` without null checks.

### Display messages#

Access the agent's conversation history:

page.tsx
    
    
    export function MessageList() {
      const { agent } = useAgent();
    
      return (
        <div>
          {agent.messages.map((msg) => (
            <div key={msg.id}>
              <strong>{msg.role}:</strong>
              <span>{msg.content}</span>
            </div>
          ))}
        </div>
      );
    }

### Show running status#

Add a loading indicator when the agent is processing:

page.tsx
    
    
    export function AgentStatus() {
      const { agent } = useAgent();
    
      return (
        <div>
          {agent.isRunning ? (
            <div>
              <div className="spinner" />
              <span>Agent is processing...</span>
            </div>
          ) : (
            <span>Ready</span>
          )}
        </div>
      );
    }

### Run the agent#

Use `copilotkit.runAgent()` to trigger your agent programmatically:

page.tsx
    
    
    import { useAgent } from "@copilotkit/react-core/v2";
    import { useCopilotKit } from "@copilotkit/react-core/v2";
    import { randomUUID } from "@copilotkit/shared";
    
    export function RunAgent() {
      const { agent } = useAgent();
      const { copilotkit } = useCopilotKit();
    
      const handleRun = async () => {
        agent.addMessage({
          id: randomUUID(),
          role: "user",
          content: "Hello, agent!",
        });
    
        await copilotkit.runAgent({ agent });
      };
    
      return <button onClick={handleRun}>Send</button>;
    }

`copilotkit.runAgent()` orchestrates the full agent lifecycle — executing frontend tools, handling follow-up runs, and streaming results. This is the same method `<CopilotChat />` uses internally.

## Working with State#

Agents expose their state through the `agent.state` property. This state is shared between your application and the agent - both can read and modify it.

### Reading State#

Access your agent's current state:

page.tsx
    
    
    export function StateDisplay() {
      const { agent } = useAgent();
    
      return (
        <div>
          <h3>Agent State</h3>
          <pre>{JSON.stringify(agent.state, null, 2)}</pre>
    
          {/* Access specific properties */}
          {agent.state.user_name && <p>User: {agent.state.user_name}</p>}
          {agent.state.preferences && (
            <p>Preferences: {JSON.stringify(agent.state.preferences)}</p>
          )}
        </div>
      );
    }

Your component automatically re-renders when the agent's state changes.

### Updating State#

Update state that your agent can access:

page.tsx
    
    
    export function ThemeSelector() {
      const { agent } = useAgent();
    
      const updateTheme = (theme: string) => {
        agent.setState({
          ...agent.state,
          user_theme: theme,
        });
      };
    
      return (
        <div>
          <button onClick={() => updateTheme("dark")}>Dark Mode</button>
          <button onClick={() => updateTheme("light")}>Light Mode</button>
          <p>Current: {agent.state.user_theme || "default"}</p>
        </div>
      );
    }

State updates are immediately available to your agent in its next execution.

## Subscribing to Agent Events#

You can subscribe to agent events using the `subscribe()` method. This is useful for logging, monitoring, or responding to specific agent behaviors.

### Basic Event Subscription#

page.tsx
    
    
    import { useEffect } from "react";
    import { useAgent } from "@copilotkit/react-core/v2";
    import type { AgentSubscriber } from "@ag-ui/client";
    
    export function EventLogger() {
      const { agent } = useAgent();
    
      useEffect(() => {
        const subscriber: AgentSubscriber = {
          onCustomEvent: ({ event }) => {
            console.log("Custom event:", event.name, event.value);
          },
          onRunStartedEvent: () => {
            console.log("Agent started running");
          },
          onRunFinalized: () => {
            console.log("Agent finished running");
          },
          onStateChanged: (state) => {
            console.log("State changed:", state);
          },
        };
    
        const { unsubscribe } = agent.subscribe(subscriber);
        return () => unsubscribe();
      }, [agent]);
    
      return null;
    }

### Available Events#

The `AgentSubscriber` interface provides:

  * **`onCustomEvent`** \- Custom events emitted by the agent
  * **`onRunStartedEvent`** \- Agent starts executing
  * **`onRunFinalized`** \- Agent completes execution
  * **`onStateChanged`** \- Agent's state changes
  * **`onMessagesChanged`** \- Messages are added or modified



## Rendering Tool Calls#

You can customize how agent tool calls are displayed in your UI. First, define your tool renderers:

components/weather-tool.tsx
    
    
    import { defineToolCallRenderer } from "@copilotkit/react-core/v2";
    
    export const weatherToolRender = defineToolCallRenderer({
      name: "get_weather",
      render: ({ args, status }) => {
        return <WeatherCard location={args.location} status={status} />;
      },
    });
    
    function WeatherCard({
      location,
      status,
    }: {
      location?: string;
      status: string;
    }) {
      return (
        <div className="rounded-lg border p-6 shadow-sm">
          <h3 className="text-xl font-semibold">Weather in {location}</h3>
          <div className="mt-4">
            <span className="text-5xl font-light">70°F</span>
          </div>
          {status === "executing" && <div className="spinner">Loading...</div>}
        </div>
      );
    }

Register your tool renderers with CopilotKit:

layout.tsx
    
    
    import { CopilotKit } from "@copilotkit/react-core/v2";
    import { weatherToolRender } from "./components/weather-tool";
    
    export default function RootLayout({ children }) {
      return (
        <CopilotKit
          runtimeUrl="/api/copilotkit"
          renderToolCalls={[weatherToolRender]}
        >
          {children}
        </CopilotKit>
      );
    }

Then use `useRenderToolCall` to render tool calls from agent messages:

components/message-list.tsx
    
    
    import { useAgent, useRenderToolCall } from "@copilotkit/react-core/v2";
    
    export function MessageList() {
      const { agent } = useAgent();
      const renderToolCall = useRenderToolCall();
    
      return (
        <div className="messages">
          {agent.messages.map((message) => (
            <div key={message.id}>
              {/* Display message content */}
              {message.content && <p>{message.content}</p>}
    
              {/* Render tool calls if present */}
              {message.role === "assistant" &&
                message.toolCalls?.map((toolCall) => {
                  const toolMessage = agent.messages.find(
                    (m) => m.role === "tool" && m.toolCallId === toolCall.id,
                  );
                  return (
                    <div key={toolCall.id}>
                      {renderToolCall({ toolCall, toolMessage })}
                    </div>
                  );
                })}
            </div>
          ))}
        </div>
      );
    }

## Building a Complete Dashboard#

Here's a full example combining all concepts into an interactive agent dashboard:

page.tsx
    
    
    "use client";
    
    import { useAgent } from "@copilotkit/react-core/v2";
    
    export default function AgentDashboard() {
      const { agent } = useAgent();
    
      return (
        <div className="p-8 max-w-4xl mx-auto space-y-6">
          {/* Status */}
          <div className="p-6 bg-white rounded-lg shadow">
            <h2 className="text-xl font-bold mb-4">Agent Status</h2>
            <div className="space-y-2">
              <div className="flex items-center gap-2">
                <div
                  className={`w-3 h-3 rounded-full ${
                    agent.isRunning ? "bg-yellow-500 animate-pulse" : "bg-green-500"
                  }`}
                />
                <span>{agent.isRunning ? "Running" : "Idle"}</span>
              </div>
              <div>Thread: {agent.threadId}</div>
              <div>Messages: {agent.messages.length}</div>
            </div>
          </div>
    
          {/* State */}
          <div className="p-6 bg-white rounded-lg shadow">
            <h2 className="text-xl font-bold mb-4">Agent State</h2>
            <pre className="bg-gray-50 p-4 rounded text-sm overflow-auto">
              {JSON.stringify(agent.state, null, 2)}
            </pre>
          </div>
    
          {/* Messages */}
          <div className="p-6 bg-white rounded-lg shadow">
            <h2 className="text-xl font-bold mb-4">Conversation</h2>
            <div className="space-y-3">
              {agent.messages.map((msg) => (
                <div
                  key={msg.id}
                  className={`p-3 rounded-lg ${
                    msg.role === "user" ? "bg-blue-50 ml-8" : "bg-gray-50 mr-8"
                  }`}
                >
                  <div className="font-semibold text-sm mb-1">
                    {msg.role === "user" ? "You" : "Agent"}
                  </div>
                  <div>{msg.content}</div>
                </div>
              ))}
            </div>
          </div>
        </div>
      );
    }

## Running the Agent Programmatically#

Use `copilotkit.runAgent()` to trigger your agent from any component — no chat UI required. This is the same method CopilotKit's built-in `<CopilotChat />` uses internally.

page.tsx
    
    
    import { useAgent } from "@copilotkit/react-core/v2";
    import { useCopilotKit } from "@copilotkit/react-core/v2";
    import { randomUUID } from "@copilotkit/shared";
    
    export function AgentTrigger() {
      const { agent } = useAgent();
      const { copilotkit } = useCopilotKit();
    
      const handleRun = async () => {
        // Add a user message to the agent's conversation
        agent.addMessage({
          id: randomUUID(),
          role: "user",
          content: "Summarize the latest sales data",
        });
    
        // Run the agent — handles tool execution, follow-ups, and streaming
        await copilotkit.runAgent({ agent });
      };
    
      return <button onClick={handleRun}>Run Agent</button>;
    }

### `copilotkit.runAgent()` vs `agent.runAgent()`#

Both methods trigger the agent, but they operate at different levels:

  * **`copilotkit.runAgent({ agent })`** — The recommended approach. Orchestrates the full agent lifecycle: executes frontend tools, handles follow-up runs when tools request them, and manages errors through the subscriber system.
  * **`agent.runAgent()`** — Low-level method on the agent instance. Sends the request to the runtime but does **not** execute frontend tools or handle follow-ups. Use this only when you need direct control over the agent execution. To resume from an interrupt, use `copilotkit.runAgent({ agent, resume })` for standard AG-UI interrupts, or `copilotkit.runAgent({ agent, forwardedProps: { command: { resume, interruptEvent } } })` for legacy `on_interrupt` custom events, so that the subscriber lifecycle still wraps the resumed run.



### Stopping a Run#

You can stop a running agent using `copilotkit.stopAgent()`:

page.tsx
    
    
    const handleStop = () => {
      copilotkit.stopAgent({ agent });
    };

### On this page

OverviewWorking with StateReading StateUpdating StateSubscribing to Agent EventsBasic Event SubscriptionAvailable EventsRendering Tool CallsBuilding a Complete DashboardRunning the Agent Programmaticallycopilotkit.runAgent() vs agent.runAgent()Stopping a Run
