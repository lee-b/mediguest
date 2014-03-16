from django.db import models
from clients.models import Client
from datetime import datetime

class DrugUnit(models.Model):
    name = models.CharField(max_length=255, help_text="Enter the name of this unit, such as mg, l, etc.  Use metric units only.")

    def __unicode__(self):
        return self.name

class Drug(models.Model):
    name = models.CharField(max_length=255, help_text="Enter the official name of this medication")
    description = models.TextField(help_text="Describe this medication's purpose")
    units = models.ForeignKey(DrugUnit, help_text="Choose/add the units this medication is given in. If changing units, change the maximum dose, too.")
    max_dose = models.DecimalField(max_digits=7, decimal_places=3, help_text="Enter the maximum dose in the above units, that you would expect ANY client to be given in one day.  Err on the side of caution.")

    def __unicode__(self):
        return self.name + u" (" + unicode(self.units) + ")"

    @classmethod
    def check_doses(self):
        invalid_doses = []
        for drug in Drug.objects.all():
            for dosage in drug.dosages.all():
                if dosage > drug.max_dose:
                    invalid_doses.append(dosage)
        return invalid_doses

class DrugFrequency(models.Model):
    name = models.CharField(max_length=255, help_text="Enter the name of this frequency.  For example, Twice daily.")

    def __unicode__(self):
        return self.name

class DrugDose(models.Model):
    client = models.ForeignKey(Client, related_name="drug_dosages", help_text="Enter the client being given this medication.")

    drug = models.ForeignKey(Drug, related_name="dosages", help_text="Choose the medication being given")
    start_date = models.DateTimeField(default=datetime.now, help_text="The start date of the medication course.")
    end_date = models.DateTimeField(blank=True, null=True, help_text="The end date of the medication course.")
    dose = models.DecimalField(max_digits=7, decimal_places=3, help_text="Enter the dose to be given")
    frequency = models.ForeignKey(DrugFrequency, help_text="Choose/add the frequency of doses. For different schedules, create a dose separate from this one.")
    purpose = models.CharField(max_length=255, blank=True, null=True, help_text="Describe why this particular prescription was given. What did the client complain of?")

    def using_time(self):
        if self.end_date:
            end = self.end_date
        else:
            end = datetime.now()

        return end - self.start_date

    def using_time_as_str(self):
        if self.end_date:
            t = self.using_time()

            years = t.days / 365
            months = t.days % 30
            days = t.days % 30

            return u"%dy %dm %dd" % (years, months, days)
        else:
            return self.start_date.strftime(u"%Y %b %d --")

    def __unicode__(self):
        args = (
            unicode(self.client),
            unicode(self.drug),
            unicode(self.dose),
            unicode(self.drug.units),
        )
        client_dose = u": %s - %s - %s %s" % args
        return client_dose

