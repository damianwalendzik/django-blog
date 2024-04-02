from django.db import models
from django.conf import settings
from django.db.models import Q


User = settings.AUTH_USER_MODEL


class Post(models.Model):
    # pk
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    public = models.BooleanField(default=True)