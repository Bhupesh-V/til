# Get Total System Memory using `vmstat` command
<!-- 31 May 2020 -->
```bash
vmstat -s | grep "total memory" | grep -Eo '[0-9]{1,}'
```

This will print the total memory (your RAM) in highlighted text.

The command `vmstat -s` is usually used to print memory statistics a sample output might look like

```bash
   1882140 K total memory
    644068 K used memory
    861172 K active memory
    653200 K inactive memory
    217160 K free memory
     55140 K buffer memory
    965772 K swap cache
   2097148 K total swap
    230400 K used swap
   1866748 K free swap
    169316 non-nice user cpu ticks
      4939 nice user cpu ticks
     37944 system cpu ticks
    666678 idle cpu ticks
     53315 IO-wait cpu ticks
         0 IRQ cpu ticks
       693 softirq cpu ticks
         0 stolen cpu ticks
   2554778 pages paged in
   1429680 pages paged out
     40722 pages swapped in
    191481 pages swapped out
   3487312 interrupts
  10042547 CPU context switches
1590932382 boot time
      9975 forks
```
