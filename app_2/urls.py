from django.urls import path
from rest_framework.routers import DefaultRouter

from app_2.views import BookViewSet

urlpatterns = [
]

router = DefaultRouter()

router.register(r'books', viewset=BookViewSet, basename='book')
urlpatterns += router.urls

