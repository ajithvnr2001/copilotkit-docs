---
url: https://docs.copilotkit.ai/angular/guides/voice-multimodal/
title: Voice and multimodal input
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:49:30.976463+00:00
---

# Voice and multimodal input

> Source: https://docs.copilotkit.ai/angular/guides/voice-multimodal/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendAngularAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/angular)[Build with agents](https://docs.copilotkit.ai/angular/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/intelligence/overview)

Basics

Generative UI

Interactivity

[WebMCP](https://docs.copilotkit.ai/angular/webmcp)

Agent capabilities

Built-in Agent

[Sub-agents](https://docs.copilotkit.ai/angular/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/angular/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/angular/learning)

[User Memories](https://docs.copilotkit.ai/angular/intelligence/memories)[Standalone collector](https://docs.copilotkit.ai/angular/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/angular/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/angular/intelligence/analytics)[Channels](https://docs.copilotkit.ai/angular/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

Concepts

Angular guides

[Using the Angular docs](https://docs.copilotkit.ai/angular/using-these-docs)[Feature examples](https://docs.copilotkit.ai/angular/features)[Angular API reference](https://docs.copilotkit.ai/reference/angular)[Chat UI and customization](https://docs.copilotkit.ai/angular/guides/chat-ui)[Frontend tools and generative UI](https://docs.copilotkit.ai/angular/guides/frontend-tools-generative-ui)[A2UI schemas, styling, and recovery](https://docs.copilotkit.ai/angular/guides/a2ui)[Voice and multimodal input](https://docs.copilotkit.ai/angular/guides/voice-multimodal)[Human-in-the-loop and interrupts](https://docs.copilotkit.ai/angular/guides/human-in-the-loop)[Shared state and agent context](https://docs.copilotkit.ai/angular/guides/shared-state)[Threads, memory, attachments, and headless UI](https://docs.copilotkit.ai/angular/guides/threads-memory-attachments-headless)[Troubleshooting Angular apps](https://docs.copilotkit.ai/angular/guides/troubleshooting)[Build with agents](https://docs.copilotkit.ai/angular/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/intelligence/overview)

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/angular/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Voice and multimodal input

LearnAngular guides

# Voice and multimodal input

Add speech transcription, file attachments, and typed media content to an Angular chat.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

`CopilotChat` includes a microphone control and an attachment composer. Voice input is transcribed through Copilot Runtime and inserted into the composer as text. Multimodal input sends image or document content parts with the user's message.

## What is voice and multimodal input?#

Voice input turns recorded speech into editable text before a message is sent. Multimodal input attaches typed image or document content parts to that message, so a compatible model can reason about more than text.

## Accept voice input#

No component option is required to display the microphone. The browser asks for microphone permission, records the audio, and sends it to the Runtime transcription endpoint. The resulting text remains editable before the user sends it.

Serve production applications over HTTPS so browsers can grant microphone access.

### Configure Runtime transcription#

Follow the [Voice backend setup](https://docs.copilotkit.ai/angular/guides/voice-multimodal#backend) to add a dedicated Runtime route and transcription service. Keep speech-provider credentials separate from credentials used for agent chat. For the Built-in Agent showcase, set:
    
    
    OPENAI_TRANSCRIPTION_API_KEY=your-api-key
    # Optional: defaults to https://api.openai.com/v1
    OPENAI_TRANSCRIPTION_BASE_URL=https://your-speech-provider.example.com/v1

The route must omit `transcriptionService` when the dedicated credential is absent. Copilot Runtime then reports `audioFileTranscriptionEnabled: false` on `/info`, and the chat hides the mic instead of exposing a control that cannot work. When the service is configured, the browser sends recorded audio to `/api/copilotkit-voice/transcribe`.

Voice requests can call the same backend tools as typed requests. Register renderers only for the exact tool names your backend exposes:

media-feature.component.ts
    
    
    export const voiceWeatherRendererConfigs: readonly RenderToolCallConfig<VoiceWeatherArgs>[] =  VOICE_WEATHER_TOOL_NAMES.map((name) => ({    name,    args: z.record(z.unknown()),    component:      WeatherToolCard as unknown as RenderToolCallConfig<VoiceWeatherArgs>["component"],  }));

The renderer registration is optional. It changes how matching tool calls are displayed, not how speech is captured or transcribed.

## Configure attachments#

Define an `AttachmentsConfig` and bind it to the chat surface. The runnable Showcase accepts images and PDFs up to 10 MiB:

media-feature.component.ts
    
    
    const MULTIMODAL_ATTACHMENTS: AttachmentsConfig = {  enabled: true,  accept: "image/*,application/pdf",  maxSize: 10 * 1024 * 1024,};

media-chat.component.html
    
    
    <copilot-chat [attachments]="multimodalAttachments" />

The `accept` value filters the file picker and `maxSize` provides immediate client feedback. They are not server-side security controls. Validate file type, size, and content again wherever uploads are stored or processed. Use the configuration's upload callbacks when files should go to object storage instead of traveling inline with a message.

## Send media programmatically#

For a bundled sample or custom uploader, add a user message whose `content` contains normal AG-UI content parts. The Showcase constructs a text part plus an image or document part:

media-model.ts
    
    
    export function createMultimodalMessage(  spec: Pick<SampleSpec, "filename" | "mimeType" | "autoPrompt">,  base64: string,  size: number,  id: string,): MediaAgentMessage {  return {    id,    role: "user",    content: [      { type: "text", text: spec.autoPrompt },      {        type: spec.mimeType === "application/pdf" ? "document" : "image",        source: {          type: "data",          value: base64,          mimeType: spec.mimeType,        },        metadata: { filename: spec.filename, size },      },    ],  };}

Add that message to the selected agent and run the agent. Keep the MIME type authoritative: use an `image` part for images and a `document` part for PDFs and other documents. The chosen model and backend converter must support each MIME type you accept.

## Next steps#

  * [Voice input](https://docs.copilotkit.ai/angular/features#voice)
  * [Multimodal attachments](https://docs.copilotkit.ai/angular/features#multimodal)
  * [Chat UI configuration](https://docs.copilotkit.ai/angular/guides/chat-ui)



### On this page

What is voice and multimodal input?Accept voice inputConfigure Runtime transcriptionConfigure attachmentsSend media programmaticallyNext steps
