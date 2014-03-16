from mediguest_admin.site import mediguest_admin_site
from models import Incident
from django.contrib import admin

class IncidentsInline(admin.TabularInline):
    model = Incident
    extra = 0

mediguest_admin_site.register(Incident)

