#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Simple script to auto-generate the README.md file for a TIL project.
"""
import os
import json
import itertools
import urllib.parse
import subprocess as sp
import pathlib

HEADER = """
<h1 align="left">Today I Learned</h1>
<p align="center">
  <img alt="TILs Count" src="https://img.shields.io/badge/dynamic/json.svg?color=black&label=TILs&query=count&url=https%3A%2F%2Fraw.githubusercontent.com%2FBhupesh-V%2Ftil%2Fmaster%2Fcount.json">
  <img alt="last commit" src="https://img.shields.io/github/last-commit/bhupesh-V/TIL?color=purple">
  <a href="https://github.com/Bhupesh-V/til/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/github/license/Bhupesh-V/til" target="_blank" />
  </a>
  <a href="https://bhupesh.gitbook.io">
    <img alt="Website" src="https://img.shields.io/website?url=https%3A%2F%2Fbhupesh.gitbook.io">
  </a>
  <a href="https://paypal.me/BhupeshVarshney">
    <img alt="PayPal-Bhupesh Varshney" src="https://camo.githubusercontent.com/4a35ad533ec57bf3c47c44dad7b9bd41c83a5fc132497acb2787973a2ae2feeb/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646f6e6174652d50617950616c2d3130343039382e7376673f6c6f676f3d50617950616c" target="_blank" />
  </a>
  <a href="https://twitter.com/bhupeshimself">
    <img alt="Twitter: Bhupesh Varshney" src="https://img.shields.io/twitter/follow/bhupeshimself.svg?style=social" target="_blank" />
  </a>
</p>

> Personal Wiki of Interesting things I learn every day at the intersection of software development, computer science & stuff.


"""

FOOTER = """## Usage

See [USAGE.md](https://github.com/Bhupesh-V/til/blob/master/USAGE.md) to know how I use this repository.

## Author [![bhupesh-twitter-image](https://kutt.it/bhupeshimself)](https://twitter.com/bhupeshimself)

👤 **[Bhupesh Varshney](https://bhupesh-v.github.io)** 

## ☺️ Show your support

Support me by giving a ⭐️ if this project helped you! or just [![Twitter URL](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2F)](https://twitter.com/intent/tweet?url=https://github.com/Bhupesh-V/til&text=til%20via%20@bhupeshimself)

<a href="https://liberapay.com/bhupesh/donate">
  <img alt="Donate using Liberapay" src="https://liberapay.com/assets/widgets/donate.svg" width="100">
</a>
<a href="https://ko-fi.com/bhupesh">
  <img title="ko-fi/bhupesh" alt="Support on ko-fi" src="https://user-images.githubusercontent.com/34342551/88784787-12507980-d1ae-11ea-82fe-f55753340168.png" width="185">
</a>

## About

Original Idea/Work [thoughtbot/til](https://github.com/thoughtbot/til).
"""


def get_category_list():
    """Walk the current directory and get a list of all subdirectories at that
    level.  These are the "categories" of TILs."""
    avoid_dirs = [
        "images",
        "stylesheets",
        "javascripts",
        "_layouts",
        ".sass-cache",
        "_site",
    ]
    dirs = [
        x
        for x in os.listdir(".")
        if os.path.isdir(x) and ".git" not in x and x not in avoid_dirs
    ]
    return dirs


def get_title(til_file):
    """Read the file until we hit the first line that starts with a #
    indicating a title in markdown.  We'll use that as the title for this
    entry."""
    with open(til_file) as file:
        for line in file:
            line = line.strip()
            if line.startswith("#"):
                # print(line[1:])
                return line[1:].lstrip()  # text after # and whitespace


def get_tils(category):
    """ For a given category, get the list of TIL titles. """
    til_files = [x for x in os.listdir(category)]
    titles = []
    for filename in til_files:
        fullname = os.path.join(category, filename)
        if (os.path.isfile(fullname)) and fullname.endswith(".md"):
            title = get_title(fullname)
            # changing path separator for Windows paths
            # https://mail.python.org/pipermail/tutor/2011-July/084788.html
            titles.append((title, fullname.replace(os.path.sep, "/")))
    return titles


def get_category_dict(category_names):
    categories = {}
    count = 0
    for category in category_names:
        titles = get_tils(category)
        categories[category] = titles
        count += len(titles)
    return (count, categories)


def read_file(filename):
    with open(filename) as file:
        return file.read()


def print_file(category_names, count, categories):
    host_url = "https://github.com/Bhupesh-V/til/blob/master/"
    # used by shields.io for creating the TIL badge
    with open("count.json", "w") as json_file:
        data = {"count": count}
        json.dump(data, json_file, indent=" ")

    with open("README.md", "w") as file:
        file.write(HEADER)
        file.write("""\n\n## Categories\n""")
        # print the list of categories with links
        for category in sorted(category_names):
            tils = categories[category]
            file.write(
                f"""* [{category}](#{category.replace(' ', '-').lower()}) [**`{len(tils)}`**]\n"""
            )

        if len(category_names) > 0:
            file.write("""\n---\n\n""")
            # print the section for each category
        for category in sorted(category_names):
            file.write("\n\n\n### {0}\n\n".format(category))
            tils = categories[category]
            file.write("<ul>")
            for (title, filename) in sorted(tils):
                root_file = urllib.parse.quote(host_url + filename)
                urlsafe_twitter = (
                    "https://twitter.com/intent/tweet?url="
                    + urllib.parse.quote_plus(
                        f"{title} by @bhupeshimself {host_url+filename}"
                    )
                )
                urlsafe_reddit = f"https://www.reddit.com/submit?title={urllib.parse.quote(title)}&url={root_file}"
                urlsafe_telegram = f"https://telegram.me/share/url?text={urllib.parse.quote(title)}&url={root_file}"
                file.write("\n<li>")
                file.write(
                    f"""<a target="_blank" href="{host_url+filename}">{title}</a>"""
                )
                # file.write("<details><summary> Read More 🔽</summary>\n\n")
            # file.write(read_file(filename))
            # file.write(
            # f"""\n<a title="Share on Twitter" target="_blank" href="{urlsafe_twitter}"><img title="Share on Twitter" src="https://img.shields.io/twitter/url?label=%20&style=social&url=https://github.com/bhupesh-V"></a>"""
            # )
            # file.write(
            # f"""\n<a title="Share on Reddit" target="_blank" href="{urlsafe_reddit}"><img title="Share on Reddit" src="https://img.shields.io/twitter/url?label=%20&logo=reddit&url=https%3A%2F%2Frandom.url"></a>"""
            # )
            # file.write(
            # f"""\n<a title="Share on Telegram" target="_blank" href="{urlsafe_telegram}"><img title="Share on Telegram" src="https://img.shields.io/twitter/url?color=red&label=%20&logo=telegram&style=social&url=http%3Afvfv.com"></a>"""
            # )
            # file.write(
            # f"""\n<a title="Share on LinkedIn" target="_blank" href="https://www.linkedin.com/sharing/share-offsite/?url={root_file}"><img title="Share on LinkedIn" src="https://img.shields.io/twitter/url?label=%20&logo=linkedin&style=social&url=http%3A%2F%2Frandom.url"></a>"""
            # )
            # file.write("\n</details>")
            # file.write("</li>")
            file.write("\n")
            file.write("</ul>\n\n")

        file.write(FOOTER)


def get_recent_tils(categories):
    cmd = "git log --no-color --date=format:'%d %b, %Y' --diff-filter=A --name-status --pretty=''"
    recent_tils = []

    result = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = result.communicate()
    clean_output = out.decode("utf-8").strip("\n").replace("A\t", "").split("\n")
    # filter filepaths that don't exist
    flattened_list = list(itertools.chain(*list(categories.values())))
    flattened_list = [item[1] for item in flattened_list]
    valid_files = list(
        filter(
            lambda path: pathlib.Path(path).exists() and path in flattened_list,
            clean_output,
        )
    )

    for til in valid_files[:10]:
        til_dict = {}
        til_dict["title"] = get_title(til)
        til_path = pathlib.Path(til)
        til_dict["url"] = f"https://bhupesh.gitbook.io/notes/{til.lower().strip('.md')}"
        recent_tils.append(til_dict)

    with open("recent_tils.json", "w") as json_file:
        json.dump(recent_tils, json_file, ensure_ascii=False, indent=" ")


def create_README():
    """Create a TIL README.md file with a nice index for using it directly
    from GitHub."""
    category_names = get_category_list()
    count, categories = get_category_dict(category_names)
    get_recent_tils(categories)
    print_file(category_names, count, categories)
    print("\n", count, "TILs read")


if __name__ == "__main__":
    create_README()
