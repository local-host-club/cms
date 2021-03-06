# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 20:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('edu', '0003_auto_20161124_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluacion',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='creador_por',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='estrategia',
            field=models.TextField(default='Estrategia de la evaluación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='nombre',
            field=models.CharField(default='Evaluación', max_length=140),
            preserve_default=False,
        ),
    ]
