from django.db import models
from clients.models import Client
from datetime import datetime

class RiskAssessment(models.Model):
    client = models.ForeignKey(Client)

    assessment_date = models.DateTimeField(default=datetime.now)
    guest_on_client_risk = models.BooleanField(default=False)
    handover_updated = models.NullBooleanField(default=False)
    copies_in_guest_monitoring_files = models.NullBooleanField(default=False)

    summary_of_risk_issues = models.TextField(blank=True, null=True)
    recommendations_for_action = models.TextField(blank=True, null=True)

    violence = models.TextField(blank=True, null=True)
    aggression = models.TextField(blank=True, null=True)
    sexual_assault = models.TextField(blank=True, null=True)
    self_neglect = models.TextField(blank=True, null=True)
    self_harm = models.TextField(blank=True, null=True)
    risk_to_property = models.TextField(blank=True, null=True)
    substance_abuse = models.TextField(blank=True, null=True)
    risk_to_other_guests = models.TextField(blank=True, null=True)
    risk_to_volunteers = models.TextField(blank=True, null=True)
    risk_to_staff = models.TextField(blank=True, null=True)
    risk_to_public = models.TextField(blank=True, null=True)
    risk_to_minors = models.TextField(blank=True, null=True)
    other_risks = models.TextField(blank=True, null=True)

