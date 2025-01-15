# Dividing Time deltas in python - Difference b/w 2 datetime values
**_Posted on 23 Mar, 2021_** 

In Python 3 you can divide two time-deltas:

```python
>>> from datetime import timedelta
>>> td = timedelta(seconds=91800)
>>> td / timedelta(hours=1)
25.5
>>> td / timedelta(seconds=3600)
25.5
>>>
```
