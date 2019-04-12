from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.landing, name='landing'),
    path('subscribe_email', views.post_email, name='subscribe_email'),
    path('story/<int:story_id>', views.get_story, name='get_story'),
    path('storymap', views.storymap, name='storymap'),
    path('sms', views.sms, name='sms'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)