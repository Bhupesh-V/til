# View git diff since the last git pull


```bash
git pull origin
git diff @{1}..
```

`@{n}` means the n-th previous value of `HEAD`
