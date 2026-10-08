---
url: https://docs.copilotkit.ai/ms-agent-harness-dotnet/tutorials/ai-powered-textarea/step-3-copilot-textarea/
title: Step 4: Copilot Textarea
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:21:12.007809+00:00
---

# Step 4: Copilot Textarea

> Source: https://docs.copilotkit.ai/ms-agent-harness-dotnet/tutorials/ai-powered-textarea/step-3-copilot-textarea/

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

# Step 4: Copilot Textarea

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Currently, our app has a simple textarea for replying to emails. Let's replace this with an AI-powered textarea so that we can benefit from our helpful AI assistant.

## The `<Reply />` Component#

Head over to the [`/components/Reply.tsx`](https://github.com/CopilotKit/CopilotKit/tree/main/examples/starters/textarea/start/components/Reply.tsx) file.

At a glance, you can see that this component uses `useState` to hold the current input value and provide it to the textarea. We also use the `onChange` prop of the textarea to update the state.

## Implementing `<CopilotTextarea />`#

The `<CopilotTextarea />` component was designed to be a drop-in replacement for the `<textarea />` component. Let's implement it!

components/Reply.tsx
    
    
    // ... the rest of the file
    
    export function Reply() {
      // ...
      return (
        <div className="mt-4 pt-4 space-y-2 bg-background p-4 rounded-md border">
          <CopilotTextarea
            className="min-h-40 border h-40 p-2 overflow-hidden"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Write your reply..."
            autosuggestionsConfig={{
              textareaPurpose: `Assist me in replying to this email thread. Remember all important details.`,
              chatApiConfigs: {},
            }}
          />
          <Button disabled={!input} onClick={handleReply}>
            Reply
          </Button>
        </div>
      );
    }

We import the `<CopilotTextarea />` component and use it in place of the `<textarea />` component. There are also some optional style changes made here.

We can provide more specific instructions for this particular textarea via the `autoSuggestionsConfig.textareaPurpose` property.

## Try it out!#

Now, go back to the app and type anything in the textarea. You will see that the AI assistant provides suggestions as you type. How cool is that?

## The `CMD + K`/`CTRL + K` Shortcut#

While focused on the textarea, you can use the `CMD + K` (macOS) or `CTRL + K` (Windows) shortcut to open the action popup. Here, you can give the copilot specific instructions, such as:

  * `Rephrase the text to be more formal`
  * `Make the reply shorter`
  * `Tell John that I'm happy to help`



The `<CopilotTextarea />` is wired in, but the copilot doesn't know about the email thread yet — autocompletions can't reference earlier messages.

### [← Previous: Set up CopilotKitWire the CopilotKit provider into the email app.](https://docs.copilotkit.ai/tutorials/ai-powered-textarea/step-2-setup-copilotkit)### [Next: Make the textarea readable →Use useAgentContext so completions are aware of the full email history.](https://docs.copilotkit.ai/tutorials/ai-powered-textarea/step-4-copilot-readable-state)

### On this page

The <Reply /> ComponentImplementing <CopilotTextarea />Try it out!The CMD + K/CTRL + K Shortcut
