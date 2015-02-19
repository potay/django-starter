#!/usr/bin/env python

import os
import sys

PROJECT_NAME = 'django_starter'

if len(sys.argv) <= 1:
    print "You must supply an app name."
    print "run 'python createapp.py [APP_NAME]'"
    sys.exit(1)

print "Creating %s App..." % sys.argv[1]
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.join(PROJECT_ROOT, 'django_starter/apps'))
os.system('python ../../manage.py createapp %s' % sys.argv[1])
print "App %s created!" % sys.argv[1]
