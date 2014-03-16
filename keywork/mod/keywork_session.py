import os
from django.db import models
from clients.models import Client
from keyworker import Keyworker
from datetime import datetime

class KeyworkSession(models.Model):
    class Meta:
        app_label = os.path.basename(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

    date = models.DateTimeField(default=datetime.now, help_text="When the session took place")
    client = models.ForeignKey(Client, help_text="Which client this keywork session was with")
    keyworker = models.ForeignKey(Keyworker, help_text="Which keyworker conducted the session")

    # assessment fields
    general_welfare = models.TextField(blank=True, null=True)
    current_benefits = models.TextField(blank=True, null=True)
    general_welfare = models.TextField(blank=True, null=True)
    housing_issues = models.TextField(blank=True, null=True)
    addictions = models.TextField(blank=True, null=True)
    healthcare = models.TextField(blank=True, null=True)
    meaningful_occupation_study = models.TextField(blank=True, null=True)
    budgeting_lifeskills = models.TextField(blank=True, null=True)
    contact_outside_agencies = models.TextField(blank=True, null=True)
    protection_from_abuse = models.TextField(blank=True, null=True)
    other_issues = models.TextField(blank=True, null=True)

    needs_assessment_support_plan = models.BooleanField(default=False)

