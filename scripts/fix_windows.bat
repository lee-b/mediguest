@echo OFF
REM Run this to fix paths on windows
REM We assume git is installed in c:\Progra~1\Git

c:\Progra~1\Git\bin\rm -rf foreignkeysearch easy_thumbnails mediguest_admin\static\dojo mediguest_admin\static\dijit static\dijit static\dojo

c:\Progra~1\Git\bin\ln -sf third-party\django-foreignkeysearch foreignkeysearch
c:\Progra~1\Git\bin\ln -sf third-party\easy-thumbnails\easy_thumbnails easy_thumbnails

cd mediguest_admin\static
c:\Progra~1\Git\bin\ln -sf dojo-release-1.6.1\dojo dojo
c:\Progra~1\Git\bin\ln -sf dojo-release-1.6.1\dijit dijit

cd ..\..

REM python manage.py collectstatic
