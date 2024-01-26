from django.db import models

# Create your models here.

class datosPersonales(models.Model):

    nombre = models.CharField(max_length=100,verbose_name="Nombre")
    edad=models.IntegerField(verbose_name='Edad')
    domicilio = models.CharField(max_length=500,verbose_name="Domicilio")
    identificacion=models.CharField(max_length=100,verbose_name='Identificacion')
    correo=models.EmailField(verbose_name='Correo')

    def __str__(self):
        return self.nombre
    
    class Meta:
        app_label = 'blog'

class datosPublicos(models.Model):
    fecha_actual=models.DateField()
    red_social=models.CharField(max_length=100,verbose_name='Red Social')
    url=models.URLField()

    def __str__(self):
        return self.red_social
    
    class Meta:
        app_label = 'blog'


class contenido_menu(models.Model):
    titulo = models.CharField(max_length=200,verbose_name="titulo")
    sub_titulo = models.CharField(max_length=100,verbose_name="titulo")
    descripcion = models.CharField(max_length=500,verbose_name="descripcion titulo",null=True)


    def __str__(self):
        return self.titulo

    class Meta:
        app_label = 'blog'


class categorias(models.Model):
    cod_categoria=models.CharField(max_length=50,verbose_name='Codigo Categoria')
    nombre=models.CharField(max_length=150,verbose_name='Categoria')    

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'blog'


class contenido(models.Model):
    tipoContenido = models.ForeignKey(categorias, on_delete=models.CASCADE, verbose_name="Categoria")
    titulo = models.CharField(max_length=100,verbose_name="Titulo")
    empresa=models.CharField(max_length=150,verbose_name='Empresa/Institucion',null=True,blank=True)
    descripcion = models.CharField(max_length=500,verbose_name="Descripcion")
    fechaInicio=models.DateField(null=True,blank=True)
    fechaFin=models.DateField(null=True,blank=True)
    estado=models.CharField(max_length=50,verbose_name="Estado")
    nota=models.IntegerField(null=True,blank=True)
    tipoNota=models.CharField(max_length=100,verbose_name="Tipo Nota", null=True,blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = 'blog'

