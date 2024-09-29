from django.urls import path
from . views import get_music_recommendations

urlpatterns = [
    path("", get_music_recommendations, name = "get_recommendations")
]

