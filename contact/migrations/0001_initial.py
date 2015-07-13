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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('company_name', models.CharField(max_length=100, blank=True)),
                ('address_1', models.CharField(verbose_name='Address', max_length=100, blank=True)),
                ('address_2', models.CharField(verbose_name='', max_length=100, blank=True)),
                ('address_3', models.CharField(verbose_name='', max_length=100, blank=True)),
                ('town', models.CharField(max_length=100, blank=True)),
                ('county', models.CharField(max_length=100, blank=True)),
                ('postcode', models.CharField(max_length=20, blank=True)),
                ('country', models.CharField(max_length=100, blank=True)),
                ('phone', models.CharField(max_length=50, blank=True)),
                ('mobile', models.CharField(max_length=50, blank=True)),
                ('website', models.URLField(blank=True)),
                ('dob', models.DateField(null=True, blank=True)),
                ('nationality', models.CharField(max_length=50, blank=True)),
                ('position', models.CharField(max_length=50, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Contact',
                'ordering': ('user__username',),
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='UserContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('contact', models.ForeignKey(to='contact.Contact')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
