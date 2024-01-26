# Generated by Django 4.2 on 2023-12-31 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='datosPersonales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('domicilio', models.CharField(max_length=500, verbose_name='Domicilio')),
                ('identificacion', models.CharField(max_length=100, verbose_name='Identificacion')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo')),
            ],
        ),
        migrations.CreateModel(
            name='datosPublicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_actual', models.DateField()),
                ('red_social', models.CharField(max_length=100, verbose_name='Red Social')),
                ('url', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='menu_lateral',
        ),
    ]
