from datetime import datetime
from decimal import Decimal
from django.db import models
from people.models import Person
from agencyservices.models import GP
from keywork.mod.keyworker import Keyworker
from faiths.models import Religion
from easy_thumbnails.fields import ThumbnailerImageField
from validators import nat_ins_validator

class Client(Person):
    _img_upload_path = 'client_photos'

    last_updated = models.DateTimeField(auto_now=True, editable=False, help_text="When this record was last updated")

    photo = ThumbnailerImageField(
        upload_to=_img_upload_path,
        help_text="Please upload a photo of this client.",
    )

    client_pack_agreed = models.NullBooleanField(null=True, blank=True, help_text="Whether the client has agreed to the client pack (and you have obtained a signature)")

    # medical details
    national_insurance_no = models.CharField(max_length=9, blank=True, null=True, unique=True, validators=[nat_ins_validator], help_text="Enter the client's national insurance number, without dashes or spaces")
    gp = models.ForeignKey(GP, related_name="patients", blank=True, null=True, help_text="Select or add the client's GP/family doctor")
    assigned_keyworker = models.ForeignKey(
        Keyworker,
        related_name="clients",
        blank=True, null=True,
        help_text="To OVERRIDE the default keyworker for the client's room, specify a keyworker here.  Otherwise, keep leave blank.",
    )
    disabled_reg_no = models.CharField(max_length=255, blank=True, null=True, help_text="If disabled, enter the client's disabled registration number here")
    contact_next_of_kin = models.NullBooleanField(help_text="Whether the client next of kin should be contacted in an emergency")
    next_of_kin = models.ForeignKey(Person, blank=True, null=True, related_name="nok_relations", help_text="Choose/add a family member to contact in emergencies")

    medical_problems = models.TextField(blank=True, null=True, help_text="Describe any general medical problems here")
    mobility_problems = models.TextField(blank=True, null=True)

    assistance_required = models.TextField(blank=True, null=True)

    # statistical details
    presented_as_homeless = models.NullBooleanField(help_text="When the client first presented theirself to the hostel, were they homeless?")
    religion = models.ForeignKey(Religion, blank=True, null=True, help_text="Choose or add the client's religion, if any")
    ethnic_origin_choices = (
        ('azin',            'Asian'),
        ('afrn',            'African'),
        ('blak',            'Black'),
        ('breu',            'British / European'),
        ('crbn',            'Caribbean'),
        ('irsh',            'Irish'),
        ('seaz',            'South East Asian'),
        ('whit',            'White'),
        ('mixd',            'Mixed'),
        ('othr',            'Other'),
    )

    ethnic_origin = models.CharField(
        max_length=4, choices=ethnic_origin_choices,
        help_text="Enter the client's racial background (for equality monitoring)",
    )

    # methods
    def keyworker(self):
        if self.assigned_keyworker:
            return self.assigned_keyworker
        else:
            booking = self.latest_booking()
            if booking:
                return booking.room.keyworker
            else:
                return None

    def latest_booking(self):
        return self.booking_set.latest()

    def earliest_booking(self):
        bookings = self.booking_set.all()
        if len(bookings) > 0:
            return bookings.reverse()[0]
        else:
            return None

    def subsequent_admissions(self):
        bookings = self.booking_set.all()
        return bookings[1:]

    def first_admission_date(self):
        b = self.earliest_booking()
        if b:
            return b.start_date
        else:
            return None

    def first_booked_in_by(self):
        b = self.earliest_booking()
        if b:
            return b.made_by
        else:
            return None

    def booking_out_date(self):
        b = self.latest_booking()
        if b:
            return b.end_date
        else:
            return None

    def reason_for_leaving(self):
        b = self.latest_booking()
        if b:
            return b.reason_for_leaving
        else:
            return None

    def initials(self):
        forenames = self.forenames.split(' ')
        surnames = self.surnames.split(' ')
        inits = []
        for f in forenames:
            inits.append(f[0])
        for s in surnames:
            inits.append(s[0])
        return "".join(inits)

    def current_medications(self):
        return self.drug_dosages.all().filter(end_date__isnull=True)

    def previous_medications(self):
        return self.drug_dosages.all().filter(end_date__isnull=False)

    def get_absolute_url(self):
        return "/clients/%d/" % self.id

    def get_edit_url(self):
        return "/admin/clients/client/%d/" % self.id

    def reference_no(self):
        # FIXME: should probably remove this and just use .id, but confirm
        # that reference_no is the same thing first
        return self.id

    def room(self):
        booking = self.booking_set.latest()
        if (booking is None or booking.end_date is not None):
            return None

        return booking.room

    def is_sched1(self):
        # TODO: this is just an example for now
        return True

    def last_booking(self):
        ended_bookings = self.booking_set.all().filter(end_date__isnull=False).order_by('-end_date')
        if len(ended_bookings) > 0:
            return ended_bookings[0]
        else:
            return None

    def object_notices(self):
        notices = []

        if self.is_sched1():
            notices.append(u"Schedule 1")

        service_charge_arrears = self.service_charge_arrears()
        if service_charge_arrears > Decimal("0.00"):
            arrears = u"Service charge arrears: &pound;%.2f" % service_charge_arrears
            notices.append(arrears)

        return notices

    def service_charge_arrears(self):
        """Calculate service charges remaining, from outstanding
        debt records"""

        amt = Decimal("0.0")

        for sc in self.service_charges.all():
            amt += sc.amount_outstanding()

        return amt

    def direct_to_crash_or_room(self):
        return True

    def crash_to_bed(self):
        return True

    def booking_out(self):
        latest_booking = self.latest_booking()
        if latest_booking:
            return latest_booking.end_date is not None
        return False

    def booking_in(self):
        latest_booking = self.latest_booking()
        if latest_booking:
            return latest_booking.end_date is None
        return False

