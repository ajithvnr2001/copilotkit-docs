---
url: https://docs.copilotkit.ai/strands/troubleshooting/migrate-to-v2/
title: Migrate to V2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:32:04.179646+00:00
---

# Migrate to V2

> Source: https://docs.copilotkit.ai/strands/troubleshooting/migrate-to-v2/

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

Your Components

[Copilot Runtime](https://docs.copilotkit.ai/strands/copilot-runtime)[AG-UI](https://docs.copilotkit.ai/strands/ag-ui)[AWS AgentCore](https://docs.copilotkit.ai/strands/deploy-agentcore)[Migrate to V2](https://docs.copilotkit.ai/strands/troubleshooting/migrate-to-v2)[Migrate to 1.10.X](https://docs.copilotkit.ai/strands/troubleshooting/migrate-to-1.10.X)[Migrate to 1.8.2](https://docs.copilotkit.ai/strands/troubleshooting/migrate-to-1.8.2)

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

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/strands/telemetry)[Community frameworks](https://docs.copilotkit.ai/strands/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Migrate to V2

Agent capabilitiesAWS Strands (Python)

# Migrate to V2

Migration guide for upgrading to CopilotKit V2 frontend packages

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview#

CopilotKit V2 consolidates the frontend into a single package. Both hooks and UI components are now exported from `@copilotkit/react-core/v2`. Your backend does not need any changes.

**What's changing:**

Before| After  
---|---  
v1 hooks from `@copilotkit/react-core`| v2 hooks from `@copilotkit/react-core/v2`  
`@copilotkit/react-ui`| `@copilotkit/react-core/v2`  
`@copilotkit/react-ui/styles.css`| `@copilotkit/react-core/v2/styles.css`  
  
**What's not changing:**

  * Backend packages (`@copilotkit/runtime`, etc.) do not need changes.
  * Your `CopilotRuntime` configuration stays the same.
  * Agent definitions and backend setup stay the same.
  * Keep the `<CopilotKit>` provider name, but import it from `@copilotkit/react-core/v2`.



## Migration Steps#

### Update v1 hook imports#

Replace v1 hooks from `@copilotkit/react-core` with their v2 equivalents from `@copilotkit/react-core/v2`. Keep the `<CopilotKit>` provider name, but import it from `@copilotkit/react-core/v2`.

#### Before
    
    
    import { CopilotKit } from "@copilotkit/react-core";
    import { useCopilotReadable, useCopilotAction } from "@copilotkit/react-core";

#### After
    
    
    import { CopilotKit, useAgent } from "@copilotkit/react-core/v2";

#### Hook mapping from v1 to v2

Use this table to find the v2 replacement for each v1 hook:

v1 hook| v2 hook  
---|---  
`useCopilotAction`| `useFrontendTool`  
`useCopilotReadable`| `useAgentContext`  
`useCopilotAdditionalInstructions`| `useAgentContext`  
`useCoAgent`| `useAgent`  
`useCopilotChat`| `useAgent` (low-level headless chat: `useCopilotChatHeadless_c`)  
  
Chat-UI customization props were also renamed in v2:

v1 (component prop)| v2 (slot / prop)  
---|---  
`AssistantMessage`| `assistantMessage` slot (under `messageView`)  
`markdownTagRenderers`| `markdownRenderer` slot (under `assistantMessage`)  
  
See [Slots](https://docs.copilotkit.ai/strands/custom-look-and-feel/slots) for how the v2 slot system replaces the v1 component-override props.

### Replace React UI imports#

UI components like `CopilotChat`, `CopilotSidebar`, and `CopilotPopup` are now exported from `@copilotkit/react-core/v2`.

#### Before
    
    
    import { CopilotPopup } from "@copilotkit/react-ui";
    import { CopilotSidebar } from "@copilotkit/react-ui";
    import { CopilotChat } from "@copilotkit/react-ui";

#### After
    
    
    import { CopilotPopup } from "@copilotkit/react-core/v2";
    import { CopilotSidebar } from "@copilotkit/react-core/v2";
    import { CopilotChat } from "@copilotkit/react-core/v2";

### Update your styles import#

#### Before
    
    
    import "@copilotkit/react-ui/styles.css";

#### After
    
    
    import "@copilotkit/react-core/v2/styles.css";

### Upgrade AG-UI client if using it directly#

If you import from `@ag-ui/client` directly, install the version that `@copilotkit/runtime` depends on:
    
    
    npm install @ag-ui/client@1.0.2

A different version installs a second copy of the package, with its own `HttpAgent` class. Run `npm ls @ag-ui/client` to make sure that only one version is installed.

Note: If you only use CopilotKit's React packages, `@ag-ui/client` types are already re-exported from `@copilotkit/react-core/v2` and you don't need a separate install.

## Full Example#

### Before#
    
    
    import { CopilotKit } from "@copilotkit/react-core";
    import { CopilotPopup } from "@copilotkit/react-ui";
    import "@copilotkit/react-ui/styles.css";
    
    export function App() {
      return (
        <CopilotKit runtimeUrl="/api/copilotkit">
          <YourApp />
          <CopilotPopup />
        </CopilotKit>
      );
    }

### After#
    
    
    import { CopilotKit, CopilotPopup } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";
    
    export function App() {
      return (
        <CopilotKit runtimeUrl="/api/copilotkit">
          <YourApp />
          <CopilotPopup />
        </CopilotKit>
      );
    }

### On this page

OverviewMigration StepsUpdate v1 hook importsReplace React UI importsUpdate your styles importUpgrade AG-UI client if using it directlyFull ExampleBeforeAfter
