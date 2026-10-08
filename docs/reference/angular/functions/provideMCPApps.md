---
url: https://docs.copilotkit.ai/reference/angular/functions/provideMCPApps/
title: provideMCPApps
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:04.981414+00:00
---

# provideMCPApps

> Source: https://docs.copilotkit.ai/reference/angular/functions/provideMCPApps/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁AngularSDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Guides

[Public API inventory](https://docs.copilotkit.ai/reference/angular/public-api)[Production and lifecycle](https://docs.copilotkit.ai/reference/angular/production-lifecycle)

Components

[CopilotActivity](https://docs.copilotkit.ai/reference/angular/components/CopilotActivity)[CopilotChat](https://docs.copilotkit.ai/reference/angular/components/CopilotChat)[CopilotChatAssistantMessage](https://docs.copilotkit.ai/reference/angular/components/CopilotChatAssistantMessage)[CopilotChatInput](https://docs.copilotkit.ai/reference/angular/components/CopilotChatInput)[CopilotChatMessageView](https://docs.copilotkit.ai/reference/angular/components/CopilotChatMessageView)[CopilotChatUserMessage](https://docs.copilotkit.ai/reference/angular/components/CopilotChatUserMessage)[CopilotChatView](https://docs.copilotkit.ai/reference/angular/components/CopilotChatView)[CopilotPopup](https://docs.copilotkit.ai/reference/angular/components/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/angular/components/CopilotSidebar)

Functions

[connectAgentContext](https://docs.copilotkit.ai/reference/angular/functions/connectAgentContext)[injectAgentStore](https://docs.copilotkit.ai/reference/angular/functions/injectAgentStore)[injectCapabilities](https://docs.copilotkit.ai/reference/angular/functions/injectCapabilities)[injectChatLabels](https://docs.copilotkit.ai/reference/angular/functions/injectChatLabels)[injectCopilotKitConfig](https://docs.copilotkit.ai/reference/angular/functions/injectCopilotKitConfig)[injectInterrupt](https://docs.copilotkit.ai/reference/angular/functions/injectInterrupt)[injectThreads](https://docs.copilotkit.ai/reference/angular/functions/injectThreads)[provideCopilotChatLabels](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotChatLabels)[provideCopilotKit](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit)[provideMCPApps](https://docs.copilotkit.ai/reference/angular/functions/provideMCPApps)[registerComponent](https://docs.copilotkit.ai/reference/angular/functions/registerComponent)[registerFrontendTool](https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool)[registerHumanInTheLoop](https://docs.copilotkit.ai/reference/angular/functions/registerHumanInTheLoop)[registerRenderActivityMessage](https://docs.copilotkit.ai/reference/angular/functions/registerRenderActivityMessage)[registerRenderToolCall](https://docs.copilotkit.ai/reference/angular/functions/registerRenderToolCall)

Services

[CopilotKit](https://docs.copilotkit.ai/reference/angular/services/CopilotKit)

Directives

[CopilotKitAgentContext](https://docs.copilotkit.ai/reference/angular/directives/CopilotKitAgentContext)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[angular](https://docs.copilotkit.ai/reference/angular)Functions

# provideMCPApps

Configure the opt-in MCP Apps activity renderer for Angular.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Import MCP Apps from the secondary entry point so applications that do not use it do not load its host and sandbox code.
    
    
    import { ApplicationConfig } from "@angular/core";
    import { provideCopilotKit } from "@copilotkit/angular";
    import { provideMCPApps } from "@copilotkit/angular/mcp-apps";
    
    export const appConfig: ApplicationConfig = {
      providers: [
        provideCopilotKit({ runtimeUrl: "/api/copilotkit" }),
        provideMCPApps({
          idleTimeoutMs: 30_000,
          initializationTimeoutMs: 30_000,
          hostInfo: { name: "Acme Copilot", version: "1.0.0" },
        }),
      ],
    };
    
    
    interface MCPAppsConfig {
      idleTimeoutMs?: number;
      initializationTimeoutMs?: number;
      sandboxProxyUrl?: string;
      hostInfo?: { name: string; version: string };
      hostCapabilities?: Record<string, unknown>;
      hostContext?: Record<string, unknown>;
    }

`provideMCPApps` contributes a lower-precedence built-in renderer for `activityType: "mcp-apps"`; an explicit application activity renderer still wins. It deliberately accepts no MCP server URL. Resource loads, tool calls, and follow-up messages travel through the selected AG-UI agent.

`sandboxProxyUrl` selects a dedicated sandbox proxy document for hosts with a strict response-level content security policy. The document must implement the CopilotKit MCP sandbox proxy protocol and use an opaque response sandbox without `allow-same-origin`.

Each widget owns an abortable FIFO queue and iframe listener. Destroying one widget cancels only its work; changing threads drops queued stale work. Busy agents and initialization handshakes use the configured timeouts. Snapshot content, JSON-RPC messages, and exact iframe event sources are validated before use. Host context is browser-visible and must not contain secrets.

During SSR the widget is inert. Its sandbox and message listener initialize in the browser after hydration. `CopilotMCPAppsWidget`, schemas, tokens, and the ready-made activity config are also public from the secondary entry point for advanced custom hosts; see the [public API inventory](https://docs.copilotkit.ai/reference/angular/public-api).
