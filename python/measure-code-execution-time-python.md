# Measure code execution time using timer


```python
from timeit import default_timer
from functools import wraps
import time


def timer(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        response = f(*args, **kwargs)
        total_elapsed_time = default_timer() - start_time
        print(f"Elapsed Time: {total_elapsed_time}")
        return response
    return wrapper


@timer
def hello():
    time.sleep(2)
    print("Hello!!")

hello()
```

Sample Output

```
Hello!!
Elapsed Time: 2.0024633289999656
```
