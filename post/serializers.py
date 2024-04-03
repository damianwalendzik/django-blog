from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Post

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    delete_url = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Post
        fields = [
            'pk',
            'detail_url',
            'edit_url',
            'delete_url',
            'user',
            'title',
            'content',
            'public',
            ]

    def get_detail_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        else:
            return reverse("post-detail",kwargs={"pk": obj.pk},request=request)
    
    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        else:
            return reverse("post-patch",kwargs={"pk": obj.pk},request=request)
    
    def get_delete_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        else:
            return reverse("post-delete",kwargs={"pk": obj.pk},request=request)