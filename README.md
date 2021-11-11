# Security console
Swiss Bank Vault Management Website

You could see active personal access cards with vault visit time.

The service will show you if this visit is strange or not.

## Install
Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
## Env Settings
Create `.env` from `.env.Example`
1. DATABASE_URL - str, variable to configure your Django application by `DJ-Database-URL`
   
    use template: `postgres://USER:PASSWORD@HOST:PORT/NAME` for default postgres

    More info on [DJ-Database-URL](https://github.com/jacobian/dj-database-url)
1. DEBUG - bool, setting for Django mode
1. SECRET_KEY - str, any secret key.
   You can use `secrets`:
   ```
   >>> import secrets
   >>> secrets.token_hex(16)
   '468e7bf2e532406d9a58e01eacb08720'
   ```

## Start
```
python manage.py runserver 0.0.0.0:8000
```