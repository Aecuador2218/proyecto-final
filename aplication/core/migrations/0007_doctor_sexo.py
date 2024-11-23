# Generated by Django 5.1.2 on 2024-11-04 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_paciente_cedula'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, null=True, verbose_name='Sexo'),
        ),
    ]
