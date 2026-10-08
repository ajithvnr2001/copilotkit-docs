---
url: https://docs.copilotkit.ai/google-adk/contributing/code-contributions/package-linking/
title: Advanced: Package Linking
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:02:36.933537+00:00
---

# Advanced: Package Linking

> Source: https://docs.copilotkit.ai/google-adk/contributing/code-contributions/package-linking/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendGoogle ADK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/google-adk)[Quickstart](https://docs.copilotkit.ai/google-adk/quickstart)[Build with agents](https://docs.copilotkit.ai/google-adk/build-with-agents)[Intelligence](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/google-adk/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/google-adk/webmcp)

Agent capabilities

Google ADK

[Sub-agents](https://docs.copilotkit.ai/google-adk/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/google-adk/learning)

[User Memories](https://docs.copilotkit.ai/google-adk/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/google-adk/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/google-adk/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/google-adk/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/google-adk/intelligence/analytics)[Channels](https://docs.copilotkit.ai/google-adk/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/google-adk/telemetry)[Community frameworks](https://docs.copilotkit.ai/google-adk/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[Google ADK](https://docs.copilotkit.ai/google-adk)ContributingCode Contributions

# Advanced: Package Linking

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

In this guide, we'll teach you how to link the CopilotKit packages to your own project to test your changes. This way, you can run `pnpm run dev` in the CopilotKit monorepo, and see changes in your own project immediately.

## Global Package Linking With `pnpm`#

We will use pnpm's [global linking feature](https://pnpm.io/cli/link#pnpm-link---global) to link the CopilotKit packages to your own project.

### In The CopilotKit Monorepo#

Assuming you followed all steps in the contribution guide, you should have everything set up properly and ready to go.

Navigate to the CopilotKit monorepo and run the following command to link the packages globally:
    
    
    pnpm exec nx run-many -t link:global

### In Your Project#

In your project, ensure you have pnpm configured. This will not prevent you from using npm or yarn as well. But for the purpose of global linking, you must use pnpm.
    
    
    cd your-project
    pnpm i

Next, link the desired package in your project:
    
    
    # For example, to link the @copilotkit/react-core package:
    pnpm link --global @copilotkit/react-core

You can run this for all packages, or just the ones you need. Your changes will now be synced.

### Unlinking#

Once you are done, you can undo the global linking by running the following command in the CopilotKit monorepo:
    
    
    pnpm exec nx run-many -t unlink:global

And then in your project:
    
    
    pnpm install

That's it, everything is now back to normal!

## Need help?#

If you need help with anything, please don't hesitate to reach out to us on [Discord](https://discord.gg/6dffbvGU3D). We have a dedicated [#contributing](https://discord.com/channels/1122926057641742418/1183863183149117561) channel.

### On this page

Global Package Linking With pnpmNeed help?
