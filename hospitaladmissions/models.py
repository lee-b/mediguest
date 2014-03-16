from django.db import models
from clients.models import Client
from people.models import Organization
from datetime import datetime

class Hospital(Organization):
    pass

class HospitalAdmission(models.Model):
    client = models.ForeignKey(Client, help_text="The client who was the subject of this hospital admission.")
    hospital = models.ForeignKey(Hospital, help_text="Which hospital the client was admitted to.")

    admission_date = models.DateTimeField(default=datetime.now, help_text="The date of admission, without breaks. Make a separate admission for other periods.")
    reason = models.TextField(blank=True, null=True, help_text="The reason for the client's admission to hospital.")

    checkout_date = models.DateTimeField(blank=True, null=True, help_text="The date when the client was discharged/left hospital.  Leave blank if ongoing.")
    exit_notes = models.TextField(blank=True, null=True, help_text="Enter any notes regarding the client's discharge or leaving. Did the doctor recommend anything, for instance?")

    def duration(self):
        return (self.checkout_date - self.admission_date)

    def pretty_duration(self):
        dur = self.duration()

        days = dur.days
        hours = dur.seconds / 3600

        return u"%dd %.1fh" % (days, hours)
