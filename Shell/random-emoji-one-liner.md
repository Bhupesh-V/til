# Random emoji 😲 in one line
<!-- 30 July 2020 -->

```bash
printf "%b\n" "\U1F$(shuf -i600-700 -n1)"
```

> PS: I am still working on a better way, this will only generate emojis in UNICODE range `1F601` to `1F700` while ignoring codepoints like `1F60A` 😊. Let me know if you have a beter way (create an issue)
