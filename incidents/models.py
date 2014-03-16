from django.db import models
from datetime import datetime
from clients.models import Client

class Incident(models.Model):
    client = models.ForeignKey(Client, help_text="Choose the client involved in this incident.")
    date = models.DateTimeField(default=datetime.now, help_text="Enter the date of the incident.")
    outline_of_incident = models.TextField(blank=True, null=True, help_text="Describe the incident")
    warning_given = models.TextField(blank=True, null=True, help_text="Record any warning(s) given to the client")
    comments = models.TextField(blank=True, null=True, help_text="Add any internal comments here.")

    def __unicode__(self):
        return unicode(self.date) + u" - " + unicode(self.client) + u": " + self.outline_of_incident[:40] + u"..."

    def incident_no(self):
        return self.id + 1999
