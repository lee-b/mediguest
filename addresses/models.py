from django.db import models
from validators import postcode_validator

class AddressCountry(models.Model):
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Address(models.Model):
    class Meta:
        verbose_name_plural = "Addresses"

    street1 = models.CharField(max_length=255)
    street2 = models.CharField(max_length=255, blank=True, null=True)
    street3 = models.CharField(max_length=255, blank=True, null=True)
    town = models.CharField(max_length=255, help_text="The village, town, or city name")
    region = models.CharField(max_length=255, help_text="The region or province. Do not use UK counties here.")
    postcode = models.CharField(max_length=9, validators=[postcode_validator], blank=True, null=True, help_text="UK postcode, US zipcode, etc.")
    country = models.ForeignKey(AddressCountry, default=1)

    def address_as_array(self):
        addr = []
        addr.append(self.street1)

        if (self.street2):
            addr.append(self.street2)

        if (self.street3):
            addr.append(self.street3)

        addr.append(self.town)
        addr.append(self.region)

        if self.postcode:
            addr.append(self.postcode)

        addr.append(unicode(self.country))

        return addr

    def address_inline(self):
        return u", ".join(self.address_as_array())

    def address_as_div(self):
        addr = '<div class="street1">'    +    self.street1        + '</div>'
        addr += '<div class="street2">'   +    self.street2        + '</div>'
        addr += '<div class="street3">'   +    self.street3        + '</div>'
        addr += '<div class="town">'      +    self.town           + '</div>'
        addr += '<div class="region">'    +    self.region         + '</div>'
        addr += '<div class="postcode">'  +    self.postcode       + '</div>'
        addr += '<div class="country">'   +    unicode(self.country)+ '</div>'
        return addr

    def __unicode__(self):
        return self.address_inline()

