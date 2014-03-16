from mediguest_admin.site import mediguest_admin_site
from models import Drug, DrugUnit, DrugFrequency, DrugDose
from django.contrib import admin

class DrugDosesInline(admin.TabularInline):
    model = DrugDose
    extra = 0

mediguest_admin_site.register(Drug)
mediguest_admin_site.register(DrugUnit)
mediguest_admin_site.register(DrugFrequency)
mediguest_admin_site.register(DrugDose)

