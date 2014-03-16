Initial Release

WINDOWS

	Extract files to c:\mediguest

	* INSTALL python 2.7 win32
	* INSTALL pip from http://pypi.python.org/pypi/pip#downloads
	* pip install django

DEBIAN LINUX

	Install dev stuff to build python modules:

		sudo apt-get install build-essential python-dev libfreetype6-dev libjpeg62-dev

	Install python modules:

		sudo apt-get install python-dateutil python-psycopg2

ALL

	pip install django django_extensions south pil django-debug-toolbar html5lib

LINUX

	apt-get install postgresql-server

WINDOWS

	Install:

		psycopg2 from http://www.stickpeople.com/projects/python/win-psycopg/psycopg2-2.4.2.win32-py2.7-pg9.0.4-release.exe
		postgresql from http://www.postgresql.org/download/windows
		pil from http://effbot.org/downloads/PIL-1.1.7.win32-py2.7.exe
		reportlab from http://www.reportlab.com/ftp/reportlab-2.5.win32-py2.7.exe

WINDOWS CLIENTS:

		Install Adobe Reader X Full version from ftp://ftp.adobe.com/pub/adobe/reader/win/10.x/10.0.0/en_US/AdbeRdr1000_en_US.exe

ALL

Setup postgresql with a database and user.

Configure the project:

    cp local_settings.py.template local_settings.py
    $EDITOR local_settings.py

WINDOWS (ONLY)

	run scripts/fix_windows.bat from the main directory

	Install prism from http://prism.mozillalabs.com/downloads/1.0b4/prism-1.0b4.en-US.win32.zip

NON-WINDOWS:

	Build static file links:

		./manage.py collectstatic -l

ALL

	Sync the DB:

		./manage.py syncdb
		./manage.py migrate

