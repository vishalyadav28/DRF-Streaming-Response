from django.urls import path
from rest_framework.routers import DefaultRouter
from streamingapp.views import StreamDataViewSet

router = DefaultRouter()
router.register('', StreamDataViewSet, basename='streamdata')

urlpatterns = router.urls
