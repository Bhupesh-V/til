# Using defaultdict to handle key not in dict
**_Posted on 02 Sep, 2021_**

We can use `defauldict` to eliminate the use of an if condition when looking up keys

```python
from collections import defaultdict

users = [
    {"username": "Jenna", "language": "English"},
    {"username": "Michael", "language": "French"},
    {"username": "Gustavo", "language": "Spanish"},
    {"username": "Bhupesh", "language": "English"},
]

# normal approach
users_by_language = {}

for user in users:
    if user["language"] not in users_by_language:
        users_by_language[user["language"]] = []
    users_by_language[user["language"]].append(user)

print(users_by_language)


# defaultdict approach
users_by_language = defaultdict(list)

for user in users:
    users_by_language[user["language"]].append(user)

print(dict(users_by_language))
```


[Credits](https://twitter.com/testdrivenio/status/1433101094654152704?s=20)
