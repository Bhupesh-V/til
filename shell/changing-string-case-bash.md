# Changing string case in bash


In newer versions of bash (>=4), changing string case is very intuitive.

```bash
x="baSh"
echo $x # baSh

echo ${x,,} # bash

echo ${x^^} # BASH

```
