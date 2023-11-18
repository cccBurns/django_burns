# Generated by Django 4.2.7 on 2023-11-18 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Placa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=250)),
                ('fecha_creacion', models.DateField()),
            ],
        ),
    ]
