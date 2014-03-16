from django.db import models
from clients.models import Client
from datetime import datetime

class BenefitType(models.Model):
    name = models.CharField(max_length=255, help_text="Enter the official name of this benefit. For example, 'Housing Benefit'")
    extra = 1

    def __unicode__(self):
        return self.name

class ReceivedBenefit(models.Model):
    client = models.ForeignKey(Client, help_text="Choose the client receiving this benefit")
    benefit_type = models.ForeignKey(BenefitType, help_text="Choose the type of benefit being received")
    start_date = models.DateTimeField(default=datetime.now, blank=True, null=True, help_text="When the client began receiving this benefit, without breaks.")
    end_date = models.DateTimeField(blank=True, null=True, help_text="When the benefit entitlement or claim ended.")
    ref_no = models.CharField(max_length=255, blank=True, null=True, help_text="Benefit-specific reference number. For example, housing benefit reference no.")
    notes = models.TextField(blank=True, null=True)

    def __unicode__(self):
        if self.end_date:
            end_date_str = self.end_date.strftime("%Y/%b/%d")
        else:
            end_date_str = u""

        args = (
            self.client,
            unicode(self.benefit_type),
            u"#%s" % self.ref_no,
            self.start_date.strftime("%Y/%b/%d"),
            end_date_str,
        )
        return u"%s - %s - %s (%s--%s)" % args

