from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostSerializer
from rest_framework import status
from django.views.generic import TemplateView

class CRUDAPIView(generics.GenericAPIView,TemplateView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    template_name = 'post/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        posts = self.get_queryset()
        serializer = PostSerializer(posts, many=True)
        context['posts_data'] = serializer.data
        print("Context Data:", context)  # Add this line to print the context data

        return context
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            post = self.get_object()
            serializer = self.get_serializer(post)
            return Response(serializer.data)
        else:
            posts = self.get_queryset()
            serializer = self.get_serializer(posts, many=True)
            return Response(serializer.data)
        
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request, *args, **kwargs):
        instance = self.get_object()
        print(instance)
        serializer = self.get_serializer(instance, data=request.data, partial = True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


CRUD_API_view = CRUDAPIView.as_view()
