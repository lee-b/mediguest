from mediguest_admin.site import mediguest_admin_site
from models import AgencyContact
from django.contrib import admin

class AgencyContactInline(admin.TabularInline):
    model = AgencyContact
    extra = 0

