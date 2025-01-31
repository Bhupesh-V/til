# Writing benchmarks for Go apps

**_Posted on 13 Jan, 2024_**

## Pre-requisites

Install the `perf` utility tools that help in analyzing the benchmarks.

```
go install golang.org/x/perf/cmd/...@latest
```

## Run benchmarks

> Close all other applications including browsers & background apps like docker to get accurate results.

Run benchmarks

```
go test -bench=BenchmarkMyFunction -benchmem -count=10 | tee old_benchmark.txt
```

Change the implementation and run the benchmarks again

```
go test -bench=BenchmarkMyFunction -benchmem -count=10 | tee new_benchmark.txt
```

Compare the benchmarks

```
benchstat old_benchmark.txt new_benchmark.txt
```

## Writing benchmarks

## Resources

- https://dave.cheney.net/high-performance-go-workshop/sydney-2019.html#comparing_benchmarks_with_benchstat