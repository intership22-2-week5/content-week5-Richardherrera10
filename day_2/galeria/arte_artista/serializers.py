# serializador convierte de json a dict y viceversa

#  importar django rest framework paquete serializer
from rest_framework import serializers

# models para usar en el serializer
from .models import Arte, Artista, Arte_Artista, Multimedia, Portafolio, Exposicion

# clase hereda de serializers.modelserializer
class ArteSerializer(serializers.ModelSerializer):
  # clase meta: decir que es lo que va a utilizar
  class Meta:
    model = Arte
    # datos a mostrar, todos
    fields = '__all__'

class ArtistaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Artista
    fields = '__all__'

class ArteArtistaSerializer(serializers.ModelSerializer):

  arte = serializers.PrimaryKeyRelatedField(queryset = Arte.objects.all())
  artista = serializers.PrimaryKeyRelatedField(queryset = Artista.objects.all())
  class Meta:
    model = Arte_Artista
    fields = '__all__'

  def to_representation(self,instance):
    return {
      'id':instance.id,
      'arte': {
        'id': instance.arte.id,
        'tipo': instance.arte.tipo,
        'valor': instance.arte.valor
      },
      'artista': {
        'id': instance.artista.id,
        'nombreCompleto': instance.artista.nombreCompleto,
        'edad': instance.artista.edad
      }
    }

class MultimediaSerializer(serializers.ModelSerializer):
  arte = serializers.PrimaryKeyRelatedField(queryset = Arte.objects.all())
  class Meta:
    model = Multimedia
    fields = '__all__'
  def to_representation(self,instance):
    return {
      'id':instance.id,
      'tipo': instance.tipo,
      'uri': instance.uri,
      'arte': {
        'id': instance.arte.id,
        'tipo': instance.arte.tipo,
        'valor': instance.arte.valor
      }
    }


class PortafolioSerializer(serializers.ModelSerializer):
  multimedia = serializers.PrimaryKeyRelatedField(queryset = Multimedia.objects.all())
  class Meta:
    model = Portafolio
    fields = '__all__'
  def to_representation(self,instance):
    return {
      'id':instance.id,
      'descripcion': instance.descripcion,
      'multimedia': {
        'tipo': instance.multimedia.tipo,
        'uri': instance.multimedia.uri,
      }
    }

class ExposicionSerializer(serializers.ModelSerializer):
  portafolio = serializers.PrimaryKeyRelatedField(queryset = Portafolio.objects.all())
  class Meta:
    model = Exposicion
    fields = '__all__'
  def to_representation(self,instance):
    return {
      'id':instance.id,
      'fecha': instance.fecha,
      'lugar': instance.lugar,
      'descripcion': instance.descripcion,
      'portafolio': {
        'id': instance.portafolio.id,
        'descripcion': instance.portafolio.descripcion,
      }
    }