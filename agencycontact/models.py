from django.db import models
from people.models import OrganizationMember
from clients.models import Client
from datetime import datetime

class AgencyContact(models.Model):
    client = models.ForeignKey(Client, help_text="Which client the agency was contacted about")
    date = models.DateTimeField(default=datetime.now, help_text="Date on which contact was made")
    agency_rep = models.ForeignKey(OrganizationMember, help_text="Person and agency that was contacted")
    reason_for_contact = models.TextField()
    outcome_of_contact = models.TextField()
    follow_up_required = models.BooleanField(help_text="Whether this should be followed-up with the contact again. If transferring elsewhere, begin a new contact, and leave this unset.")

