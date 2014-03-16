# MediGuest

This is a a web-based management tool for medical / social support facilities.

## Features

  * User-friendly:
    - Web-based UI
    - Many features, but following logical, uniform UI design, so learning one part of the system familarises you with the rest quickly
  * Client management:
    - Name, address, contact details, etc.
    - Photographs
    - Criminal records
    - Medical histories, including external services
    - Social care histories, including external services and internal support workers
    - History of previous stays
    - General notes
    - Print letters of offer, contracts, emergency sheets (quick reference of client needs for paramedics / ambulance crews), etc.
    - Track medications given, required dosages, etc.
  * Room management:
    - track rooms
    - organise rooms by type
    - track room inventory
  * Booking:
    - log booking start / end times
    - see previous bookings
    - add notes on reason for leaving
    - previous leaving reasons easily visible before booking client in again
  * Verification / report tools
    - Analyse dosages given, report on medications given over expected dosage limits (NOTE: this is intended as an example of reporting only; it is NOT well tested as yet)
  * Keywork tracking
    - Log each time a keyworker / medical worker / social support worker inand medication tracking
    - Track client goals and progress across multiple keywork sessions
  * Flexible document / letter creation:
    - Includes a PDF document / report creation engine, for printing letters to external agencies, letters of offer to clients, etc.
    - Print up-to-date documents direct from the database records, ensuring the database is always the authoritative copy of the information
  * Audit trail
    - All changes to data are tracked, with action taken
  * Web-based, multi-user design:
    - one instance per organisation
    - access from any computer with a web browser
    - suitable for deploying on a local server OR on a remote, hosted webserver (additional security layers, such as a VPN are recommended)
  * Flexible, extensible architecture
    - Built on Django, one of the most powerful, flexible, well-supported, and extensible web application frameworks
    - Database abstraction layer: capable of running on PostgreSQL, MySQL, SQLite, or any other database fully supported by Django
    - Easy to add new reports, new types of records, etc.
    - Auditing engine automatically included in any new features


## TO DO

  * Currently based on Django 1.3; needs updated to Django 1.5+


## Installation

### Windows

Extract files to c:\mediguest

  * INSTALL python 2.7 win32
  * INSTALL pip from http://pypi.python.org/pypi/pip#downloads
  * pip install django
  * psycopg2 from http://www.stickpeople.com/projects/python/win-psycopg/psycopg2-2.4.2.win32-py2.7-pg9.0.4-release.exe
  * postgresql from http://www.postgresql.org/download/windows
  * pil from http://effbot.org/downloads/PIL-1.1.7.win32-py2.7.exe
  * reportlab from http://www.reportlab.com/ftp/reportlab-2.5.win32-py2.7.exe


### Debian Linux

Install dev stuff to build python modules:

    sudo apt-get install build-essential python-dev libfreetype6-dev libjpeg62-dev

Install python modules:

    sudo apt-get install python-dateutil python-psycopg2


### Linuxes (including debian)

    apt-get install postgresql-server


### ALL

    pip install django django_extensions south pil django-debug-toolbar html5lib

Setup postgresql with a database and user.

Configure the project:

    cp local_settings.py.template local_settings.py
    $EDITOR local_settings.py




### Windows clients (staff terminals which will access the server)

Install Adobe Reader X Full version from ftp://ftp.adobe.com/pub/adobe/reader/win/10.x/10.0.0/en_US/AdbeRdr1000_en_US.exe


WINDOWS (ONLY)

  * Run scripts/fix_windows.bat from the main directory
  * Install prism from http://prism.mozillalabs.com/downloads/1.0b4/prism-1.0b4.en-US.win32.zip

## NON-WINDOWS:

Build static file links:

    ./manage.py collectstatic -l

## ALL

Sync the DB:

    ./manage.py syncdb
    ./manage.py migrate

