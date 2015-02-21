#django_starter

A user-friendly Django 1.7 Starter Template with an organized file structure for team development.

## Requirements
* [Pip](https://pip.pypa.io/en/latest/installing.html)
* [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)

## Installation
1. Clone it ```git clone git@github.com:potay/django-starter.git```
2. Run ```cd django_starter```
3. Run ```python setup.py [PROJECT_NAME]```
4. Delete setup.py file
5. Replace this file with your readme.
6. Start making awesome django web apps!
7. Run the local test server: ```python runserver.py```
8. Create new apps: ```python createapp.py [APP_NAME]```

## Structure
In this Django structure, all static and template files are stored in the root folder and not in their respective apps. This allows the frontend and backend process to be developed separately while still maintaining interdependence. Furthermore, this allows the namespace and structure of the template and static files to be more explicit and clear. All local development files, such as the database or log files, will be stored in the `tmp` folder and not be committed to git. The settings are now stored in multiple files for different environments, namely the production and development environment, where the development environment inherits from the product environment but makes the necessary changes for local development.

### File Structure
```
django_starter/            - Main Project Folder
  apps/                    - Contains all django apps
  settings/                - Contains production and development settings files
  prefixed_storage.py      - For storages plugin, if need be
  ...
static/                    - Contains all static files
templates/                 - Contains all the dynamic template files
tests/                     - Contains all the testing files
tmp/                       - Contains local development environment files (e.g. database files, log files, etc.)
createapp.py               - Run 'python createapp.py [APP_NAME]' to create an app following the file structure
manage.py                  - Standard django management file
runserver.py               - Run 'python runserver.py' to run a local test server. Does relevant checks and updates db first.
setup.py                   - Run python setup.py [PROJECT_NAME] after cloning starter template to setup the web app
requirements.txt           - Contains all pip requirements
Procfile                   - For heroku deployment
```
