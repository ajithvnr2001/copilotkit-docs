---
url: https://docs.copilotkit.ai/reference/react-native/hooks/useAttachments/
title: useAttachments
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:47.883096+00:00
---

# useAttachments

> Source: https://docs.copilotkit.ai/reference/react-native/hooks/useAttachments/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁React NativeSDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Components

[AssistantMessage](https://docs.copilotkit.ai/reference/react-native/components/AssistantMessage)[CopilotChat](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat)[CopilotKitProvider](https://docs.copilotkit.ai/reference/react-native/components/CopilotKitProvider)[CopilotMarkdown](https://docs.copilotkit.ai/reference/react-native/components/CopilotMarkdown)[CopilotModal](https://docs.copilotkit.ai/reference/react-native/components/CopilotModal)[CopilotPopup](https://docs.copilotkit.ai/reference/react-native/components/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/react-native/components/CopilotSidebar)[UserMessage](https://docs.copilotkit.ai/reference/react-native/components/UserMessage)

Hooks

[useAgent](https://docs.copilotkit.ai/reference/react-native/hooks/useAgent)[useAgentContext](https://docs.copilotkit.ai/reference/react-native/hooks/useAgentContext)[useAttachments](https://docs.copilotkit.ai/reference/react-native/hooks/useAttachments)[useCapabilities](https://docs.copilotkit.ai/reference/react-native/hooks/useCapabilities)[useComponent](https://docs.copilotkit.ai/reference/react-native/hooks/useComponent)[useConfigureSuggestions](https://docs.copilotkit.ai/reference/react-native/hooks/useConfigureSuggestions)[useCopilotKit](https://docs.copilotkit.ai/reference/react-native/hooks/useCopilotKit)[useFrontendTool](https://docs.copilotkit.ai/reference/react-native/hooks/useFrontendTool)[useHumanInTheLoop](https://docs.copilotkit.ai/reference/react-native/hooks/useHumanInTheLoop)[useInterrupt](https://docs.copilotkit.ai/reference/react-native/hooks/useInterrupt)[useRenderTool](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool)[useSuggestions](https://docs.copilotkit.ai/reference/react-native/hooks/useSuggestions)[useThreads](https://docs.copilotkit.ai/reference/react-native/hooks/useThreads)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[react-native](https://docs.copilotkit.ai/reference/react-native)Hooks

# useAttachments

React Native hook for adding multimodal file attachments to a chat using Expo's document picker and file system.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useAttachments` is the React Native counterpart of the web `useAttachments` hook. It manages picking, validating, uploading, and consuming file attachments for a chat, using [`expo-document-picker`](https://docs.expo.dev/versions/latest/sdk/document-picker/) and [`expo-file-system`](https://docs.expo.dev/versions/latest/sdk/filesystem/) in place of the web `FileReader` / `<input type="file">` APIs.

The headless [`CopilotChat`](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat) wires this hook up for you when you pass its `attachments` prop. Call `useAttachments` directly only when you manage attachments outside of `CopilotChat`. Requires the `expo-document-picker` and `expo-file-system` peer dependencies.

## Signature
    
    
    import { useAttachments } from "@copilotkit/react-native";
    
    function useAttachments(props: UseNativeAttachmentsProps): UseNativeAttachmentsReturn;

## Parameters

Prop

Type

`props?`UseNativeAttachmentsProps

## Return Value

Prop

Type

`attachments?`Attachment[]

Prop

Type

`enabled?`boolean

Prop

Type

`openPicker?`() => Promise<void>

Prop

Type

`processFiles?`(files: NativeFileInput[]) => Promise<void>

Prop

Type

`removeAttachment?`(id: string) => void

Prop

Type

`consumeAttachments?`() => Attachment[]

### `NativeFileInput`

The React Native equivalent of the web `File` object.

Prop

Type

`uri?`string

Prop

Type

`name?`string

Prop

Type

`size?`number

Prop

Type

`mimeType?`string

## Usage
    
    
    import { useAttachments } from "@copilotkit/react-native";
    import { getSourceUrl } from "@copilotkit/shared";
    import { Button, Image, View } from "react-native";
    
    function Composer() {
      const { attachments, openPicker, removeAttachment } = useAttachments({
        config: {
          enabled: true,
          accept: "image/*,application/pdf",
          maxSize: 10 * 1024 * 1024,
        },
      });
    
      return (
        <View>
          <Button title="Attach file" onPress={openPicker} />
          {attachments.map((a) => (
            <Image
              key={a.id}
              source={{ uri: getSourceUrl(a.source) }}
              style={{ width: 48, height: 48 }}
            />
          ))}
        </View>
      );
    }

Each `Attachment` exposes its content as a `source` (a base64 data source or a URL source), not a ready-made URL. `getSourceUrl` from `@copilotkit/shared` converts either form to a string you can pass to `Image`.

Most apps enable attachments declaratively through `CopilotChat` instead:
    
    
    <CopilotChat agentId="default" attachments={{ enabled: true, accept: "image/*" }}>
      <MyChatUI />
    </CopilotChat>

## Related

  * [`CopilotChat`](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat): wires up attachments via its `attachments` prop and exposes `openPicker` / `removeAttachment` through `useCopilotChatContext`


