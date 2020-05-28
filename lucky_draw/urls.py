from lucky_draw.views.viewsets import *
from rest_framework.routers import DefaultRouter
from django.urls import path
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'contestants', ContestantViewSet, basename='contestant')
router.register(r'events', EventViewSet, basename='event')
router.register(r'draws', DrawViewSet, basename='draw')
router.register(r'prizes', PrizeViewSet, basename='prize')

urlpatterns = router.urls
