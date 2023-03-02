# Public link
- [Beyond The Seas](https://beyond-the-seas.onrender.com/)

# Steps to run in local

- git clone
- cd into the repo (not into the project root)
- create a new virtual environment and activate it
- run ```pip -r requirements.txt``` to install dependencies
- cd into the project root
- ready!


# Development Logs

## 1. Virtual Environment

- [venv link](https://docs.python.org/3/tutorial/venv.html)
- python3.10-venv
- $ python3 -m venv <name>
- $ source <name>/bin/activate
- ```(name)$``` => activated
- ```deactivate```
- $ python -m pip install Django
- ```pip list``` to check the package list inside
- [psycopg-binary link](https://pypi.org/project/psycopg2-binary/)
- $ pip install psycopg2-binary
- $ pip install dj-database-url
- $ pip install django-environ

## 2. Django
### Project and Apps

- $ django-admin startproject ```beyondtheseas```
- ```beyondtheseas``` is the root
- python manage.py runserver <port> (by default 8000)
- $ python manage.py startapp ```homepage```
- $ python manage.py startapp ```university```


### Views

- app/views
- app/urls (create new)
- project/urls
- project/settings/DIR -> templates directory add
- templates/html
- git add, commit, push

### Models

- write model classes in app/models
- python manage.py makemigrations app
- python manage.py migrate
- git add, commit, push
- register the models to admin site

### Database (for local)

- install postgresql
- [server error](https://dba.stackexchange.com/questions/182189/how-do-i-access-postgres-when-i-get-an-error-about-var-run-postgresql-s-pgsql)
- [change port to 5432](https://dba.stackexchange.com/questions/182189/how-do-i-access-postgres-when-i-get-an-error-about-var-run-postgresql-s-pgsql)
- sudo service postgresql restart


## 3. Deployment

### Render 

- Create account and authorize with GitHub profile
- Create a postgres database and web hosting services
- pip install gunicorn