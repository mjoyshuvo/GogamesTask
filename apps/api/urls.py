from django.conf.urls import include
from django.urls import path

app_name = 'Api'

urlpatterns = [
    path('', include('apps.game.urls', 'game-api')),
]
