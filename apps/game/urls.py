from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from django.urls import path
from apps.game.views import GameViewSet

app_name = 'game'

router = DefaultRouter()
router.register(r'game', GameViewSet)

urlpatterns = [
    path('', include(router.urls))
]
