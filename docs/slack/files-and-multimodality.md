---
url: https://docs.copilotkit.ai/slack/files-and-multimodality/
title: Slack: Files and multimodal input
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:27:08.660530+00:00
---

# Slack: Files and multimodal input

> Source: https://docs.copilotkit.ai/slack/files-and-multimodality/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

ChannelSlackAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Getting Started

[Overview](https://docs.copilotkit.ai/slack)[Configure the Channel in Intelligence](https://docs.copilotkit.ai/slack/intelligence)[Connect and run your agent](https://docs.copilotkit.ai/slack/connect)

Build

[Tools and context](https://docs.copilotkit.ai/slack/tools)[Identity and Memory](https://docs.copilotkit.ai/slack/identity-and-memory)[Rich messages and components](https://docs.copilotkit.ai/slack/rich-messages)[Interactive messages and approvals](https://docs.copilotkit.ai/slack/interactive)[Commands and reactions](https://docs.copilotkit.ai/slack/commands-and-reactions)[Files and multimodal input](https://docs.copilotkit.ai/slack/files-and-multimodality)[Threads and state](https://docs.copilotkit.ai/slack/threads-and-state)

Production

[Persistence and scaling](https://docs.copilotkit.ai/slack/persistence-and-scaling)[History and transcripts](https://docs.copilotkit.ai/slack/history-and-transcripts)[Deploy and operate](https://docs.copilotkit.ai/slack/deploy-and-operate)[API reference](https://docs.copilotkit.ai/reference/channels)

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

Intelligence downloads files using the managed Slack bot token. The app must be in the conversation and have permission to read the file. Slack documents [`files:read`](https://api.slack.com/scopes/files%3Aread) as the scope that allows an app to download files from conversations it can access.

The current Intelligence-generated manifest requests both `files:read` and `files:write`. If the app predates that manifest:

  1. Open the Channel in Intelligence, return to its Slack setup instructions, and apply the generated manifest so both bot token scopes are present. See [Configure the Channel in Intelligence](https://docs.copilotkit.ai/slack/intelligence).
  2. Reinstall the app so the workspace grants the scopes.
  3. Copy the current Bot User OAuth token into Intelligence if Slack reissued it.
  4. Invite the app to the source conversation.
  5. Send a new file and verify the model receives it.



If attachments are omitted or arrive as retrieval-failure notes:

  1. Confirm the reinstalled bot token includes `files:read`.
  2. Confirm the app is a member of the source conversation.
  3. Send a new file and inspect the real agent turn.



## Teams file access#

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

Managed Slack uses Slack's external-upload flow and can send general file types. The generated manifest includes the `files:write` bot scope. Apply the current manifest and reinstall if the Slack app predates it. Check `result.ok`, then verify the real Slack message when provider-side display matters.

## Treat attachments as untrusted input#

  * Validate declared MIME type and file signature before application-side processing.
  * Put limits on decompression, parsing, page count, and extracted text.
  * Do not execute macros or uploaded code.
  * Resolve the provider user to an authenticated application identity before a file can trigger a consequential write.
  * Avoid logging base64 content, signed download URLs, or document text.



See the [`IncomingMessage` reference](https://docs.copilotkit.ai/reference/channels/types/IncomingMessage) and [`AgentContentPart` reference](https://docs.copilotkit.ai/reference/channels/types/AgentContentPart) for the exact public shapes.

### On this page

Pass attachments to the agentUnderstand the content mappingSlack file accessTeams file accessPost a fileTreat attachments as untrusted input
