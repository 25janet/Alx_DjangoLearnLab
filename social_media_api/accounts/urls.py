from django.urls import path
from .views import RegisterView,LoginView,ProfileView,follow_user, unfollow_user

urlpatterns = [
    path("register/", RegisterView.as_view(), name = "register_view"),
    path("login/", LoginView.as_view(),name="login_view"),
    path("profile/", ProfileView.as_view(),name="profile_view"),
    path('follow/<int:user_id>/', follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow_user'),
]