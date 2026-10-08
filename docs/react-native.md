---
url: https://docs.copilotkit.ai/react-native/
title: React Native quickstart
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:50.836486+00:00
---

# React Native quickstart

> Source: https://docs.copilotkit.ai/react-native/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReact NativeAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Getting Started

[Quickstart](https://docs.copilotkit.ai/react-native)[Docs status](https://docs.copilotkit.ai/react-native/using-these-docs)[Reference docs](https://docs.copilotkit.ai/reference/react-native)

Guides coming soon...React Native is feature complete, but the docs are still catching up. The [quickstart](https://docs.copilotkit.ai/react-native) and [reference](https://docs.copilotkit.ai/reference/react-native) guides are ready with more guides on the way.

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Getting Started

# React Native

Build with CopilotKit in React Native — quickstart, Metro and polyfill setup, frontend tools, and device deployment.

`@copilotkit/react-native` gives you CopilotKit's provider and hooks for React Native, plus optional pre-built chat components. This guide builds a fully custom chat UI with the hooks, backed by a [Copilot Runtime](https://docs.copilotkit.ai/backend/copilot-runtime) endpoint on your server.

The package has three import surfaces — `/headless` (provider + hooks, no native peer dependencies, **1.64.0+**), the root barrel, and `/components` (the rendered chat UI). See Import surfaces for what each one pulls in; this guide uses `/headless` throughout.

## Start with your coding agent#

Use this prompt to set up CopilotKit in your React Native app, configure Metro and polyfills, and verify chat against your Runtime. You can also follow the manual steps below.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Prerequisites#

  * An OpenAI API key (or another model provider supported by [Model Selection](https://docs.copilotkit.ai/model-selection))
  * React Native 0.70+ (bare CLI or Expo)
  * Node.js 20+
  * `@react-native-community/cli` in your `devDependencies` **if you are on React Native 0.87 or later** , which no longer bundles it. A freshly `init`ed app already has it; an app you have upgraded may not, and without it `react-native bundle` and `react-native start` stop with a message naming the missing package instead of running.



## Getting started#

### Create your React Native app#

If you don't have one already:
    
    
    npx @react-native-community/cli@latest init MyCopilotApp
    cd MyCopilotApp

### Install CopilotKit#

Install the React Native frontend package and `@copilotkit/runtime` for your local Copilot Runtime server:

npmpnpmyarn
    
    
    npm install @copilotkit/react-native @copilotkit/runtime
    npm install -D tsx typescript @types/node
    
    
    pnpm add @copilotkit/react-native @copilotkit/runtime
    pnpm add -D tsx typescript @types/node
    
    
    yarn add @copilotkit/react-native @copilotkit/runtime
    yarn add -D tsx typescript @types/node

`/headless` needs `@copilotkit/react-native` 1.64.0 or later

This guide imports from `@copilotkit/react-native/headless` throughout. That subpath first ships in **1.64.0** — the commands above install the latest version, so a fresh install has it, but a project already pinned to 1.63.x or earlier does not. There, every `/headless` import fails at bundle time with `Unable to resolve module @copilotkit/react-native/headless`, which on Metro reads like a broken install rather than a version skew.

Check what you actually resolved before going further:
    
    
    npm ls @copilotkit/react-native

On 1.63.x or earlier, prefer upgrading to 1.64.0+. If you cannot — because you are matching a pinned `@copilotkit/runtime` — the same `CopilotKitProvider`, `useAgent` and `useCopilotKit` are exported from the package root, so dropping `/headless` from the import path is the whole code change. It is not a free swap, though: on those versions the root barrel statically imports `expo-document-picker` and `expo-file-system`, so you must also install (or stub) both, or your release bundle fails with `Unable to resolve module expo-document-picker`. See Import surfaces.

TypeScript: use bundler module resolution

The `/headless`, `/components` and `/polyfills` subpaths are published through the package `exports` map, which TypeScript's legacy `"moduleResolution": "node"` (`node10`) ignores. Under that setting, type checking fails with `Cannot find module '@copilotkit/react-native/headless'` even though Metro bundles the app. Set `"moduleResolution": "bundler"` in `tsconfig.json`; if `module` is `commonjs` or unset, also set `"module": "esnext"`. `@react-native/typescript-config` and Expo's base config already use `bundler`.

### Add polyfills#

React Native's JS runtime (Hermes) lacks several Web APIs that CopilotKit depends on. The package installs these polyfills itself on first import, but two things must happen **at the very top of your entry point, before any CopilotKit import** : a secure random source, then the polyfill barrel.

Install the secure RNG first:
    
    
    npm install react-native-get-random-values

index.js
    
    
    import "react-native-get-random-values"; // secure RNG — must be first
    import "@copilotkit/react-native/polyfills";
    
    import { AppRegistry } from "react-native";
    import App from "./App";
    import { name as appName } from "./app.json";
    
    AppRegistry.registerComponent(appName, () => App);

Import order is load-bearing for crypto

CopilotKit's `crypto` polyfill and `react-native-get-random-values` both install only if `crypto.getRandomValues` is still undefined — first writer wins. If any CopilotKit module is evaluated first, CopilotKit's **non-cryptographic** `Math.random` fallback is locked in permanently and `react-native-get-random-values` becomes a silent no-op. Keep it on the first line. See Polyfills.

Granular polyfills

If you already polyfill some of these APIs (e.g. `ReadableStream`), you can import only what you need instead of the barrel:
    
    
    import "@copilotkit/react-native/polyfills/streams";
    import "@copilotkit/react-native/polyfills/encoding";
    import "@copilotkit/react-native/polyfills/crypto";
    import "@copilotkit/react-native/polyfills/dom";
    import "@copilotkit/react-native/polyfills/location";

### Create the Copilot Runtime#

Add a small Node server that hosts Copilot Runtime at `/api/copilotkit` and registers a `default` built-in agent:

server.ts
    
    
    import { createServer } from "node:http";
    import { BuiltInAgent, CopilotRuntime } from "@copilotkit/runtime/v2";
    import { createCopilotNodeListener } from "@copilotkit/runtime/v2/node";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({
          model: "openai:gpt-5-mini",
          prompt: "You are a helpful assistant for a React Native app.",
        }),
      },
    });
    
    const port = Number(process.env.PORT ?? 8200);
    
    createServer(
      createCopilotNodeListener({
        runtime,
        basePath: "/api/copilotkit",
        cors: true,
      }),
    ).listen(port, () => {
      console.log(
        `Copilot Runtime listening at http://localhost:${port}/api/copilotkit`,
      );
    });

### Wrap your app with CopilotKitProvider#

Point the provider at the runtime endpoint. Android emulators reach the host machine at `10.0.2.2`; iOS simulators can use `localhost`.

App.tsx
    
    
    import { CopilotKitProvider } from "@copilotkit/react-native/headless"; 
    import { Platform } from "react-native";
    import { ChatScreen } from "./src/ChatScreen";
    
    const runtimeUrl =
      Platform.OS === "android"
        ? "http://10.0.2.2:8200/api/copilotkit"
        : "http://localhost:8200/api/copilotkit";
    
    export default function App() {
      return (
        <CopilotKitProvider runtimeUrl={runtimeUrl}> {}
          <ChatScreen />
        </CopilotKitProvider>
      );
    }

Testing on a physical device

Replace `localhost` or `10.0.2.2` with your development machine's LAN IP address, for example `http://192.168.1.23:8200/api/copilotkit`.

### Build your chat UI#

The platform-agnostic hooks work the same way here as on the web. Below is a minimal chat screen using `useAgent` and `useCopilotKit`:

src/ChatScreen.tsx
    
    
    import { useCallback, useRef, useState } from "react";
    import {
      FlatList,
      KeyboardAvoidingView,
      Platform,
      Text,
      TextInput,
      TouchableOpacity,
      View,
    } from "react-native";
    import { useAgent, useCopilotKit } from "@copilotkit/react-native/headless"; 
    
    export function ChatScreen() {
      const [inputText, setInputText] = useState("");
      const flatListRef = useRef<FlatList>(null);
    
      const { copilotkit } = useCopilotKit(); 
      const { agent } = useAgent({ agentId: "default" });
    
      const messages = agent?.messages ?? [];
      const isLoading = agent?.isRunning ?? false;
      const chatMessages = messages.flatMap((message) => {
        if (
    (message.role === "user" || message.role === "assistant") &&
          typeof message.content === "string" &&
          message.content.length > 0
        ) {
          return [
            {
              id: message.id,
              content: message.content,
            },
          ];
        }
        return [];
      });
    
      const handleSend = useCallback(async () => {
        const text = inputText.trim();
    if (!text || isLoading || !agent) return;
    
        setInputText("");
        agent.addMessage({ 
          id: `user-${Date.now()}`,
          role: "user",
          content: text,
        });
        await copilotkit.runAgent({ agent }); 
      }, [inputText, isLoading, agent, copilotkit]);
    
      return (
        <KeyboardAvoidingView
          style={{ flex: 1 }}
          behavior={Platform.OS === "ios" ? "padding" : "height"}
        >
          <FlatList
            ref={flatListRef}
            data={chatMessages}
            renderItem={({ item }) => (
              <View style={{ padding: 12, maxWidth: "80%" }}>
                <Text>{item.content}</Text>
              </View>
            )}
            keyExtractor={(item, i) => item.id ?? String(i)}
            onContentSizeChange={() =>
              flatListRef.current?.scrollToEnd({ animated: true })
            }
          />
          <View style={{ flexDirection: "row", padding: 8 }}>
            <TextInput
              style={{ flex: 1, borderWidth: 1, borderRadius: 8, padding: 8 }}
              value={inputText}
              onChangeText={setInputText}
              placeholder="Type a message..."
            />
            <TouchableOpacity onPress={handleSend} style={{ padding: 8 }}>
              <Text>Send</Text>
            </TouchableOpacity>
          </View>
        </KeyboardAvoidingView>
      );
    }

Headless by design

`@copilotkit/react-native/headless` provides hooks, not UI components, so you have full control over your chat interface using standard React Native components. If you'd rather not build one, a rendered chat is available from `@copilotkit/react-native/components` — see Import surfaces.

### Run the runtime and app#

Start Copilot Runtime in one terminal:
    
    
    export OPENAI_API_KEY=sk-...
    npx tsx server.ts

Run the React Native app in another terminal:

iOSAndroid
    
    
    npx react-native run-ios
    
    
    npx react-native run-android

### Start chatting!#

Your React Native app is now connected to Copilot Runtime. The shared hooks are available here:

  * `useAgent` \- connect to an agent and manage messages
  * `useFrontendTool` \- let the agent call functions in your app
  * `useHumanInTheLoop` \- add approval flows for agent actions
  * `useCopilotKit` \- access the CopilotKit instance directly
  * `useRenderTool` \- draw UI for a tool call you don't own, by name or with a `"*"` fallback (see Frontend tools)



Troubleshooting

  * **Metro can't resolve modules** : Clear the cache with `npx react-native start --reset-cache`.
  * **Streaming not working** : Make sure polyfills are imported before any CopilotKit code in your entry point.
  * **No response from the runtime** : Confirm the runtime server is running, `http://localhost:8200/api/copilotkit/info` returns the `default` agent, and the device can reach `runtimeUrl`. For physical devices, use your machine's LAN IP instead of `localhost`.
  * **Model auth errors** : Confirm `OPENAI_API_KEY` is set in the terminal running `npx tsx server.ts`.
  * **`Property 'ReadableStream' doesn't exist`** (or the same for `TextEncoder`, `DOMException` or `Headers`): the polyfills did not install. In **1.69.2 and every earlier version** the `polyfills` barrel was published empty — the build dropped all five polyfill imports out of it — so following the setup above installed nothing and the first runtime call failed. Upgrade to the latest version, or, if you are pinned, use the granular imports, which were never affected. This is the _opposite_ of the conflict case below: here you have no polyfill at all, not a competing one.
  * **Existing polyfill conflicts** : Use the granular imports instead of the barrel `polyfills` import.



## Import surfaces#

`@copilotkit/react-native` has three JavaScript entry points. They differ in what UI they give you and — crucially for release bundles — which native peer dependencies Metro has to resolve.

Import| Available since| What you get| Native peers Metro must resolve  
---|---|---|---  
`@copilotkit/react-native/headless`| **1.64.0**| `CopilotKitProvider` and every platform-agnostic hook. No components.| **None**  
`@copilotkit/react-native` (root)| all versions| Everything in `/headless`, plus `useAttachments`, the two _headless_ chat wrappers (`CopilotChat`, `CopilotModal`) and the `CopilotSidebar` / `CopilotPopup` chrome| `expo-document-picker`, `expo-file-system` (via `useAttachments`)  
`@copilotkit/react-native/components`| all versions| The **rendered** chat UI: a `CopilotChat` with a message list, a bottom-sheet `CopilotModal`, `CopilotMarkdown`, `AssistantMessage`, `UserMessage`| `@gorhom/bottom-sheet` (which itself needs `react-native-reanimated` \+ `react-native-gesture-handler`), `react-native-streamdown`  
  
Supporting entry points:

Import| Description  
---|---  
`@copilotkit/react-native/polyfills`| Barrel that installs every polyfill (streams, encoding, crypto, dom, location) plus the streaming-fetch shim  
`@copilotkit/react-native/polyfills/{streams,encoding,crypto,dom,location}`| Granular subpaths for installing a single polyfill  
`@copilotkit/runtime`| Server-side runtime (`CopilotRuntime` / `BuiltInAgent` / `createCopilotNodeListener`) used to host your agent  
  
`CopilotChat` means two different things

The root barrel's `CopilotChat` and `CopilotModal` are **headless wrappers** — they render only context and `children`, no messages and no tool UI. The versions that actually draw a chat are the same-named exports from `@copilotkit/react-native/components`. If you imported `CopilotChat` expecting a chat and got a blank screen, you imported the root one.

Because these are static re-exports, Metro resolves a surface's peers at bundle time whether or not you call the code — so a custom-UI app importing the root barrel must still install `expo-document-picker` and `expo-file-system` (or stub them) or the release bundle fails with `Unable to resolve module expo-document-picker`. Importing from `/headless` avoids that entirely, which is why this guide uses it:

App.tsx
    
    
    import {
      CopilotKitProvider,
      useAgent,
      useFrontendTool,
    } from "@copilotkit/react-native/headless"; 

On `@copilotkit/react-native` 1.63.x and earlier there is no `/headless` — the subpath was added in 1.64.0 ([#6142](https://github.com/CopilotKit/CopilotKit/pull/6142)) precisely to make this custom-UI case possible without the chat and attachment peers. The root barrel is still the package's default, full surface, and it exports the same provider and hooks on every version; `/headless` is the lean alternative, not a replacement. On a pinned older version, import from the root and install or stub `expo-document-picker` and `expo-file-system`.

Importing the provider auto-installs the polyfills: `/headless` runs the polyfill barrel as its first statement, and the root barrel gets it through its `/headless` re-export. `/components` does **not** install them itself — it relies on the provider you import alongside it (from `/headless` or the root). And because the root barrel re-exports everything from `/headless`, existing `@copilotkit/react-native` imports keep working unchanged.

### Which hooks are shared, and which aren't#

The **package** (both `/headless` and the root barrel) re-exports the platform-agnostic hooks from `@copilotkit/react-core`: `useAgent`, `useFrontendTool`, `useHumanInTheLoop`, `useInterrupt`, `useSuggestions`, `useConfigureSuggestions`, `useAgentContext`, `useThreads`, `useCapabilities`, `useComponent`, `useCopilotKit`, and `useRenderToolCall`. These behave the same as on the web.

`useRenderTool` comes from `@copilotkit/react-core` too, and behaves the same as on the web — but it has history worth knowing. React Native used to export a _different_ hook under that name, one that registered a tool as well as a renderer, so `name: "*"` registered a frontend tool literally called `*`. It was replaced by react-core's hook in 1.68 and kept working behind a deprecated compatibility shim, which has since been removed. If you are coming from a version that predates 1.68, see [Migrating from the old React Native `useRenderTool`](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool#migrating-from-the-old-react-native-userendertool).

Two more things are worth knowing:

  * **`useFrontendTool` and `useRenderTool` are not interchangeable**, and the distinction is the same one the web draws. `useFrontendTool` registers a **tool** and (optionally) its renderer: the tool is advertised to the model on every run and the model may call it, so it takes a `description` and a `handler`. `useRenderTool` registers a **renderer only** — nothing is advertised and nothing becomes callable; it draws a tool call somebody else owns, such as a server-side tool, and `name: "*"` makes it the fallback for every tool call with no renderer of its own. Both write into the same react-core renderer registry, which the rendered chat reads. Their render types differ too, exactly as they do on the web: `useRenderTool`'s `render` must return `ReactElement | null`, while `useFrontendTool`'s `render` is a component type that also accepts a bare string. What _is_ React-Native-specific is the consequence of that looser type — a bare string typechecks and then throws inside a `FlatList`. Annotate a `useFrontendTool` renderer with the opt-in [`FrontendToolRenderFunction<T>`](https://docs.copilotkit.ai/reference/react-native/hooks/useFrontendTool#the-render-type-react-native-needs) to have the compiler reject it.
  * **Most of the web rendering hooks are deliberately not exported** : `useDefaultRenderTool` (its built-in card renders `<div>` / `<svg>`), `useRenderCustomMessages`, and `useRenderActivityMessage` (both link the web chat-message stack). `useRenderToolCall` **is** exported, though — it is platform-agnostic, pulls no DOM, and returns `ReactElement | null`, which is exactly what `FlatList`'s `renderItem` needs, so you can draw a registered tool call on any surface rather than only inside the chat.



Rendering data on screen does not give the agent access to it

`useAgentContext` is in the shared list above, and it is the one whose absence fails _silently_. A screen that renders a list has put that list in the view tree, not in the agent's context — those are separate steps. An agent wired without the second one still answers: the prose is coherent, the tool UI paints, the values look plausible, and nothing errors. On the web you would at least have a console to inspect. Here you do not.

Register the data with `useAgentContext`, and write the agent's instructions to refuse to answer about records that context does not carry. Then check one answer against the records your app actually holds — if it names anything else, the context never arrived, however right the screen looks.

## Metro configuration for release bundles#

With package exports enabled, a release bundle can fail with `Unable to resolve module node:crypto` (or another `node:` specifier) pointing at `jose`. This surfaces **only at bundle time** , never at typecheck.

`jose` is not a direct dependency. It arrives transitively through telemetry: `@copilotkit/shared` → `@segment/analytics-node` → `jose`. `jose` publishes separate Node and browser builds behind its `exports` map, and its Node build imports `node:`-prefixed modules that Hermes cannot bundle.

The fix is to resolve **`jose` specifically** against its `browser` condition, using `resolveRequest`:

metro.config.js
    
    
    const { getDefaultConfig, mergeConfig } = require("@react-native/metro-config");
    
    const config = {
      resolver: {
        resolveRequest: (context, moduleImport, platform) => {
          // jose reaches the bundle via @copilotkit/shared -> @segment/analytics-node.
          // Its Node build imports node:* modules that Hermes can't bundle.
          if (moduleImport === "jose" || moduleImport.startsWith("jose/")) {
            return context.resolveRequest(
              { ...context, unstable_conditionNames: ["browser"] }, 
              moduleImport,
              platform,
            );
          }
          return context.resolveRequest(context, moduleImport, platform);
        },
      },
    };
    
    module.exports = mergeConfig(getDefaultConfig(__dirname), config);

On Expo, swap in `getDefaultConfig` from `expo/metro-config`; the `resolver` block is identical.

Don't assert `browser` globally

It's tempting to set `resolver.unstable_conditionNames = ["browser", ...]` instead. Avoid it:

  * `unstable_conditionNames` is an **unordered set of asserted conditions** , not a priority list. The winning target is chosen by the key order in _each package's own_ `exports` map, so reordering this array changes nothing.
  * It applies **globally** , so every dual-build dependency in your graph switches to its browser build — not just `jose`.
  * Metro's React Native default is `["require", "react-native"]`. Replacing it wholesale drops the `react-native` condition, which changes resolution for any package that ships one.



Scoping with `resolveRequest` keeps Metro's defaults intact everywhere else.

Do you need `unstable_enablePackageExports`?

Package `exports` resolution is **enabled by default from Metro 0.82 / React Native 0.79** , so no flag is needed there. It arrived opt-in in React Native 0.72 (Metro 0.76.1) — on React Native 0.72–0.78 set `resolver.unstable_enablePackageExports = true`, which is also what lets Metro resolve this package's `/headless`, `/components`, and `/polyfills` subpaths. React Native below 0.72 has no package-exports support.

Headless removes the need to stub

Importing from `@copilotkit/react-native/headless` means Metro never resolves the chat or attachment peer dependencies, so you don't need `@gorhom/bottom-sheet`, `expo-document-picker`, or `expo-file-system` at all. The `jose` resolver above is independent of that choice — it's needed either way.

## Polyfills#

Hermes lacks several Web APIs CopilotKit relies on: `ReadableStream` / `WritableStream` / `TransformStream`, `TextEncoder` / `TextDecoder`, `DOMException` and `Headers`, `crypto.getRandomValues`, and `window.location`. It also lacks streaming `fetch` bodies (`response.body.getReader()`), which AG-UI's SSE transport needs.

Importing the provider installs these automatically: `/headless` runs the polyfill barrel as its first statement (and the root barrel gets it through `/headless`), also installing an XHR-based streaming-fetch shim on load. The `/components` surface does **not** install them on its own, so it relies on the provider imported alongside it. Each polyfill is skipped if the global it defines already exists, so importing more than once is safe.

Keep the explicit `import "@copilotkit/react-native/polyfills"` from the quickstart at the top of your entry point anyway. Because every polyfill is **first writer wins** , the entry point is the only place you control what gets installed before CopilotKit's own defaults do — which is what makes the secure-RNG ordering below work.

For granular control — for example, if you already polyfill `ReadableStream` yourself — import only the pieces you need instead of the barrel:
    
    
    import "@copilotkit/react-native/polyfills/streams";
    import "@copilotkit/react-native/polyfills/encoding";
    import "@copilotkit/react-native/polyfills/crypto";
    import "@copilotkit/react-native/polyfills/dom";
    import "@copilotkit/react-native/polyfills/location";

The bundled crypto polyfill is not cryptographically secure

CopilotKit's `crypto` polyfill backs `crypto.getRandomValues` with `Math.random` — enough for the message and run IDs it generates, and it logs a warning on install. For production, install [`react-native-get-random-values`](https://github.com/LinusU/react-native-get-random-values) and import it on the **first line of your entry point, before any CopilotKit import** :

index.js
    
    
    import "react-native-get-random-values"; // secure RNG — must be first
    import "@copilotkit/react-native/polyfills";
    // ...

This ordering is a hard requirement, not a precaution. Both implementations install only when `crypto.getRandomValues` is undefined, so whichever loads first wins permanently. If any CopilotKit module is evaluated first, the `Math.random` fallback is locked in and `react-native-get-random-values` silently becomes a no-op — no warning, no error, and every ID stays non-cryptographic for the life of the process.

## Provider options#

`CopilotKitProvider` is a context-only provider (it renders no view of its own), so it composes cleanly as the outermost wrapper around your app. `runtimeUrl` is the only required prop, but several others are available:

Prop| Type| Description  
---|---|---  
`runtimeUrl`| `string`| URL of the Copilot Runtime endpoint (**required**)  
`headers`| `Record<string, string> | (() => Record<string, string>)`| Custom headers sent with every request. Use this for auth — e.g. an `Authorization` bearer token. A function form is called **when the provider renders** , not per request (see the callout below)  
`credentials`| `RequestCredentials`| Fetch credentials mode, e.g. `"include"` to send HTTP-only cookies on cross-origin requests  
`properties`| `Record<string, unknown>`| Custom properties forwarded to agents (e.g. a scoped user id)  
`onError`| `(event) => void`| Called for all error types (runtime connection, agent, tool). Defaults to `console.error`  
`debug`| `DebugConfig`| Enables verbose client-side event logging  
`defaultThrottleMs`| `number`| Default re-render throttle for streaming updates; individual `useAgent` calls can override  
`useSingleEndpoint`| `boolean`| Whether the runtime uses a single-route endpoint (defaults to auto-detect)  
  
App.tsx
    
    
    <CopilotKitProvider
      runtimeUrl={runtimeUrl}
      headers={{ Authorization: `Bearer ${token}` }} 
      properties={{ userId }}
    >
      <ChatScreen />
    </CopilotKitProvider>

Rotating auth tokens: `headers` is resolved on render, not per request

If you pass a function, the provider calls it **in its render body** , memoizes the result, and pushes that object into the core, which snapshots it onto each agent. Nothing re-reads the function at request time.

So a refreshed token is only picked up if the provider **re-renders** and the resulting headers differ. Drive the token from React state (or context) so a refresh triggers a render:
    
    
    const [token, setToken] = useState(initialToken);
    
    <CopilotKitProvider runtimeUrl={runtimeUrl} headers={{ Authorization: `Bearer ${token}` }}>

A token kept in a ref, module variable, or async SDK cache with no accompanying render will keep sending the **stale** value indefinitely. If you can't re-render, call `copilotkit.setHeaders({ ... })` directly when the token rotates.

Cloud props aren't wired on React Native yet

The web provider's `publicApiKey` / `licenseToken` cloud props are not supported by the React Native provider. Point `runtimeUrl` at your own Copilot Runtime.

## Runtime and model wiring#

The runtime from the quickstart hosts a `BuiltInAgent` and serves it with `createCopilotNodeListener`, which plugs straight into Node's built-in `node:http` `createServer` — no Hono or Express dependency required. `createCopilotNodeListener({ runtime, basePath, cors })` returns a request listener.

`cors: true` adds `Access-Control-*` response headers and answers `OPTIONS` preflights. That matters for **browser** clients — Expo Web or `react-native-web` — but it has no bearing on whether a native iOS or Android build can reach the server: CORS is enforced by the browser, and React Native's native networking stack (`NSURLSession` / OkHttp) neither sends an `Origin` header nor consults `Access-Control-Allow-Origin`. Native reachability is decided by the server's bind address, LAN routing and firewall, and platform transport security — see Connecting from a device or bench.

`BuiltInAgent` accepts a model **string** in `provider:model` (or `provider/model`) form for OpenAI, Anthropic, and Google:
    
    
    new BuiltInAgent({ model: "openai:gpt-5-mini", prompt: "..." });      // OPENAI_API_KEY
    new BuiltInAgent({ model: "anthropic:claude-sonnet-4-6", prompt: "..." }); // ANTHROPIC_API_KEY
    new BuiltInAgent({ model: "google:gemini-2.5-pro", prompt: "..." });  // GOOGLE_API_KEY

The string form reads the matching provider API key from the environment. You can also pass `apiKey` on the config, or an already-constructed AI SDK `LanguageModel` instance in place of the string.

### OpenAI-compatible endpoints#

To point the string model form at an OpenAI-compatible endpoint (a gateway, Azure OpenAI, a self-hosted server, etc.), set the base-URL environment variable — the runtime honors it when it constructs the provider:
    
    
    export OPENAI_BASE_URL=https://your-gateway.example.com/v1
    export OPENAI_API_KEY=sk-...
    npx tsx server.ts

The same applies to `ANTHROPIC_BASE_URL` and `GOOGLE_GENERATIVE_AI_BASE_URL`. When the variable is unset, the provider falls back to its default endpoint, so this is fully backward compatible — you do **not** need to build a custom model instance just to change the base URL.

Other BuiltInAgent options

Beyond `model` and `prompt`, `BuiltInAgent` accepts `maxSteps` (tool-calling iterations, default `1`), `tools` (server-executed tools via `defineTool`), `temperature`, `maxOutputTokens`, `providerOptions` (e.g. OpenAI `reasoningEffort`), and `mcpServers` / `mcpClients`. Tools that mutate the app's UI belong on the **client** via `useFrontendTool` (below), not in the server `tools` list.

## Connecting from a device or bench#

`runtimeUrl` must be an address the **device** can reach — `localhost` on a physical device or emulator resolves to the device itself, not your dev machine.

Setup| `runtimeUrl` host  
---|---  
iOS simulator| `localhost` reaches the host machine  
Android emulator| `10.0.2.2` is the emulator's alias for the host's `localhost`  
Android device over USB| run `adb reverse tcp:8200 tcp:8200`, then use `localhost` on the device. `adb reverse` is Android-only — there is no iOS equivalent  
iOS device| your dev machine's LAN IP, on the same Wi-Fi network — plus the ATS exception a plain `http://` address needs  
Physical device on the same LAN (a bench)| your dev machine's LAN IP, e.g. `http://192.168.1.23:8200/api/copilotkit`  
Production| a hosted runtime URL over HTTPS  
  
The quickstart already branches on `Platform.OS` for the simulator/emulator case. Keep the URL a single named constant with a comment so it's easy to swap per environment.

### Plaintext HTTP on a physical device#

Both platforms block plaintext (non-TLS) HTTP by default, so a device silently fails to reach a plain `http://<lan-ip>` dev runtime. These are dev-only affordances — a hosted TLS runtime needs none of them.

On Expo, configure both through `app.json` so they survive the `android/` and `ios/` regeneration that `expo prebuild` performs (never hand-edit the generated `AndroidManifest.xml` or `Info.plist` — they're discarded on the next prebuild). Install the config plugin first:
    
    
    npx expo install expo-build-properties

**Android** — an Android _release_ build needs cleartext opted in:

app.json
    
    
    {
      "expo": {
        "plugins": [
          ["expo-build-properties", { "android": { "usesCleartextTraffic": true } }]
        ]
      }
    }

**iOS** — App Transport Security applies to debug _and_ release builds alike, and `expo-build-properties` has no iOS ATS option, so this goes in `ios.infoPlist`. Since iOS 17, ATS refuses raw IP addresses unless the address is listed in `NSExceptionDomains`, so name your dev machine's IP explicitly (no port):

app.json
    
    
    {
      "expo": {
        "ios": {
          "infoPlist": {
            "NSAppTransportSecurity": {
              "NSExceptionDomains": {
                "192.168.1.23": { "NSExceptionAllowsInsecureHTTPLoads": true }
              }
            },
            "NSLocalNetworkUsageDescription": "Connects to the local Copilot Runtime during development."
          }
        }
      }
    }

`NSLocalNetworkUsageDescription` is required separately: iOS gates local-network access behind a user permission prompt, and without the string the connection fails regardless of ATS.

Keep these out of production builds

`usesCleartextTraffic` and an ATS exception are bench affordances. Scope them to a dev build (a separate Expo profile or app variant), and ship production against an HTTPS runtime with neither. On Android you can tighten further by scoping cleartext to just the dev host with a network-security-config.

`NSAllowsLocalNetworking` isn't enough on its own

Expo and React Native templates already ship `NSAllowsLocalNetworking: true`, which covers `.local` hostnames and unqualified names — but **not** raw IP addresses on iOS 17+. Its presence also causes `NSAllowsArbitraryLoads` to be ignored. The `NSExceptionDomains` entry above is the form that actually works for a LAN IP.

## Frontend tools and generative UI#

Frontend tools let the agent call functions in your app — and render UI — while the model runs. Register them with `useFrontendTool`. `parameters` is a [Standard Schema](https://standardschema.dev), so a `zod` schema (zod ≥ 3.24 implements Standard Schema) is the expected shape. `zod` is an optional peer dependency of `@copilotkit/react-native`, so add it to your app:

src/useComposeStage.ts
    
    
    import { useFrontendTool } from "@copilotkit/react-native/headless";
    import { z } from "zod";
    
    export function useComposeStage() {
      useFrontendTool({
        name: "composeStage",
        description: "Render POI panels on the screen.",
        agentId: "default", // scope the tool to one agent
        parameters: z.object({
          mode: z.enum(["home", "nearby", "hotels"]),
          panels: z.array(
            z.object({ title: z.string(), body: z.string().optional() }),
          ),
        }),
        handler: async (args) => {
          // Runs on the device. Push args into your own state/reducer here.
          return "rendered";
        },
      });
    }

Because the tool is registered on the device, the model's call reaches your `handler` on the client — the ideal place to drive a state reducer that your React Native views render declaratively (the agent sends _state_ , the client owns rendering). Discriminated-union / `oneOf` / `anyOf` param schemas are preserved through the runtime's schema conversion, so `z.discriminatedUnion(...)` params work. It's still good practice to normalize defensively in the handler — coerce a partially populated tool call into valid state rather than letting a malformed one render broken UI.

Choose the hook by who owns the tool, not by where the UI goes

Both hooks write to the **same** place: react-core's renderer registry, which the rendered React Native chat (`@copilotkit/react-native/components`) reads through `useRenderToolCall`. So inline chat UI is available from either — a `render` passed to `useFrontendTool` _is_ drawn there. What differs is whether a **tool** gets registered.

Use `useFrontendTool` for a tool your app owns: it advertises the tool to the model and runs your `handler` on the device. Pass `render` alongside the handler when you also want it drawn in the chat.
    
    
    import { useFrontendTool } from "@copilotkit/react-native/headless";
    
    useFrontendTool({
      name: "composeStage",
      description: "Render POI panels on the screen.",
      parameters: z.object({ mode: z.string() }),
      handler: async (args) => { /* drive your own state */ return "rendered"; },
      render: ({ args, status }) => (
        <StagePreview mode={args.mode} pending={status !== "complete"} />
      ),
    });

Use [`useRenderTool`](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool) when the tool is **not** yours — a server-side tool you only want to draw, or `name: "*"` as a fallback for every tool call with no renderer of its own. It registers no tool, takes no `description` and no `handler`, and exposes arguments as `parameters`:
    
    
    import { useRenderTool } from "@copilotkit/react-native/headless";
    
    useRenderTool(
      {
        name: "lookupPlaces",
        parameters: z.object({ mode: z.string() }),
        render: ({ parameters, status }) => (
          <StagePreview mode={parameters.mode} pending={status !== "complete"} />
        ),
      },
      [],
    );

`useRenderTool`'s `render` must return `ReactElement | null`, so returning `null` draws nothing. `useFrontendTool`'s `render` is a component type that also accepts a bare string, which typechecks and then throws inside a `FlatList` — return an element or `null` there too, and annotate the renderer with the opt-in [`FrontendToolRenderFunction<T>`](https://docs.copilotkit.ai/reference/react-native/hooks/useFrontendTool#the-render-type-react-native-needs) if you want the compiler to hold you to it.

On React Native before 1.68, `useRenderTool` was a _different_ , RN-local hook that registered a tool as well as a renderer. A call carrying `description` or `handler` no longer type-checks — rename it to `useFrontendTool`. [Migration notes](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool#migrating-from-the-old-react-native-userendertool).

`status` is `"inProgress"` / `"executing"` / `"complete"` in both hooks — typed as string literals in `useRenderTool`'s render props and as `ToolCallStatus` enum members in `useFrontendTool`'s. **You do not have to care which.** A string-enum member is assignable to its own literal type, so the string and the member compare interchangeably against either shape, and both forms narrow. `ToolCallStatus` is exported as a value from `/headless` if you prefer the members.

For agent-authored content whose length you can't predict, render it in a `ScrollView` with a `maxHeight` set to the available band — it sizes to content when short and scrolls when long, so it never hard-clips.

### Sending a turn and reading run state#

Running a user turn is the two-step the quickstart shows: `agent.addMessage(...)` then `copilotkit.runAgent({ agent })` (the runner lives on the core, not the agent). To cancel an in-flight run, call `copilotkit.stopAgent({ agent })`.

When another component needs only the run flag — a "thinking" indicator, say — subscribe with `useAgent` (a plain read that registers nothing) and read `agent.isRunning`. Call the tool-registering hook exactly **once** per agent so a tool isn't registered twice.

## Run lifecycle and UI#

A client-executed frontend tool renders its UI **mid-run** : the tool fires, your handler paints the screen, and the agent's run keeps going (further reasoning, a trailing summary). So `agent.isRunning` stays `true` past the moment the content is visible — the more so with a reasoning-tier model. Design run-gated UI around that gap:

  * Tie a loading overlay strictly to `isRunning` (render nothing when it's `false`) so an errored turn can't leave it stuck on. Keep always-available controls (a home or cancel button) above the overlay so they stay tappable while the run finishes.
  * If you gate a reveal animation, trigger it on the **falling edge** of `isRunning` (true → false) rather than on the content-arrived state change — otherwise the animation plays while the overlay is still up and the user never sees it.
  * Bound the run's tail with `maxSteps` on the agent so it doesn't linger longer than needed.



## Voice and speech-to-text#

`@copilotkit/voice` has **not** been adapted for React Native, so there's no drop-in voice hook. Voice is a bring-your-own-STT concern: capture a transcript with a React Native speech recognizer, then feed the final text through the same send-a-turn path (`agent.addMessage` \+ `copilotkit.runAgent`).

Don't assume a platform speech recognizer exists

Recognizers that wrap the OS speech service (iOS `SFSpeechRecognizer` / Android `SpeechRecognizer`) can be **absent** on de-Googled or automotive hardware, where the call throws rather than degrading. If you target that kind of device, guard the unavailable case and fall back to text input, or embed an on-device recognizer (e.g. Vosk) as a guaranteed floor. Always give voice a deterministic **Send** control rather than relying on silence detection to end a turn.

## Proving it works#

On the web you prove an integration by opening a browser and watching the tool UI paint. There is no browser here, so that step does not translate — and the substitutes each prove less than they appear to. Three checks together cover it; none of them is sufficient alone.

### 1\. The runtime is reachable and its agent answers#
    
    
    npx copilotkit verify --round-trip

This sends one request through the runtime and reads the answer back off the thread, so it separates an agent that is _configured_ from an agent that _works_ — with no browser and no device involved. Run it from the machine hosting the runtime, not from the device. The CLI probes `http://localhost:3000/api/copilotkit` by default, so pass `--runtime-url http://localhost:8200/api/copilotkit` for the runtime this guide sets up, and `--agent <id>` if the runtime declares more than one.

What --round-trip does not prove

It proves an answer came back — never what the answer said, and never _which_ deployment answered. See [what `--round-trip` does not prove](https://docs.copilotkit.ai/cli#verify-your-setup) for the full boundary. So this is step one of three, not a green light.

### 2\. The tool UI actually renders on the device#

Boot an emulator, drive the app, and capture the screen. On Android:
    
    
    adb devices                                   # confirm one booted target
    adb exec-out screencap -p > proof.png         # capture the rendered screen
    adb logcat -d -s ReactNativeJS:E              # no unresolved redbox

`adb reverse tcp:8200 tcp:8200` first if you are on a USB device, so `localhost` on the device reaches your runtime — see Connecting from a device or bench.

There is no iOS equivalent of `adb` for this. `xcrun simctl io booted screenshot proof.png` is the closest, and it needs full Xcode — the Command Line Tools alone do not ship `simctl`. If your environment has no emulator at all, say so rather than substituting a browser: a web screenshot proves a different application.

### 3\. The answer is about your data#

The check that catches what the first two cannot. A tool-rendered card over records your app does not hold looks _identical_ to a correct one — in a screenshot, in a video, and to anyone unfamiliar with your data.

So read the records your app actually holds, and confirm the answer names those and no others. If it names something else, the failure is upstream of the UI: the context was never registered (see the callout under Which hooks are shared, and which aren't), the agent's instructions ignore it, or the screen loaded its data after the context was registered.

## Known limitations#

  * **Markdown in a custom UI** — the rendered chat on `@copilotkit/react-native/components` renders markdown for you (via `CopilotMarkdown`, backed by `react-native-streamdown`). If you build your own UI, a plain `Text` shows markdown as-is — reuse `CopilotMarkdown` or bring your own renderer.
  * **Inspector** — the [Inspector](https://docs.copilotkit.ai/inspector#where-inspector-runs) is a browser overlay that mounts a custom element into the DOM, so it has no React Native surface and `@copilotkit/react-native` does not ship it. The three checks under Proving it works cover what it would have shown you.
  * **Voice** — `@copilotkit/voice` has not been adapted for React Native; wire your own STT as above.
  * **`threadId` on `useAgent`** — not supported yet ([#6141](https://github.com/CopilotKit/CopilotKit/pull/6141)). Thread scoping comes from a chat-configuration provider; a `threadId` passed to `useAgent` does not typecheck and is ignored.
  * **Cloud provider props** — `publicApiKey` / `licenseToken` are not supported on the React Native provider; connect via `runtimeUrl`.
  * **Web-only rendering hooks** — `useDefaultRenderTool`, `useRenderCustomMessages`, and `useRenderActivityMessage` are not exported, because they render host DOM or link the web chat-message stack. `useRenderToolCall` **is** exported; use it to draw a registered tool call outside the chat.



## Next steps#

  * **Model selection:** provider strings, keys, and custom endpoints in [Model Selection](https://docs.copilotkit.ai/model-selection)
  * **Copilot Runtime:** hosting and configuring the server in [Copilot Runtime](https://docs.copilotkit.ai/backend/copilot-runtime)
  * **Agents:** what the built-in agent supports in [Build with agents](https://docs.copilotkit.ai/build-with-agents)


