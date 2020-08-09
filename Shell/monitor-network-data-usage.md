# Monitor network (data) usage

The amount of data sent(uploaded) & received (downloaded) can be found out
using the following bash script.

- Only works per session, i.e stats are gathered once you power up your PC (or login).
- Good to have if you have limited data avaiability & want to montior your data usage.

```bash

netu() {
    # [net]work [u]sage: check network usage stats

    net_device=$(route | awk '/default/ {print $8}')
    TRANSMITTED=$(ifconfig "$net_device" | awk '/TX packets/ {print $6$7}')
    RECEIVED=$(ifconfig "$net_device" | awk '/RX packets/ {print $6$7}')

    pc_uptime=$(uptime -p | awk '{for (i=2; i<NF; i++) printf $i " "; if (NF >= 1) print $NF; }')
    printf "%s\n\n" "Network Usage since $pc_uptime"
    printf "%s\n" "$(tput bold)🔼 TRANSMITTED $(tput sgr0): $TRANSMITTED"
    printf "%s\n" "$(tput bold)🔽 RECEIVED    $(tput sgr0): $RECEIVED"
}

```

### Demo
![netu](https://user-images.githubusercontent.com/34342551/89729900-9d0b6100-da57-11ea-8497-233b64e42dc6.png)


[Grab it from here](https://github.com/Bhupesh-V/.Varshney/blob/316cde84f3a666cf3f503a2de34e8289074ffbce/.bash_functions#L69)