from collections import defaultdict 
import json 

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.template import loader

from .models import InterestedUsers, Story, StoryChapters

from twilio.twiml.messaging_response import MessagingResponse


# Create your views here.

def sms(request):
    resp = MessagingResponse()

    # Add a message
    resp.message("Ahoy! Thanks so much for your message.")

    return HttpResponse(str(resp))

def index(request):
    template = loader.get_template('loreMain/index.html')
    all_stories = Story.objects.all()
    context = {"stories" : all_stories}
    return HttpResponse(template.render(context, request))
    #return render(request, 'loreMain/index.html', {})

def landing(request):
	template = loader.get_template('loreMain/landing.html')
	return HttpResponse(template.render({}, request))

def storymap(request):
    template = loader.get_template('loreMain/storymap.html')
    return HttpResponse(template.render({}, request))

def post_email(request):
    if request.POST:
        email = request.POST['email']
        try:
            emailobj = InterestedUsers.objects.get(email_id=email)
        except InterestedUsers.DoesNotExist:
            new_interested_user = InterestedUsers(email_id=email)
            new_interested_user.save()
        return HttpResponse(204)
    return HttpResponseForbidden("Allowed Only Via Post")

def get_story(request, story_id):
    template = loader.get_template('loreMain/story.html')
    try: 
    	story_object = Story.objects.get(pk=story_id)
    except Story.DoesNotExist:
    	return HttpResponse("Uh oh, not a valid story")
    story_chapters = StoryChapters.objects.filter(story_id=story_object)
    root = StoryChapters.objects.get(story_id=story_object, depth=1, prev_chapter=None)

    depth_dict = defaultdict(list)
    bfsq = [root]
    while bfsq:
        cur = bfsq.pop()
        chapter_audio_url = ''
        chapter_question_audio_url = ''
        if cur.chapter_audio:
            chapter_audio_url = cur.chapter_audio.url 
        if cur.chapter_question_audio:
            chapter_question_audio_url = cur.chapter_question_audio.url 
        depth_dict[cur.depth].append((cur.chapter_title, chapter_audio_url, chapter_question_audio_url))
        if cur.no_chapter:
            bfsq.append(cur.no_chapter)
        if cur.yes_chapter:
            bfsq.append(cur.yes_chapter)

    context = {"story" : story_object, "chapters": story_chapters, "depth_dict": json.dumps(depth_dict)}
    return HttpResponse(template.render(context, request))
    