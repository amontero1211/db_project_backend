from django.urls import path
from . import views

urlpatterns = [
    path('artworks/',views.get_artworks),
]