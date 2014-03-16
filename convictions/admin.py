from mediguest_admin.site import mediguest_admin_site
from django.contrib import admin
from models import ConvictionType, Conviction

class ConvictionsInline(admin.TabularInline):
    model = Conviction
    extra = 0

mediguest_admin_site.register(ConvictionType)
mediguest_admin_site.register(Conviction)

