from django.urls import path
from .views import active


urlpatterns = [
    path("active/", active),
]