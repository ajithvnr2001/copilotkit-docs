---
url: https://docs.copilotkit.ai/langgraph-fastapi/troubleshooting/migrate-to-1.8.2
title: Migrate to 1.8.2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:06:04.484900+00:00
---

# Migrate to 1.8.2

> Source: https://docs.copilotkit.ai/langgraph-fastapi/troubleshooting/migrate-to-1.8.2

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

On this page

[LangGraph (FastAPI)](https://docs.copilotkit.ai/langgraph-fastapi)Troubleshooting

# Migrate to 1.8.2

Migration guide for CopilotKit 1.8.2

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What's changed?#

### New Look and Feel#

CopilotKit 1.8.2 introduces a new default look and feel. This includes new use of theming variables, new components, and generally a fresh look.

**Click the button in the bottom right to see the new look and feel in action!**

### Thumbs Up/Down Handlers#

The chat components now have `onThumbsUp` and `onThumbsDown` handlers. Specifying these will add icons to each message on hover allowing the user to provide feedback.
    
    
    <CopilotChat
      onThumbsUp={(message) => console.log(message)}
      onThumbsDown={(message) => console.log(message)}
    />

This was previously achievable in our framework, but we're making it first class now! You can use this to help fine-tune your model through CopilotKit or just generally track user feedback.

### ResponseButton prop removed#

The `ResponseButton` prop has been removed. This was a prop that was used to customize the button that appears after a response was generated in the chat.

In its place, we now place buttons below each message for:

  * Thumbs up
  * Thumbs down
  * Copy
  * Regenerate



The behvior, icons and styling for each of these buttons can be customized. Checkout our [look and feel guides](https://docs.copilotkit.ai/custom-look-and-feel) for more details.

### Out-of-the-box dark mode support#

CopilotKit now has out-of-the-box dark mode support. This is controlled by the `.dark` class (Tailwind) as well as the `color-scheme` CSS selector.

If you would like to make a custom theme, you can do so by checking out the [custom look and feel](https://docs.copilotkit.ai/custom-look-and-feel) guides.

### On this page

What's changed?New Look and FeelThumbs Up/Down HandlersResponseButton prop removedOut-of-the-box dark mode support
