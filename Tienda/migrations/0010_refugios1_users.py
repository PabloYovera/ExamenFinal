# Generated by Django 3.2.6 on 2022-07-03 22:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Tienda', '0009_fundaciones'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refugios1',
            fields=[
                ('id_refugio', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID_Fundacion')),
                ('nombre_refugio', models.CharField(max_length=50, verbose_name='Nombre de Refugio')),
                ('descripcion_refugio', models.CharField(max_length=60, verbose_name='Descripcion de refugio')),
                ('subscrito', models.BooleanField(verbose_name='Nuevo')),
                ('imagen_refugio', models.ImageField(null=True, upload_to='productos')),
                ('cuenta_refugio', models.IntegerField(verbose_name='Cuenta de fundacion')),
                ('rut_refugio', models.IntegerField(verbose_name='Rut de fundacion')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donó', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Tienda.refugios1')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
