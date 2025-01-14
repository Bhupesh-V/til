# Mega List of Tips for Writing Performant Go Code

**_Posted on 13 Jan, 2024_**

1. For variable with short lived scope, use non-pointer return value. For variable with long lived scope, use pointer return value. Heap allocation is expensive.
2. Use `sync.Pool` for frequently allocated and released objects. Buffer pool is a good example.
3. Use `strings.Builder` in favor of `bytes.Buffer` for string operations.
4. Pre-allcate memory for slices, maps if possible (when using `make()`).
