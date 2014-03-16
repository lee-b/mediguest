from django.db import models

class Religion(models.Model):
    name = models.CharField(max_length=255, help_text="Enter the name of this faith")

    def __unicode__(self):
        return self.name
