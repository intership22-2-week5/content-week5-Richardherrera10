from django.urls import path
from django.db import router

# django rest framework
from rest_framework.routers import DefaultRouter

# views
from .views import ArteViewSet, ArtistaViewSet, ArteArtistaViewSet, MultimediaViewSet, PortafolioViewSet, ExposicionViewSet

router = DefaultRouter()
# ruta y la vista que se encarga de responder al endpoint
router.register(r'arte', ArteViewSet)
router.register(r'artista', ArtistaViewSet)
router.register(r'arteartista', ArteArtistaViewSet)
router.register(r'multimedia', MultimediaViewSet)
router.register(r'portafolio', PortafolioViewSet)
router.register(r'exposicion', ExposicionViewSet)
urlpatterns = router.urls


urlpatterns += [
  
]
