# Generated by Django 4.2.7 on 2023-11-30 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0004_remove_monitor_foto_monitor_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitor',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagen'),
        ),
    ]
