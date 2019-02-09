from django.db import models
from datetime import datetime


# Create your models here.

class InterestedUsers(models.Model):
    email_id = models.CharField(max_length=50, unique=True)
    signedup_timestamp = models.DateTimeField(default=datetime.now)

class Story(models.Model):
    story_id = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

class StoryChapters(models.Model):
    story_id = models.ForeignKey(Story, on_delete=models.CASCADE)
    chapter_number = models.IntegerField()
    prev_chapter = models.IntegerField() #models.ForeignKey('StoryChapters', on_delete=models.CASCADE)
    yes_chapter = models.IntegerField() #models.ForeignKey('StoryChapters', on_delete=models.CASCADE)
    no_chapter = models.IntegerField() #models.ForeignKey('StoryChapters', on_delete=models.CASCADE)
