# Find boot-up time in linux 🐧
<!-- 18 Oct 2020 -->
We can achieve this using the `systemd` service. Just run this

```bash
systemd-analyze
```

Demo:

```bash
Startup finished in 36.655s (kernel) + 58.030s (userspace) = 1min 34.685s
graphical.target reached after 57.709s in userspace
```

> The `graphical.target` specifies how long it took to reach to the _log-in_ screen.

## Other tricks

1. You can also plot service initializations in a SVG graph.
```bash
systemd-analyze plot > demo.svg
```

2. Check which service takes most of the time.
```bash
systemd-analyze blame
```