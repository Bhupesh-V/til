# Writing Unit Tests in Python ✅
<!--27 Jun 2019 -->
1. Simple and easy just import the Python 3 built-in library `unittest`.
2. Wrap up tests in a Class.
3. Use assert methods.

```python
import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()

```

### Resources
- [Getting Started With Testing in Python](https://realpython.com/python-testing/)
- [unittest — Unit testing framework](https://docs.python.org/3.6/library/unittest.html)