# Get System info using Shell Commands
<!-- 19 July 2020 -->

### Memory Used/Total

```shell
free -h | awk '/^Mem:/ {print $3 "/" $2}'
```

### Show CPU temperature

```shell
sensors | awk '/^Core*/ {print $1$2, $3}'
```

### Most Memory Intensive processes

```shell
ps axch -o cmd:15,%mem --sort=-%mem | head
```

### Most CPU Intensive processes

```shell
ps axch -o cmd:15,%cpu --sort=-%cpu | head
```

I [wrote a small shell script](https://github.com/Bhupesh-V/.Varshney/blob/master/scripts/sys.sh) to get _(almost)_ realtime update of your system.