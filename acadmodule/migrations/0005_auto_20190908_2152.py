# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-09-08 16:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acadmodule', '0004_auto_20190908_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='btechcurriculum',
            name='sem1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Semester1', to='acadmodule.BatchSemester'),
        ),
        migrations.AlterField(
            model_name='btechcurriculum',
            name='sem2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Semester2', to='acadmodule.BatchSemester'),
        ),
        migrations.AlterField(
            model_name='btechcurriculum',
            name='sem3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Semester3', to='acadmodule.BatchSemester'),
        ),
        migrations.AlterField(
            model_name='btechcurriculum',
            name='sem4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Semester4', to='acadmodule.BatchSemester'),
        ),
        migrations.AlterField(
            model_name='btechcurriculum',
            name='sem5',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Semester5', to='acadmodule.BatchSemester'),
        ),
        migrations.AlterField(
            model_name='btechcurriculum',
            name='sem6',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Semester6', to='acadmodule.BatchSemester'),
        ),
        migrations.AlterField(
            model_name='btechcurriculum',
            name='sem7',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Semester7', to='acadmodule.BatchSemester'),
        ),
        migrations.AlterField(
            model_name='btechcurriculum',
            name='sem8',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Semester8', to='acadmodule.BatchSemester'),
        ),
    ]
