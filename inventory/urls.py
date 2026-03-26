from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'components', views.ComponentViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'bom', views.BOMItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('analytics/', views.analytics, name='analytics'),
    path('trigger-low-stock/', views.trigger_low_stock_check, name='trigger-low-stock'),
]
