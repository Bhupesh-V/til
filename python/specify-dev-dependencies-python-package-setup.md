# Specify dev dependencies in setup.py
<!--21 jul 2020 -->
```python
# setup.py
...

extras_require = {
    "dev": [
        "pytest>=3.7",
    ],
}
```

Test it locally

```bash
pip install -e .[dev]
```
