from mediguest_admin.site import mediguest_admin_site
from models import BenefitType, ReceivedBenefit
from django.contrib import admin

class ReceivedBenefitsInline(admin.TabularInline):
    model = ReceivedBenefit
    extra = 0

mediguest_admin_site.register(BenefitType)
mediguest_admin_site.register(ReceivedBenefit)

