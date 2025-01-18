# Easy & Lazy way to flatten a python list


```python
from itertools import chain
myList = [["bhupesh", 1], ["amanda", 2], ["robin", 3]]

print(list(chain.from_iterable(myList)))
# ['bhupesh', 1, 'amanda', 2, 'robin', 3]
```

`itertools.chain.from_iterable` would work lazily, i.e no work done unless you loop over the returned iterator

