---
url: https://docs.copilotkit.ai/deepagents/custom-look-and-feel/css/
title: CSS Customization
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:59:35.072916+00:00
---

# CSS Customization

> Source: https://docs.copilotkit.ai/deepagents/custom-look-and-feel/css/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendDeep Agents

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/deepagents)[Quickstart](https://docs.copilotkit.ai/deepagents/quickstart)[Build with agents](https://docs.copilotkit.ai/deepagents/build-with-agents)[Intelligence](https://docs.copilotkit.ai/deepagents/intelligence/overview)

Basics

Chat

Prebuilt Components

Custom Look and Feel

[CSS Customization](https://docs.copilotkit.ai/deepagents/custom-look-and-feel/css)[Slots (Subcomponents)](https://docs.copilotkit.ai/deepagents/custom-look-and-feel/slots)[Markdown Rendering](https://docs.copilotkit.ai/deepagents/custom-look-and-feel/markdown)[Headless UI](https://docs.copilotkit.ai/deepagents/custom-look-and-feel/headless-ui)[Reasoning Messages](https://docs.copilotkit.ai/deepagents/custom-look-and-feel/reasoning-messages)

[Multimodal Attachments](https://docs.copilotkit.ai/deepagents/multimodal-attachments)[Voice](https://docs.copilotkit.ai/deepagents/voice)[Reasoning](https://docs.copilotkit.ai/deepagents/generative-ui/reasoning)

Threads

[Frontend-tools](https://docs.copilotkit.ai/deepagents/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/deepagents/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/deepagents/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/deepagents/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/deepagents/learning)

[User Memories](https://docs.copilotkit.ai/deepagents/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/deepagents/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/deepagents/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/deepagents/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/deepagents/intelligence/analytics)[Channels](https://docs.copilotkit.ai/deepagents/intelligence/channels)

Hosting

Backend

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

[Open-source telemetry](https://docs.copilotkit.ai/deepagents/telemetry)[Community frameworks](https://docs.copilotkit.ai/deepagents/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

CSS Customization

BasicsChatCustom Look and Feel

# CSS Customization

Theme CopilotKit components via CSS variables and class overrides.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Not available for Deep Agents yet

This feature (`chat-customization-css`) hasn't been tagged in any Deep Agents cell yet. Try [CopilotKit's Built-in Agent](https://docs.copilotkit.ai/built-in-agent/custom-look-and-feel/css), [LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python/custom-look-and-feel/css), [LangGraph (TypeScript)](https://docs.copilotkit.ai/langgraph-typescript/custom-look-and-feel/css).

## What is this?#

CopilotKit has a variety of ways to customize the colors and structure of the Copilot UI components via plain CSS. You can:

  * Override CopilotKit CSS variables to re-tint the whole UI
  * Target the built-in class names (`.copilotKit...`) for structural tweaks
  * Swap fonts per surface (messages, input, bubbles)
  * Replace icons and labels via component props



If you need to change behavior, not just look, see [slots](https://docs.copilotkit.ai/deepagents/custom-look-and-feel/slots) or [fully headless UI](https://docs.copilotkit.ai/deepagents/custom-look-and-feel/headless-ui).

## Scoping the theme#

The demo keeps all of its styling in a sibling `theme.css` file and applies it only to the wrapper div holding `<CopilotChat>`. Importing the stylesheet from the page module is enough; Next.js bundles it with the route:

Missing snippet

No demo found for `deepagents::chat-customization-css`. Known demos are bundled from manifest `demos[i]`; check the cell id and framework slug.

Scoping every selector under a wrapper class keeps the overrides from leaking into the rest of the app.

## CSS Variables (Easiest)#

The easiest way to change the colors used in the Copilot UI components is to override CopilotKit CSS variables. The demo sets them on the scope wrapper so they cascade into every nested chat component:

Missing snippet

No demo found for `deepagents::chat-customization-css`. Known demos are bundled from manifest `demos[i]`; check the cell id and framework slug.

Once you've found the right variable, you can also apply the overrides inline via the `CopilotKitCSSProperties` helper:
    
    
    import { CopilotKitCSSProperties } from "@copilotkit/react-ui";
    
    <div
      style={
        {
          "--copilot-kit-primary-color": "#222222",
        } as CopilotKitCSSProperties
      }
    >
      <CopilotSidebar />
    </div>

### Reference#

CSS Variable| Description  
---|---  
`--copilot-kit-primary-color`| Main brand/action color for buttons and interactive elements  
`--copilot-kit-contrast-color`| Color that contrasts with primary, used for text on primary elements  
`--copilot-kit-background-color`| Main page/container background color  
`--copilot-kit-secondary-color`| Secondary background for cards, panels, and elevated surfaces  
`--copilot-kit-secondary-contrast-color`| Primary text color for main content  
`--copilot-kit-separator-color`| Border color for dividers and containers  
`--copilot-kit-muted-color`| Muted color for disabled/inactive states  
`--copilot-kit-shadow-sm` / `-md` / `-lg`| Elevation shadows for subtle surfaces, cards, and modals  
  
Two token systems

The `--copilot-kit-*` variables above style the **v1** component CSS (`@copilotkit/react-ui`). The newer **v2** components (`@copilotkit/react-core/v2`) are Tailwind + shadcn-based and use a separate set of design tokens. See v2 design tokens below.

## v2 Design Tokens (shadcn)#

The v2 components (`@copilotkit/react-core/v2`) ship a Tailwind v4 theme built on the standard shadcn/ui token set. Instead of the `--copilot-kit-*` variables, they read [oklch](https://oklch.com) color tokens that are scoped to the `[data-copilotkit]` root and wired into Tailwind utilities through an `@theme inline` block. This means you can re-skin the entire v2 UI by overriding a handful of CSS custom properties. Every component picks the change up automatically.

Override them on the `[data-copilotkit]` element (or any ancestor) the same way you would in a shadcn project:

globals.css
    
    
    [data-copilotkit] {
      --primary: oklch(0.55 0.22 264); /* accent / action color */
      --primary-foreground: oklch(0.99 0 0); /* text on primary */
      --background: oklch(1 0 0); /* surface background */
      --foreground: oklch(0.145 0 0); /* primary text */
      --muted: oklch(0.97 0 0); /* subtle backgrounds */
      --border: oklch(0.922 0 0); /* dividers, outlines */
      --radius: 0.625rem; /* global corner radius */
    }
    
    /* Dark mode is keyed off a `.dark` ancestor */
    .dark [data-copilotkit] {
      --background: oklch(0.145 0 0);
      --foreground: oklch(0.985 0 0);
      --border: oklch(0.269 0 0);
    }

### Reference#

These are the most commonly overridden v2 tokens. Each light value has a matching dark-mode value under `.dark [data-copilotkit]`. The full set (popover, accent, destructive, chart, and sidebar variants) lives in `@copilotkit/react-core/v2/styles.css`.

Token| Description  
---|---  
`--background` / `--foreground`| Base surface background and primary text color  
`--primary` / `--primary-foreground`| Accent/action color and the text rendered on top of it  
`--secondary` / `--secondary-foreground`| Secondary surfaces (cards, panels) and their text  
`--muted` / `--muted-foreground`| Subtle backgrounds and de-emphasized text  
`--accent` / `--accent-foreground`| Hover/active states and their text  
`--border` / `--input` / `--ring`| Divider/outline color, input borders, focus ring  
`--destructive` / `--destructive-foreground`| Error/danger color and its text  
`--card` / `--popover` (+ `-foreground`)| Elevated surface backgrounds and their text  
`--sidebar-*`| The sidebar's own background/foreground/border/ring set  
`--radius`| Base corner radius; `--radius-sm/md/lg/xl` derive from it  
  
oklch values

v2 tokens use the `oklch()` color space, which keeps perceived lightness consistent across hues. You can still pass `hsl()`, `rgb()`, or hex; any valid CSS color works.

## Custom CSS#

The CopilotKit CSS is structured to allow customization via CSS classes. You can target specific pieces of the UI from your own stylesheet:

globals.css
    
    
    .copilotKitButton {
      border-radius: 0;
    }
    
    .copilotKitMessages {
      padding: 2rem;
    }
    
    .copilotKitUserMessage {
      background: #007AFF;
    }

The demo's `theme.css` wraps every selector under `.chat-css-demo-scope` so the overrides don't leak out. Here's the user message bubble block from that file:

Missing snippet

No demo found for `deepagents::chat-customization-css`. Known demos are bundled from manifest `demos[i]`; check the cell id and framework slug.

### Reference#

CSS Class| Description  
---|---  
`.copilotKitMessages`| Main container for all chat messages  
`.copilotKitMessage`| Base class applied to every message bubble (user and assistant)  
`.copilotKitInput`| Text input container with typing area and send button  
`.copilotKitUserMessage`| Styling for user messages  
`.copilotKitAssistantMessage`| Styling for AI responses  
`.copilotKitHeader`| Top bar of chat window containing title and controls  
`.copilotKitButton`| Primary chat toggle button  
`.copilotKitWindow`| Root container defining overall chat window dimensions  
`.copilotKitMarkdown`| Styles for rendered markdown content  
`.copilotKitCodeBlock`| Code snippet container with syntax highlighting  
`.copilotKitSidebar`| Styles for sidebar chat mode  
`.copilotKitPopup`| Styles for popup chat mode  
  
## Custom Fonts#

You can customize the fonts by updating the `fontFamily` property on the relevant CopilotKit classes:

globals.css
    
    
    .copilotKitMessages {
      font-family: "Arial, sans-serif";
    }
    
    .copilotKitInput {
      font-family: "Arial, sans-serif";
    }

## Custom Icons#

Customize icons by passing the `icons` prop to `CopilotSidebar`, `CopilotPopup`, or `CopilotChat`:
    
    
    <CopilotChat
      icons={{
        openIcon: <YourOpenIconComponent />,
        closeIcon: <YourCloseIconComponent />,
      }}
    />

## Custom Labels#

Customize all user-facing copy via the `labels` prop:
    
    
    <CopilotChat
      labels={{
        welcomeMessageText: "Hello! How can I help you today?",
        modalHeaderTitle: "My Copilot",
        chatInputPlaceholder: "Ask me anything!",
      }}
    />

### On this page

What is this?Scoping the themeCSS Variables (Easiest)Referencev2 Design Tokens (shadcn)ReferenceCustom CSSReferenceCustom FontsCustom IconsCustom Labels
