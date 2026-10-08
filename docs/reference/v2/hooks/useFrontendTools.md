---
url: https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTools/
title: useFrontendTools
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:34:44.517027+00:00
---

# useFrontendTools

> Source: https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTools/

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

# useFrontendTools

React hook for registering a list of client-side tools whose length can change between renders

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useFrontendTools` registers many client-side tools in one call. Use it when the set of tools is not known when you write the component: tools built from state, from props, or from a list the backend returned.

[`useFrontendTool`](https://docs.copilotkit.ai/reference/hooks/useFrontendTool) registers exactly one tool per call, so it cannot be called in a loop over a list whose length changes. That breaks the rules of hooks. `useFrontendTools` runs a single effect over the whole array instead, so the array may be empty on one render and hold twenty entries on the next.

Each entry is the same `ReactFrontendTool` object that `useFrontendTool` takes. See that page for the full tool shape, including `parameters`, `handler`, `render`, and `webmcp`.

## Signature
    
    
    import { useFrontendTools } from "@copilotkit/react-core/v2";
    
    function useFrontendTools(
      tools: ReadonlyArray<ReactFrontendTool<any>> | undefined,
      deps?: ReadonlyArray<unknown>,
    ): void;

## Parameters

Prop

Type

`tools`ReadonlyArray<ReactFrontendTool<any>> | undefined

Prop

Type

`deps?`ReadonlyArray<unknown>

## Usage

### Tools built from application state
    
    
    function ReportTools({ reports }: { reports: Report[] }) {
      const navigate = useNavigate();
    
      useFrontendTools(
        reports.map((report) => ({
          name: `open_${report.id}`,
          description: `Open the ${report.title} report`,
          handler: async () => {
            navigate(`/reports/${report.id}`);
            return `Opened ${report.title}`;
          },
        })),
        [navigate],
      );
    
      return null;
    }

When `reports` grows, the new tools are registered. When a report disappears from the list, its tool is unregistered and the rest stay registered.

### Tools described by the backend
    
    
    function BackendTools() {
      const { data, isLoading } = useQuery({
        queryKey: ["tool-descriptors"],
        queryFn: fetchToolDescriptors,
      });
    
      useFrontendTools(
        data?.map((descriptor) => ({
          name: descriptor.name,
          description: descriptor.description,
          parameters: z.object({
            query: z.string().describe("What to look up"),
          }),
          handler: async ({ query }) => {
            const result = await runDescriptor(descriptor.id, query);
            return JSON.stringify(result);
          },
        })),
        [],
      );
    
      return isLoading ? <Spinner /> : null;
    }

Passing `undefined` while the query is in flight registers nothing. The tools appear once the data arrives, without a second code path for the loading state.

### Turning a subset of tools off
    
    
    function PermissionedTools({ isAdmin }: { isAdmin: boolean }) {
      useFrontendTools([
        {
          name: "searchOrders",
          description: "Search orders by status",
          parameters: z.object({ status: z.string() }),
          handler: async ({ status }) => JSON.stringify(await search(status)),
        },
        {
          name: "refundOrder",
          description: "Refund an order by ID (admin only)",
          parameters: z.object({ orderId: z.string() }),
          handler: async ({ orderId }) => refund(orderId),
          available: isAdmin,
        },
      ]);
    
      return null;
    }

`available: false` keeps the tool registered but hides it from the agent. Toggling it re-registers that tool, the same as with `useFrontendTool`.

### Tools with render components
    
    
    function ChartTools({ metrics }: { metrics: Metric[] }) {
      useFrontendTools(
        metrics.map((metric) => ({
          name: `chart_${metric.key}`,
          description: `Chart the ${metric.label} metric`,
          parameters: z.object({ days: z.number() }),
          handler: async ({ days }) => JSON.stringify(await load(metric, days)),
          render: ({ status, result }) => {
            if (status !== ToolCallStatus.Complete || !result) {
              return <div className="animate-pulse">Loading {metric.label}…</div>;
            }
            return <Chart data={JSON.parse(result)} />;
          },
        })),
        [],
      );
    
      return null;
    }

## Behavior

  * **Value-based re-registration** : The array is normally built inline, so its identity changes on every render. The hook keys on the `name`, `description`, `agentId`, `available`, and `webmcp` of every entry instead. A re-render that produces an equal list does not re-register anything.
  * **Descriptions stay current** : `description` is part of the key. A description derived from your data, such as ``Open the ${report.title} report``, reaches the agent as soon as the data changes, with no `deps` entry. This is the one place the key differs from [`useFrontendTool`](https://docs.copilotkit.ai/reference/hooks/useFrontendTool), which keys only on `name`, `available`, and `webmcp`.
  * **Adding and removing** : When the list changes, tools that are new get registered and tools that left get unregistered. Tools present in both the old and new list are re-registered with their latest definition.
  * **Unmount** : Every tool the hook registered is unregistered on unmount.
  * **Duplicate names** : A `name` and `agentId` pair listed twice in one array is a mistake in the calling code. The last entry wins and the hook logs a warning naming the tool.
  * **Overriding another registration** : If a tool with the same `name` and `agentId` was already registered elsewhere, the hook overrides it and logs a warning, matching `useFrontendTool`.
  * **Render component lifecycle** : Entries with a `render` function register a renderer. Renderers are deliberately left in place after unmount so that past tool calls still render in the chat history.
  * **Handlers and parameters are not part of the key** : A `handler` is a function and a `parameters` schema is an object, so neither can be compared by value. Changing only one of them does not re-register on its own. Pass `deps` when a handler closes over a value that must stay current, as the examples above do with `navigate`.
  * **No return value** : The hook returns `void`.



## Related

  * [`useFrontendTool`](https://docs.copilotkit.ai/reference/hooks/useFrontendTool) \-- register a single tool; the reference for the tool shape
  * [`useHumanInTheLoop`](https://docs.copilotkit.ai/reference/hooks/useHumanInTheLoop) \-- for tools that pause execution and wait for user input
  * [`useRenderTool`](https://docs.copilotkit.ai/reference/hooks/useRenderTool) \-- register renderer-only tool call UI (named or wildcard)


