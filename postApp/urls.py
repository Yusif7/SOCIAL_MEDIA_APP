from django.urls import path
from . import views

app_name = 'postApp'

urlpatterns = [
    path('create/', views.post_create, name='post_create'),
]
