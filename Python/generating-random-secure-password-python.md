# Generate random secure password using python
**_Posted on 23 Mar, 2021_** 

```python
>>> import string, random
>>> print("".join([random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(random.randint(12,15))])
)
X6[!:p0yTZ^+
```

[Credits](https://twitter.com/AkopKesheshyan/status/1371050204762411008?s=20)


''.join(random.choice(string.ascii_lowercase) for _ in range(260))
