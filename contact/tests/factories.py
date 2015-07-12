# -*- encoding: utf-8 -*-
import factory

from decimal import Decimal

from contact.models import (
    Contact,
    UserContact,
)
from login.tests.factories import UserFactory


class ContactFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Contact

    hourly_rate = Decimal('20.00')
    user = factory.SubFactory(UserFactory)

    @factory.sequence
    def slug(n):
        return 'contact_{:02d}'.format(n)


class UserContactFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = UserContact

    contact = factory.SubFactory(ContactFactory)
    user = factory.SubFactory(UserFactory)
