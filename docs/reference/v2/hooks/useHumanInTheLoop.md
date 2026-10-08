---
url: https://docs.copilotkit.ai/reference/v2/hooks/useHumanInTheLoop/
title: useHumanInTheLoop
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:34:44.668555+00:00
---

# useHumanInTheLoop

> Source: https://docs.copilotkit.ai/reference/v2/hooks/useHumanInTheLoop/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁React (V2)SDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Components

[CopilotChat](https://docs.copilotkit.ai/reference/v2/components/CopilotChat)[CopilotChatAssistantMessage](https://docs.copilotkit.ai/reference/v2/components/CopilotChatAssistantMessage)[CopilotChatInput](https://docs.copilotkit.ai/reference/v2/components/CopilotChatInput)[CopilotChatMessageView](https://docs.copilotkit.ai/reference/v2/components/CopilotChatMessageView)[CopilotChatUserMessage](https://docs.copilotkit.ai/reference/v2/components/CopilotChatUserMessage)[CopilotChatView](https://docs.copilotkit.ai/reference/v2/components/CopilotChatView)[CopilotKit](https://docs.copilotkit.ai/reference/v2/components/CopilotKit)[CopilotPopup](https://docs.copilotkit.ai/reference/v2/components/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/v2/components/CopilotSidebar)[CopilotThreadsDrawer](https://docs.copilotkit.ai/reference/v2/components/CopilotThreadsDrawer)

Hooks

[useAgent](https://docs.copilotkit.ai/reference/v2/hooks/useAgent)[useAgentContext](https://docs.copilotkit.ai/reference/v2/hooks/useAgentContext)[useCapabilities](https://docs.copilotkit.ai/reference/v2/hooks/useCapabilities)[useComponent](https://docs.copilotkit.ai/reference/v2/hooks/useComponent)[useConfigureSuggestions](https://docs.copilotkit.ai/reference/v2/hooks/useConfigureSuggestions)[useCopilotChatConfiguration](https://docs.copilotkit.ai/reference/v2/hooks/useCopilotChatConfiguration)[useCopilotKit](https://docs.copilotkit.ai/reference/v2/hooks/useCopilotKit)[useDefaultRenderTool](https://docs.copilotkit.ai/reference/v2/hooks/useDefaultRenderTool)[useFrontendTool](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTool)[useFrontendTools](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTools)[useHumanInTheLoop](https://docs.copilotkit.ai/reference/v2/hooks/useHumanInTheLoop)[useInterrupt](https://docs.copilotkit.ai/reference/v2/hooks/useInterrupt)[useRenderTool](https://docs.copilotkit.ai/reference/v2/hooks/useRenderTool)[useRenderToolCall](https://docs.copilotkit.ai/reference/v2/hooks/useRenderToolCall)[useSuggestions](https://docs.copilotkit.ai/reference/v2/hooks/useSuggestions)[useThreads](https://docs.copilotkit.ai/reference/v2/hooks/useThreads)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[v2](https://docs.copilotkit.ai/reference/v2)Hooks

# useHumanInTheLoop

React hook for interactive tools that pause agent execution and wait for user input

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useHumanInTheLoop` registers an interactive tool that pauses agent execution until the user responds through your custom UI. Unlike `useFrontendTool`, there is no `handler` function. Instead, the hook provides an internal status machine (`InProgress` -> `Executing` -> `Complete`) and supplies a `respond` callback to the render component while the tool is in the `Executing` state. The agent remains paused until `respond` is called with the user's input.

This hook is built on top of `useFrontendTool` with an internally managed handler that resolves the tool call promise when `respond` is invoked. Use it for confirmation dialogs, approval workflows, form collection, or any scenario where a human must provide input before the agent can continue.

## Signature
    
    
    import { useHumanInTheLoop } from "@copilotkit/react-core/v2";
    
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
                <div className="p-4 text-gray-500">Preparing confirmation...</div>
              );
            }
    
            if (status === ToolCallStatus.Executing && respond) {
              return (
                <div className="p-4 border rounded">
                  <p>
                    Are you sure you want to delete {args.itemCount} {args.itemName}
                    (s)?
                  </p>
                  <div className="flex gap-2 mt-4">
                    <button
                      onClick={() => respond({ confirmed: true })}
                      className="bg-red-500 text-white px-4 py-2 rounded"
                    >
                      Delete
                    </button>
                    <button
                      onClick={() => respond({ confirmed: false })}
                      className="bg-gray-300 px-4 py-2 rounded"
                    >
                      Cancel
                    </button>
                  </div>
                </div>
              );
            }
    
            if (status === ToolCallStatus.Complete && result) {
              const parsed = JSON.parse(result);
              return (
                <div className="p-2 text-sm text-gray-600">
                  {parsed.confirmed ? "Items deleted." : "Deletion cancelled."}
                </div>
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
                <div className="p-4 border rounded space-y-3">
                  <p className="font-medium">Order: {args.orderSummary}</p>
                  <p>Please enter your shipping address:</p>
                  <input
                    placeholder="Street address"
                    value={address.street}
                    onChange={(e) =>
                      setAddress({ ...address, street: e.target.value })
                    }
                    className="w-full border p-2 rounded"
                  />
                  <input
                    placeholder="City"
                    value={address.city}
                    onChange={(e) =>
                      setAddress({ ...address, city: e.target.value })
                    }
                    className="w-full border p-2 rounded"
                  />
                  <input
                    placeholder="ZIP code"
                    value={address.zip}
                    onChange={(e) =>
                      setAddress({ ...address, zip: e.target.value })
                    }
                    className="w-full border p-2 rounded"
                  />
                  <button
                    onClick={() => respond(address)}
                    className="bg-blue-500 text-white px-4 py-2 rounded"
                  >
                    Submit Address
                  </button>
                </div>
              );
            }
    
            if (status === ToolCallStatus.Complete) {
              return (
                <div className="p-2 text-green-600">
                  Shipping address submitted.
                </div>
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
                <div className="p-4 border rounded">
                  <h3 className="font-bold">Expense Approval Required</h3>
                  <div className="mt-2 space-y-1 text-sm">
                    <p>Employee: {args.employeeName}</p>
                    <p>Amount: ${args.amount.toFixed(2)}</p>
                    <p>Category: {args.category}</p>
                    <p>Description: {args.description}</p>
                  </div>
                  <div className="flex gap-2 mt-4">
                    <button
                      onClick={() => respond({ approved: true })}
                      className="bg-green-500 text-white px-4 py-2 rounded"
                    >
                      Approve
                    </button>
                    <button
                      onClick={() =>
                        respond({ approved: false, reason: "Needs more detail" })
                      }
                      className="bg-red-500 text-white px-4 py-2 rounded"
                    >
                      Reject
                    </button>
                  </div>
                </div>
              );
            }
    
            if (status === ToolCallStatus.Complete && result) {
              const parsed = JSON.parse(result);
              return (
                <div
                  className={`p-2 text-sm ${parsed.approved ? "text-green-600" : "text-red-600"}`}
                >
                  {parsed.approved
                    ? "Expense approved."
                    : `Expense rejected: ${parsed.reason}`}
                </div>
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
  * **Internal status machine** : The hook manages three states -- `InProgress` (arguments streaming in), `Executing` (waiting for user response), and `Complete` (user has responded). Your render component receives the appropriate props for each state.
  * **Single response** : The `respond` callback should only be called once per tool invocation. Calling it resolves the tool call promise with the provided value.
  * **Built on`useFrontendTool`**: Under the hood, this hook wraps `useFrontendTool` with an internally generated handler, so all the same lifecycle behavior (mount/unmount registration, duplicate warnings) applies.
  * **Mount/Unmount lifecycle** : The tool and its render component are registered on mount and removed on unmount.
  * **No return value** : The hook returns `void`.



## Related

  * [`useFrontendTool`](https://docs.copilotkit.ai/reference/hooks/useFrontendTool) \-- for tools with automated handlers that do not require user interaction
  * [`useRenderToolCall`](https://docs.copilotkit.ai/reference/hooks/useRenderToolCall) \-- for rendering backend tool calls
  * `ToolCallStatus` \-- the status enum used across tool hooks



## ToolCallStatus

The `ToolCallStatus` enum is exported from `@copilotkit/react-core` and defines the three phases of tool execution:

Value| Description  
---|---  
`ToolCallStatus.InProgress`| Arguments are being streamed from the agent. The tool has not started executing yet.  
`ToolCallStatus.Executing`| Arguments are fully resolved. For `useHumanInTheLoop`, the `respond` callback is available.  
`ToolCallStatus.Complete`| Execution is finished. The `result` string is available.
