#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import itertools
import subprocess as sp
import pathlib
import asyncio

HEADER = """<h1 align="left">Today I Learned</h1>
<p align="center">
  <img alt="TILs Count" src="https://img.shields.io/badge/dynamic/json.svg?color=black&label=TILs&query=count&url=https%3A%2F%2Fraw.githubusercontent.com%2FBhupesh-V%2Ftil%2Fmaster%2Fcount.json">
  <img alt="last commit" src="https://img.shields.io/github/last-commit/bhupesh-V/TIL?color=purple">
  <a href="https://github.com/Bhupesh-V/til/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/github/license/Bhupesh-V/til" target="_blank" />
  </a>
  <a href="https://til.bhupesh.me">
    <img alt="Website" src="https://img.shields.io/website?url=https%3A%2F%2Ftil.bhupesh.me">
  </a>
  <a href="https://twitter.com/bhupeshimself">
    <img alt="Twitter: Bhupesh Varshney" src="https://img.shields.io/twitter/follow/bhupeshimself.svg?style=social" target="_blank" />
  </a>
</p>

> Welcome to my digital garden/second brain where I try to dump everything I learn in its most raw form 🌱


"""

SUMMARY_HEADER = """# Table of contents

* [Today I Learned](README.md)

"""

FOOTER = """## Usage

See [USAGE.md](https://github.com/Bhupesh-V/til/blob/master/USAGE.md) to know how I use this repository.

## ☺️ Show your support

Support me by giving a ⭐️ if this project helped you! or just [![Twitter URL](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2F)](https://twitter.com/intent/tweet?url=https://github.com/Bhupesh-V/til&text=til%20via%20@bhupeshimself)


## About

Original Idea/Work [thoughtbot/til](https://github.com/thoughtbot/til).
"""


async def get_category_list():
    """
    Walk the current directory and get a list of all subdirectories at that
    level.  These are the "categories" of TILs.
    """
    avoid_dirs = [
        "images",
        "stylesheets",
        "javascripts",
        "temp",
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
    """
    Read the file until we hit the first line that starts with a #
    indicating a title in markdown.
    """
    with open(til_file) as file:
        for line in file:
            line = line.strip()
            if line.startswith("#"):
                # print(line[1:])
                return line[1:].lstrip()  # text after # and whitespace


def get_tils(category):
    """
    For a given category, get the list of TIL titles
    """
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


async def create_gitbooks_summary(category_names, categories):
    """
    Create SUMMARY.md for GitBooks site
    """
    print("Generating SUMMARY.md")
    with open("SUMMARY.md", "w") as summary:
        summary.write(SUMMARY_HEADER)
        for category in sorted(category_names):
            summary.write("\n\n## {0}\n\n".format(category.replace("-", " ").title()))
            tils = categories[category]
            summary.write("<ul>")
            for (title, filename) in sorted(tils):
                summary.write("\n<li>")
                summary.write(f"""<a href="{filename}">{title}</a>""")
            summary.write("\n")
            summary.write("</ul>")


async def create_til_count_file(count):
    """
    Used by shields.io for generating the TILs count badge on GitHub
    """
    print("Generating count.json")
    with open("count.json", "w") as json_file:
        data = {"count": count}
        json.dump(data, json_file, indent=" ")


async def create_readme(category_names, categories):
    """
    Generate the README.md for github repo
    """
    host_url = "https://github.com/Bhupesh-V/til/blob/master/"
    print("Generating README.md")

    num_columns = 3  # Number of columns for the grid
    num_rows = (len(category_names) + num_columns - 1) // num_columns  # Calculate the number of rows

    category_names = sorted(category_names)

    with open("README.md", "w") as file:
        file.write(HEADER)
        file.write("""\n\n## Categories\n""")

        # Generate the table header
        file.write('<table align="center">\n')

        # Generate the table rows
        for row in range(num_rows):
            file.write("<tr>\n")
            for col in range(num_columns):
                index = row * num_columns + col
                if index < len(category_names):
                    category = category_names[index]
                    tils = categories[category]
                    file.write(f"""<td><a href="#{category.replace(' ', '-').lower()}">{category.title()}</a><sup><strong>[{len(tils)}]</strong></sup></td>\n""")
                else:
                    file.write("<td></td>\n")  # Empty cell if no category
            file.write("</tr>\n")

        file.write("</table>\n")

        if len(category_names) > 0:
            file.write("""\n---\n\n""")
            # print the section for each category
        for category in sorted(category_names):
            file.write("\n\n\n### {0}\n\n".format(category.replace("-", " ").title()))
            tils = categories[category]
            file.write("<ul>")
            for (title, filename) in sorted(tils):
                file.write("\n<li>")
                file.write(
                    f"""<a target="_blank" href="{host_url+filename}">{title}</a>"""
                )
            file.write("\n")
            file.write("</ul>\n\n")

        file.write(FOOTER)


async def create_recent_tils_file(categories):
    """
    Generate recent_tils.json to be used by my website & github profile readme
    """

    print("Generating recent_tils.json")
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
        til_dict["url"] = f"https://til.bhupesh.me/{til[:til.rfind('.')].lower().replace(' ', '-')}"
        recent_tils.append(til_dict)

    with open("recent_tils.json", "w") as json_file:
        json.dump(recent_tils, json_file, ensure_ascii=False, indent=" ")


async def main():
    """
    TIL Build Script Algorithm:

    1. Get list of directories
    2. For each valid TIL category, find markdown files inside it
    3. Generate recent_tils using git
    4. Generate SUMMARY.md for gitbook
    5. Generate README.md for GitHub
    """

    get_categories = asyncio.create_task(get_category_list())
    category_names = await get_categories
    count, categories = get_category_dict(category_names)

    task1 = asyncio.create_task(create_recent_tils_file(categories))
    task2 = asyncio.create_task(create_readme(category_names, categories))
    task3 = asyncio.create_task(create_gitbooks_summary(category_names, categories))
    task4 = asyncio.create_task(create_til_count_file(count))

    await task1
    await task2
    await task3
    await task4

    print(count, "TILs read")


asyncio.run(main())
