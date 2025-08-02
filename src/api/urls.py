# src/api/urls.py
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from rest_framework.routers import DefaultRouter
from .views import ProfissionalViewSet, ConsultaViewSet



router = DefaultRouter()
router.register(r'profissional', ProfissionalViewSet)
router.register(r'consulta', ConsultaViewSet)

urlpatterns = [
    path('', include(router.urls)),
     path('i18n/', include('django.conf.urls.i18n')), 
]
