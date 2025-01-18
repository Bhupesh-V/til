# Get total download stats from GitHub & Homebrew



## Get 365 download stats from homebrew

```bash
curl -sq https://formulae.brew.sh/api/formula/ugit.json | jq '.analytics.install_on_request."365d".ugit'
```

## Get all download count from github api

```bash
(curl -sq https://api.github.com/repos/Bhupesh-V/ugit/releases | jq .[].assets[0].download_count | tr "\012" "+" ; echo "0") | bc
```


## Combining both results

```bash
(curl -sq https://formulae.brew.sh/api/formula/ugit.json | jq '.analytics.install_on_request."365d".ugit' | tr "\012" "+" && (curl -sq https://api.github.com/repos/Bhupesh-V/ugit/releases | jq .[].assets[0].download_count | tr "\012" "+" ; echo "0")) | bc
```
