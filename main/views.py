from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
# from rest_framework.permissions import AllowAny


from main.models import User, CycleInfo, Post, Comment, Chat, Message, Friend, UserProfile, Cycle
from main.serializers import UserSerializer, CycleInfoSerializer, PostSerializer, CommentSerializer, ChatSerializer, MessageSerializer, FriendSerializer, UserProfileSerializer, CycleSerializer
# from main.permissions import IsLoggedInUserOrAdmin, IsAdminUser
# from rest_framework import generics

from rest_framework_extensions.mixins import NestedViewSetMixin

class CycleViewSet(viewsets.ModelViewSet):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['email']

# def get_permissions(self):
#         permission_classes = []
#         if self.action == 'create':
#             permission_classes = [AllowAny]
#         elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
#             permission_classes = [IsLoggedInUserOrAdmin]
#         elif self.action == 'list' or self.action == 'destroy':
#             permission_classes = [IsAdminUser]
#         return [permission() for permission in permission_classes]


class CycleInfoViewSet(viewsets.ModelViewSet):
    queryset = CycleInfo.objects.all()
    serializer_class = CycleInfoSerializer
    def get_queryset(self):
        return CycleInfo.objects.filter(user=self.kwargs['user_pk'])
  
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def get_queryset(self):
        user = self.kwargs.get("user_pk", None)
        if user: 
            return Post.objects.filter(user=user)
        else:
            return Post.objects.all()

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    def get_queryset(self):
        return UserProfile.objects.filter(user=self.kwargs['user_pk'])
    # def update(self):
    #     print("update")

# class DetailUserProfile(generics.RetrieveUpdateDestroyAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer
