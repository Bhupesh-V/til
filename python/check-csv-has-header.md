# Check if csv has header in python


Consider the following csv data

```csv
id, name, editor
1, Bhupesh, NeoVim
2, Mark, VSCode
3, Jennifer, JetBrains
```

```csv
1, Banana, 34
2, Apples, 5
3, Orange, 33
4, Mango, 12
```

The [`csv.Sniffer`](https://docs.python.org/3/library/csv.html#csv.Sniffer) class provides a method called `has_header` which return `True` if the first row appears to be a header

```python
import csv

csv_with_header = """
id, name, editor
1, Bhupesh, NeoVim
2, Mark, VSCode
3, Jennifer, JetBrains
"""

csv_without_header = """
1, Banana, 34
2, Apples, 5
3, Orange, 33
4, Mango, 12
"""

def has_header(file): 
        with open(file, 'r') as csvfile: 
        sniffer = csv.Sniffer()
        return sniffer.has_header(csvfile.read())


print(has_header('csv_with_header.csv'))
# true
print(has_header('csv_without_header.csv'))
# false
```

