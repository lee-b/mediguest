from django.db import models
from datetime import datetime
from clients.models import Client

class ConvictionType(models.Model):
    name = models.CharField(max_length=255, help_text="Enter the official name of this conviction type")

    def __unicode__(self):
        return self.name

class Conviction(models.Model):
    client = models.ForeignKey(Client, help_text="The client who has been given this conviction")
    conviction_type = models.ForeignKey(ConvictionType, help_text="Choose/add the type of conviction")
    conviction_date = models.DateField(default=datetime.now, help_text="Choose/add the date when the conviction was given")

    def __unicode__(self):
        args = (
            self.client,
            self.conviction_date.strftime("%Y/%b/%d"),
            self.conviction_type,
        )
        return u"%s - %s - %s" % args

