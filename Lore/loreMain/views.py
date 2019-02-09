from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.template import loader

from .models import InterestedUsers

# Create your views here.

def index(request):
    template = loader.get_template('loreMain/index.html')
    return HttpResponse(template.render({}, request))
    #return render(request, 'loreMain/index.html', {})

def landing(request):
	template = loader.get_template('loreMain/landing.html')
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
    return HttpResponse(template.render({}, request))
    