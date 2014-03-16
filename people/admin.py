from addresses.models import Address
from models import Organization, OrganizationMember, Person
from mediguest_admin.site import mediguest_admin_site
from django.contrib import admin

from foreignkeysearch.widgets import ForeignKeySearchForm
from foreignkeysearch.handler import BaseHandler

class address_SearchHandler(BaseHandler):
    model = Address

class PersonAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(PersonAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in ('address'):
            field.widget = ForeignKeySearchForm(
                db_field=db_field, 
                handler=eval(db_field.name + '_SearchHandler'),
            )
        return field

mediguest_admin_site.register(Organization)
mediguest_admin_site.register(OrganizationMember)
mediguest_admin_site.register(Person, PersonAdmin)

