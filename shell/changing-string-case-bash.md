# Changing string case in bash
**_Posted on 10 Aug, 2021_**

In newer versions of bash (>=4), changing string case is very intuitive.

```bash
x="baSh"
echo $x # baSh

echo ${x,,} # bash

echo ${x^^} # BASH

```
