from django.db import models

class Hub(models.Model):
    name = models.CharField(max_length=255)
    #word for using in the url than the name
    slug = models.SlugField(unique=True)
