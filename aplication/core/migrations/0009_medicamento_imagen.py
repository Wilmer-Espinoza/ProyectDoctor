# Generated by Django 5.1.2 on 2024-11-16 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_doctor_direccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicamento',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='medicamentos/', verbose_name='Imagen'),
        ),
    ]
