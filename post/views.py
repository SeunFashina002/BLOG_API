from django.shortcuts import render
from .models import Post
# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PostSerializer
from api.permissions import IsStaffIsAuthorOrReadOnly, isAuthenticatedAndCreate


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (isAuthenticatedAndCreate,) # any user can view post, only authenticated users can create post
    

class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsStaffIsAuthorOrReadOnly,) #authors can edit thier own post, #staff or super users can edit all