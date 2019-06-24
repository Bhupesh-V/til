#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Simple script to auto-generate the README.md file for a TIL project. 
'''
import os

HEADER = '''# TIL

> Today I Learned

A collection of concise write-ups on small things I learn across a variety of 
languages and technologies.

'''

FOOTER = '''## Usage
See [USAGE.md](https://github.com/Bhupesh-V/til/blob/master/USAGE.md) to know how I use this repository.

## Author

👥 **Bhupesh Varshney**

- Twitter: [@bhupeshimself](https://twitter.com/bhupeshimself)
- Github: [@Bhupesh-V](https://github.com/Bhupesh-V)

## About

Original Idea/Work [thoughtbot/til](https://github.com/thoughtbot/til).
'''


def get_category_list():
    ''' Walk the current directory and get a list of all subdirectories at that
    level.  These are the "categories" in which there are TILs. '''
    dirs = [x for x in os.listdir('.') if os.path.isdir(x) and '.git' not in x]
    return dirs


def get_title(til_file):
    ''' Read the file until we hit the first line that starts with a #
    indicating a title in markdown.  We'll use that as the title for this
    entry. '''
    with open(til_file) as file:
        for line in file:
            line = line.strip()
            if line.startswith('#'):
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


def print_file(category_names, count, categories):
    ''' Now we have all the information, print it out in markdown format. '''
    with open('README.md', 'w') as file:
        file.write(HEADER)
        if count == 1:
            file.write('_{0} TIL and counting..._'.format(count))
        else:
            file.write('_{0} TILs and counting..._'.format(count))
        file.write ('''

## Categories
''')
        # print the list of categories with links
        for category in sorted(category_names):
            file.write(
                '* [{0}](#{1})\n'.format(category, category))

        if len(category_names) > 0:
            file.write ('''
---

''')
        # print the section for each category
        for category in sorted(category_names):
            file.write('### {0}\n'.format(category))
            file.write('\n')
            tils = categories[category]
            for (title, filename) in sorted(tils):
                file.write('- [{0}]({1})\n'.format(title, filename))
            file.write('\n')

        if len(category_names) > 0:
            file.write ('''---

''')
        file.write(FOOTER)


def create_README():
    ''' Create a TIL README.md file with a nice index for using it directly
            from GitHub. '''
    category_names = get_category_list()
    count, categories = get_category_dict(category_names)
    print_file(category_names, count, categories)

if __name__ == '__main__':
    create_README()
