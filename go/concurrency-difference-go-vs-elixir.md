# Concurrency Comparison: Go v/s Elixir




## Goroutines = [CSP Process](https://en.wikipedia.org/wiki/Communicating_sequential_processes)

- One goroutine only knows about channels, its not aware about other goroutines.
- There are anonymous
- Message passing is synchronous.
- Go routines are managed by Go runtime.
- Avg size in order on 2KB.

### Example

```go
go someFunction()
```

## Elixir Process = [Actor Model](https://www.brianstorti.com/the-actor-model/)

- Processes communicate directly to each other
- Elixir process has an id (non-anonymous).
- Managed by BEAM Virtual Machine.
- Separate stack & heap.
- Average size of 0.5KB.

### Example

```elixir
spawn(fn -> ... end)
```

## Resources

- [Anna Neyzberg & Hannah Howard - Go vs Elixir: A concurrency comparison | Code BEAM SF 19](https://www.youtube.com/watch?v=SbRvX1CQ9ic)
- [Discussion on r/elixir about Go v/s Elixir](https://www.reddit.com/r/elixir/comments/kx4pyr/i_need_some_help_fully_understanding_the/)
- [The Soul of Erlang and Elixir • Sasa Juric • GOTO 2019](https://www.youtube.com/watch?v=JvBT4XBdoUE) - MUST WATCH!
- [](https://www.cloudbees.com/blog/comparing-elixir-go)
