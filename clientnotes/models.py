from django.db import models
from clients.models import Client
from datetime import datetime

class ClientNote(models.Model):
    client = models.ForeignKey(Client, help_text="Which client this note is regarding")
    date = models.DateTimeField(default=datetime.now, help_text="When this note was made")
    note = models.TextField()

