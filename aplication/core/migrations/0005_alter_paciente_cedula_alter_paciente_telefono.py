# Generated by Django 4.2.16 on 2024-10-28 16:30

import django.core.validators
from django.db import migrations, models
import doctor.utils


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_paciente_cedula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='cedula',
            field=models.CharField(max_length=10, unique=True, validators=[doctor.utils.valida_cedula], verbose_name='Cédula'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='telefono',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Caracteres inválidos para un número de teléfono.', regex='^\\d{9,15}$')], verbose_name='Teléfono(s)'),
        ),
    ]
