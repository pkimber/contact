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

    user = factory.SubFactory(UserFactory)

    @factory.sequence
    def address_1(n):
        return 'address_1_{:02d}'.format(n)

    @factory.sequence
    def company_name(n):
        return 'company_{:02d}'.format(n)


class UserContactFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = UserContact

    contact = factory.SubFactory(ContactFactory)
    user = factory.SubFactory(UserFactory)
