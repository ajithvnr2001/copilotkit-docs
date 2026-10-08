---
url: https://docs.copilotkit.ai/google-adk/multimodal-attachments/
title: Multimodal Attachments
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:03:23.715685+00:00
---

# Multimodal Attachments

> Source: https://docs.copilotkit.ai/google-adk/multimodal-attachments/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendGoogle ADK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/google-adk)[Quickstart](https://docs.copilotkit.ai/google-adk/quickstart)[Build with agents](https://docs.copilotkit.ai/google-adk/build-with-agents)[Intelligence](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Basics

Chat

Prebuilt Components

Custom Look and Feel

[Multimodal Attachments](https://docs.copilotkit.ai/google-adk/multimodal-attachments)[Voice](https://docs.copilotkit.ai/google-adk/voice)[Reasoning](https://docs.copilotkit.ai/google-adk/generative-ui/reasoning)

Threads

[Frontend-tools](https://docs.copilotkit.ai/google-adk/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/google-adk/webmcp)

Agent capabilities

Google ADK

[Sub-agents](https://docs.copilotkit.ai/google-adk/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/google-adk/learning)

[User Memories](https://docs.copilotkit.ai/google-adk/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/google-adk/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/google-adk/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/google-adk/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/google-adk/intelligence/analytics)[Channels](https://docs.copilotkit.ai/google-adk/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/google-adk/telemetry)[Community frameworks](https://docs.copilotkit.ai/google-adk/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Multimodal Attachments

BasicsChat

# Multimodal Attachments

Let users send images, audio, video, and documents to the AI alongside their messages.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

You have a working CopilotChat and want users to attach files — images, PDFs, audio, video — that the AI can see and respond to. By the end of this guide, your chat will support drag-and-drop file attachments with previews, lightbox viewing, and multimodal AI responses.

## Quick start#

Add `attachments` to your `CopilotChat` component:

page.tsx
    
    
    import { CopilotChat } from "@copilotkit/react-core/v2";
    
    <CopilotChat
      agentId="my-agent"
      attachments={{ enabled: true }} 
    />

That's it. Users can now click the attachment button or drag-and-drop files into the chat. The files are sent as part of the message content to your agent.

## Configuration#

The `attachments` prop accepts an `AttachmentsConfig` object:
    
    
    <CopilotChat
      attachments={{
        enabled: true,
        // Omit `accept` to allow all file types (default: "*/*").
        // Restrict with a MIME filter if needed:
        accept: "image/*,audio/*,video/*,application/pdf",
        maxSize: 10 * 1024 * 1024,      // 10MB limit (default: 20MB)
      }}
    />

Option| Type| Default| Description  
---|---|---|---  
`enabled`| `boolean`| —| Enable file attachments in the chat input.  
`accept`| `string`| `"*/*"`| MIME type filter. Supports patterns like `"image/*"`, `".pdf,.docx"`, or comma-separated lists.  
`maxSize`| `number`| `20 * 1024 * 1024`| Maximum file size in bytes.  
`maxConcurrentUploads`| `number`| `1`| How many files upload at the same time. See Upload concurrency.  
`onUpload`| `(file: File) => AttachmentUploadResult | Promise<...>`| —| Custom upload handler. See Custom upload handler.  
`onUploadFailed`| `(error: AttachmentUploadError) => void`| —| Called when a file fails validation or upload. See Handling upload errors.  
  
## Supported file types#

Attachments are categorized by modality based on their MIME type:

Modality| MIME types| Preview| AI support  
---|---|---|---  
**Image**| `image/*`| Thumbnail with lightbox| Supported by most vision-capable models (GPT-4o, Claude, etc.)  
**Audio**| `audio/*`| Audio player| Model-dependent  
**Video**| `video/*`| Thumbnail with play button + lightbox| Model-dependent  
**Document**|  Everything else| File icon + name; PDF and text get lightbox preview| Sent as file content — model support varies  
  
Not all models support all modalities. For example, OpenAI's GPT-4o supports images but not audio file parts. If the model doesn't support a file type, you'll get a `RUN_ERROR` event. Use the `onError` callback to handle this gracefully.

## Custom upload handler#

By default, files are read as base64 and sent inline. For large files or production apps, you'll want to upload to your own storage and pass a URL instead.

`onUpload` returns an `AttachmentUploadResult` — a discriminated union with two variants:

Base64 (inline)URL (hosted)
    
    
    <CopilotChat
      attachments={{
        enabled: true,
        onUpload: async (file) => {
          const buffer = await file.arrayBuffer();
          const base64 = btoa(String.fromCharCode(...new Uint8Array(buffer)));
          return {
            type: "data",
            value: base64,
            mimeType: file.type,
          };
        },
      }}
    />
    
    
    <CopilotChat
      attachments={{
        enabled: true,
        onUpload: async (file) => {
          const formData = new FormData();
          formData.append("file", file);
          const res = await fetch("/api/upload", { method: "POST", body: formData });
          const { url } = await res.json();
          return {
            type: "url",
            value: url,
            mimeType: file.type,
          };
        },
      }}
    />

### Adding metadata#

You can attach custom metadata to any upload. It's included in the `InputContent` part sent to the agent and accessible via `metadata` on the content part.
    
    
    onUpload: async (file) => {
      const url = await uploadToStorage(file);
      return {
        type: "url",
        value: url,
        mimeType: file.type,
        metadata: {
          uploadedBy: currentUser.id,
          category: "support-ticket",
        },
      };
    },

The filename is always included in metadata automatically — you don't need to add it yourself.

## Upload concurrency#

When a user attaches several files at once, they upload one at a time by default. Every picked file shows in the attachment queue immediately, whether or not its upload has started.

Set `maxConcurrentUploads` to upload several together — worth raising when your upload endpoint handles parallel requests:
    
    
    <CopilotChat
      attachments={{
        enabled: true,
        maxConcurrentUploads: 3, // three files at a time
        onUpload: async (file) => uploadToStorage(file),
      }}
    />

The limit covers every upload in flight, not each batch: if a paste lands while a dropped selection is still uploading, both share the same slots. `Infinity` lifts the limit entirely.

Above `1`, your `onUpload` handler may be called concurrently, so it must not rely on the previous file having finished.

## Handling upload errors#

Use `onUploadFailed` to react when a file is rejected or an upload fails — for example, to show a toast:
    
    
    <CopilotChat
      attachments={{
        enabled: true,
        accept: "image/*",
        maxSize: 5 * 1024 * 1024, // 5MB
        onUploadFailed: (error) => {
          // error.reason: "file-too-large" | "invalid-type" | "upload-failed"
          // error.file: the original File object
          // error.message: human-readable description
          toast.error(error.message);
        },
      }}
    />

Reason| When it fires  
---|---  
`invalid-type`| File doesn't match the `accept` filter.  
`file-too-large`| File exceeds `maxSize`.  
`upload-failed`| The `onUpload` handler threw, or the default base64 reader failed.  
  
For errors that happen _after_ the message is sent (e.g., the model doesn't support the file type), use the `onError` callback on `CopilotChat`:
    
    
    <CopilotChat
      attachments={{ enabled: true }}
      onError={(event) => {
        console.error(`[${event.code}]`, event.error.message);
      }}
    />

## How it works#

When a user attaches files and sends a message, CopilotKit:

  1. Reads each file (via the default base64 reader or your `onUpload` handler)
  2. Builds an array of `InputContent` parts — text + one part per attachment
  3. Adds the message to the agent with `content: [{ type: "text", ... }, { type: "image", source: ... }, ...]`
  4. The agent receives the multimodal content via the AG-UI protocol and forwards it to the model



The attachments are part of the standard AG-UI `InputContent` schema, so any AG-UI-compatible agent (BuiltInAgent, LangGraph, custom) can receive them.

### On this page

Quick startConfigurationSupported file typesCustom upload handlerAdding metadataUpload concurrencyHandling upload errorsHow it works
