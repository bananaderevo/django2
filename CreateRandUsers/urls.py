from django.urls import path

from . import views

app_name = 'CreateRandUsers'
urlpatterns = [
    path('', views.create, name='create'),
]
