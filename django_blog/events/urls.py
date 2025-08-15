from django.urls import path
from django.shortcuts import render

def events_view(request):
    return render(request, 'events.html')

urlpatterns = [
    path('', events_view, name='events'),  # /events/
]
