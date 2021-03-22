from django.urls import path, include
from .views import index

urlpatterns = [
    path('', include("djoser.urls")),
    path('', include("djoser.urls.authtoken"))
]