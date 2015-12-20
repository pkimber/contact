# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, max_length=100, blank=True, unique=True, populate_from=('generate_slug',), verbose_name='slug')),
                ('company_name', models.CharField(max_length=100, blank=True)),
                ('address_1', models.CharField(max_length=100, blank=True, verbose_name='Address')),
                ('address_2', models.CharField(max_length=100, blank=True, verbose_name='')),
                ('address_3', models.CharField(max_length=100, blank=True, verbose_name='')),
                ('town', models.CharField(max_length=100, blank=True)),
                ('county', models.CharField(max_length=100, blank=True)),
                ('postcode', models.CharField(max_length=20, blank=True)),
                ('country', models.CharField(max_length=100, blank=True)),
                ('phone', models.CharField(max_length=50, blank=True)),
                ('mobile', models.CharField(max_length=50, blank=True)),
                ('website', models.URLField(blank=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(max_length=50, blank=True)),
                ('position', models.CharField(max_length=50, blank=True)),
                ('hourly_rate', models.DecimalField(max_digits=8, blank=True, decimal_places=2, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Contacts',
                'ordering': ('user__username',),
                'verbose_name': 'Contact',
            },
        ),
        migrations.CreateModel(
            name='UserContact',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
