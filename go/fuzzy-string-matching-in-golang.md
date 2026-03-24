# Getting close string matches in Go

A while back I got to know about [`get_close_matches`](https://docs.python.org/3.8/library/difflib.html#difflib.get_close_matches) in Python's `difflib` that works like a fuzzy string match. It returns a list of the best "good enough" close string matches from a list of words.

```python
>>> from difflib import get_close_matches                                  
>>> fruits = ["apple", "orange", "banana", "peach"]                        
>>> get_close_matches('app', fruits)                                       
['apple']                                                                  
>>> get_close_matches('aple', fruits)                                      
['apple']                                                                  
```

This sparked my curiosity to hunt a similar method in Go. Unfortunately there is no direct alternative to this in Go but I was able to put together 2 different ways to do so, let's have a look at them

## The `strings.Index()` approach

Go standard library `strings` offers various method to manipulate strings, once such method is `Index()` which returns the first index of a sub-string match.

```go
func SubstringSearchSimple() {

	words := []string{"bhupesh", "varshney", "golang"}
	var first_index int
	lookup_word := "bhu"

	for index := range words {
		first_index = strings.Index(words[index], lookup_word)
		if first_index != -1 {
			break
		}
	}
	fmt.Println(words[first_index])
}
```

## The `suffixarray` approach`

The [`suffixarray`](https://pkg.go.dev/index/suffixarray#pkg-overview) package provides substring search in logarithmic time by building an index over available data.

### What's a suffixarray anyways?

A suffix array is a sorted array of all suffixes of a string.

```go
func SubstringSearchSuffixArray() {

	words := []byte("bhupesh varshney golang")

	// Create a new suffixarray index.
	index := suffixarray.New(words)

	// Find exactly 1 instance of this byte slice in the source slice.
	lookup_word := index.Lookup([]byte("bhu"), 1)
	data := string(words[lookup_word[0]:])

	fmt.Println(strings.Split(data, " ")[0])
}
```

## So what's the best/fast way?

I did some rudimentary benchmarking, and it turns out that the suffixarray approach is probably the fastest way to do fuzzy string match in Go. But in comes with a unnecessary overhead over serialising your data in `byte` form, If that's a problem for you, go with the standard strings approach.


## Resources

Some of the stuff I read while writing this blog post

- [Why is []byte used as a string type?](https://www.reddit.com/r/golang/comments/4ologg/why_is_byte_used_as_a_string_type/)
- [Demystifying Bytes, Runes, and Strings in Go](https://levelup.gitconnected.com/demystifying-bytes-runes-and-strings-in-go-1f94df215615)
- [Suffix arrays in the Go standard library](https://eli.thegreenplace.net/2016/suffix-arrays-in-the-go-standard-library/)
