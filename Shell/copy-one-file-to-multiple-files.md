# Copy one file to multiple files in Bash
**_Posted on 24 Dec, 2019_**

```bash
for f in file{1..10}.py; do cp main.py $f; done
```
> this will create new files file_1.py, file_2.py etc and copy contents of _main.py_ file to all of them.