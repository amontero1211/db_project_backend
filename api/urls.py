from django.urls import path
from . import views

urlpatterns = [
    path('artworks/',views.get_artworks),
    path('artworks/<int:id>',views.get_artwork),
    path('artists/',views.get_artists),
    path('artists/<int:id>',views.get_artist),
    path('user',views.post_user),

]
