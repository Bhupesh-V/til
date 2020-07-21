#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Simple script to auto-generate the README.md file for a TIL project.
'''
import os
import json

HEADER = '''
<h1 align="center">Today I Learned</h1>
<p align="center">
  <img height="200px" src="https://repository-images.githubusercontent.com/192476462/fdd6ce80-0b94-11ea-8b50-812ee66b0599" />
  <br>
  <img alt="TILs Count" src="https://img.shields.io/badge/dynamic/json.svg?color=black&label=TILs&query=count&url=https%3A%2F%2Fraw.githubusercontent.com%2FBhupesh-V%2Ftil%2Fmaster%2Fcount.json">
  <img alt="last commit" src="https://img.shields.io/github/last-commit/bhupesh-V/TIL?color=purple">
  <a href="https://github.com/Bhupesh-V/til/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/github/license/Bhupesh-V/til" target="_blank" />
  </a>
  <a href="https://bhupesh.codes/til/">
    <img alt="Website Status" src="https://img.shields.io/website?down_color=red&down_message=offline&up_color=orange&up_message=online&url=https%3A%2F%2Fbhupesh.codes%2Ftil%2F" />
  </a>
  <a href="https://twitter.com/bhupeshimself">
    <img alt="Twitter: Bhupesh Varshney" src="https://img.shields.io/twitter/follow/bhupeshimself.svg?style=social" target="_blank" />
  </a>
</p>

> Today I Learned.
A collection of concise write-ups on small things I learn across a variety of 
languages and technologies.


'''

FOOTER = '''## Usage

See [USAGE.md](https://github.com/Bhupesh-V/til/blob/master/USAGE.md) to know how I use this repository.

## Author

👤 **Bhupesh Varshney**

- Web : [bhupesh.codes](https://bhupesh-v.github.io)
- Twitter : [@bhupeshimself](https://twitter.com/bhupeshimself)
- DEV : [bhupesh](https://dev.to/bhupesh)


## ☺️ Show your support

Support me by giving a ⭐️ if this project helped you! or just [![Twitter URL](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2F)](https://twitter.com/intent/tweet?url=https://github.com/Bhupesh-V/til&text=til%20via%20@bhupeshimself)

<a href="https://liberapay.com/bhupesh/donate">
  <img alt="Donate using Liberapay" src="https://liberapay.com/assets/widgets/donate.svg" width="100">
</a>

<a href="https://www.patreon.com/bhupesh">
  <img alt="Patron Bhupesh" src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>

## 📝 License

Copyright © 2020 [Bhupesh Varshney](https://github.com/Bhupesh-V).<br />
This project is [MIT](https://github.com/Bhupesh-V/til/blob/master/LICENSE) licensed.

## About

Original Idea/Work [thoughtbot/til](https://github.com/thoughtbot/til).
'''


def get_category_list():
    ''' Walk the current directory and get a list of all subdirectories at that
    level.  These are the "categories" in which there are TILs. '''
    dirs = [x for x in os.listdir('.') if os.path.isdir(x) and '.git' not in x and '_layouts' not in x]
    return dirs


def get_title(til_file):
    ''' Read the file until we hit the first line that starts with a #
    indicating a title in markdown.  We'll use that as the title for this
    entry. '''
    with open(til_file) as file:
        for line in file:
            line = line.strip()
            if line.startswith('#'):
                print(line[1:])
                return line[1:].lstrip()  # text after # and whitespace


def get_tils(category):
    ''' For a given category, get the list of TIL titles. '''
    til_files = [x for x in os.listdir(category)]
    titles = []
    for filename in til_files:
        fullname = os.path.join(category, filename)
        if (os.path.isfile(fullname)) and fullname.endswith('.md'):
            title = get_title(fullname)
            # changing path separator for Windows paths
            # https://mail.python.org/pipermail/tutor/2011-July/084788.html
            titles.append((title, fullname.replace(os.path.sep, '/')))
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
    ''' Now we have all the information, print it out in markdown format. '''
    with open('count.json', 'w') as json_file:
        data = {'count': count}
        json.dump(data, json_file)

    with open('README.md', 'w') as file:
        file.write(HEADER)
        file.write('''

## Categories
''')
        # print the list of categories with links
        for category in sorted(category_names):
            file.write(
                '* [{0}](#{1})\n'.format(category, category.lower()))

        if len(category_names) > 0:
            file.write('''
---

''')
        # print the section for each category
        for category in sorted(category_names):
            file.write('\n\n\n### {0}\n'.format(category))
            file.write('\n')
            tils = categories[category]
            file.write('<ul>')
            for (title, filename) in sorted(tils):
                file.write('\n<li>')
                file.write('<a href="{1}">{0}</a>'.format(title, filename))
                file.write('<details><summary> Read More 👇</summary>')
                file.write('\n\n')
                file.write(read_file(filename))
                file.write('\n</details>')
                file.write('</li>')
            file.write('\n')
            file.write('</ul>')

        if len(category_names) > 0:
            file.write('''\n---

''')
        file.write(FOOTER)


def create_README():
    ''' Create a TIL README.md file with a nice index for using it directly
            from GitHub. '''
    category_names = get_category_list()
    count, categories = get_category_dict(category_names)
    print_file(category_names, count, categories)
    print("\n", count, "TILs read")


if __name__ == '__main__':
    create_README()
