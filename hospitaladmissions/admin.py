from mediguest_admin.site import mediguest_admin_site
from models import Hospital, HospitalAdmission
from django.forms.models import BaseInlineFormSet
from django.contrib import admin

class HospitalAdmissionsInline(admin.TabularInline):
    model = HospitalAdmission
    extra = 0

mediguest_admin_site.register(HospitalAdmission)
mediguest_admin_site.register(Hospital)

