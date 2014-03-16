from mediguest_admin.site import mediguest_admin_site
from models import RoomType, Room, Booking
from inventory.admin import InventoryItemInline
from django.forms.models import BaseInlineFormSet
from django.contrib import admin

class BookingsInline(admin.TabularInline):
    model = Booking
    extra = 0

class RoomAdmin(admin.ModelAdmin):
    inlines = [
        InventoryItemInline,
    ]

mediguest_admin_site.register(RoomType)
mediguest_admin_site.register(Room, RoomAdmin)
mediguest_admin_site.register(Booking)

