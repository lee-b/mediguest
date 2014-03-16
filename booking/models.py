from django.db import models
from clients.models import Client
from django.contrib.auth.models import User
from datetime import datetime
from decimal import Decimal
from keywork.mod.keyworker import Keyworker

class RoomType(models.Model):
    class Meta:
        ordering = ('name',)

    code = models.CharField(max_length=1, help_text="Single-letter code for this type of room.  For example, crash beds might use C or B, storage rooms: S, etc. Consult organisation policy.")
    name = models.CharField(max_length=255, help_text="Name of this room type")
    daily_rate = models.DecimalField(max_digits=10, decimal_places=5, default=Decimal("0.00"), help_text="Daily charge for this room type")
    is_client_room = models.BooleanField(default=False, help_text="Whether this room can be used by clients.  For example, storage rooms and offices cannot.")

    def plural_name(self):
        return self.name + u"s"

    def first_rooms_inline(self):
        first_rooms = self.room_set.all()[:3]
        first_room_names = [ unicode(r) for r in first_rooms ]
        first_rooms_inline_str = u", ".join(first_room_names)
        return first_rooms_inline_str

    def last_room(self):
        # FIXME: django doesn't support negative indexing on querysets, so this is the inefficient way.  Find another.
        tmp_list = list(self.room_set.all())
        return unicode(tmp_list[-1:][0])

    def as_example(self):
        return self.first_rooms_inline() + u"..." + self.last_room()

    def __unicode__(self):
        return self.name + " (" + self.code + ")"

class Room(models.Model):
    class Meta:
        ordering = ('type', 'number')

    type = models.ForeignKey(RoomType, help_text="Choose the which type of room this is.")
    number = models.IntegerField(help_text="Room number")
    keyworker = models.ForeignKey(Keyworker, help_text="Keyworker assigned to this room.  NOTE: For changes specific to one client, override in the client's details.")

    def __unicode__(self):
        return self.type.code + unicode(self.number)

class Booking(models.Model):
    class Meta:
        get_latest_by = 'start_date'

    client = models.ForeignKey(Client, help_text="Client who was/is booked in.")
    made_by = models.ForeignKey(User, help_text="Which staff member made, or is making, the booking")
    room_choice_filter = {
        'type__is_client_room': True,
    }
    room = models.ForeignKey(Room, limit_choices_to=room_choice_filter, help_text="Which room the client is booked into")

    rules_read = models.NullBooleanField(help_text="Have the rules (from the client pack) been read to this client?")

    start_date = models.DateTimeField(default=datetime.now, help_text="When the booking began")
    end_date = models.DateTimeField(blank=True, null=True, help_text="When the booking ended.  Leave blank if still resident.")

    reason_for_leaving = models.TextField(blank=True, null=True, help_text="Why the client booked out.  Leave blank if still resident.")

    def days_stayed(self):
        if self.end_date:
            date_diff = self.end_date - self.start_date
        else:
            date_diff = datetime.now() - self.start_date
        num_days = date_diff.days
        return num_days

    def total_payable(self):
        # FIXME: what IS this?!
        #        should probably generate it from a foreignkey on ServiceCharge
        #        to Booking.  -- ServiceCharges accrued during a given stay, in
        #        other words.
        num_days = self.days_stayed()
        amt = self.room.type.daily_rate * num_days
        return amt

    def __unicode__(self):
        desc = unicode(self.client) + " booked into " + unicode(self.room) + " from " + unicode(self.start_date)
        if (self.end_date):
            desc += " to " + unicode(self.end_date)
        else:
            desc += " (ongoing)"
        return desc

