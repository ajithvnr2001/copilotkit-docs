---
url: https://docs.copilotkit.ai/reference/react-native/hooks/useHumanInTheLoop/
title: useHumanInTheLoop
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:52.133987+00:00
---

# useHumanInTheLoop

> Source: https://docs.copilotkit.ai/reference/react-native/hooks/useHumanInTheLoop/

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

# useHumanInTheLoop

React hook for interactive tools that pause agent execution and wait for user input

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useHumanInTheLoop` registers an interactive tool that pauses agent execution until the user responds through your custom UI. Unlike `useFrontendTool`, there is no `handler` function. Instead, the hook provides an internal status machine (`InProgress` -> `Executing` -> `Complete`) and supplies a `respond` callback to the render component while the tool is in the `Executing` state. The agent remains paused until `respond` is called with the user's input.

Re-exported from `@copilotkit/react-core/v2`, identical to the [React (V2) `useHumanInTheLoop`](https://docs.copilotkit.ai/reference/v2/hooks/useHumanInTheLoop). The only difference is the import path.

This hook is built on top of `useFrontendTool` with an internally managed handler that resolves the tool call promise when `respond` is invoked. Use it for confirmation dialogs, approval workflows, form collection, or any scenario where a human must provide input before the agent can continue. The `render` component returns React Native elements that CopilotKit surfaces in the chat, through the same shared renderer registry [`useRenderTool`](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool) and `useFrontendTool` write to.

## Signature
    
    
    import { useHumanInTheLoop } from "@copilotkit/react-native";
    
    function useHumanInTheLoop<T extends Record<string, unknown>>(
      tool: ReactHumanInTheLoop<T>,
      deps?: ReadonlyArray<unknown>,
    ): void;

## Parameters

Prop

Type

`tool`ReactHumanInTheLoop<T>

Prop

Type

`deps?`ReadonlyArray<unknown>

## Usage

### Confirmation Dialog

A common pattern where the agent asks the user to confirm a destructive action.
    
    
    import { Text, TouchableOpacity, View } from "react-native";
    import { useHumanInTheLoop, ToolCallStatus } from "@copilotkit/react-native";
    import { z } from "zod";
    
    function DeleteConfirmation() {
      useHumanInTheLoop(
        {
          name: "confirmDeletion",
          description: "Ask the user to confirm before deleting items",
          parameters: z.object({
            itemName: z.string().describe("Name of the item to delete"),
            itemCount: z.number().describe("Number of items to delete"),
          }),
          render: ({ args, status, respond, result }) => {
            if (status === ToolCallStatus.InProgress) {
              return (
                <View style={{ padding: 16 }}>
                  <Text style={{ color: "#6b7280" }}>Preparing confirmation...</Text>
                </View>
              );
            }
    
            if (status === ToolCallStatus.Executing && respond) {
              return (
                <View style={{ padding: 16, borderWidth: 1, borderRadius: 8 }}>
                  <Text>
                    Are you sure you want to delete {args.itemCount} {args.itemName}
                    (s)?
                  </Text>
                  <View style={{ flexDirection: "row", gap: 8, marginTop: 16 }}>
                    <TouchableOpacity
                      onPress={() => respond({ confirmed: true })}
                      style={{ backgroundColor: "#ef4444", paddingHorizontal: 16, paddingVertical: 8, borderRadius: 6 }}
                    >
                      <Text style={{ color: "#fff" }}>Delete</Text>
                    </TouchableOpacity>
                    <TouchableOpacity
                      onPress={() => respond({ confirmed: false })}
                      style={{ backgroundColor: "#d1d5db", paddingHorizontal: 16, paddingVertical: 8, borderRadius: 6 }}
                    >
                      <Text>Cancel</Text>
                    </TouchableOpacity>
                  </View>
                </View>
              );
            }
    
            if (status === ToolCallStatus.Complete && result) {
              const parsed = JSON.parse(result);
              return (
                <View style={{ padding: 8 }}>
                  <Text style={{ fontSize: 12, color: "#4b5563" }}>
                    {parsed.confirmed ? "Items deleted." : "Deletion cancelled."}
                  </Text>
                </View>
              );
            }
    
            return null;
          },
        },
        [],
      );
    
      return null;
    }

### Form Input Collection

Collect structured input from the user before the agent proceeds.
    
    
    import { useState } from "react";
    import { Text, TextInput, TouchableOpacity, View } from "react-native";
    import { useHumanInTheLoop, ToolCallStatus } from "@copilotkit/react-native";
    import { z } from "zod";
    
    function ShippingAddressForm() {
      useHumanInTheLoop(
        {
          name: "collectShippingAddress",
          description:
            "Collect shipping address from the user before placing an order",
          parameters: z.object({
            orderSummary: z
              .string()
              .describe("A summary of the order being placed"),
          }),
          render: ({ args, status, respond }) => {
            const [address, setAddress] = useState({
              street: "",
              city: "",
              zip: "",
            });
    
            if (status === ToolCallStatus.Executing && respond) {
              return (
                <View style={{ padding: 16, borderWidth: 1, borderRadius: 8, gap: 12 }}>
                  <Text style={{ fontWeight: "500" }}>Order: {args.orderSummary}</Text>
                  <Text>Please enter your shipping address:</Text>
                  <TextInput
                    placeholder="Street address"
                    value={address.street}
                    onChangeText={(street) => setAddress({ ...address, street })}
                    style={{ borderWidth: 1, padding: 8, borderRadius: 6 }}
                  />
                  <TextInput
                    placeholder="City"
                    value={address.city}
                    onChangeText={(city) => setAddress({ ...address, city })}
                    style={{ borderWidth: 1, padding: 8, borderRadius: 6 }}
                  />
                  <TextInput
                    placeholder="ZIP code"
                    value={address.zip}
                    onChangeText={(zip) => setAddress({ ...address, zip })}
                    style={{ borderWidth: 1, padding: 8, borderRadius: 6 }}
                  />
                  <TouchableOpacity
                    onPress={() => respond(address)}
                    style={{ backgroundColor: "#3b82f6", paddingHorizontal: 16, paddingVertical: 8, borderRadius: 6 }}
                  >
                    <Text style={{ color: "#fff" }}>Submit Address</Text>
                  </TouchableOpacity>
                </View>
              );
            }
    
            if (status === ToolCallStatus.Complete) {
              return (
                <View style={{ padding: 8 }}>
                  <Text style={{ color: "#16a34a" }}>
                    Shipping address submitted.
                  </Text>
                </View>
              );
            }
    
            return null;
          },
        },
        [],
      );
    
      return null;
    }

### Approval Workflow with Context
    
    
    import { Text, TouchableOpacity, View } from "react-native";
    import { useHumanInTheLoop, ToolCallStatus } from "@copilotkit/react-native";
    import { z } from "zod";
    
    function ExpenseApproval() {
      useHumanInTheLoop(
        {
          name: "approveExpense",
          description: "Request manager approval for an expense report",
          parameters: z.object({
            employeeName: z.string().describe("Name of the employee"),
            amount: z.number().describe("Expense amount in dollars"),
            category: z.string().describe("Expense category"),
            description: z.string().describe("Description of the expense"),
          }),
          render: ({ args, status, respond, result }) => {
            if (status === ToolCallStatus.Executing && respond) {
              return (
                <View style={{ padding: 16, borderWidth: 1, borderRadius: 8 }}>
                  <Text style={{ fontWeight: "700" }}>Expense Approval Required</Text>
                  <View style={{ marginTop: 8, gap: 4 }}>
                    <Text style={{ fontSize: 12 }}>Employee: {args.employeeName}</Text>
                    <Text style={{ fontSize: 12 }}>Amount: ${args.amount.toFixed(2)}</Text>
                    <Text style={{ fontSize: 12 }}>Category: {args.category}</Text>
                    <Text style={{ fontSize: 12 }}>Description: {args.description}</Text>
                  </View>
                  <View style={{ flexDirection: "row", gap: 8, marginTop: 16 }}>
                    <TouchableOpacity
                      onPress={() => respond({ approved: true })}
                      style={{ backgroundColor: "#22c55e", paddingHorizontal: 16, paddingVertical: 8, borderRadius: 6 }}
                    >
                      <Text style={{ color: "#fff" }}>Approve</Text>
                    </TouchableOpacity>
                    <TouchableOpacity
                      onPress={() =>
                        respond({ approved: false, reason: "Needs more detail" })
                      }
                      style={{ backgroundColor: "#ef4444", paddingHorizontal: 16, paddingVertical: 8, borderRadius: 6 }}
                    >
                      <Text style={{ color: "#fff" }}>Reject</Text>
                    </TouchableOpacity>
                  </View>
                </View>
              );
            }
    
            if (status === ToolCallStatus.Complete && result) {
              const parsed = JSON.parse(result);
              return (
                <View style={{ padding: 8 }}>
                  <Text style={{ fontSize: 12, color: parsed.approved ? "#16a34a" : "#dc2626" }}>
                    {parsed.approved
                      ? "Expense approved."
                      : `Expense rejected: ${parsed.reason}`}
                  </Text>
                </View>
              );
            }
    
            return null;
          },
        },
        [],
      );
    
      return null;
    }

## Behavior

  * **Blocks agent execution** : The agent pauses when this tool is called and waits for the `respond` callback to be invoked before continuing.
  * **Internal status machine** : The hook manages three states: `InProgress` (arguments streaming in), `Executing` (waiting for user response), and `Complete` (user has responded). Your render component receives the appropriate props for each state.
  * **Single response** : The `respond` callback should only be called once per tool invocation. Calling it resolves the tool call promise with the provided value.
  * **Built on`useFrontendTool`**: Under the hood, this hook wraps `useFrontendTool` with an internally generated handler, so all the same lifecycle behavior (mount/unmount registration, duplicate warnings) applies.
  * **Mount/Unmount lifecycle** : The tool and its render component are registered on mount and removed on unmount.
  * **No return value** : The hook returns `void`.



## Related

  * [`useFrontendTool`](https://docs.copilotkit.ai/reference/react-native/hooks/useFrontendTool): for tools with automated handlers that do not require user interaction
  * [`useRenderTool`](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool): register renderer-only tool call UI (named or wildcard)
  * `ToolCallStatus`: the status enum used across tool hooks
  * [React (V2) reference](https://docs.copilotkit.ai/reference/v2/hooks/useHumanInTheLoop)



## ToolCallStatus

The `ToolCallStatus` enum is exported from `@copilotkit/react-native` and defines the three phases of tool execution:

Value| Description  
---|---  
`ToolCallStatus.InProgress`| Arguments are being streamed from the agent. The tool has not started executing yet.  
`ToolCallStatus.Executing`| Arguments are fully resolved. For `useHumanInTheLoop`, the `respond` callback is available.  
`ToolCallStatus.Complete`| Execution is finished. The `result` string is available.
