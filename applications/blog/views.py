from django.shortcuts import render
from rest_framework import generics,status
from .models import *
from .serializers import *
from django.http import JsonResponse
from rest_framework.views import APIView
from .baseViews import *
from django.http import Http404
import logging
from django.shortcuts import get_object_or_404
from rest_framework.response import Response



logger = logging.getLogger(__name__)


error_messages = {'incorrect_type': 'El tipo de dato enviado en la categoría es incorrecto',
                  'does_not_exist': 'No se puede guardar información con la categoría seleccionada',
                  'not_found_cat': 'La categoria seleccionada no existe',                  
                }

def indexPage(request):
    return render(request,'blog/inicio.html')




# --vistas para api de contenido
class ContenidoMenuListCreateView(BaseJsonResponseView, generics.ListCreateAPIView):
    serializer_class = contMenuSer

    def get_queryset(self):
        return contenido.objects.all()


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if not queryset.exists():
            return self.custom_response(status="Exito", message="No se encontraron datos", code="02")

        serializer = self.get_serializer(queryset, many=True)
        return self.success_response(data=serializer.data)


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



 


class ContenidoMenuDetailView(BaseJsonResponseView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = contMenuSer

    def get_queryset(self):
        return contenido_menu.objects.all()


    def get_object(self):
        try:

            pk = self.kwargs.get(self.lookup_url_kwarg or self.lookup_field)
            return get_object_or_404(contenido, pk=pk)
        except Http404:
            return None


    def retrieve(self, request, *args, **kwargs):
        print('Entrando al metodo retrieve')
        instance = self.get_object()

        if not instance:
            return self.custom_response(status="Exito", message="No se encontraron datos", code="02")

        serializer = self.get_serializer(instance)
        return self.success_response(data=serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        nueva_categoria_id = request.data.get('categoria', {}).get('id')


        tipo_error = error_messages.get('not_found_cat','Hubo un error al enviar la petición')


        if not categorias.objects.filter(id=nueva_categoria_id).exists():
            response = self.custom_response(status="error",message=tipo_error,code="04")

            response.status_code = status.HTTP_400_BAD_REQUEST

            return response



        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        instance.tipoContenido_id = nueva_categoria_id
        instance.save()

        return self.success_response(message="Elemento actualizado correctamente")

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return self.success_response(message="Elemento eliminado correctamente")

