from django.db import models
from people.models import Person, Organization

class GP(Person):
    class Meta:
        verbose_name_plural = "General Practitioners"

class HealthProvider(Organization):
    pass

