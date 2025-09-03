from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    register, profile_view,
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView,
    CommentCreateView, CommentUpdateView, CommentDeleteView,
    search_posts, posts_by_tag

)

app_name = "blog"

urlpatterns = [
    # Authentication
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", profile_view, name="profile"),

    # Blog posts
    path("", PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/new/", PostCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/edit/", PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),

    # Comments
    path("post/<int:pk>/comment/new/", CommentCreateView.as_view(), name="comment_create"),
    path("comment/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment_update"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),
    path("search/", search_posts, name="search_posts"),
    path("tags/<str:tag_name>/", posts_by_tag, name="posts_by_tag"),
]
