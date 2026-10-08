---
url: https://docs.copilotkit.ai/ms-agent-python/generative-ui/frontend-cards/
title: Frontend-Driven Cards
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:22:06.880076+00:00
---

# Frontend-Driven Cards

> Source: https://docs.copilotkit.ai/ms-agent-python/generative-ui/frontend-cards/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMS Agent Framework (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ms-agent-python)[Quickstart](https://docs.copilotkit.ai/ms-agent-python/quickstart)[Build with agents](https://docs.copilotkit.ai/ms-agent-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ms-agent-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ms-agent-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ms-agent-python/webmcp)

Agent capabilities

Microsoft Agent Framework

[Sub-agents](https://docs.copilotkit.ai/ms-agent-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ms-agent-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ms-agent-python/learning)

[User Memories](https://docs.copilotkit.ai/ms-agent-python/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ms-agent-python/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ms-agent-python/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ms-agent-python/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ms-agent-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ms-agent-python/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ms-agent-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/ms-agent-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[MS Agent Framework (Python)](https://docs.copilotkit.ai/ms-agent-python)[Build Generative UI](https://docs.copilotkit.ai/ms-agent-python/generative-ui)

# Frontend-Driven Cards

Insert a card into the chat transcript from frontend code, without a tool call and without adding to the conversation.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

Sometimes your application, not your agent, has something to show in the chat. A background job finishes, a websocket pushes an alert, or the user clicks a button. You want a card in the transcript, but there is no agent turn to hang it on, and you do not want to add a fake message to the conversation.

Activity messages solve this. An activity message is a message with `role: "activity"`. It renders in the transcript like any other message, and it is stripped from the payload sent to your agent on every run. The agent and the model never see it.

## When should I use this?#

Use a frontend-driven card when:

  * A frontend event, not the agent, is the source of the card.
  * The card must not become part of the conversation the model reads.
  * Session-only is acceptable. The card is not persisted with the thread.



Use [tool-based generative UI](https://docs.copilotkit.ai/ms-agent-python/generative-ui/tool-based) instead when the agent decides to show the card, or when the card must survive a page reload.

## How it works in code#

### 1\. Write the renderer#

A renderer pairs an `activityType` with a component and a schema for the card's content.

app/event-card.tsx
    
    
    import { z } from "zod";
    import type { ReactActivityMessageRenderer } from "@copilotkit/react-core/v2";
    
    const contentSchema = z.object({
      title: z.string(),
      detail: z.string().optional(),
    });
    
    export const eventCardRenderer: ReactActivityMessageRenderer<
      z.infer<typeof contentSchema>
    > = {
      activityType: "app-event-card", 
      content: contentSchema,
      render: ({ content }) => (
        <div className="rounded-lg border p-4">
          <strong>{content.title}</strong>
          {content.detail ? <p>{content.detail}</p> : null}
        </div>
      ),
    };

### 2\. Register it on the provider#

app/page.tsx
    
    
    import { CopilotKit, CopilotChat } from "@copilotkit/react-core/v2";
    import { eventCardRenderer } from "./event-card";
    
    export default function Page() {
      return (
        <CopilotKit
          runtimeUrl="/api/copilotkit"
          renderActivityMessages={[eventCardRenderer]} 
        >
          <CopilotChat />
        </CopilotKit>
      );
    }

### 3\. Add the card from frontend code#

Get the live agent with `useAgent()`, then call `addMessage` with `role: "activity"`.

app/deployment-watcher.tsx
    
    
    import { useEffect } from "react";
    import { useAgent } from "@copilotkit/react-core/v2";
    
    export function DeploymentWatcher() {
      const { agent } = useAgent();
    
      useEffect(() => {
        const socket = new WebSocket("wss://example.com/deployments");
        socket.onmessage = (event) => {
          const deployment = JSON.parse(event.data);
          agent.addMessage({
            id: crypto.randomUUID(),
            role: "activity", 
            activityType: "app-event-card",
            content: { title: "Deployment finished", detail: deployment.sha },
          });
        };
        return () => socket.close();
      }, [agent]);
    
      return null;
    }

Use the agent returned by `useAgent()`. An agent instance you construct and hold yourself is not the instance the chat renders, so messages added to it never appear.

The same works inside an `agent.subscribe` handler, a button `onClick`, or any other frontend code that can reach the agent.

## What the agent receives#

Activity messages stay in `agent.messages` so the transcript renders them, and `prepareRunAgentInput` removes them before the run payload leaves the browser.

Given a transcript of one user message and one card:

Where| Roles present  
---|---  
`agent.messages` (what the chat renders)| `user`, `activity`  
Run payload (what your agent receives)| `user`  
  
A `MESSAGES_SNAPSHOT` from the backend does not remove your card either. The snapshot merge preserves activity messages, so a card added in the browser survives a server-side history replay.

## Limitations#

  * **Not persisted.** The card never reaches the backend, so it is gone after a reload. If you need the card to come back, emit it from the agent as an activity event instead.
  * **One renderer per activity type.** Register a renderer whose `activityType` matches, or use `"*"` as a wildcard. An activity message with no matching renderer renders nothing.



### On this page

What is this?When should I use this?How it works in code1\. Write the renderer2\. Register it on the provider3\. Add the card from frontend codeWhat the agent receivesLimitations
