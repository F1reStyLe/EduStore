from django.urls import path
from .views import login, register, profile, logout

urlpatterns = [
    path('login/', login, name='login'),
    path('registration', register, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
]
