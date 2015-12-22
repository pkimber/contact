# -*- encoding: utf-8 -*-
from datetime import date
from decimal import Decimal

import reversion

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django_extensions.db.fields import AutoSlugField

from base.model_utils import TimeStampedModel


class ContactError(Exception):

    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return repr('{}, {}'.format(self.__class__.__name__, self.value))


class ContactManager(models.Manager):

    def create_contact(self, user, **kwargs):
        obj = self.model(user=user, **kwargs)
        obj.save()
        return obj


class Contact(TimeStampedModel):

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    slug = models.SlugField(unique=True)
    # slug = AutoSlugField(
    #     'slug',
    #     max_length=100,
    #     unique=True,
    #     populate_from=('generate_slug',),
    # )
    # address
    company_name = models.CharField(max_length=100, blank=True)
    address_1 = models.CharField('Address', max_length=100, blank=True)
    address_2 = models.CharField('', max_length=100, blank=True)
    address_3 = models.CharField('', max_length=100, blank=True)
    town = models.CharField(max_length=100, blank=True)
    county = models.CharField(max_length=100, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, blank=True)
    # contact
    phone = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)
    # personal
    dob = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True)
    position = models.CharField(max_length=50, blank=True)
    # accounts
    hourly_rate = models.DecimalField(
        blank=True, null=True, max_digits=8, decimal_places=2
    )
    # internal
    deleted = models.BooleanField(default=False)
    objects = ContactManager()

    class Meta:
        ordering = ('user__username',)
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return '{}'.format(self.user.get_full_name())

    @property
    def checkout_can_charge(self):
        return True

    @property
    def checkout_description(self):
        return self.get_summary_description()

    @property
    def checkout_actions(self):
        return []

    @property
    def checkout_email(self):
        return self.user.email

    def checkout_fail(self, *args, **kwargs):
        pass

    def checkout_fail_url(self, checkout_pk):
        pass

    #def checkout_mail(self, checkout_action):
    #    pass

    @property
    def checkout_name(self):
        return '{}'.format(self.user.get_full_name())

    def checkout_success(self, checkout_action):
        pass

    def checkout_success_url(self, checkout_pk):
        pass

    @property
    def checkout_total(self):
        return Decimal()

    @property
    def deleted(self):
        """No actual delete (yet), so just return 'False'."""
        return False

    @property
    def full_name(self):
        return '{}'.format(self.user.get_full_name())

    # @property
    # def generate_slug(self):
    #     return self.company_name if self.company_name else self.full_name

    def get_absolute_url(self):
        return reverse('contact.detail', args=[self.user.username])

    def get_summary_description(self):
        return filter(None, (
            self.user.get_full_name(),
            self.company_name,
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
    """A user is linked to a contact.

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
