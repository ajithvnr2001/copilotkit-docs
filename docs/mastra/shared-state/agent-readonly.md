---
url: https://docs.copilotkit.ai/mastra/shared-state/agent-readonly/
title: Agent Read-Only Context
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:17:07.657188+00:00
---

# Agent Read-Only Context

> Source: https://docs.copilotkit.ai/mastra/shared-state/agent-readonly/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMastra

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/mastra)[Quickstart](https://docs.copilotkit.ai/mastra/quickstart)[Build with agents](https://docs.copilotkit.ai/mastra/build-with-agents)[Intelligence](https://docs.copilotkit.ai/mastra/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/mastra/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/mastra/webmcp)

Agent capabilities

Mastra

[Sub-agents](https://docs.copilotkit.ai/mastra/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/mastra/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/mastra/learning)

[User Memories](https://docs.copilotkit.ai/mastra/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/mastra/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/mastra/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/mastra/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/mastra/intelligence/analytics)[Channels](https://docs.copilotkit.ai/mastra/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/mastra/telemetry)[Community frameworks](https://docs.copilotkit.ai/mastra/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Mastra](https://docs.copilotkit.ai/mastra)[Shared State](https://docs.copilotkit.ai/mastra/shared-state)

# Agent Read-Only Context

Publish UI values to the agent as a one-way read-only channel via useAgentContext.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

page.tsx

route.ts
    
    
    "use client";import React, { useState } from "react";import {  CopilotKit,  CopilotPopup,  useAgentContext,} from "@copilotkit/react-core/v2";import { ACTIVITIES, DemoLayout } from "./demo-layout";import { useReadonlyStateAgentContextSuggestions } from "./suggestions";export default function ReadonlyStateAgentContextDemo() {  return (    <CopilotKit      runtimeUrl="/api/copilotkit"      agent="readonly-state-agent-context"    >      <DemoContent />      <CopilotPopup        agentId="readonly-state-agent-context"        defaultOpen={true}        labels={{ chatInputPlaceholder: "Ask about your context..." }}      />    </CopilotKit>  );}function DemoContent() {  const [userName, setUserName] = useState("Atai");  const [userTimezone, setUserTimezone] = useState("America/Los_Angeles");  const [recentActivity, setRecentActivity] = useState<string[]>([    ACTIVITIES[0],    ACTIVITIES[2],  ]);  useAgentContext({    description: "The currently logged-in user's display name",    value: userName,  });  useAgentContext({    description: "The user's IANA timezone (used when mentioning times)",    value: userTimezone,  });  useAgentContext({    description: "The user's recent activity in the app, newest first",    value: recentActivity,  });  useReadonlyStateAgentContextSuggestions();  const toggleActivity = (activity: string) => {    setRecentActivity((prev) =>      prev.includes(activity)        ? prev.filter((a) => a !== activity)        : [...prev, activity],    );  };  return (    <DemoLayout      userName={userName}      userTimezone={userTimezone}      recentActivity={recentActivity}      onUserNameChange={setUserName}      onUserTimezoneChange={setUserTimezone}      onToggleActivity={toggleActivity}    />  );}

See this in Inspector

Open Inspector on localhost. Go to **Agents** , then **Context**. The values you publish with `useAgentContext` appear here.

More detail: [Inspector](https://docs.copilotkit.ai/mastra/inspector).

## What is this?#

Sometimes you want the agent to _know_ something about the current UI, like the logged-in user, the current page, or a recent activity log, but you don't want the agent to be able to modify it. That's what `useAgentContext` is for: a one-way **UI → agent** channel for read-only context.

Unlike full shared state (where the agent can call tools that mutate the state back to the UI), `useAgentContext` values are pure inputs. The agent sees them on every turn via the runtime's context injection, but it has no setter and no tool to write them back.

## When should I use this?#

Reach for `useAgentContext` instead of full shared state when:

  * The value is **UI-owned** and has no meaning to the agent beyond "what the user is looking at right now".
  * The agent should read but never write (user identity, feature flags, selected record, scroll position).
  * You want the value to automatically unregister on unmount (e.g. the "current record" context disappears when you leave the page).



Think of it as "props for the agent".

## How it works in code#

Call `useAgentContext({ description, value })` once per value you want to publish. Each call registers a dynamic context entry with the runtime that is:

  * Refreshed whenever `value` changes (React re-renders).
  * Automatically removed when the component unmounts.
  * Surfaced to the agent via the backend's `CopilotKitMiddleware`, which threads the entries into the model's message history on every turn.



page.tsx
    
    
      useAgentContext({    description: "The currently logged-in user's display name",    value: userName,  });  useAgentContext({    description: "The user's IANA timezone (used when mentioning times)",    value: userTimezone,  });  useAgentContext({    description: "The user's recent activity in the app, newest first",    value: recentActivity,  });

The `description` is important: it's a short human-readable label the agent sees alongside the value, so it knows what to do with it. Treat it like a parameter docstring.

## Wire it to your own state#

`useAgentContext` doesn't care where the value comes from: local state, a React Context, Redux, a query cache, anything. The only requirement is that the identity of the value is stable enough for React to avoid a render loop. In the demo we use a handful of `useState` hooks; in a real app these would likely come from an auth provider, a router hook, and your domain state stores.

page.tsx
    
    
    import React, { useState } from "react";import {  CopilotKit,  CopilotPopup,  useAgentContext,} from "@copilotkit/react-core/v2";import { ACTIVITIES, DemoLayout } from "./demo-layout";import { useReadonlyStateAgentContextSuggestions } from "./suggestions";export default function ReadonlyStateAgentContextDemo() {  return (    <CopilotKit      runtimeUrl="/api/copilotkit"      agent="readonly-state-agent-context"    >      <DemoContent />      <CopilotPopup        agentId="readonly-state-agent-context"        defaultOpen={true}        labels={{ chatInputPlaceholder: "Ask about your context..." }}      />    </CopilotKit>  );}function DemoContent() {  const [userName, setUserName] = useState("Atai");  const [userTimezone, setUserTimezone] = useState("America/Los_Angeles");  const [recentActivity, setRecentActivity] = useState<string[]>([    ACTIVITIES[0],    ACTIVITIES[2],  ]);

## Read-only, by design#

Because the agent never sees a setter or a mutation tool for these values, there's no way for a confused LLM to "update" them. That makes `useAgentContext` the right tool whenever the value in question is an input, not a field: the "context object passed to the agent on every turn", rather than "shared workspace you both edit".

When you need both reads _and_ writes, you want full **[shared state](https://docs.copilotkit.ai/mastra/shared-state)** instead.

## Related#

  * **[Shared State (overview)](https://docs.copilotkit.ai/mastra/shared-state)** — bidirectional reads + writes.
  * **[State streaming](https://docs.copilotkit.ai/mastra/shared-state/streaming)** — stream agent-written state back to the UI during a run.


