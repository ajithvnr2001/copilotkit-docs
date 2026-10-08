---
url: https://docs.copilotkit.ai/langgraph-typescript/generative-ui/a2ui/styling/
title: Styling
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:11:12.775098+00:00
---

# Styling

> Source: https://docs.copilotkit.ai/langgraph-typescript/generative-ui/a2ui/styling/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-typescript)[Quickstart](https://docs.copilotkit.ai/langgraph-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-typescript/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-typescript/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/langgraph-typescript/webmcp)

Agent capabilities

LangGraph (TypeScript)

[Sub-agents](https://docs.copilotkit.ai/langgraph-typescript/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/langgraph-typescript/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/langgraph-typescript/learning)

[User Memories](https://docs.copilotkit.ai/langgraph-typescript/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/langgraph-typescript/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/langgraph-typescript/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/langgraph-typescript/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/langgraph-typescript/intelligence/analytics)[Channels](https://docs.copilotkit.ai/langgraph-typescript/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/langgraph-typescript/telemetry)[Community frameworks](https://docs.copilotkit.ai/langgraph-typescript/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[LangGraph (TypeScript)](https://docs.copilotkit.ai/langgraph-typescript)[Build Generative UI](https://docs.copilotkit.ai/langgraph-typescript/generative-ui)[A2UI](https://docs.copilotkit.ai/langgraph-typescript/generative-ui/a2ui)

# Styling

Customize the appearance of A2UI surfaces with CSS custom properties, fonts, and component-level overrides.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

A2UI surfaces support theming through CSS custom properties scoped to the `.a2ui-surface` class.

## Theme CSS#

Create a theme file and import it in your layout:

src/a2ui/theme.css
    
    
    .a2ui-surface {
      --primary: #111111;
      --primary-foreground: #ffffff;
      --card: #ffffff;
      --border: #e0e0e0;
      --radius: 12px;
      --foreground: #111111;
      --input: #d4d4d4;
      --background: #fafafa;
    }

src/app/layout.tsx
    
    
    import "@/a2ui/theme.css";

## CSS custom properties reference#

Variable| Default| Description  
---|---|---  
`--primary`| —| Primary accent color (buttons, links)  
`--primary-foreground`| —| Text color on primary backgrounds  
`--card`| —| Card background color  
`--border`| —| Border color for cards, dividers, inputs  
`--radius`| —| Border radius for cards and buttons  
`--foreground`| —| Default text color  
`--input`| —| Input field border color  
`--background`| —| Surface background color  
  
These variables are scoped to `.a2ui-surface` — they won't affect the rest of your app. You can also set them on `:root` if you want global defaults.

## Custom fonts#

Override the font family on the surface container:

src/a2ui/theme.css
    
    
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
    
    .a2ui-surface {
      font-family: "Plus Jakarta Sans", -apple-system, BlinkMacSystemFont, system-ui, sans-serif !important;
      letter-spacing: -0.01em;
    }

## Image sizing#

A2UI surfaces render Image components at their natural size. For consistent layouts (e.g., airline logos, avatars), constrain images with CSS:

src/a2ui/theme.css
    
    
    /* Constrain logos and avatars */
    .a2ui-surface img {
      max-width: 28px;
      max-height: 28px;
      border-radius: 4px;
    }
    
    /* Smaller status indicator icons */
    .a2ui-surface img[alt="On Time"],
    .a2ui-surface img[alt="Delayed"] {
      max-width: 10px;
      max-height: 10px;
      border-radius: 50%;
    }

## Card width#

When streaming cards one-by-one, a single card can collapse to a narrow width. Set a minimum:

src/a2ui/theme.css
    
    
    .a2ui-surface .a2ui-card {
      min-width: 280px;
    }

## Dark mode#

Target dark mode with a class or media query:

src/a2ui/theme.css
    
    
    .dark .a2ui-surface,
    @media (prefers-color-scheme: dark) {
      .a2ui-surface {
        --primary: #e5e5e5;
        --primary-foreground: #111111;
        --card: #1a1a1a;
        --border: #333333;
        --foreground: #e5e5e5;
        --input: #444444;
        --background: #111111;
      }
    }

## Full example#

Here's a complete theme file combining all the patterns above:

src/a2ui/theme.css
    
    
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
    
    .a2ui-surface {
      /* Colors */
      --primary: #111111;
      --primary-foreground: #ffffff;
      --card: #ffffff;
      --border: #e0e0e0;
      --radius: 12px;
      --foreground: #111111;
      --input: #d4d4d4;
      --background: #fafafa;
    
      /* Typography */
      font-family: "Plus Jakarta Sans", -apple-system, BlinkMacSystemFont, system-ui, sans-serif !important;
      letter-spacing: -0.01em;
    }
    
    /* Image constraints */
    .a2ui-surface img {
      max-width: 28px;
      max-height: 28px;
      border-radius: 4px;
    }
    
    /* Streaming card width */
    .a2ui-surface .a2ui-card {
      min-width: 280px;
    }

### On this page

Theme CSSCSS custom properties referenceCustom fontsImage sizingCard widthDark modeFull example
