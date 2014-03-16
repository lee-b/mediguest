from django.db import models
from addresses.models import *

class Person(models.Model):
	gender_choices = (
		('m', 'Male'),
		('f', 'Female'),
		('o', 'Other')
	)

	gender = models.CharField(max_length=1, choices=gender_choices)
	title = models.CharField(max_length=6, help_text="Enter any prefixes/honorifics, such as Dr. or Rev.")
	forenames = models.CharField(max_length=255, blank=True, null=True, help_text="Enter any/all forenames, in order.")
	surnames = models.CharField(max_length=255, help_text="Enter the person's CURRENT surname, or surnames if double-barrelled. Do not include previous surnames here.")
	suffix = models.CharField(max_length=16, blank=True, null=True, help_text="Enter any suffixes, such as Jr.")
	nee = models.CharField(max_length=255, blank=True, null=True, help_text="Enter person's the previous surname or maiden name, if any")
	date_of_birth = models.DateField(blank=True, null=True, help_text="Enter the person's date of birth, if known")

	address = models.ForeignKey(Address, blank=True, null=True, help_text="Choose/Add the person's address")

	phone_no = models.CharField(max_length=32, blank=True, null=True, help_text="Enter the person's phone number, if known")
	mobile_phone_no = models.CharField(max_length=32, blank=True, null=True, help_text="Enter the person's mobile phone number, if known")

	def __unicode__(self):
		full_name = u""
		full_name += self.title + u" " + self.forenames + u" " + self.surnames + u" " + self.suffix
		return full_name

class Organization(models.Model):
	name = models.CharField(max_length=255, help_text="Official name of this organisation")
	members = models.ManyToManyField(Person, through='OrganizationMember', help_text="Members of the organisation")

	def __unicode__(self):
		return self.name
	address = models.ForeignKey(Address)

class OrganizationMember(models.Model):
	organization = models.ForeignKey(Organization)
	member = models.ForeignKey(Person)

	def __unicode__(self):
		return unicode(self.member) + " (" + unicode(self.organization) + ")"

