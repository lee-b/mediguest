from mediguest_admin.site import mediguest_admin_site
from models import RiskAssessment
from django.contrib import admin

class RiskAssessmentsInline(admin.TabularInline):
    model = RiskAssessment
    extra = 0

mediguest_admin_site.register(RiskAssessment)

