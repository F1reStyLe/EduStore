from django.urls import path
from .views import login, register, profile

urlpatterns = [
    path('login/', login, name='login'),
    path('registration', register, name='registration'),
    path('profile/', profile, name='profile'),
]
