# -*- encoding: utf-8 -*-
import pytest

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.db.models.loading import get_model

from contact.models import UserContact
from login.tests.factories import UserFactory
from .factories import ContactFactory


@pytest.mark.django_db
def test_link_user_to_contact():
    """Create a contact and link it to a user"""
    user = UserFactory(username='pat')
    contact = ContactFactory(user=UserFactory(username='abc'), phone='123')
    UserContact.objects.create_user_contact(user, contact)
    # check the user
    user = get_user_model().objects.get(username='pat')
    assert  '123' == user.usercontact.contact.phone
    # check the contact
    model = get_model(settings.CONTACT_MODEL)
    contact = model.objects.get(phone='123')
    assert 'pat' == contact.usercontact_set.first().user.username
    assert 'abc' == contact.user.username


@pytest.mark.django_db
def test_one_contact_per_user():
    """Make sure a user can only link to one contact"""
    user = UserFactory(username='pat')
    UserContact.objects.create_user_contact(user, ContactFactory())
    with pytest.raises(IntegrityError) as e:
        UserContact.objects.create_user_contact(user, ContactFactory())
    assert 'UNIQUE constraint failed' in str(e.value)
