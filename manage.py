#!/usr/bin/env python
from django.core.management import execute_manager
import imp
import sys
try:
    imp.find_module('settings') # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)

import settings

def validate():
    if sys.argv[1] == 'runserver_plus':
        print """
    
    ERROR:
    
    runserver_plus does NOT support all features needed
    by this project.  Specifically, static file resolution order
    will be incorrect, causing theme errors and other anomalies
    in the browser.

    PLEASE USE runserver INSTEAD.

    """
        sys.exit(20)

    from settings import STATIC_URL
    if STATIC_URL != "/static/":
        print """

    ERROR:

    STATIC_URL is not set to '/static/'.  Currently, some template paths
    are hard-coded to this value, as STATIC_URL isn't available to them.  You
    need to adjust these files for consistency, then modify this script to
    be aware of the change.

    """
        sys.exit(20)

if __name__ == "__main__":
    validate()
    execute_manager(settings)
