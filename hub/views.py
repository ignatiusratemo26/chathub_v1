#to ensure the user is logged in before joining a Hub
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Hub, Message

@login_required
def hubs(request):
    hubs = Hub.objects.all()
    return render(request, 'hub/hubs.html', {'hubs': hubs})

@login_required
def hub(request, slug):
    hub = Hub.objects.get(slug=slug)
    messages = Message.objects.filter(hub=hub)[0:25]

    return render(request, 'hub/hub.html', {'hub': hub, 'messages' : messages})