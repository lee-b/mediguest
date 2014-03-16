from django.db import models
from clients.models import Client
from datetime import datetime
from keywork.models import Keyworker

class SupportPlanReview(models.Model):
    client = models.ForeignKey(Client)
    keyworker = models.ForeignKey(Keyworker, blank=True, null=True)
    review_date = models.DateTimeField(default=datetime.now)
    outline_of_previous_goals = models.TextField()
    how_goals_were_achieved = models.TextField()
    notes_on_discussion = models.TextField()

