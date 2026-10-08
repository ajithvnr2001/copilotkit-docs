---
url: https://docs.copilotkit.ai/reference/channels/types/StateStore/
title: StateStore
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:23.791518+00:00
---

# StateStore

> Source: https://docs.copilotkit.ai/reference/channels/types/StateStore/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁ChannelsSDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Components

[Actions](https://docs.copilotkit.ai/reference/channels/components/Actions)[Button](https://docs.copilotkit.ai/reference/channels/components/Button)[Chart](https://docs.copilotkit.ai/reference/channels/components/Chart)[Context](https://docs.copilotkit.ai/reference/channels/components/Context)[Divider](https://docs.copilotkit.ai/reference/channels/components/Divider)[Fields and Field](https://docs.copilotkit.ai/reference/channels/components/Fields)[Header](https://docs.copilotkit.ai/reference/channels/components/Header)[Image](https://docs.copilotkit.ai/reference/channels/components/Image)[Input](https://docs.copilotkit.ai/reference/channels/components/Input)[Markdown](https://docs.copilotkit.ai/reference/channels/components/Markdown)[Message](https://docs.copilotkit.ai/reference/channels/components/Message)[Modal](https://docs.copilotkit.ai/reference/channels/components/Modal)[Section](https://docs.copilotkit.ai/reference/channels/components/Section)[Select](https://docs.copilotkit.ai/reference/channels/components/Select)[Table, Row, and Cell](https://docs.copilotkit.ai/reference/channels/components/Table)

Functions

[bind](https://docs.copilotkit.ai/reference/channels/functions/bind)[createChannel](https://docs.copilotkit.ai/reference/channels/functions/createChannel)[defineChannelCommand](https://docs.copilotkit.ai/reference/channels/functions/defineChannelCommand)[defineChannelTool](https://docs.copilotkit.ai/reference/channels/functions/defineChannelTool)[renderToIR](https://docs.copilotkit.ai/reference/channels/functions/renderToIR)

Classes

[Channel](https://docs.copilotkit.ai/reference/channels/classes/Channel)[MemoryStore](https://docs.copilotkit.ai/reference/channels/classes/MemoryStore)[Thread](https://docs.copilotkit.ai/reference/channels/classes/Thread)[Transcripts](https://docs.copilotkit.ai/reference/channels/classes/Transcripts)

Types

[ActionStore](https://docs.copilotkit.ai/reference/channels/types/ActionStore)[AgentContentPart](https://docs.copilotkit.ai/reference/channels/types/AgentContentPart)[ChannelNode](https://docs.copilotkit.ai/reference/channels/types/ChannelNode)[IncomingMessage](https://docs.copilotkit.ai/reference/channels/types/IncomingMessage)[InteractionContext](https://docs.copilotkit.ai/reference/channels/types/InteractionContext)[JSX callbacks](https://docs.copilotkit.ai/reference/channels/types/JSXCallbacks)[MessageRef](https://docs.copilotkit.ai/reference/channels/types/MessageRef)[StateStore](https://docs.copilotkit.ai/reference/channels/types/StateStore)[StoreConfig](https://docs.copilotkit.ai/reference/channels/types/StoreConfig)

SDKs

[Direct provider adapters](https://docs.copilotkit.ai/reference/channels/sdk/direct-adapters)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[channels](https://docs.copilotkit.ai/reference/channels)Types

# StateStore

The pluggable persistence contract for Channel state, callbacks, transcripts, locks, deduplication, and queues.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

`StateStore` is the asynchronous persistence boundary used by the Channels runtime.

## Interface
    
    
    interface StateStore {
      kv: {
        get<T>(key: string): Promise<T | undefined>;
        set<T>(key: string, value: T, ttlMs?: number): Promise<void>;
        consume<T>(key: string): Promise<T | undefined>;
        delete(key: string): Promise<void>;
      };
      list: {
        append<T>(
          key: string,
          value: T,
          options?: { maxLen?: number; ttlMs?: number },
        ): Promise<number>;
        range<T>(key: string, start?: number, stop?: number): Promise<T[]>;
        trim(key: string, maxLen: number): Promise<void>;
        delete(key: string): Promise<void>;
      };
      lock: {
        acquire(
          key: string,
          options?: { ttlMs?: number },
        ): Promise<{ token: string } | null>;
        release(key: string, token: string): Promise<void>;
      };
      dedup: {
        seen(key: string, ttlMs: number): Promise<boolean>;
      };
      queue: {
        enqueue<T>(
          key: string,
          value: T,
          options?: {
            maxSize?: number;
            onFull?: "drop-oldest" | "drop-newest";
          },
        ): Promise<number>;
        dequeue<T>(key: string): Promise<T | undefined>;
        depth(key: string): Promise<number>;
      };
    }

## Semantics

  * `list.range` is oldest-first and uses non-negative, inclusive indices.
  * `kv.consume` atomically returns and deletes one value. Concurrent callers must observe at most one non-`undefined` result.
  * `list.append({ ttlMs })` sets the expiry for the whole list. An append without `ttlMs` preserves an existing expiry.
  * `lock.acquire` returns `null` while another token holds an unexpired lock.
  * `lock.release` must not release a lock owned by another or newer token.
  * `dedup.seen` returns `false` for the first observation and `true` for a repeat inside the TTL.
  * Queues are FIFO. The configured overflow policy must be deterministic.



Remote stores must support JSON-serializable values. `MemoryStore` preserves objects by reference, but that behavior is not portable.

## Conformance test
    
    
    import { runStateStoreConformance } from "@copilotkit/channels/testing";
    
    runStateStoreConformance("postgres", () => createPostgresStateStore());

KV consumption, locks, deduplication, and queues must be atomic across processes. Use project/Channel namespacing to prevent key collisions.

Pass the adapter through `createChannel({ store: { adapter } })`. See [Persistence and scaling](https://docs.copilotkit.ai/slack/persistence-and-scaling).
