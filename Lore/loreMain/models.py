from django.db import models
from datetime import datetime
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.

class InterestedUsers(models.Model):
    email_id = models.CharField(max_length=50, unique=True)
    signedup_timestamp = models.DateTimeField(default=datetime.now)

class Story(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)


class StoryChapters(MPTTModel):
    story_id = models.ForeignKey(Story, on_delete=models.CASCADE)
    chapter_number = models.IntegerField()
    chapter_title = models.CharField(max_length=100)
    prev_chapter = TreeForeignKey('self', null=True, blank=True, 
        related_name='children', db_index=True, on_delete=models.CASCADE)
    yes_chapter = models.PositiveIntegerField(null=True, blank=True)
    no_chapter = models.PositiveIntegerField(null=True, blank=True)
    #yes_chapter = models.ForeignKey('self', null=True, blank=True, 
     #   related_name='+', on_delete=models.CASCADE)
    #no_chapter = models.ForeignKey('self', null=True, blank=True, 
     #   related_name='+', on_delete=models.CASCADE)
    #prev_chapter = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE) #models.ForeignKey('StoryChapters', on_delete=models.CASCADE)
    #yes_chapter = models.IntegerField(blank=True, null=True) #models.ForeignKey('StoryChapters', on_delete=models.CASCADE)
    #no_chapter = models.IntegerField(blank=True, null=True) #models.ForeignKey('StoryChapters', on_delete=models.CASCADE)

    class MPTTMeta:
        parent_attr = 'prev_chapter'
        order_insertion_by = ['chapter_number']
        #left_attr = 'no_chapter'
        #right_attr = 'yes_chapter'

