# Generated by Django 4.1.3 on 2022-12-11 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0004_aseguradora'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auto_Buscado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_comprador', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('dni', models.CharField(max_length=20)),
                ('celular', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Vendedor',
        ),
    ]