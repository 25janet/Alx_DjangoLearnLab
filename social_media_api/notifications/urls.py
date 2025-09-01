from django.urls import path
from .views import NotificationListView,notifications_landing

urlpatterns = [
    path("", NotificationListView.as_view(), name="notifications"),
    path("", notifications_landing, name="notifications_landing"),  
    path("list/", NotificationListView.as_view(), name="notifications_list"),
]

