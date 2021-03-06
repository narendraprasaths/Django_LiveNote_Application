# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-15 07:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LNote', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sharedNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('tag', models.CharField(max_length=1000)),
                ('text', models.TextField(null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='note',
            name='isShared',
        ),
        migrations.RemoveField(
            model_name='notebook',
            name='isShared',
        ),
        migrations.AddField(
            model_name='notebook',
            name='sharedWith',
            field=models.ManyToManyField(default=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sharednote',
            name='note',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LNote.note'),
        ),
        migrations.AddField(
            model_name='sharednote',
            name='sharedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
