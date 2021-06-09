from django.urls import path

from . import views

app_name = 'person'
urlpatterns = [
    path('', views.create, name='create'),
    path('<int:pk>', views.UpdateDetailView.as_view(), name='update'),
]
