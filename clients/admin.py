from clients.models import Client
from addresses.models import Address
from mediguest_admin.site import mediguest_admin_site
from people.models import Person
from django.contrib import admin

from foreignkeysearch.widgets import ForeignKeySearchForm
from foreignkeysearch.handler import BaseHandler

from keywork.mod.keyworker import Keyworker
from agencyservices.models import GP

from convictions.admin import ConvictionsInline
from booking.admin import BookingsInline
from benefits.admin import ReceivedBenefitsInline
from drug_db.admin import DrugDosesInline
from keywork.admin import KeyworkSessionsInline
from supportplans.admin import SupportPlanReviewsInline
from incidents.admin import IncidentsInline
from risks.admin import RiskAssessmentsInline
from clientnotes.admin import ClientNotesInline
from hospitaladmissions.admin import HospitalAdmissionsInline
from agencycontact.admin import AgencyContactInline
from servicecharges.admin import ServiceChargesInline, ServiceChargePaymentsInline

from forms import ClientForm


class address_SearchHandler(BaseHandler):
    model = Address
    exclude = (
        'country',
    )

class next_of_kin_SearchHandler(BaseHandler):
    model = Person
    exclude = (
        'gender',
        'address',
    )

class keyworker_SearchHandler(BaseHandler):
    model = Keyworker
    exclude = (
        'gender',
        'address',
    )

class gp_SearchHandler(BaseHandler):
    model = GP
    exclude = (
        'gender',
        'address',
    )

class ClientAdmin(admin.ModelAdmin):
    form = ClientForm

    inlines = [
        ConvictionsInline,
        BookingsInline,
        ReceivedBenefitsInline,
        DrugDosesInline,
        KeyworkSessionsInline,
        SupportPlanReviewsInline,
        RiskAssessmentsInline,
        IncidentsInline,
        HospitalAdmissionsInline,
        AgencyContactInline,
        ServiceChargesInline,
        ServiceChargePaymentsInline,
        ClientNotesInline,
    ]

    fieldsets = (
        ('General', {
            'fields': (
                'photo',
                'gender',
                'title',
                'forenames',
                'surnames',
                'suffix',
                'nee',
                'date_of_birth',
                'religion',
                'client_pack_agreed',
            )
        }),
        ('Contact Details', {
            'fields': (
               'address',
               'mobile_phone_no',
            )
        }),
        ('Medical Information', {
            'fields': (
               'national_insurance_no',
               'gp',
               'assigned_keyworker',
               'contact_next_of_kin',
               'next_of_kin',
               'medical_problems',
               'mobility_problems',
               'assistance_required',
            )
        }),
        ('Statistics', {
            'fields': (
               'presented_as_homeless',
               'ethnic_origin',
            )
        }),
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(ClientAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in ('address', 'keyworker', 'gp', 'next_of_kin'):
            field.widget = ForeignKeySearchForm(
                db_field=db_field,
                handler=eval(db_field.name + '_SearchHandler'),
            )
        return field

mediguest_admin_site.register(Client, ClientAdmin)

