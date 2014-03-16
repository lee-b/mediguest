from django.db import models
from datetime import datetime
from clients.models import Client
from decimal import Decimal
from django.contrib.auth.models import User
from booking.models import Booking

class ServiceChargeType(models.Model):
    name = models.CharField(max_length=255)
    include_on_control_sheet = models.BooleanField(default=True, help_text="Should this service charge be listed on the control sheet, for financial reports?")

    def __unicode__(self):
        return self.name

class ServiceCharge(models.Model):
    client = models.ForeignKey(Client, related_name="service_charges")
    authorizing_ssw = models.ForeignKey(User, related_name="service_charges_authorized", blank=True, null=True, help_text="Senior support worker who authorised the charge.")
    date_charged = models.DateTimeField(default=datetime.now)
    related_booking = models.ForeignKey(Booking, blank=True, null=True, help_text="If this service charge is associated with a room booking, enter the booking here.", related_name="service_charges")
    type = models.ForeignKey(ServiceChargeType)
    amount = models.DecimalField(max_digits=9, decimal_places=5)
    comments = models.CharField(max_length=255, blank=True, null=True)

    def amount_paid(self):
        amt = Decimal(0.0)
        for p in self.payments.all():
            amt += p.amount
        return amt

    def amount_outstanding(self):
        return self.amount - self.amount_paid()

    def last_payment_date(self):
        if self.payments.count() > 0:
            return self.payments.order_by('-date_paid')[0].date_paid.date()
        else:
            return None

    def paid_in_full(self):
        paid = self.amount_paid()
        return paid >= self.amount

    def __unicode__(self):
        return unicode(self.date_charged) + u" " + unicode(self.client) + u": \u00A3%.2f" % self.amount + u" (%s) [%s] " % (self.comments, self.type)

class ServiceChargePayment(models.Model):
    client = models.ForeignKey(Client, related_name="service_charge_payments")
    service_charge = models.ForeignKey(ServiceCharge, related_name="payments")
    date_paid = models.DateTimeField(default=datetime.now)
    amount = models.DecimalField(max_digits=9, decimal_places=5, help_text="How much was paid by the client.  Enter negative a amount for a refund.")
    comments = models.TextField(blank=True, null=True)

    def payment_no(self):
        """Return a payment number offset from 19999, to
        avoid confusion with payments from previous system
        """
        return self.id + 19999

    def __unicode__(self):
        return unicode(self.id) + u": " + unicode(self.service_charge.client) + u": \u00A3%.2f" % self.amount

