from rest_framework import serializers
from .models import *


error_messages = {'incorrect_type': 'El tipo de dato enviado en la categoría es incorrecto',
                  'does_not_exist': 'No se puede guardar información con la categoría seleccionada',
                  'not_found_cat': 'La categoria seleccionada no existe',                  
                }

class catSer(serializers.ModelSerializer):
    class Meta:
        model = categorias
        fields = ('nombre',)
        extra_kwargs = {'nombre': {'required': False}}


class contMenuSer(serializers.ModelSerializer):

    categoria = catSer()

    class Meta:
        model = contenido
        fields = ['id','categoria','titulo','empresa','descripcion','fechaInicio','fechaFin','estado','nota','tipoNota']
#        fields = ['id', 'tipoContenido', 'titulo', 'empresa', 'descripcion', 'fechaInicio', 'fechaFin', 'estado', 'nota', 'tipoNota']

#    def update(self, instance, validated_data):
#        tipo_contenido_data = validated_data.pop('tipoContenido', None)

#        instance.titulo = validated_data.get('titulo', instance.titulo)
#        instance.empresa = validated_data.get('empresa', instance.empresa)
#        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
#        instance.fechaInicio = validated_data.get('fechaInicio', instance.fechaInicio)
#        instance.fechaFin = validated_data.get('fechaFin', instance.fechaFin)
#        instance.estado = validated_data.get('estado', instance.estado) 
#        instance.nota = validated_data.get('nota', instance.nota)
#        instance.tipoNota = validated_data.get('tipoNota', instance.tipoNota) 

#        instance.save()

#        return instance


    def create(self, validated_data):
        categoria_data = validated_data.pop('categoria', None)
        
        # Crear una nueva instancia de contenido
        contenido_instance = contenido.objects.create(**validated_data)

        # Asociar la categoría existente a la nueva instancia
        if categoria_data:
            categoria_instance, created = categorias.objects.get_or_create(**categoria_data)
            contenido_instance.tipoContenido = categoria_instance
            contenido_instance.save()

        return contenido_instance


    def update(self, instance, validated_data):
        categoria_data = validated_data.pop('categoria', None)

        # Actualizar campos del contenido
        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.empresa = validated_data.get('empresa', instance.empresa)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.fechaInicio = validated_data.get('fechaInicio', instance.fechaInicio)
        instance.fechaFin = validated_data.get('fechaFin', instance.fechaFin)
        instance.estado = validated_data.get('estado', instance.estado) 
        instance.nota = validated_data.get('nota', instance.nota)
        instance.tipoNota = validated_data.get('tipoNota', instance.tipoNota)

        # Guardar los cambios en el contenido
        instance.save()

        # Asociar la categoría existente a la instancia actualizada
        if categoria_data:
            categoria_instance, created = categorias.objects.get_or_create(**categoria_data)
            instance.tipoContenido = categoria_instance
            instance.save()

        return instance

