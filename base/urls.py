from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='base'),
    path('login/', Login.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
]
