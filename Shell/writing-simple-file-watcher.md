# Writing a simple file watcher using GNU Utils
**_Posted on 13 Dec, 2021_**

This simple file change watching script requires these two key utilities:

1. `gdate`
2. `gstat`

```bash
#!/usr/bin/env bash

set -eo pipefail
IFS=$'\n\t'

cleanup() {
    # perform any post script completion tasks
    printf "\n%s" "Cleanup Tasks ..."
    exit
}

perform_task() {
    # do stuff
    printf "\n%s" "Performing Task ($(date +%I:%M:%S)) ..."
}

trap "cleanup" SIGINT

watch_changes() {
    echo -en "\rWatching file $(tput bold)$1$(tput sgr0) ...\n"
    while true; do
        past_modify_time=$(gdate -d "@$(gstat -c '%Y' "$1")" '+%T')
        # sleep for 100 milliseconds
        sleep 0.1
        new_modify_time=$(gdate -d "@$(gstat -c '%Y' "$1")" '+%T')

        [[ "$past_modify_time" != "$new_modify_time" ]] && perform_task
    done
}

if [[ -z "$1" ]]; then
    echo -e "requires a file as an argument"
    exit 1
else
    watch_changes "$1"
fi
```