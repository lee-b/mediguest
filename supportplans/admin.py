from mediguest_admin.site import mediguest_admin_site
from models import SupportPlanReview
from django.contrib import admin

class SupportPlanReviewsInline(admin.TabularInline):
    model = SupportPlanReview
    extra = 0

mediguest_admin_site.register(SupportPlanReview)

