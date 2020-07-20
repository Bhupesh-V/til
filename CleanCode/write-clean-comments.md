# Writing Comments
<!--24 Jun 2019 -->
1. The proper use of comments is to compensate for our _failure to express
   ourself in code_.
2. Inaccurate comments are far worse than no comments at all.
3. Comments do not make up for the bad code.
   i.e if you find yourself writing comments for a code that is complex to understand.
   *MAKE IT LESS COMPLEX*.
4. Short functions don't need much description. A well-chosen name for a small function
   that does one thing is usually better than a comment header.
5. For example. In this code the comments are not needed bcoz the fucntion name describes what it is doing.
   
```python
def get_category_list():
    ''' Walk the current directory and get a list of all subdirectories at that
    level.  These are the "categories" in which there are TILs. '''
    dirs = [x for x in os.listdir('.') if os.path.isdir(x) and '.git' not in x]
    return dirs
```
   
### Summary
Until now I thought writing comments is a good practice & we should write comments wherever possible.
But know reading it is an eye opener & shocking 😱. I will try to avoid comments now.

---
_PS : I have been reading [CleanCode](https://www.oreilly.com/library/view/clean-code/9780136083238/) for a while & logging what I learn here._
