# -*- encoding: utf-8 -*-
"""Simple tests to make sure a view doesn't throw any exceptions"""
from django.core.urlresolvers import reverse
from django.test import TestCase

from base.tests.test_utils import PermTestCase
from contact.tests.factories import UserContactFactory
from contact.tests.scenario import (
    default_scenario_contact,
    get_contact_farm,
)
from login.tests.factories import TEST_PASSWORD
from login.tests.scenario import (
    default_scenario_login,
    get_user_staff,
    get_user_web,
    user_contractor,
)


class TestView(PermTestCase):
    """Make sure a staff user can access all the standard screens"""

    def setUp(self):
        self.setup_users()

    #def setUp(self):
    #    user_contractor()
    #    default_scenario_login()
    #    self.contact = get_contact_farm()
    #    self.staff = get_user_staff()

    def test_contact_create(self):
        url = reverse('contact.create')
        self.assert_staff_only(url)

    def test_contact_detail(self):
        web = get_user_web()
        UserContactFactory(user=web)
        user_contact = UserContactFactory()
        url = reverse(
            'contact.detail', kwargs={'slug': user_contact.contact.slug}
        )
        self.assert_staff_only(url)

    def test_contact_list(self):
        url = reverse('contact.list')
        self.assert_staff_only(url)

    def test_contact_update(self):
        user_contact = UserContactFactory()
        url = reverse(
            'contact.update', kwargs={'slug': user_contact.contact.slug}
        )
        self.assert_staff_only(url)
