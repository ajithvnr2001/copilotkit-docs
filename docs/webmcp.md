---
url: https://docs.copilotkit.ai/webmcp/
title: WebMCP
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:34:25.351826+00:00
---

# WebMCP

> Source: https://docs.copilotkit.ai/webmcp/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/)[Quickstart](https://docs.copilotkit.ai/quickstart)[Build with agents](https://docs.copilotkit.ai/build-with-agents)[Intelligence](https://docs.copilotkit.ai/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/webmcp)

Agent capabilities

Built-in Agent

[Sub-agents](https://docs.copilotkit.ai/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/learning)

[User Memories](https://docs.copilotkit.ai/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/intelligence/analytics)[Channels](https://docs.copilotkit.ai/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/telemetry)[Community frameworks](https://docs.copilotkit.ai/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

WebMCP

Interactivity

# WebMCP

Expose browser-side actions as structured tools that compatible agents can discover and call.

## Overview#

WebMCP lets your website tell compatible browser agents what they can do. Instead of guessing which buttons to click, an agent discovers a named tool with a description, a typed input schema, and a JavaScript handler.

CopilotKit can publish an existing frontend tool to [`document.modelContext`](https://webmachinelearning.github.io/webmcp/). The same handler then works for your CopilotKit agent and for WebMCP-aware browser agents.

WebMCP is experimental

WebMCP is a draft Community Group report, not a W3C Standard. Chrome offers it through an origin trial beginning in Chrome 149, or through the `chrome://flags/#enable-webmcp-testing` flag for local development. CopilotKit safely does nothing when `document.modelContext` is unavailable. Check the [current Chrome setup instructions](https://developer.chrome.com/docs/ai/webmcp) before testing.

## Start with your coding agent#

Use this pre-built prompt to add WebMCP to your project. Your coding agent will adapt the implementation to your app and verify that a compatible browser can discover and call the tool.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Do I need an agent?#

You do not need a CopilotKit backend agent to handle a WebMCP call. A compatible browser agent calls the frontend tool handler directly on the page; in that path, the handler context has no `agent`.

Choose the smallest path that fits your app:

What your app has today| What to do  
---|---  
A CopilotKit frontend tool for the action| Add `webmcp: true`, or add annotations with `webmcp: { annotations: ... }`.  
CopilotKit, but no frontend tool for the action| Wrap the smallest suitable browser-side action in a frontend tool, then opt it into WebMCP.  
A backend agent| Keep it. The tool can remain available to that agent, but WebMCP calls do not pass through it.  
No backend agent| Use `CopilotKitCore` directly in browser code, or add the appropriate frontend integration. Do not create an agent only for WebMCP.  
  
React Native does not expose `document.modelContext`, so WebMCP registration is a no-op there. CopilotKit currently supports this WebMCP option in its browser integrations for React, Vue, Angular, and direct core usage.

## How CopilotKit connects WebMCP#

  1. Your app registers a CopilotKit frontend tool with `webmcp` enabled.
  2. CopilotKit mirrors the tool's name, description, JSON Schema, annotations, and handler onto `document.modelContext`.
  3. A compatible browser agent discovers the tool and calls the same JavaScript handler while the page is open.
  4. CopilotKit unregisters the WebMCP tool when the frontend tool is removed or becomes unavailable.



The WebMCP call stays in the browser unless your handler deliberately calls an API. CopilotKit does not route that call through a Runtime or backend agent.

## Add WebMCP manually#

### React frontend tool#

Add `webmcp` to the tool you already register. This code must run inside your existing `CopilotKitProvider`.

OrderSearch.tsx
    
    
    "use client";
    
    import { useFrontendTool } from "@copilotkit/react-core/v2";
    import { z } from "zod";
    
    export function OrderSearch() {
      useFrontendTool({
        name: "searchOrders",
        description: "Search the signed-in user's orders by status",
        parameters: z.object({
          status: z.enum(["open", "shipped", "delivered"]),
        }),
        handler: async ({ status }) => {
          const orders = await searchOrders(status);
          return JSON.stringify(orders);
        },
        webmcp: {
          annotations: {
            readOnlyHint: true,
          },
        },
      });
    
      return null;
    }

Use the equivalent option with [`useFrontendTool` for Vue](https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool) or [`registerFrontendTool` for Angular](https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool). The React API is documented in [`useFrontendTool`](https://docs.copilotkit.ai/reference/hooks/useFrontendTool).

### WebMCP only, with no agent#

For browser code that does not use a framework provider, register the frontend tool directly with the core. Keep the core instance alive for as long as the tool should remain available.

webmcp.ts
    
    
    import { CopilotKitCore } from "@copilotkit/core";
    import { z } from "zod";
    
    export const copilotkit = new CopilotKitCore({
      tools: [
        {
          name: "searchOrders",
          description: "Search the signed-in user's orders by status",
          parameters: z.object({
            status: z.enum(["open", "shipped", "delivered"]),
          }),
          handler: async ({ status }) => {
            const orders = await searchOrders(status);
            return JSON.stringify(orders);
          },
          webmcp: {
            annotations: {
              readOnlyHint: true,
            },
          },
        },
      ],
    });

This path does not configure a Runtime or an agent. It only registers browser-side tools through CopilotKit's core lifecycle.

## Design tools agents can use reliably#

  * Give every WebMCP tool a non-empty, specific `description`. CopilotKit skips WebMCP registration when it is missing.
  * Keep each tool focused on one action and give every parameter a useful description.
  * Use `readOnlyHint: true` only when the handler cannot change state.
  * Use `untrustedContentHint: true` when results may contain user-generated or external content.
  * Return concise, structured results that tell the caller what happened.
  * Set the frontend tool to unavailable when the action cannot currently run; CopilotKit removes it from WebMCP until it is available again.



Annotations are hints for browser agents, not security controls. Enforce authentication, authorization, validation, rate limits, and required user confirmation inside the handler or the API it calls. See Chrome's [WebMCP tool security guidance](https://developer.chrome.com/docs/ai/webmcp/secure-tools).

Agent scope does not scope WebMCP

`agentId` limits which CopilotKit agent receives a frontend tool. WebMCP tools are page-level, so `agentId` does not restrict browser-agent access. If multiple opted-in tools share a name across agent IDs, CopilotKit exposes the first one and logs a warning.

## Test the complete path#

  1. Open Chrome 149 or newer and enable the WebMCP origin trial or local testing flag.
  2. Load the app in an [origin-isolated document](https://developer.chrome.com/docs/ai/webmcp#origin-isolation). The `tools` permissions policy defaults to `self`; cross-origin iframes also need `allow="tools"`.
  3. Confirm that `document.modelContext` exists.
  4. Use Chrome's [Model Context Tool Inspector](https://developer.chrome.com/docs/ai/webmcp#imitate-agent-chat-with-the-inspector-extension) to confirm the tool name and schema, call it with representative inputs, and inspect its result.
  5. Ask the inspector's agent to complete the user task in natural language. Verify that it chooses the right tool and that authentication and confirmation boundaries still hold.



If the tool does not appear, check the browser setup first, then verify that the tool has a description, `webmcp` is enabled, and the frontend tool is currently available.

## Related#

  * [Frontend tools](https://docs.copilotkit.ai/frontend-tools)


  * [React `useFrontendTool` reference](https://docs.copilotkit.ai/reference/hooks/useFrontendTool)


  * [WebMCP specification](https://webmachinelearning.github.io/webmcp/)
  * [Chrome WebMCP best practices](https://developer.chrome.com/docs/ai/webmcp/best-practices)



### On this page

OverviewStart with your coding agentDo I need an agent?How CopilotKit connects WebMCPAdd WebMCP manuallyReact frontend toolWebMCP only, with no agentDesign tools agents can use reliablyTest the complete pathRelated
