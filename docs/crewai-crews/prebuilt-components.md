---
url: https://docs.copilotkit.ai/crewai-crews/prebuilt-components/
title: Prebuilt Components
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:57:51.922253+00:00
---

# Prebuilt Components

> Source: https://docs.copilotkit.ai/crewai-crews/prebuilt-components/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendCrewAI Flows

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/crewai-crews)[Quickstart](https://docs.copilotkit.ai/crewai-crews/quickstart)[Build with agents](https://docs.copilotkit.ai/crewai-crews/build-with-agents)[Intelligence](https://docs.copilotkit.ai/crewai-crews/intelligence/overview)

Basics

Chat

[Prebuilt Components](https://docs.copilotkit.ai/crewai-crews/prebuilt-components)

Custom Look and Feel

[Programmatic Control](https://docs.copilotkit.ai/crewai-crews/programmatic-control)

Threads

[Frontend-tools](https://docs.copilotkit.ai/crewai-crews/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/crewai-crews/webmcp)

Agent capabilities

CrewAI Flows

[Sub-agents](https://docs.copilotkit.ai/crewai-crews/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/crewai-crews/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/crewai-crews/learning)

[User Memories](https://docs.copilotkit.ai/crewai-crews/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/crewai-crews/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/crewai-crews/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/crewai-crews/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/crewai-crews/intelligence/analytics)[Channels](https://docs.copilotkit.ai/crewai-crews/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/crewai-crews/telemetry)[Community frameworks](https://docs.copilotkit.ai/crewai-crews/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

BasicsChat

# Prebuilt Components

Drop-in chat components for your CrewAI Flows agent.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

CopilotKit ships three prebuilt chat components that connect directly to your agent. Each is a wrapper around `CopilotChat` with a different layout — pick the one that fits your app and you're done.

If you've completed the quickstart, you already have one of these set up.

DemoCode

## Setup

Import the default styles in your root layout:

layout.tsx
    
    
    import "@copilotkit/react-core/v2/styles.css";

### CopilotChat

A flexible chat component that can be placed anywhere in your app and sized as needed.

page.tsx
    
    
    import { CopilotChat } from "@copilotkit/react-core/v2";
    
    export function YourComponent() {
      return (
        <CopilotChat
          labels={{
            welcomeMessageText: "Hi! How can I assist you today?",
          }}
        />
      );
    }

![CopilotChat example](https://cdn.copilotkit.ai/docs/copilotkit/images/copilotchat-example.gif)

### CopilotSidebar

Wraps your main content and provides a collapsible sidebar chat.

page.tsx
    
    
    import { CopilotSidebar } from "@copilotkit/react-core/v2";
    
    export default function YourApp() {
      return (
        <main>
          <CopilotSidebar
            defaultOpen={true}
            labels={{
              modalHeaderTitle: "Sidebar Assistant",
              welcomeMessageText: "How can I help you today?",
            }}
          />
          <h1>Your App</h1>
        </main>
      );
    }

![CopilotSidebar example](https://cdn.copilotkit.ai/docs/copilotkit/images/sidebar-example.gif)

### CopilotPopup

A floating chat bubble that sits alongside your content and toggles open/closed.

page.tsx
    
    
    import { CopilotPopup } from "@copilotkit/react-core/v2";
    
    export default function YourApp() {
      return (
        <main>
          <h1>Your App</h1>
          <CopilotPopup
            labels={{
              modalHeaderTitle: "Popup Assistant",
              welcomeMessageText: "Need any help?",
            }}
          />
        </main>
      );
    }

![CopilotPopup example](https://cdn.copilotkit.ai/docs/copilotkit/images/popup-example.gif)

## Customization

All three components support the slot system for deep customization — from Tailwind classes to full component replacement:

page.tsx
    
    
    <CopilotChat
      // Style slots with Tailwind classes
      input={{
        textArea: "text-blue-500",
        sendButton: "bg-blue-600 hover:bg-blue-700",
      }}
      // Customize nested message slots
      messageView={{
        assistantMessage: "bg-blue-50 rounded-xl p-2",
        userMessage: "bg-blue-100 rounded-xl",
      }}
    />
