from django.urls import path
from . import views
from .views import register_view, login_view, logout_view
def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

urlpatterns = [
    path('', views.register_view),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
]
