from mediguest_admin.site import mediguest_admin_site
from models import InventoryItemType, InventoryItem
from django.contrib import admin

class InventoryItemInline(admin.TabularInline):
    model = InventoryItem
    extra = 0

mediguest_admin_site.register(InventoryItemType)
mediguest_admin_site.register(InventoryItem)

