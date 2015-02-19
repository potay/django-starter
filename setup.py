#!/usr/bin/env python

"""
configure.py
Sets up the Django template as a new, distinct project.
"""

import os
import sys

if len(sys.argv) <= 1:
    print "You must supply a project name."
    print "run 'python setup.py [PROJECT_NAME]'"
    sys.exit(1)

PROJECT_NAME = sys.argv[1]

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
        raise NoDjProjectDir()

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


def generate_key():
    """ Generate a new Django secret key for use in settings.py. """

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

    # Insert the new key into settings.py
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

    print "Installing virtualenv at %s..." % os.path.join(PROJECT_ROOT, 'venv')
    os.system('virtualenv venv')
    print "Done!"

    print "Installing python packages via pip..."
    os.system('source venv/bin/activate; pip install -r requirements.txt')
    print "Done!"

    print "Renaming directory 'django_starter' to '%s'... " % PROJECT_NAME,
    rename_directory()
    print "Done!"

    print "Replacing 'django_starter' references with '%s'... " % PROJECT_NAME,
    replace_references(PROJECT_ROOT)
    print "Done!"

    print "Generating new Django secret key...",
    generate_key()
    print "Done!"

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
    print "Remember to source your virtual environment before continuing (run 'source venv/bin/activate')."

    return 0


if __name__ == '__main__':
    sys.exit(main())
