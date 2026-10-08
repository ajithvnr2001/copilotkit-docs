---
url: https://docs.copilotkit.ai/slack/agno/rich-messages/
title: Slack + Agno: Rich messages and components
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:44.042023+00:00
---

# Slack + Agno: Rich messages and components

> Source: https://docs.copilotkit.ai/slack/agno/rich-messages/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

ChannelSlackAgent backendAgno

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Getting Started

[Overview](https://docs.copilotkit.ai/slack/agno)[Configure the Channel in Intelligence](https://docs.copilotkit.ai/slack/agno/intelligence)[Connect and run your agent](https://docs.copilotkit.ai/slack/agno/connect)

Build

[Tools and context](https://docs.copilotkit.ai/slack/agno/tools)[Identity and Memory](https://docs.copilotkit.ai/slack/agno/identity-and-memory)[Rich messages and components](https://docs.copilotkit.ai/slack/agno/rich-messages)[Interactive messages and approvals](https://docs.copilotkit.ai/slack/agno/interactive)[Commands and reactions](https://docs.copilotkit.ai/slack/agno/commands-and-reactions)[Files and multimodal input](https://docs.copilotkit.ai/slack/agno/files-and-multimodality)[Threads and state](https://docs.copilotkit.ai/slack/agno/threads-and-state)

Production

[Persistence and scaling](https://docs.copilotkit.ai/slack/agno/persistence-and-scaling)[History and transcripts](https://docs.copilotkit.ai/slack/agno/history-and-transcripts)[Deploy and operate](https://docs.copilotkit.ai/slack/agno/deploy-and-operate)[API reference](https://docs.copilotkit.ai/reference/channels)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Rich messages and components

Build

# Rich messages and components

Build portable channel UI that renders as Slack Block Kit or Microsoft Teams Adaptive Cards, with explicit provider fallbacks.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Channels JSX lets application code describe a message once and lets the selected provider renderer turn it into native UI. The same component can produce Slack Block Kit or a Microsoft Teams Adaptive Card.

## Enable Channels JSX#

Channels JSX does not use React at runtime. Point the TypeScript JSX transform at `@copilotkit/channels`:

tsconfig.json
    
    
    {
      "compilerOptions": {
        "target": "ES2022",
        "module": "NodeNext",
        "moduleResolution": "NodeNext",
        "jsx": "react-jsx",
        "jsxImportSource": "@copilotkit/channels",
        "strict": true,
        "noEmit": true
      },
      "include": ["*.ts", "*.tsx"]
    }

Keep `"type": "module"` in `package.json` and use `.tsx` for files containing JSX.

## Build a portable status card#

incident-card.tsx
    
    
    import {
      Context,
      Divider,
      Field,
      Fields,
      Header,
      Message,
      Section,
    } from "@copilotkit/channels/ui";
    
    export function IncidentCard(props: {
      id: string;
      summary: string;
      owner: string;
      status: string;
    }) {
      return (
        <Message>
          <Header>{`${props.id} · ${props.status}`}</Header>
          <Section>{props.summary}</Section>
          <Divider />
          <Fields>
            <Field>{`Owner: ${props.owner}`}</Field>
            <Field>{`Status: ${props.status}`}</Field>
          </Fields>
          <Context>Updated from the incident service</Context>
        </Message>
      );
    }

Post the component from a message handler or tool:

channel.tsx
    
    
    channel.onMessage(async ({ thread }) => {
      await thread.post(
        <IncidentCard
          id="INC-421"
          summary="Checkout latency is above the SLO."
          owner="Payments"
          status="Investigating"
        />,
      );
    });

Use named components with JSON-serializable props when they contain callbacks, then register them in `createChannel({ components: [...] })`. Pure display components do not need registration.

## Know what each provider renders#

Channels component| Slack| Microsoft Teams  
---|---|---  
`Message`| Flattens to Block Kit; the current managed connector does not forward `accent`| Flattens into an Adaptive Card; `accent` has no native mapping  
`Header`| Header block| Large bold text block  
`Section`, `Markdown`| Slack `mrkdwn` section| Wrapped Adaptive Card text  
`Fields`, `Field`| Section fields; honors `Field.label`| Fact set; derives a label from `Label: value` text  
`Context`| Context block| Small, subtle text  
`Actions`, `Button`| Actions block and button| Top-level `Action.Submit` or `Action.OpenUrl`  
`Select`, `Input`| Native Block Kit controls| Adaptive Card inputs  
`Image`, `Divider`| Native image and divider blocks| Image and separator  
`Table`, `Row`, `Cell`| Native Slack table block| Adaptive Card 1.5 table  
`Chart`| Omitted by the Slack renderer| Teams chart extension where the client supports it  
  
Unknown or unsupported nodes are omitted instead of failing the whole message. That makes portable rendering resilient, but it also means the text around an optional visual must still carry the important result.

`Select` and `Input` have different interaction behavior by provider. Managed Slack dispatches those controls directly. Managed Teams renders Adaptive Card fields and submits them with a `Button`'s `Action.Submit`; that Button callback receives the other named fields in `ctx.values`. Teams does not dispatch `Select.onSelect` or `Input.onSubmit` independently.

Slack text is translated from GitHub-flavored Markdown to `mrkdwn`. Collections and strings are clamped to Slack's native limits. If a message exceeds the top-level block budget, the renderer adds a truncation notice.

Although the direct Slack renderer can return an attachment accent, the current cloud-hosted Intelligence post and update path forwards only blocks. Do not rely on `Message.accent` in a managed Slack workflow.

Do not put essential information only in `Chart`: the Slack renderer currently skips chart nodes. Pair a chart with a `Section`, `Fields`, or `Table`.

## Update a message safely#

`thread.post()` returns a `MessageRef` that can be updated during the current managed delivery:

update.tsx
    
    
    const ref = await thread.post(<IncidentCard {...incident} status="Loading" />);
    
    await thread.update(ref, <IncidentCard {...incident} status="Investigating" />);

Do not persist that ref and assume it remains updateable in a later delivery. For a later button click, use the interaction's `message.ref`, check that `message.ref.id` is non-empty, and treat the update as best-effort.

Managed Slack supports post, update, and delete frames.

## Keep provider-specific payloads at the edge#

The `{ raw: nativePayload, provider }` escape hatch is part of the low-level renderable type, but it is not portable. Tag Slack Block Kit with `provider: "slack"` and a Teams Adaptive Card object with `provider: "teams"`. A provider mismatch fails explicitly before the effect reaches the provider. Prefer Channels components in shared managed code.

Use [interactive messages and approvals](https://docs.copilotkit.ai/slack/agno/interactive) for callbacks, or browse the [Channels UI reference](https://docs.copilotkit.ai/reference/channels/components/Message) for component props.

### On this page

Enable Channels JSXBuild a portable status cardKnow what each provider rendersUpdate a message safelyKeep provider-specific payloads at the edge
