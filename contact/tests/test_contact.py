# -*- encoding: utf-8 -*-
import pytest

from search.tests.helper import check_search_methods
from .factories import ContactFactory


@pytest.mark.django_db
def test_search_methods():
    contact = ContactFactory()
    check_search_methods(contact)


@pytest.mark.django_db
def test_str():
    contact = ContactFactory()
    str(contact)
