from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.landing, name='landing'),
    path('subscribe_email', views.post_email, name='subscribe_email'),
    path('story/<int:story_id>', views.get_story, name='get_story')

]