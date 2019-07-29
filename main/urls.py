from django.conf.urls import url, include
from rest_framework import routers
from main.views import UserViewSet, CycleInfoViewSet, PostViewSet, CommentViewSet, ChatViewSet, MessageViewSet, FriendViewSet, UserProfileViewSet, CycleViewSet
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt

from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import NestedRouterMixin
from rest_framework_nested import routers
from . import views

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'cycles', CycleViewSet)
router.register(r'cycleinfos', CycleInfoViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'chats', ChatViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'friends', FriendViewSet)
router.register(r'userprofiles', UserProfileViewSet)


users_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
users_router.register(r'profile', UserProfileViewSet, basename="userprofile")

usercycleinfo_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
usercycleinfo_router.register(r'cycleinfo', CycleInfoViewSet, base_name='usercycleinfo')

userposts_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
userposts_router.register(r'posts', PostViewSet, base_name='userpost')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration', include('rest_auth.registration.urls')),
    #  url(r'^rest-auth/', include('rest_auth.urls')),
    # url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
    path('', include(users_router.urls)),
    path('', include(usercycleinfo_router.urls)),
    path('', include(userposts_router.urls)),
]


# class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
#     pass

# router = NestedDefaultRouter()

# users_router = router.register('users', UserViewSet)
# users_router.register(
#     'userprofile',
#     UserProfileViewSet,
#     basename='userprofile',
#     parents_query_lookups=['user'])