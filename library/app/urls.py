from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import MyAPIView

app_name = 'authors'
urlpatterns = [
    path('', MyAPIView.as_view())
]
