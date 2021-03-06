# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 16:36
from __future__ import unicode_literals

import datetime
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
            name='CaseMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default='')),
                ('order', models.IntegerField(default=0)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('updated', models.DateTimeField(default=datetime.datetime.now)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case_module_created_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='MethodologyMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default='')),
                ('order', models.IntegerField(default=0)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('updated', models.DateTimeField(default=datetime.datetime.now)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='methodology_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='methodology_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ModuleMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default='')),
                ('order', models.IntegerField(default=0)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('updated', models.DateTimeField(default=datetime.datetime.now)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='module_created_by', to=settings.AUTH_USER_MODEL)),
                ('methodology', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='configuration.MethodologyMaster')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='module_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='casemaster',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.ModuleMaster'),
        ),
        migrations.AddField(
            model_name='casemaster',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case_module_updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
