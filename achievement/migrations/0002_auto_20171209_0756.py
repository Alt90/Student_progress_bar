# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-09 07:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('achievement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название группы')),
            ],
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['name'], 'verbose_name': 'Студент', 'verbose_name_plural': 'Студенты'},
        ),
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='achievement.StudentsGroup'),
        ),
    ]
