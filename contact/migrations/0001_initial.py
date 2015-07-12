# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField(blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('mail', models.EmailField(blank=True, max_length=254)),
                ('hourly_rate', models.DecimalField(blank=True, max_digits=8, null=True, decimal_places=2)),
            ],
            options={
                'verbose_name_plural': 'Contacts',
                'verbose_name': 'Contact',
                'ordering': ('slug',),
            },
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Industries',
                'verbose_name': 'Industry',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='UserContact',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('contact', models.ForeignKey(to='contact.Contact')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='contact',
            name='industry',
            field=models.ForeignKey(to='contact.Industry', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
