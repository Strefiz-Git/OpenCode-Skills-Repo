# Prior art

| Project | Idea worth studying |
|---|---|
| Folia | Regionised multithreading: independent regions tick on their own threads. |
| C2ME | Concurrent chunk IO, loading and generation. |
| Lithium | Algorithmic optimisations that keep vanilla behaviour. |
| VMP | Parallel entity/chunk work for Velocity-style setups. |
| Moonrise | Chunk system rewrite and threading model used by modern forks. |

Read their docs and issue trackers for the failure modes (deadlocks, desyncs, mod incompatibility) before designing your own.
