from rest_framework import serializers
from .models import Usuario,Servicio


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('url','username','password') 

class ServicioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Servicio
        fields = ('url','nombre','descripcion') 


