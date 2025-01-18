# Mega List of Tips for Writing Performant Go Code

## Stack vs Heap Allocations

For variable with short lived scope, use non-pointer return value. For variable with long lived scope, use pointer return value. Heap allocation is expensive.

**Benchmark**: https://github.com/Bhupesh-V/pocs/tree/main/go/heap-escape

## Buffer Pools

Use `sync.Pool` for frequently allocated and released objects. Buffer pool is a good example.

**Benchmark**: https://github.com/Bhupesh-V/pocs/tree/main/go/buffer-pool

## Working with strings

Use `strings.Builder` in favor of `bytes.Buffer` for string operations.

## Capping slice length

Pre-allcate memory for slices, maps if possible (when using `make()`).

## Field Alignment in Structs

- https://go.dev/play/p/dNWspo2Dxv
- https://go.dev/play/p/0qsgpuAHHp
- https://itnext.io/structure-size-optimization-in-golang-alignment-padding-more-effective-memory-layout-linters-fffdcba27c61
- https://go101.org/article/memory-layout.html