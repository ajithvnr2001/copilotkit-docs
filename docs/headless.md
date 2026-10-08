---
url: https://docs.copilotkit.ai/headless/
title: Headless UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:03:57.180023+00:00
---

# Headless UI

> Source: https://docs.copilotkit.ai/headless/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/)[Quickstart](https://docs.copilotkit.ai/quickstart)[Build with agents](https://docs.copilotkit.ai/build-with-agents)[Intelligence](https://docs.copilotkit.ai/intelligence/overview)

Basics

Chat

[Prebuilt Components](https://docs.copilotkit.ai/prebuilt-components)

Custom Look and Feel

[Slots](https://docs.copilotkit.ai/custom-look-and-feel/slots)[Headless UI](https://docs.copilotkit.ai/custom-look-and-feel/headless-ui)

[Programmatic Control](https://docs.copilotkit.ai/programmatic-control)

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

Headless UI

BasicsChatCustom Look and Feel

# Headless UI

Fully customize your Copilot's UI from the ground up using headless UI

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

A headless UI gives you full control over the chat experience — you bring your own components, layout, and styling while CopilotKit handles agent communication, message management, and streaming. This is built on top of the same primitives (`useAgent` and `useCopilotKit`) covered in Programmatic Control.

## When should I use this?#

Use headless UI when the slot system isn't enough — for example, when you need a completely different layout, want to embed the chat into an existing UI, or are building a non-chat interface that still communicates with an agent.

## Implementation#

### Access the agent and CopilotKit#

Use `useAgent` to get the agent instance (messages, state, execution status) and `useCopilotKit` to run the agent.

components/custom-chat.tsx
    
    
    import { useAgent } from "@copilotkit/react-core/v2";
    import { useCopilotKit } from "@copilotkit/react-core/v2";
    import { randomUUID } from "@copilotkit/shared";
    
    export function CustomChat() {
      const { agent } = useAgent();
      const { copilotkit } = useCopilotKit();
    
      return <div>{/* Your custom UI */}</div>;
    }

### Display messages#

The agent's messages are available via `agent.messages`. Each message has an `id`, `role` (`"user"` or `"assistant"`), and `content`.

components/custom-chat.tsx
    
    
    export function CustomChat() {
      const { agent } = useAgent();
      const { copilotkit } = useCopilotKit();
    
      return (
        <div className="flex flex-col h-full">
          <div className="flex-1 overflow-y-auto p-4 space-y-4">
            {agent.messages.map((msg) => (
              <div
                key={msg.id}
                className={
                  msg.role === "user"
                    ? "ml-auto bg-blue-100 rounded-lg p-3 max-w-md"
                    : "bg-gray-100 rounded-lg p-3 max-w-md"
                }
              >
                <p className="text-sm font-medium">{msg.role}</p>
                <p>{msg.content}</p>
              </div>
            ))}
            {agent.isRunning && <div className="text-gray-400">Thinking...</div>}
          </div>
        </div>
      );
    }

### Send messages and run the agent#

Add a message to the agent's conversation, then call `copilotkit.runAgent()` to trigger execution. This is the same method CopilotKit's built-in `<CopilotChat />` uses internally.

components/custom-chat.tsx
    
    
    import { useState, useCallback } from "react";
    
    export function CustomChat() {
      const { agent } = useAgent();
      const { copilotkit } = useCopilotKit();
      const [input, setInput] = useState("");
    
      const sendMessage = useCallback(async () => {
        if (!input.trim()) return;
    
        agent.addMessage({
          id: randomUUID(),
          role: "user",
          content: input,
        });
    
        setInput("");
    
        await copilotkit.runAgent({ agent });
      }, [input, agent, copilotkit]);
    
      return (
        <div className="flex flex-col h-full">
          <div className="flex-1 overflow-y-auto p-4 space-y-4">
            {agent.messages.map((msg) => (
              <div
                key={msg.id}
                className={
                  msg.role === "user"
                    ? "ml-auto bg-blue-100 rounded-lg p-3 max-w-md"
                    : "bg-gray-100 rounded-lg p-3 max-w-md"
                }
              >
                <p>{msg.content}</p>
              </div>
            ))}
            {agent.isRunning && <div className="text-gray-400">Thinking...</div>}
          </div>
    
          <form
            className="border-t p-4 flex gap-2"
            onSubmit={(e) => {
              e.preventDefault();
              sendMessage();
            }}
          >
            <input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Type a message..."
              className="flex-1 border rounded-lg px-3 py-2"
            />
            <button type="submit" disabled={agent.isRunning}>
              Send
            </button>
          </form>
        </div>
      );
    }

### Stop the agent#

Use `copilotkit.stopAgent()` to cancel a running agent:

components/custom-chat.tsx
    
    
    const stopAgent = useCallback(() => {
      copilotkit.stopAgent({ agent });
    }, [agent, copilotkit]);
    
    // In your JSX:
    {
      agent.isRunning && (
        <button onClick={stopAgent} className="text-red-500">
          Stop
        </button>
      );
    }

### On this page

What is this?When should I use this?ImplementationAccess the agent and CopilotKitDisplay messagesSend messages and run the agentStop the agent
