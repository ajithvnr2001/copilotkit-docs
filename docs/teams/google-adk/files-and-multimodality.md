---
url: https://docs.copilotkit.ai/teams/google-adk/files-and-multimodality/
title: Microsoft Teams + Google ADK: Files and multimodal input
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:32:58.605753+00:00
---

# Microsoft Teams + Google ADK: Files and multimodal input

> Source: https://docs.copilotkit.ai/teams/google-adk/files-and-multimodality/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

ChannelTeamsAgent backendGoogle ADK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Getting Started

[Overview](https://docs.copilotkit.ai/teams/google-adk)[Configure the Channel in Intelligence](https://docs.copilotkit.ai/teams/google-adk/intelligence)[Connect and run your agent](https://docs.copilotkit.ai/teams/google-adk/connect)

Build

[Tools and context](https://docs.copilotkit.ai/teams/google-adk/tools)[Identity and Memory](https://docs.copilotkit.ai/teams/google-adk/identity-and-memory)[Rich messages and components](https://docs.copilotkit.ai/teams/google-adk/rich-messages)[Interactive messages and approvals](https://docs.copilotkit.ai/teams/google-adk/interactive)[Commands and reactions](https://docs.copilotkit.ai/teams/google-adk/commands-and-reactions)[Files and multimodal input](https://docs.copilotkit.ai/teams/google-adk/files-and-multimodality)[Threads and state](https://docs.copilotkit.ai/teams/google-adk/threads-and-state)

Production

[Persistence and scaling](https://docs.copilotkit.ai/teams/google-adk/persistence-and-scaling)[History and transcripts](https://docs.copilotkit.ai/teams/google-adk/history-and-transcripts)[Deploy and operate](https://docs.copilotkit.ai/teams/google-adk/deploy-and-operate)[API reference](https://docs.copilotkit.ai/reference/channels)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Files and multimodal input

Build

# Files and multimodal input

Pass managed Slack and Teams attachments to multimodal agents and post supported files back to the conversation.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Managed Channels can hydrate provider attachments into `message.contentParts`. The SDK carries text, images, audio, video, and PDF documents in one provider-neutral prompt shape.

## Pass attachments to the agent#

Managed conversation history does not contain the current inbound turn. `runAgent()` automatically chooses the inbound text or attachment parts when `prompt` is omitted. Build a combined prompt when the same turn can contain both `message.text` and `message.contentParts`:

channel.ts
    
    
    channel.onMessage(async ({ thread, message }) => {
      const prompt = message.contentParts?.length
        ? [
            ...(message.text
              ? [{ type: "text" as const, text: message.text }]
              : []),
            ...message.contentParts,
          ]
        : message.text;
    
      await thread.runAgent({ prompt });
    });

If you pass only `message.text`, the model will not receive hydrated binary attachments. If `contentParts` exists, do not append it to managed history yourself; `runAgent` adds the explicit prompt for this turn.

## Understand the content mapping#

Provider file| `AgentContentPart`  
---|---  
Image MIME type| `{ type: "image", source: { type: "data", value, mimeType } }`  
Audio MIME type| `{ type: "audio", source: ... }`  
Video MIME type| `{ type: "video", source: ... }`  
PDF| `{ type: "document", source: ... }`  
`text/*`| UTF-8 `{ type: "text", text }`  
Other binary type| A text note naming the attachment and MIME type  
  
The binary `value` is base64. Whether the agent actually understands a media part depends on its selected model and framework. Choose a multimodal model and test the exact media types you accept.

File retrieval is best-effort. A provider-ingest failure can omit the attachment before the SDK receives a file handle. If Intelligence delivers a handle but the SDK cannot hydrate it, the SDK inserts a short failure note instead of failing the whole turn.

Managed file-size ceiling

Intelligence currently accepts individual inbound and outbound Channel files up to 25 MiB. Provider limits can be lower.

## Slack file access#

## Teams file access#

Teams exposes files differently by surface:

  * Personal 1:1 chat uploads can arrive as downloadable `file.download.info` attachments.
  * Inline media such as images, audio, video, and PDFs with a Bot Connector `contentUrl` can hydrate in chats or channels through the connector token. This path does not require Graph consent.
  * In team channels, SharePoint-reference uploads and inline pasted images use Microsoft Graph. Intelligence reads the channel message, then resolves its reference files or hosted content.
  * Other group-chat file-upload shapes remain unsupported. Test every attachment shape your workflow accepts.



The generated Teams package already declares the supported `personal` and `team` bot scopes, sets `supportsFiles: true`, and requests `ChannelMessage.Read.Group` resource-specific consent. Upload that generated package as-is. Do not add `groupChat`; managed group chats are not supported. A team owner grants the resource-specific permission during installation.

For Graph-backed team-channel messages:

  * The app manifest's `ChannelMessage.Read.Group` resource-specific consent lets Intelligence read the channel message and inline hosted content. A team owner grants it during installation; it does not need tenant-admin Graph consent. Microsoft documents it as a [resource-specific consent permission](https://learn.microsoft.com/en-us/microsoftteams/platform/graph-api/rsc/resource-specific-consent).
  * `Files.Read.All` is an **application** permission and covers only one case: a file uploaded to a Team channel, which arrives as a SharePoint reference rather than as content. It requires tenant-admin consent, so Teams setup offers it and defaults to skipping it. A tenant that already consented to the broader `Files.ReadWrite.All` satisfies this without a second grant.



This permission is optional and its absence does not hold the connection back from reporting ready. Without it the text turn still runs and the message is still delivered; only the referenced file is omitted or represented by a retrieval-failure note. Files shared in a 1:1 chat and images pasted into a channel do not go through SharePoint and are unaffected. Test personal chat, standard/private team channels, inline media, pasted images, and SharePoint-reference uploads separately.

## Post a file#

`thread.postFile()` takes bytes and returns a result instead of throwing for an unsupported provider capability:

export-report.ts
    
    
    const csv = new TextEncoder().encode(
      ["id,status", "INC-421,investigating"].join("\n"),
    );
    
    const result = await thread.postFile({
      bytes: csv,
      filename: "incident-report.csv",
      title: "Incident report",
      altText: "CSV export of the incident report",
    });
    
    if (!result.ok) {
      await thread.post(`The report could not be attached: ${result.error}`);
    }

On managed Channels, `result.ok` means Intelligence stored the managed asset, the provider acknowledged the file or image effect, and the SDK recorded the asset in canonical Thread history.

Managed Teams supports general outbound files. In standard and private Team channels, Intelligence uploads the original bytes to the channel's SharePoint files area and sends a visible card or link. In personal chat, the same `postFile()` call starts Microsoft's native consent-card flow when required; acceptance completes the trusted upload and a decline remains a normal user choice. Images may use the inline Bot Connector path. Always check `result.ok` and send a text fallback when delivery is rejected.

## Treat attachments as untrusted input#

  * Validate declared MIME type and file signature before application-side processing.
  * Put limits on decompression, parsing, page count, and extracted text.
  * Do not execute macros or uploaded code.
  * Resolve the provider user to an authenticated application identity before a file can trigger a consequential write.
  * Avoid logging base64 content, signed download URLs, or document text.



See the [`IncomingMessage` reference](https://docs.copilotkit.ai/reference/channels/types/IncomingMessage) and [`AgentContentPart` reference](https://docs.copilotkit.ai/reference/channels/types/AgentContentPart) for the exact public shapes.

### On this page

Pass attachments to the agentUnderstand the content mappingSlack file accessTeams file accessPost a fileTreat attachments as untrusted input
