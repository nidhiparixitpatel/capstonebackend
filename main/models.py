from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=40)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField()
    # friends = models.ManyToManyField(Friend)
    name = models.TextField()

class Friend(models.Model):
    users = models.ManyToManyField(UserProfile)
    current_user = models.ForeignKey(UserProfile, related_name="owner", null=True, on_delete=models.CASCADE)

      
class CycleInfo(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cycle_info')
    menarche_date = models.DateField()
    average_length = models.PositiveIntegerField()
    average_duration = models.PositiveIntegerField()

class Cycle(models.Model):
  user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE
    )
  start_date = models.DateField()
  end_date = models.DateField()
  period_length = models.PositiveIntegerField()

class Post(models.Model):
  user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE
    )
  timestamp = models.DateTimeField(auto_now_add=True)
  content = models.TextField()

class Comment(models.Model):
  post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
    )
  user_from = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
  timestamp = models.DateTimeField(auto_now_add=True)
  content = models.TextField()

class Chat(models.Model):
  user_one = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='user_one'
    )
  user_two = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='user_two'
    )

class Message(models.Model):
  user_from = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
  timestamp = models.DateTimeField(auto_now_add=True)
  content = models.TextField()


  