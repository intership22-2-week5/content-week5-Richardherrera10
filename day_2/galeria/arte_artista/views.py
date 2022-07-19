from .models import Artista, Arte, Arte_Artista, Multimedia, Portafolio, Exposicion

from rest_framework.views import Response


from rest_framework import viewsets

from .serializers import ArteSerializer, ArtistaSerializer, ArteArtistaSerializer, MultimediaSerializer, PortafolioSerializer, ExposicionSerializer

class ArteViewSet(viewsets.ModelViewSet):
  queryset = Arte.objects.all()
  serializer_class = ArteSerializer

class ArtistaViewSet(viewsets.ModelViewSet):
  queryset = Artista.objects.all()
  serializer_class = ArtistaSerializer  

class ArteArtistaViewSet(viewsets.ModelViewSet):
  queryset = Arte_Artista.objects.all()
  serializer_class = ArteArtistaSerializer  

class MultimediaViewSet(viewsets.ModelViewSet):
  queryset = Multimedia.objects.all()
  serializer_class = MultimediaSerializer  

class PortafolioViewSet(viewsets.ModelViewSet):
  queryset = Portafolio.objects.all()
  serializer_class = PortafolioSerializer  

class ExposicionViewSet(viewsets.ModelViewSet):
  queryset = Portafolio.objects.all()
  serializer_class = ExposicionSerializer  