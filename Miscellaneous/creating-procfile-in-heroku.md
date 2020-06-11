# What's a Procfile 👀
<!--1 Jul 2019 -->
I recently deployed a Python application on Heroku, there I encountered a `Procfile`.
This is what I got to know :

- The Procfile is a simple text file that is named `Procfile` without a file extension. For example, `Procfile.txt` is not a valid Procfile.
- It specifies the commands that are executed by the app on startup. For e.g A Django server.
- Example: If you want to run a python script on Heroku, your *Procfile* content should be
   `worker: python script.py`

### Resources
- [The Procfile](https://devcenter.heroku.com/articles/procfile)