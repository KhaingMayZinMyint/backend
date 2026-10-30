from django.shortcuts import render

from .models import *
from rest_framework import viewsets
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset =User.objects.all()
    serializer_class = UserSerializer

class CategoryViewSet(viewsets.ModelViewSet):
     queryset =Category.objects.all()
     serializer_class = CategorySerializer

     
class PostViewSet(viewsets.ModelViewSet):
    queryset =Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset =Comment.objects.all()
    serializer_class = CommentSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset =UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset =Tag.objects.all()
    serializer_class = TagSerializer

class PostTagViewSet(viewsets.ModelViewSet):
    queryset =PostTag.objects.all()
    serializer_class = PostTagSerializer

class PostLikeViewSet(viewsets.ModelViewSet):
    queryset =PostLike.objects.all()
    serializer_class = PostLikeSerializer
# Create your views here.