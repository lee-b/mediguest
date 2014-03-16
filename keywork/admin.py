from mediguest_admin.site import mediguest_admin_site
from models import Keyworker, KeyworkSession
from django.contrib import admin

class KeyworkSessionsInline(admin.TabularInline):
    model = KeyworkSession
    extra = 0

mediguest_admin_site.register(Keyworker)
mediguest_admin_site.register(KeyworkSession)
