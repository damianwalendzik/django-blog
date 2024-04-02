from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Post

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['pk', 'user', 'title', 'content', 'public']