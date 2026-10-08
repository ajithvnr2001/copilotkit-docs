---
url: https://docs.copilotkit.ai/reference/react-native/hooks/useFrontendTool/
title: useFrontendTool
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:52.058082+00:00
---

# useFrontendTool

> Source: https://docs.copilotkit.ai/reference/react-native/hooks/useFrontendTool/

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

# useFrontendTool

React hook for registering client-side tool handlers with optional UI rendering in React Native

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useFrontendTool` registers a client-side tool with CopilotKit at component scope. When the agent decides to call the tool, the provided `handler` function executes on the device. Optionally, you can supply a `render` component to display custom UI in the chat showing the tool's execution progress and results.

Re-exported from `@copilotkit/react-core/v2`. It is identical to the [React (V2) `useFrontendTool`](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTool); only the import path differs.

The hook manages the full registration lifecycle: it warns if a tool with the same name already exists, registers the tool and its render component on mount, and cleans up both registrations on unmount. In v2, parameter schemas are defined using [Zod](https://zod.dev) instead of plain parameter arrays.

## Signature
    
    
    import { useFrontendTool } from "@copilotkit/react-native";
    
    function useFrontendTool<T extends Record<string, unknown>>(
      tool: ReactFrontendTool<T>,
      deps?: ReadonlyArray<unknown>,
    ): void;

## Parameters

Prop

Type

`tool`ReactFrontendTool<T>

Prop

Type

`deps?`ReadonlyArray<unknown>

## Usage

### Basic Tool with Zod Parameters
    
    
    import { useState } from "react";
    import { Text, View } from "react-native";
    import { useFrontendTool } from "@copilotkit/react-native";
    import { z } from "zod";
    
    function TodoManager() {
      const [todos, setTodos] = useState<string[]>([]);
    
      useFrontendTool(
        {
          name: "addTodo",
          description: "Add a new item to the user's todo list",
          parameters: z.object({
            text: z.string().describe("The todo item text"),
            priority: z.enum(["low", "medium", "high"]).describe("Priority level"),
          }),
          handler: async ({ text, priority }) => {
            setTodos((prev) => [...prev, text]);
            return `Added "${text}" with ${priority} priority`;
          },
        },
        [],
      );
    
      return (
        <View>
          {todos.map((t, i) => (
            <Text key={i}>{t}</Text>
          ))}
        </View>
      );
    }

### Tool with Custom Render Component
    
    
    import { Text, View } from "react-native";
    import { useFrontendTool, ToolCallStatus } from "@copilotkit/react-native";
    import { z } from "zod";
    
    function WeatherWidget() {
      useFrontendTool(
        {
          name: "getWeather",
          description: "Fetch and display weather information for a city",
          parameters: z.object({
            city: z.string().describe("City name"),
            units: z.enum(["celsius", "fahrenheit"]).default("celsius"),
          }),
          handler: async ({ city, units }, { signal }) => {
            const response = await fetch(
              `https://your-server/api/weather?city=${city}&units=${units}`,
              { signal },
            );
            const data = await response.json();
            return JSON.stringify(data);
          },
          render: ({ args, status, result }) => {
            if (status === ToolCallStatus.InProgress) {
              return (
                <View>
                  <Text>Fetching weather for {args.city}...</Text>
                </View>
              );
            }
            if (status === ToolCallStatus.Complete && result) {
              const data = JSON.parse(result);
              return (
                <View>
                  <Text>{data.city}</Text>
                  <Text>
                    {data.temperature}&deg; {data.units}
                  </Text>
                  <Text>{data.conditions}</Text>
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

### Conditionally Available Tool
    
    
    import { View } from "react-native";
    import { useFrontendTool } from "@copilotkit/react-native";
    import { z } from "zod";
    
    function AdminPanel({ isAdmin }: { isAdmin: boolean }) {
      useFrontendTool(
        {
          name: "deleteUser",
          description: "Delete a user account by ID (admin only)",
          parameters: z.object({
            userId: z.string().describe("The ID of the user to delete"),
          }),
          handler: async ({ userId }) => {
            await fetch(`https://your-server/api/users/${userId}`, {
              method: "DELETE",
            });
            return `User ${userId} deleted`;
          },
          available: isAdmin ? "enabled" : "disabled",
        },
        [isAdmin],
      );
    
      return <View>{/* admin UI */}</View>;
    }

## The render type React Native needs

`render` is typed as `ReactToolCallRenderer<T>["render"]`, which is a `React.ComponentType`. A function component's return type is `ReactNode`, so **this compiles** :
    
    
    useFrontendTool({
      name: "showWeather",
      description: "Show the weather",
      parameters: z.object({ city: z.string() }),
      handler: async ({ city }) => city,
      // Compiles. `ReactNode` includes `string`.
      render: ({ args }) => `Weather in ${args.city}`,
    });

and then fails on a device. The string reaches the prebuilt chat's `FlatList` as a bare text child of a host view, and React Native throws _Text strings must be rendered within a`<Text>` component_. The same applies to a number, an array of elements, or `undefined` — all of them are `ReactNode`, and none of them is something React Native's list renderer can draw.

`@copilotkit/react-native` exports an **opt-in** type that narrows the return to `ReactElement | null`, so the compiler rejects it instead:
    
    
    import { useFrontendTool } from "@copilotkit/react-native";
    import type { FrontendToolRenderFunction } from "@copilotkit/react-native";
    import { Text } from "react-native";
    import { z } from "zod";
    
    const renderWeather: FrontendToolRenderFunction<{ city: string }> = ({
      args,
    }) => <Text>{args.city}</Text>;
    
    // `TS2322: Type 'string' is not assignable to type 'ReactElement…'`
    const broken: FrontendToolRenderFunction<{ city: string }> = ({ args }) =>
      `Weather in ${args.city}`;
    
    useFrontendTool({
      name: "showWeather",
      description: "Show the weather",
      parameters: z.object({ city: z.string() }),
      handler: async ({ city }) => city,
      render: renderWeather,
    });

Prop

Type

`FrontendToolRenderFunction<T>?`(props: React.ComponentProps<ReactToolCallRenderer<T>['render']>) => React.ReactElement | null

It is opt-in, and only opt-in

This type changes no hook signature. A renderer written **inline** in a `useFrontendTool` call is still checked against react-core's `ReactNode`-returning contract, and a bare string still compiles there. You get the narrowing on renderers you annotate with it — declare `render` as a standalone `FrontendToolRenderFunction<T>` and pass it in, as above. It does not make the package safe on its own.

[`useRenderTool`](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool) needs none of this: it declares its own `render` as `(props) => ReactElement | null`, so a bare string is rejected there without any annotation.

## Behavior

  * **Duplicate detection** : If a tool with the same `name` is already registered, the hook logs a warning. Only one tool per name is active at a time.
  * **Mount/Unmount lifecycle** : The tool and its optional render component are registered on mount and removed on unmount.
  * **Dependency tracking** : When `deps` is provided, the registration is refreshed whenever the **serialised** array changes — `JSON.stringify(deps)`, not `useEffect`'s per-element `Object.is`. See Dependency comparison below; the difference is load-bearing.
  * **Handler and render are captured at registration** : Neither closure is re-read on every render. A value your `handler` or `render` reads from component state or props is frozen at whatever it was when the tool was last registered, so it must be declared in `deps` (subject to the comparison rules below).
  * **Render component lifecycle** : If a `render` function is provided, it is added to the internal render tool calls registry. It receives streaming `args` (partial during `InProgress`, complete during `Executing` and `Complete`).
  * **`render`'s return type is `ReactNode`, not `ReactElement | null`**: a bare string typechecks and then throws in the chat's `FlatList`. Annotate the renderer with `FrontendToolRenderFunction<T>` to have the compiler reject it.
  * **No return value** : The hook returns `void`.



## Dependency comparison

The registration effect's real dependency list is `[tool.name, tool.available, copilotkit, JSON.stringify(extraDeps)]` (`packages/react-core/src/v2/hooks/use-frontend-tool.tsx:45`, where `extraDeps` is your `deps ?? []`). Your array reaches React as **one serialised string** , so the reference identity that `useEffect` compares never enters into it.

What that means in practice — the middle column is actual `JSON.stringify` output for the value wrapped in an array:

Value in `deps`| Serialises to| Effect  
---|---|---  
Primitives: `string`, `number`, `boolean`, `null`| themselves| Compared correctly. Prefer these.  
A function| `null`| **Never re-registers** — every function serialises identically.  
`undefined`, a `Symbol`| `null`| **Never re-registers.**  
`new Map([["a", 1]])`, `new Set([1, 2, 3])`| `{}`| **Never re-registers** — an empty and a populated `Map` compare equal.  
Class instance with own enumerable fields (`this.n = n`)| `{"n":1}`| Compared correctly.  
Class instance whose state is in `#private` fields| `{}`| **Never re-registers.**  
Class instance whose state is behind a prototype getter| `{}` (only own fields appear)| **Never re-registers** on the getter's value.  
`{ x: 1, y: 2 }` vs `{ y: 2, x: 1 }`| `{"x":1,"y":2}` vs `{"y":2,"x":1}`| Re-registers even though the objects are equivalent — key order counts.  
A circular object, a `BigInt`| throws `TypeError`| **Crashes the component** — see below.  
  
A circular value in `deps` is not a silent bug. `JSON.stringify` throws `TypeError: Converting circular structure to JSON` while the component is rendering, which takes the component down. Never put a value that may reference itself — a graph node, a parent-linked tree, a store instance — into `deps`. A `BigInt` throws the same way (`Do not know how to serialize a BigInt`).

### Passing values that do not serialise

Two patterns work.

**Derive a primitive** that changes exactly when the thing you care about changes, and put that in `deps`:
    
    
    // Not `[items]`, `[cache]`, `[onSubmit]` — those are invisible or unstable.
    useFrontendTool({ ...tool }, [items.length, cache.size, selectedId, revision]);

**Or keep the value out of`deps` and read it through a latest-value ref.** The registration stays stable while the closure always sees the current value. This is the only option for a changing callback, which `deps` cannot detect at all:
    
    
    import { useEffect, useRef } from "react";
    import { useFrontendTool } from "@copilotkit/react-native";
    import { z } from "zod";
    
    function DraftTool({ onSubmit }: { onSubmit: () => Promise<string> }) {
      const latestOnSubmit = useRef(onSubmit);
      useEffect(() => {
        latestOnSubmit.current = onSubmit;
      });
    
      useFrontendTool(
        {
          name: "submitDraft",
          description: "Submit the current draft",
          parameters: z.object({}),
          handler: async () => latestOnSubmit.current(),
        },
        [],
      );
    
      return null;
    }

The same ref pattern applies to a `render` component that needs live state, and to any `Map`, `Set` or class instance you would otherwise have been tempted to list in `deps`.

## Related

  * [`useRenderTool`](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool): register renderer-only tool call UI (named or wildcard), and the migration notes for React Native's older local hook of the same name
  * [`useCopilotKit`](https://docs.copilotkit.ai/reference/react-native/hooks/useCopilotKit): access the core instance and run tools programmatically
  * [React (V2) reference](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTool): the web equivalent this page mirrors


