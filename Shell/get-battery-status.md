# Check battery status
**_Posted on 11 Sep, 2021_**

### Linux

```
upower -i /org/freedesktop/UPower/devices/battery_BAT0 | awk '/percentage/ {print $2}'
```

