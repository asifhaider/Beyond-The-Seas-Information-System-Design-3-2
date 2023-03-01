# Steps to run in local

- git clone
- cd into the repo (not into the project root)
- $ source testenv/bin/activate
- cd into the project root
- go
- $ deactivate, when done


# Development

## Virtual Environment

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

## Django Project

- $ django-admin startproject ```beyondtheseas```
- ```beyondtheseas``` is the root
- python manage.py runserver <port> (by default 8000)
- $ python manage.py startapp ```homepage```


## Django App

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


# Deploy

## Render 

- Create account and authorize with GitHub profile
- Create a postgres database 
    - Hostname: ```dpg-cfv2gmd3t39doavp4hu0-a```
    - Port: ```5432```
    - Database: ```beyondtheseasdatabase```
    - Username: ```beyondtheseasdatabase_user```
    - Password: ```CzGn3A8SvcwZ23ooYHPZ8NYHjn52MH5O```
    - Internal DB URL: ```postgres://beyondtheseasdatabase_user:CzGn3A8SvcwZ23ooYHPZ8NYHjn52MH5O@dpg-cfv2gmd3t39doavp4hu0-a/beyondtheseasdatabase```
    - External DB URL: ```postgres://beyondtheseasdatabase_user:CzGn3A8SvcwZ23ooYHPZ8NYHjn52MH5O@dpg-cfv2gmd3t39doavp4hu0-a.singapore-postgres.render.com/beyondtheseasdatabase```
    - PSQL command: ```PGPASSWORD=CzGn3A8SvcwZ23ooYHPZ8NYHjn52MH5O psql -h dpg-cfv2gmd3t39doavp4hu0-a.singapore-postgres.render.com -U beyondtheseasdatabase_user beyondtheseasdatabase```

- pip install gunicorn
