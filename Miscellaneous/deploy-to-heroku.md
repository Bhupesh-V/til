# Deploying to Heroku
<!--15 Oct 2019 -->
## List of steps to follow when you are deployihg a **new** repository/project (Python).

1. `heroku login`
2. `touch Procfile`
Create Procfile for deployment. For a Django Web-App the contents of Procfile would be.
```
gunicorn djangoherokuapp.wsgi --log-file -
```
3. `touch runtime.txt`
Specify your Python version here. For example
```
python-3.6.8
```
4. `heroku create herokuAPPName`
Before running this, Make sure to add `appname.herokuapp.com` in ALLOWED_HOSTS and your `requirements.txt` is updated.


## List of commands to run when you are deployihg a **cloned** repository.

1. `heroku login`
Login with your e-mail and password.
2. `heroku git:remote -a <app-name>`
Where `app-name` is the name of app on heroku.
3. `git push heroku master`
Push new changes to heroku.