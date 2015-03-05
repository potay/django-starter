#!/usr/bin/env python

"""
configure.py
Sets up the Django template as a new, distinct project.
"""

import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("projectname", help="You must supply a project name.")
parser.add_argument("--noheroku", help="Don't set heroku as desired deployment option",
                    action="store_true")
parser.add_argument("--novenv", help="Don't use virtual environment and use local environment instead (Not recommended)",
                    action="store_true")
parser.add_argument("--nogit", help="Don't use git (not recommended)",
                    action="store_true")
args = parser.parse_args()

if args.noheroku:
    HEROKU = False
    requirements = "requirements.txt"
else:
    HEROKU = True
    requirements = "requirements-heroku.txt"

NO_VENV = args.novenv
NO_GIT = args.nogit

PROJECT_NAME = args.projectname

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


class NoDjProjectDir(Exception):
    def __str__(self):
        return (
            "Directory 'django_starter' does not exist. "
            "Are you sure this is a valid django_starter fork?"
        )


class NoDjSettings(Exception):
    def __str__(self):
        return (
            "Could not open %s/settings.py. "
            "Are you sure this is a valid django_starter fork?"
                % (PROJECT_NAME)
        )


def rename_directory():
    """ Renames the django_starter directory to PROJECT_NAME. """

    djprojectPath = os.path.join(PROJECT_ROOT, 'django_starter')

    if not os.path.exists(djprojectPath):
        if not os.path.exists(os.path.join(PROJECT_ROOT, PROJECT_NAME)):
            raise NoDjProjectDir()
        else:
            print "Directory already renamed"
    else:
        os.rename(djprojectPath, PROJECT_NAME)


def rename_root_directory():
    """ Renames the root django_starter directory to PROJECT_NAME. """

    djMainPath = PROJECT_ROOT

    if not os.path.exists(djMainPath):
        raise NoDjProjectDir()

    os.chdir('..')
    os.rename(djMainPath, PROJECT_NAME)
    os.chdir(PROJECT_NAME)


def replace_references(dir=PROJECT_ROOT):
    """ Recursively walks through the project and replaces references to
    'django_starter' with PROJECT_NAME.

    """

    for item in os.listdir(dir):
        itemPath = os.path.join(dir, item)

        if os.path.isdir(itemPath) and item != '.git':
            # Recursively walk directories and replace references
            replace_references(itemPath)

        # Replace references in all *.py files (except setup.py),
        # and also the Procfile.
        elif ((item.endswith('.py') and item != 'setup.py')
                or item == 'Procfile' or item == 'README.md'):

            # Read the file data
            with open(itemPath, 'r') as f:
                data = f.read()

            # Replace all references
            newData = data.replace('django_starter', PROJECT_NAME)

            # Re-save the file
            with open(itemPath, 'w') as f:
                f.write(newData)


def install_venv():
    """ Installs virtualenv for user. """
    if not os.path.exists(os.path.join(PROJECT_ROOT, "venv")):
        os.system('virtualenv venv')
    else:
        if (os.system('rm -rf venv') == 0):
            os.system('virtualenv venv')
        else:
            print "Unable to recreate virtual environment"


def set_heroku(heroku=True):
    """ Turn heroku on or off in settings.py. """

    settingsPath = os.path.join(PROJECT_ROOT, '%s/settings/production.py' % PROJECT_NAME)

    try:
        with open(settingsPath, 'r') as f:
            data = f.read()

    except IOError:
        raise NoDjSettings()

    # Change heroku settings in settings.py
    newData = data.replace("{{HEROKU_VALUE}}", "%s" % str(heroku))

    # Save the new settings.py
    with open(settingsPath, 'w') as f:
        f.write(newData)

    os.rename(requirements, "requirements.txt")


def generate_key():
    """ Generate a new Django secret key for use in settings.py. """

    if NO_VENV:
        settingsPath = os.path.join(PROJECT_ROOT, '%s/settings/production.py' % PROJECT_NAME)
    else:
        settingsPath = os.path.join(PROJECT_ROOT, 'venv/bin/activate')

    try:
        with open(settingsPath, 'r') as f:
            data = f.read()

    except IOError:
        raise NoDjSettings()

    # Generate a new secret key (consisting of 50 OS-produced random bytes)
    import random, string
    validList = (string.digits + string.letters + string.punctuation).translate(None, '`"\'')
    newKey = "".join([random.SystemRandom().choice(validList) for i in range(100)])

    if NO_VENV:
        # Insert the new key into settings.py
        newData = data.replace("os.environ['DJANGO_SECRET_KEY']", "'%s'" % newKey)
    else:
        # Insert the key into environment variable
        newData = data + '\n\nexport DJANGO_SECRET_KEY="%s"\n\n' % newKey

    # Save the new settings.py
    with open(settingsPath, 'w') as f:
        f.write(newData)


def main():
    global PROJECT_ROOT

    print "Renaming root 'django_starter' to '%s'... " % PROJECT_NAME,
    rename_root_directory()
    PROJECT_ROOT = os.path.join(os.path.dirname(PROJECT_ROOT), PROJECT_NAME)
    print "Done!"

    if not NO_VENV:
        print "Installing virtualenv at %s..." % os.path.join(PROJECT_ROOT, 'venv')
        install_venv()
        print "Done!"

    print "Installing python packages via pip..."
    if NO_VENV:
        os.system('pip install -r %s' % requirements)
    else:
        os.system('source venv/bin/activate; pip install -r %s' % requirements)
    print "Done!"

    print "Renaming directory 'django_starter' to '%s'... " % PROJECT_NAME,
    rename_directory()
    print "Done!"

    print "Replacing 'django_starter' references with '%s'... " % PROJECT_NAME,
    replace_references(PROJECT_ROOT)
    print "Done!"

    if HEROKU:
        print "Modifying settings for heroku setup...",
        set_heroku(True)
        print "Done!"
    else:
        print "Modifying settings for non-heroku setup...",
        set_heroku(False)
        print "Done!"

    print "Generating new Django secret key...",
    generate_key()
    print "Done!"

    if NO_GIT:
        print "Deleting git...",
        os.system('rm -rf .git')
        print "Done!"
    else:
        print "Restarting git...",
        os.system('rm -rf .git')
        os.system('git init .')
        print "Done!"

        print "Commiting initial to git...",
        os.system('git add .')
        os.system('git commit -m "Initial commit"')
        print "Done!"

    print
    print "Setup finished!"
    print "You may now remove this file (setup.py)."
    if not NO_VENV:
        print "Remember to source your virtual environment before continuing (run 'source venv/bin/activate')."

    return 0


if __name__ == '__main__':
    sys.exit(main())
