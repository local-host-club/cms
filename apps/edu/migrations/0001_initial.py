# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 16:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='alumno', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Alumnos',
                'verbose_name': 'Alumno',
            },
        ),
        migrations.CreateModel(
            name='Competencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Competencias',
                'verbose_name': 'Competencia',
            },
        ),
        migrations.CreateModel(
            name='CompetenciaArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Áreas de competencias',
                'verbose_name': 'Área de competencias',
            },
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(verbose_name='descripción')),
            ],
            options={
                'verbose_name_plural': 'Evaluaciones',
                'verbose_name': 'Evaluación',
            },
        ),
        migrations.CreateModel(
            name='EvaluacionAlumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edu.Alumno')),
                ('evaluacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edu.Evaluacion', verbose_name='evaluación')),
            ],
            options={
                'verbose_name_plural': 'EvaluacionAlumnos',
                'verbose_name': 'EvaluacionAlumno',
            },
        ),
        migrations.CreateModel(
            name='EvaluacionIndicador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edu.Evaluacion')),
            ],
            options={
                'verbose_name_plural': 'Indicadores por evaluación',
                'verbose_name': 'Indicador por evaluación',
            },
        ),
        migrations.CreateModel(
            name='EvaluacionNota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ev_alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edu.EvaluacionAlumno')),
                ('ev_indicador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edu.EvaluacionIndicador')),
            ],
            options={
                'verbose_name_plural': 'Notas de evaluación',
                'verbose_name': 'Nota de evaluación',
            },
        ),
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(verbose_name='descripción')),
            ],
            options={
                'verbose_name_plural': 'Indicadores',
                'verbose_name': 'Indicador',
            },
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('porcentaje', models.PositiveIntegerField()),
                ('competencia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='edu.Competencia')),
            ],
            options={
                'verbose_name_plural': 'Niveles de competencia',
                'verbose_name': 'Nivel de competencia',
            },
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(default=1, verbose_name='número')),
                ('descripcion', models.CharField(blank=True, max_length=20, null=True, verbose_name='descripcion')),
                ('indicador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nota', to='edu.Indicador')),
            ],
            options={
                'verbose_name_plural': 'Notas',
                'verbose_name': 'Nota',
            },
        ),
        migrations.AddField(
            model_name='indicador',
            name='nivel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edu.Nivel'),
        ),
        migrations.AddField(
            model_name='evaluacionnota',
            name='ev_nota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edu.Nota'),
        ),
        migrations.AddField(
            model_name='evaluacionindicador',
            name='indicador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edu.Indicador'),
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='indicador',
            field=models.ManyToManyField(blank=True, through='edu.EvaluacionIndicador', to='edu.Indicador'),
        ),
        migrations.AddField(
            model_name='competencia',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='edu.CompetenciaArea', verbose_name='área'),
        ),
        migrations.AlterUniqueTogether(
            name='evaluacionnota',
            unique_together=set([('ev_alumno', 'ev_indicador')]),
        ),
    ]
