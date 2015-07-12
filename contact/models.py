# -*- encoding: utf-8 -*-
from datetime import date

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

import reversion

from base.model_utils import TimeStampedModel


class ContactError(Exception):

    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return repr('{}, {}'.format(self.__class__.__name__, self.value))


class Industry(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Industry'
        verbose_name_plural = 'Industries'

    def __str__(self):
        return '{}'.format(self.name)

reversion.register(Industry)


class ContactManager(models.Manager):

    def create_contact(self, user, slug, name, **kwargs):
        obj = self.model(
            user=user,
            slug=slug,
            name=name,
            **kwargs
        )
        obj.save()
        return obj


class Contact(TimeStampedModel):

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    url = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True)
    mail = models.EmailField(blank=True)
    industry = models.ForeignKey(Industry, blank=True, null=True)
    hourly_rate = models.DecimalField(
        blank=True, null=True, max_digits=8, decimal_places=2
    )
    objects = ContactManager()

    class Meta:
        ordering = ('slug',)
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return '{}'.format(self.name)

    @property
    def deleted(self):
        """No actual delete (yet), so just return 'False'."""
        return False

    def get_absolute_url(self):
        return reverse('contact.detail', args=[self.slug])

    def get_summary_description(self):
        return filter(None, (
            self.name,
            self.address,
        ))

reversion.register(Contact)


class UserContactManager(models.Manager):

    def create_user_contact(self, user, contact):
        obj = self.model(
            user=user,
            contact=contact,
        )
        obj.save()
        return obj


class UserContact(TimeStampedModel):
    """
    A user is linked to a single contact.
    More than one user can link to the same contact, but a user cannot
    link to more than one contact.

    e.g.
    Andy - ConnexionSW
    Fred - ConnexionSW
    Kate - British Sugar

    """

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    contact = models.ForeignKey(Contact)
    objects = UserContactManager()

    def __str__(self):
        return '{} - {}'.format(self.user.username, self.contact.name)

reversion.register(UserContact)
