from django.db import models
from django.contrib.auth.models import User

class Hub(models.Model):
    name = models.CharField(max_length=255)
    #word for using in the url than the name
    slug = models.SlugField(unique=True)

class Message(models.Model):
    hub = models.ForeignKey(Hub, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)