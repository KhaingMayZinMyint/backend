from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .models import *
from .serializers import *

router = DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'categories',CategoryViewSet)
router.register(r'posts',PostViewSet)
router.register(r'comments',CommentViewSet)
router.register(r'userprofiles',UserProfileViewSet)
router.register(r'tags',TagViewSet)
router.register(r'posttags',PostTagViewSet)
router.register(r'postlikes',PostLikeViewSet)

urlpatterns = [
    path('',include(router.urls)),
]