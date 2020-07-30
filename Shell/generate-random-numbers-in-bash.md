# Generate random numbers in bash
<!-- July 29 2020 -->
Easiest way is to use the `$RANDOM` variable.

```bash
>> echo "$RANDOM"
12261
```

Each time this parameter is referenced, a random integer between **0** and **32767** is generated.

A better way which I like is to use the GNU coreutil, `shuf`

One Random number between 69 & 420
```bash
shuf -i69-420 -n1
```

Five Random numbers between 69 & 420
```bash
shuf -i69-420 -n5
```