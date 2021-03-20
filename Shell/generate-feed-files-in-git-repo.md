# Generate a RSS Feed of recent files inside a Git repository
**_Posted on 16 Mar, 2021_**

I like to log my notes & [TILs](https://github.com/Bhupesh-V/til) in a git repository and recently I had an idea to showcase (& automate) my most recent learnings on my [github profile](https://github.com/Bhupesh-V/#recent-works).

Github is nice enough to provide us with RSS feeds for the latest commits inside a repo but it lacks the most basic thing of telling me what commit introduced a new file (i.e recent files in a repo).

The following command will show each new relative path that was added to the git history along with the commit date (sorted by most recent).

```bash
git log --no-color --date=format:'%d %b, %Y' --diff-filter=A --name-status --pretty='%ad'
```

If you just want the file names, leave the `--pretty` option empty

```bash
git log --no-color --date=format:'%d %b, %Y' --diff-filter=A --name-status --pretty=''
```

You should see something like this

```
 A   scripts/oib
 A   scripts/surf
 A   snippets/python.snippets
 A   snippets/markdown.snippets
 A   .Xmodmap
 A   codesnippets/go.md
 A   scripts/areyouok.go
 A   scripts/convert-to-gif.sh
 A   scripts/backup_as_gist.py
 ...
```

To generate recent N results use the `-n` flag

```bash
git log --no-color -n 5 --date=format:'%d %b, %Y' --diff-filter=A --name-status --pretty=''
```

If you want to follow renames as well,

```bash
git log --no-color --date=format:'%d %b, %Y' --diff-filter=AR --name-status --pretty=''
```

The magic here is done by the [`--diff-filter=A`](https://www.git-scm.com/docs/git-log#Documentation/git-log.txt---diff-filterACDMRTUXB82308203) option that only shows files that were **A**dded. I remember using this to find [birthday of README files](https://bhupesh-v.github.io/git-cake-when-is-my-readme-birthday/).

> NOTE: We are assuming that the file creation date to be the _date of the commit that introduced the file_ and since its a Feed for a git repo, this should make sense (I was born when I was committed 😁️)

Here is a python [script to generate a valid RSS feed](https://github.com/Bhupesh-V/.Varshney/blob/master/scripts/git-feed)


```python
#!/usr/bin/env python3

# Script to generate a feed of recently committed files in a git repository

# TODO: Add Commit Author #

import subprocess as sp
import pathlib
import re, os
import datetime
from dateutil.parser import parse

HEAD = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
"""

FOOTER = """</channel>
</rss>
"""

# Assuming your current working dir is the repo
repo_name = os.path.basename(os.getcwd())
current_date = datetime.datetime.now().strftime("%a, %d %b %Y")


def get_recent_files():
    cmd = "git log --no-color -n 10 --date=rfc --diff-filter=A --name-status --pretty='%ad'"
    result = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = result.communicate()
    clean_output = out.decode("utf-8").replace("A\t", "").split("\n")
    clean_output = list(filter(lambda x: x != "", clean_output))

    files = []
    for item in clean_output:
        if is_valid(item):
            date = item
        elif pathlib.Path(item).exists():
            entry = item, date
            files.append(entry)
    return files


def is_valid(date):
    try:
        if isinstance(parse(date), datetime.datetime):
            return True
    except ValueError:
        return False


def get_repo_link():
    repo_origin = "git config --get remote.origin.url"
    result = sp.Popen(repo_origin, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    result, err = result.communicate()
    return result.decode("utf-8")


if __name__ == "__main__":
    files = get_recent_files()
    with open("feed.xml", "w") as feed:
        feed.write(HEAD)
        feed.write(
            f"""<title>{repo_name}.git</title>\n<link>{get_repo_link()}</link>\n"""
        )
        feed.write(
            f"""<description>Recently committed files in {repo_name}</description>\n"""
        )
        feed.write(f"""<lastBuildDate>{current_date}</lastBuildDate>""")
        for item in files:
            feed.write("""<item>\n""")
            feed.write(f"""<title>{item[0]}</title>\n""")
            feed.write(f"""<pubDate>{item[1]}</pubDate>\n""")
            feed.write("""</item>\n""")
        feed.write(FOOTER)
```

The XML generated is valid enough to be consumed without any issue. Here is a [demo](https://github.com/Bhupesh-V/til/blob/master/feed.xml) of output from the above script.

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
<title>til.git</title>
<link>https://github.com/Bhupesh-V/til
</link>
<description>Recently committed files in til</description>
<lastBuildDate>Wed, 17 Mar 2021</lastBuildDate><item>
<title>Shell/generate-feed-for-files-in-git-repo.md</title>
<pubDate>Tue, 16 Mar 2021 16:24:47 +0530</pubDate>
</item>
<item>
<title>recent_tils.json</title>
<pubDate>Tue, 16 Mar 2021 16:24:47 +0530</pubDate>
</item>
<item>
<title>Shell/parsing-git-status-for-tracked-untracked-changes.md</title>
<pubDate>Mon, 15 Mar 2021 19:26:12 +0530</pubDate>
</item>
<item>
<title>Shell/get-current-git-branch-name.md</title>
<pubDate>Sat, 13 Mar 2021 13:11:02 +0530</pubDate>
</item>
<item>
<title>Miscellaneous/chaos-engineering-collected-notes.md</title>
<pubDate>Sun, 7 Mar 2021 19:42:28 +0530</pubDate>
</item>
<item>
</channel>
</rss>
```
