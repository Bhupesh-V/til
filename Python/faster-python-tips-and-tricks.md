# Fastest Python First: Tips and Tricks 🏃
<!--27 Jun 2019 -->
Here are some tips that I learned to make Python Programs faster (_WIP_).

1. Always compile regular expression, if you have to match patterns a lot of times.

```python
import re

pattern = re.compile(some_regular_expression)
some_text = re.sub(pattern, '', data)

```

2. Use List comprehension for iterating over a list.

```python
import time

itemlist = [23, 45, 56, 67, 1, 100, 340, 90]
""" Normal Iteration """
start_time = time.time()
for item in itemlist:
	if item % 2 == 0:
		print(item)
end_time = time.time()

print("Without List Comprehension : " + str(end_time - start_time))

""" List Comprehension """
start_time = time.time()
[print(item) for item in itemlist if item % 2 == 0]
end_time = time.time()

print("With List Comprehension : " + str(end_time - start_time))
```

Output : 
```bash
56
100
340
90
Without List Comprehension : 0.0002067089080810547
56
100
340
90
With List Comprehension : 0.00019121170043945312
```