# Generated by Django 5.1.2 on 2024-11-18 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attention', '0004_costoatenciondetalle_alter_costosatencion_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='horarioatencion',
            options={'verbose_name': 'Horario de Atención del Doctor', 'verbose_name_plural': 'Horarios de Atención de los Doctores'},
        ),
        migrations.RenameField(
            model_name='horarioatencion',
            old_name='Intervalo_desde',
            new_name='intervalo_desde',
        ),
        migrations.RenameField(
            model_name='horarioatencion',
            old_name='Intervalo_hasta',
            new_name='intervalo_hasta',
        ),
    ]