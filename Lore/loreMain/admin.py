from django.contrib import admin

# Register your models here.

from .models import InterestedUsers, Story, StoryChapters

admin.site.register(InterestedUsers)
admin.site.register(Story)
admin.site.register(StoryChapters)