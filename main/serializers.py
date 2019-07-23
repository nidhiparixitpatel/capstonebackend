from rest_framework import serializers
from main.models import User, CycleInfo, Post, Comment, Chat, Message, Friend, UserProfile, Cycle

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class CycleInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CycleInfo
        fields = ('id', 'user', 'menarche_date', 'average_length', 'average_duration')

class CycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cycle
        fields = ('id', 'user', 'start_date', 'end_date', 'period_length')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =  ('id', 'user', 'timestamp', 'content')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user_from', 'timestamp', 'content')

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'user_one', 'user_two')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'user_from', 'timestamp', 'content')

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'bio', 'name')