---
url: https://docs.copilotkit.ai/ms-agent-harness-dotnet/tutorials/ai-powered-textarea/step-4-copilot-readable-state/
title: Step 3: Copilot Readable State
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:21:12.076708+00:00
---

# Step 3: Copilot Readable State

> Source: https://docs.copilotkit.ai/ms-agent-harness-dotnet/tutorials/ai-powered-textarea/step-4-copilot-readable-state/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMS Agent Harness (.NET)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ms-agent-harness-dotnet)[Quickstart](https://docs.copilotkit.ai/ms-agent-harness-dotnet/quickstart)[Build with agents](https://docs.copilotkit.ai/ms-agent-harness-dotnet/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ms-agent-harness-dotnet/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ms-agent-harness-dotnet/webmcp)

Agent capabilities

MS Agent Harness (.NET)

[Sub-agents](https://docs.copilotkit.ai/ms-agent-harness-dotnet/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ms-agent-harness-dotnet/learning)

[User Memories](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/ms-agent-harness-dotnet/telemetry)[Community frameworks](https://docs.copilotkit.ai/ms-agent-harness-dotnet/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[MS Agent Harness (.NET)](https://docs.copilotkit.ai/ms-agent-harness-dotnet)TutorialsTutorial: AI Textarea

# Step 3: Copilot Readable State

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

At this point, we have set up our CopilotKit provider and `<CopilotTextarea />`, and we already benefit from a great AI assistant. However, there is one last problem - the copilot assistant is not aware of the email thread. Let's fix that.

## Our App's State#

Let's quickly review how our app's state works. Open up the [`lib/hooks/use-emails.tsx`](https://github.com/CopilotKit/CopilotKit/tree/main/examples/starters/textarea/start/lib/hooks/use-emails.tsx) file.

At a glance, we can see that the file exposes a provider (`EmailsProvider`) which holds our `emails`. This is the context we need to provide to our copilot to get AI autocompletions.

## The `useAgentContext` hook#

Our goal is to make our copilot aware of this state, so that it can provide more accurate and helpful responses. We can easily achieve this by using the [`useAgentContext`](https://docs.copilotkit.ai/reference/hooks/useAgentContext) hook.

libs/hooks/use-emails.tsx
    
    
    // ... the rest of the file
    
    export const EmailsProvider = ({ children }: { children: ReactNode }) => {
      const [emails, setEmails] = useState<Email[]>(emailHistory);
    
      useAgentContext({
        description: "The history of this email thread",
        value: emails,
      });
    
      // ... the rest of the file
    };

In this example, we use the `useAgentContext` hook to provide the copilot with the state of our email thread.

  * For the `description` property, we provide a concise description that tells the copilot what this piece of readable data means.
  * For the `value` property, we pass the entire state as a JSON string.



In the next step, we'll set up our AI-powered textarea, which will use this readable state to provide accurate and helpful responses.

## Try it out!#

Now, go back to the app and start typing things related to the email thread. Some ideas:

  * `"Thanks Jo..."` (the assistant will complete John's name)
  * `"I'm glad Spac..."` (the assistant will complete the company's name to SpaceY)
  * `"I'm glad they liked my..."` (the assistant will add context)



Your textarea is now fully aware of the email thread, and therefore it provides helpful, relevant autocompletions. 🚀

### [← Previous: Add CopilotTextareaSwap the plain textarea for CopilotKit's AI-aware version.](https://docs.copilotkit.ai/tutorials/ai-powered-textarea/step-3-copilot-textarea)### [Next: Wrap up →Find the source code, ideas for what to build next, and more tutorials.](https://docs.copilotkit.ai/tutorials/ai-powered-textarea/next-steps)

### On this page

Our App's StateThe useAgentContext hookTry it out!
