#django_starter

A user-friendly Django 1.7 Starter Template with an organized file structure for team development (like during Hackathons) and optional Heroku deployment.

## Requirements
* Mandatory:
  * [Pip](https://pip.pypa.io/en/latest/installing.html)
* Optional:
  * If you would like to use git, you will need:
    * [Git](http://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
  * If you would like to use a virtual envrionment (highly recommended), you will need:
    * Installed Python and [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) in a unix-style environment.
  * If you would like Heroku Deployment, you will also need:
    * The Heroku Toolbelt, as described in [Getting Started with Python](https://devcenter.heroku.com/articles/getting-started-with-python).
    * An installed version of [Postgres](http://www.postgresql.org/) to test locally.

## Installation
1. Clone it ```git clone git@github.com:potay/django-starter.git```
2. Run ```cd django_starter```
3. Setup the project:
  * If you would like all the features:
    * Run ```python setup.py [PROJECT_NAME]```
  * If you would not like to use heroku:
    * Run ```python setup.py [PROJECT_NAME] --noheroku```
  * If you would not like to use git:
    * Run ```python setup.py [PROJECT_NAME] --nogit```
  * If you would not like to use virtual environment (really not recommended for safety and security):
    * Run ```python setup.py [PROJECT_NAME] --novenv```
  * You can combine the flags:
    * ```python setup.py [PROJECT_NAME] --novenv --noheroku```...
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
