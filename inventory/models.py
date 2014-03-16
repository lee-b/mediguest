from django.db import models
from booking.models import Room

class InventoryItemType(models.Model):
    name = models.CharField(max_length=255, help_text="Name this item type. For example: Philips Dayglo Lamp, or Rooster alarm clock")
    stock_level = models.IntegerField(default=0, help_text="How many are currently in stock.")
    reorder_level = models.IntegerField(default=0, help_text="The minimum number that should be kept available for immediate use.")
    reorder_amount = models.IntegerField(blank=True, null=True, help_text="How many should be re-ordered at once, when stock runs low?")

    def __unicode__(self):
        return self.name

class InventoryCondition(models.Model):
    name = models.CharField(max_length=255, help_text="Name this condition. For example: Brand new, Minor Scratches, Not working, etc.")

    def __unicode__(self):
        return self.name

class InventoryItem(models.Model):
    item_type = models.ForeignKey(InventoryItemType, help_text="Choose/add which type of item this is")
    identifier = models.CharField(max_length=255, help_text="Enter something that uniquely identifies this item, such as its serial number")
    condition = models.ForeignKey(InventoryCondition, default=1, help_text="Choose/add this item's current condition")
    notes = models.TextField(blank=True, null=True, help_text="Add any notes about this item, such as 'scraped on the left side', why it doesn't work, when the repairman is coming to fix it, etc.")
    location = models.ForeignKey(Room, help_text="Where this item is CURRENTLY located. Do not enter where it is intended to go, until it gets there.")

    def __unicode__(self):
        return "%s - %s" % (unicode(self.item_type), self.identifier)

