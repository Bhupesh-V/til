# Exploring Large Codebases
 

> Since more than 50% of the time developers spent reading & modifying existing source code rather then writing new one, reading code is an essential skill for a developer that's why I am maintaining a log of resources, tips etc. to explore unknown Codebases

Usually picking a small task will help explore the codebase but ofc as a developer we need some powerstuff as well.
	
- Write a glossary (class/function names, file/variable prefixes), As you read the code and encounter terms/words you don't know, write them down. Try to explain what they mean and how they relate to other terms. Create Docs for yourself
- Check commit log in general for some interesting commits.
  - Check most commonly edited files
- Read and run the tests (if any). The tests are (usually) a very clear and simple insight into otherwise complex functionality. This method should do this, this class should do that etc.
- Read the documentation and comments (if any). This can really help you understand the how's and why's.


## Tools
- [ack](https://github.com/beyondgrep/ack3)
- [ag](https://github.com/ggreer/the_silver_searcher)
- [Sourcetrail](https://www.sourcetrail.com/)
- [codetour](https://aka.ms/codetour)
- [vim-bookmarks](https://github.com/MattesGroeger/vim-bookmarks)
- When exploring a git repo add these aliases to find more insights like 
  - `git top10`: most actively edited files.
  - `git his`: Examples of commits that modify a file (helps in understanding what needs to be changed)
  - `git wot`: See how a function evolved 

  ```
  [alias]
        # find commits that changed a file: git his <filepath>
        his = log --follow --color=always --date=format:'%d %b, %Y' --pretty=format:'(%Cgreen%h%Creset)[%ad] %C(blue bold)%s%Creset'
        # search code in commit history: git wot :function_name:filepath
        wot = log --date=format:'%d %b, %Y' --pretty='%n%C(yellow bold)📅️ %ad%Creset by (%C(green bold)%an%Creset) %C(cyan bold)%h%Creset' --graph -L
        # top 10 most edited files
        top10 = ! git log --pretty=format: --name-only | sort | uniq -c | sort -rg | head -10
  ```


## Resources & Internet Threads
- [Ask HN: How do you familiarize yourself with a new codebase?](https://news.ycombinator.com/item?id=9784008)
- [General Guide For Exploring Large Open Source Codebases](https://pncnmnp.github.io/blogs/oss-guide.html)
- [A better way to learn a new codebase](https://xdg.me/learn-a-new-codebase/)
- [7 tools for visualizing a codebase](https://lmy.medium.com/7-tools-for-visualizing-a-codebase-41b7cddb1a14)
- [How to interrogate unfamiliar code](https://stackoverflow.blog/2022/08/15/how-to-interrogate-unfamiliar-code/?utm_source=linkedin&utm_medium=social&utm_campaign=so-blog&utm_content=unfamiliar-code)
