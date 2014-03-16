from mediguest_admin.site import mediguest_admin_site
from models import ClientNote
from django.contrib import admin

class ClientNotesInline(admin.TabularInline):
    model = ClientNote
    extra = 0

mediguest_admin_site.register(ClientNote)

