from django.db import models
from datetime import datetime


# Create your models here.

class InterestedUsers(models.Model):
    email_id = models.CharField(max_length=50, unique=True)
    signedup_timestamp = models.DateTimeField(default=datetime.now)