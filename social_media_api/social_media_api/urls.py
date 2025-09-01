"""
URL configuration for social_media_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .views import home

@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        "accounts": "/api/accounts/",
        "posts": "/api/posts/",
        "notifications" : "api/notifications/",
    })

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("api/accounts/", include("accounts.urls")),
    path("api/posts/", include("posts.urls")),
    path("api/notifications/",include("notifications.urls")),
    path("api/", api_root),  # API root
    path("", api_root),      # Root URL also points to API root
]
