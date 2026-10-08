---
url: https://docs.copilotkit.ai/strands/concepts/which-hook/
title: Which Hook for Which Job
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:30:55.916610+00:00
---

# Which Hook for Which Job

> Source: https://docs.copilotkit.ai/strands/concepts/which-hook/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAWS Strands (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/strands)[Quickstart](https://docs.copilotkit.ai/strands/quickstart)[Build with agents](https://docs.copilotkit.ai/strands/build-with-agents)[Intelligence](https://docs.copilotkit.ai/strands/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/strands/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/strands/webmcp)

Agent capabilities

AWS Strands (Python)

[Sub-agents](https://docs.copilotkit.ai/strands/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/strands/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/strands/learning)

[User Memories](https://docs.copilotkit.ai/strands/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/strands/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/strands/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/strands/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/strands/intelligence/analytics)[Channels](https://docs.copilotkit.ai/strands/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

Learn

Concepts

[Architecture](https://docs.copilotkit.ai/strands/concepts/architecture)[Generative UI](https://docs.copilotkit.ai/strands/concepts/generative-ui-overview)[Which Hook for Which Job](https://docs.copilotkit.ai/strands/concepts/which-hook)[Open source vs Intelligence](https://docs.copilotkit.ai/strands/concepts/oss-vs-enterprise)

[Agentic Protocols](https://docs.copilotkit.ai/strands/agentic-protocols)

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/strands/telemetry)[Community frameworks](https://docs.copilotkit.ai/strands/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Which Hook for Which Job

LearnConcepts

# Which Hook for Which Job

Choose the right CopilotKit v2 hook for tools, rendering, human review, and custom chat surfaces.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

CopilotKit v2 has a focused set of hooks for letting the agent _do things_ in your app and for _rendering_ what it does. They split into two groups: hooks that register behavior, and hooks that register how a tool call looks in the chat. Use this page as the quick map, then follow each hook to its full reference.

## The 30-second version#

Hook| Use it when you want to  
---|---  
[`useFrontendTool`](https://docs.copilotkit.ai/reference/hooks/useFrontendTool)| Give the agent a client-side tool to call (run logic in the browser), with optional inline UI.  
[`useRenderTool`](https://docs.copilotkit.ai/reference/hooks/useRenderTool)| Render the UI for a specific tool call by name (typed), without defining the tool's handler.  
[`useDefaultRenderTool`](https://docs.copilotkit.ai/reference/hooks/useDefaultRenderTool)| Provide one wildcard renderer for any tool call that has no specific renderer.  
[`useComponent`](https://docs.copilotkit.ai/reference/hooks/useComponent)| Register a React component as a named tool renderer (component-first generative UI).  
[`useHumanInTheLoop`](https://docs.copilotkit.ai/reference/hooks/useHumanInTheLoop)| Pause the agent on a tool call and wait for the user to approve, edit, or supply input.  
[`useInterrupt`](https://docs.copilotkit.ai/reference/hooks/useInterrupt)| Handle an agent-initiated interrupt and resume execution once the user responds.  
[`useRenderToolCall`](https://docs.copilotkit.ai/reference/hooks/useRenderToolCall)| Get a render function for tool calls to drive your own custom chat surface (headless).  
  
## How to choose#

Start with the verb.

  * **"The agent should _run_ something in my app."** Use [`useFrontendTool`](https://docs.copilotkit.ai/reference/hooks/useFrontendTool). You define the tool's schema and handler; the agent calls it. Add a `render` to also show inline UI for the call.
  * **"The agent's tool call should _look_ like something."** Use a render hook. Use [`useRenderTool`](https://docs.copilotkit.ai/reference/hooks/useRenderTool) to render one named tool, [`useComponent`](https://docs.copilotkit.ai/reference/hooks/useComponent) to bind a React component to a tool name, or [`useDefaultRenderTool`](https://docs.copilotkit.ai/reference/hooks/useDefaultRenderTool) as the catch-all for anything you didn't render explicitly.
  * **"The agent should _stop and ask me_ before continuing."** Use [`useHumanInTheLoop`](https://docs.copilotkit.ai/reference/hooks/useHumanInTheLoop) for tool-level approval/edit gates, or [`useInterrupt`](https://docs.copilotkit.ai/reference/hooks/useInterrupt) for agent-driven interrupts you resume with user input.
  * **"I'm building my _own_ chat UI."** Use [`useRenderToolCall`](https://docs.copilotkit.ai/reference/hooks/useRenderToolCall). It returns the renderer function so you can place tool-call output anywhere in a headless layout.



### Tool vs. renderer#

Two hooks in this set _register a tool_ the agent can call: `useFrontendTool` (schema and handler) and `useComponent` (a component-first shorthand that wraps `useFrontendTool` internally, registering a tool whose "handler" is rendering your component). The render-only hooks, `useRenderTool`, `useDefaultRenderTool`, and `useRenderToolCall`, _don't_ define a tool; they only _render_ tool calls, which can come from your frontend (`useFrontendTool` / `useComponent`) or from the agent/backend. That's why you can pair a backend tool with `useRenderTool` and never write a handler on the client.

## Related#

  * [Frontend Tools](https://docs.copilotkit.ai/strands/frontend-tools): the full guide to `useFrontendTool`.
  * [Generative UI](https://docs.copilotkit.ai/strands/generative-ui/tool-rendering): rendering tool calls as rich UI.
  * [Human in the Loop](https://docs.copilotkit.ai/strands/human-in-the-loop): approval and interrupt patterns.
  * [Hooks reference](https://docs.copilotkit.ai/reference): every v2 hook in detail.



### On this page

The 30-second versionHow to chooseTool vs. rendererRelated
