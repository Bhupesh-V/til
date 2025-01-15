# Check indentation errors in python 🐍
**_Posted on 18 Oct 2020_**

Use `tabnanny` in python standard library for this.

```bash
python -m tabnanny hack-nasa.py
```

another way is to check if the files successfully compliles or not

```
python3 -m py_compile hack-nasa.py
# or
python3 -c 'import py_compile; py_compile.compile("path/to/file")'
```

> Read more about [`py_compile`](https://docs.python.org/3/library/py_compile.html)
