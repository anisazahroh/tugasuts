# skincare_shop/urls.py

from django.urls import path, include
from rest_framework import routers
from skincare.views import CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
