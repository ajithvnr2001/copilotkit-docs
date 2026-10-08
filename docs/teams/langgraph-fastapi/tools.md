---
url: https://docs.copilotkit.ai/teams/langgraph-fastapi/tools/
title: Microsoft Teams + LangGraph (FastAPI): Tools and context
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:33:14.626588+00:00
---

# Microsoft Teams + LangGraph (FastAPI): Tools and context

> Source: https://docs.copilotkit.ai/teams/langgraph-fastapi/tools/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

ChannelTeamsAgent backendLangGraph (FastAPI)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Getting Started

[Overview](https://docs.copilotkit.ai/teams/langgraph-fastapi)[Configure the Channel in Intelligence](https://docs.copilotkit.ai/teams/langgraph-fastapi/intelligence)[Connect and run your agent](https://docs.copilotkit.ai/teams/langgraph-fastapi/connect)

Build

[Tools and context](https://docs.copilotkit.ai/teams/langgraph-fastapi/tools)[Identity and Memory](https://docs.copilotkit.ai/teams/langgraph-fastapi/identity-and-memory)[Rich messages and components](https://docs.copilotkit.ai/teams/langgraph-fastapi/rich-messages)[Interactive messages and approvals](https://docs.copilotkit.ai/teams/langgraph-fastapi/interactive)[Commands and reactions](https://docs.copilotkit.ai/teams/langgraph-fastapi/commands-and-reactions)[Files and multimodal input](https://docs.copilotkit.ai/teams/langgraph-fastapi/files-and-multimodality)[Threads and state](https://docs.copilotkit.ai/teams/langgraph-fastapi/threads-and-state)

Production

[Persistence and scaling](https://docs.copilotkit.ai/teams/langgraph-fastapi/persistence-and-scaling)[History and transcripts](https://docs.copilotkit.ai/teams/langgraph-fastapi/history-and-transcripts)[Deploy and operate](https://docs.copilotkit.ai/teams/langgraph-fastapi/deploy-and-operate)[API reference](https://docs.copilotkit.ai/reference/channels)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Tools and context

Build

# Tools and context

Give a Slack or Teams agent typed application actions and the right context for each managed turn.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Channel tools let your agent call application code while it works in Slack or Teams. Context gives the agent information it should consider without exposing another callable action.

Install the schema library used in these examples:

Terminal
    
    
    npm install zod

## Add a channel-level tool#

Use `defineChannelTool` for actions that are available in every conversation. The parameter schema becomes the tool's JSON schema and types the handler.

tools.ts
    
    
    import { defineChannelTool } from "@copilotkit/channels";
    import { z } from "zod";
    
    export const getIncident = defineChannelTool({
      name: "get_incident",
      description: "Read the current status of an incident by its id.",
      parameters: z.object({
        incidentId: z.string().describe("Incident id, for example INC-421"),
      }),
      async handler({ incidentId }) {
        const incident = await incidents.get(incidentId);
        return incident; // objects are serialized for the model
      },
    });

Register it when you create the Channel:

channel.ts
    
    
    import { createChannel } from "@copilotkit/channels";
    import { makeAgent } from "./agent.js";
    import { getIncident } from "./tools.js";
    
    function required(name: string): string {
      const value = process.env[name];
      if (!value) throw new Error(`Missing ${name}`);
      return value;
    }
    
    const channel = createChannel({
      name: required("CHANNEL_CODE"),
      identifyUser: "platform",
      agent: makeAgent,
      tools: [getIncident],
    });

Return information the model can act on:

  * Return raw objects or arrays for data tools.
  * Return a short confirmation when the handler already posted UI.
  * Return or throw the real failure reason so the model can recover.
  * Do not manually `JSON.stringify` successful data.



## Add stable context#

Channel context is sent on every agent run:

channel.ts
    
    
    import { createChannel } from "@copilotkit/channels";
    import { makeAgent } from "./agent.js";
    
    function required(name: string): string {
      const value = process.env[name];
      if (!value) throw new Error(`Missing ${name}`);
      return value;
    }
    
    const channel = createChannel({
      name: required("CHANNEL_CODE"),
      identifyUser: "platform",
      agent: makeAgent,
      context: [
        {
          description: "Support policy",
          value:
            "Never disclose credentials. Escalate Sev-1 incidents immediately.",
        },
        {
          description: "Response style",
          value: "Use short paragraphs and put the next action first.",
        },
      ],
    });

Keep this list stable and small. Fetch frequently changing data through a tool instead of embedding stale snapshots in every prompt.

## Use provider and user context for one turn#

On a managed Channel, `message.platform`, `thread.platform`, and a channel-level tool's `ctx.platform` report the native origin (`"slack"` or `"teams"`).

Add native context when you run the agent:

channel.ts
    
    
    channel.onMessage(async ({ thread, message }) => {
      await thread.runAgent({
        prompt: message.contentParts?.length
          ? [
              ...(message.text
                ? [{ type: "text" as const, text: message.text }]
                : []),
              ...message.contentParts,
            ]
          : message.text,
        context: [
          { description: "Originating platform", value: message.platform },
          {
            description: "Requesting user",
            value: message.user?.name ?? "Unidentified application user",
          },
        ],
      });
    });

If a tool must be scoped to the current person, define it inside the handler and pass it for that run. Its closure captures the trusted inbound identity:

channel.ts
    
    
    channel.onMessage(async ({ thread, message }) => {
      if (!message.user) return;
      const listMyApprovals = defineChannelTool({
        name: "list_my_approvals",
        description: "List approvals assigned to the requesting user.",
        parameters: z.object({}),
        async handler() {
          return approvals.forApplicationUser(message.user.id);
        },
      });
    
      await thread.runAgent({
        prompt: message.text,
        tools: [listMyApprovals],
      });
    });

Treat provider actor IDs as external identifiers. Use the resolved application `user` for personal product data, and check it for `null` before a write.

## Render a tool result as native UI#

A tool can post a portable JSX message and return a short acknowledgement to the model:

tools.tsx
    
    
    import { defineChannelTool } from "@copilotkit/channels";
    import { Header, Message, Section } from "@copilotkit/channels/ui";
    import { z } from "zod";
    
    export const showIncident = defineChannelTool({
      name: "show_incident",
      description: "Display an incident summary in the conversation.",
      parameters: z.object({
        id: z.string(),
        status: z.string(),
        summary: z.string(),
      }),
      async handler({ id, status, summary }, { thread }) {
        await thread.post(
          <Message>
            <Header>{`${id} · ${status}`}</Header>
            <Section>{summary}</Section>
          </Message>,
        );
        return `Displayed ${id}.`;
      },
    });

Enable Channels JSX before using this example:

tsconfig.json
    
    
    {
      "compilerOptions": {
        "jsx": "react-jsx",
        "jsxImportSource": "@copilotkit/channels"
      }
    }

The portable message is rendered as a Microsoft Teams Adaptive Card before Intelligence sends it to the conversation.

## Where MCP belongs#

Connect MCP servers to the selected agent backend. The Channels SDK forwards channel tools over AG-UI alongside the tools already exposed by that agent, so you do not need a second channel-specific MCP transport. Start with [MCP tools](https://docs.copilotkit.ai/agentic-protocols/mcp), then use `defineChannelTool` only for actions that need the current channel conversation.

Continue with [interactive messages and approvals](https://docs.copilotkit.ai/teams/langgraph-fastapi/interactive), or use the [Channel API reference](https://docs.copilotkit.ai/reference/channels/classes/Channel).

### On this page

Add a channel-level toolAdd stable contextUse provider and user context for one turnRender a tool result as native UIWhere MCP belongs
