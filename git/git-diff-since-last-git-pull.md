# View git diff since the last git pull
**_Posted on 25 Dec, 2021_**

```bash
git pull origin
git diff @{1}..
```

`@{n}` means the n-th previous value of `HEAD`
