# Generated by Django 5.1.6 on 2025-02-22 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banco_dados', '0002_usuario_datanascimento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='dataNascimento',
        ),
    ]
