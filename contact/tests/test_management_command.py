# -*- encoding: utf-8 -*-
from django.test import TestCase

from contact.management.commands import (
    demo_data_contact,
    init_app_contact,
)
from login.management.commands import demo_data_login


class TestCommand(TestCase):

    def test_demo_data(self):
        """ Test the management command """
        pre_command = demo_data_login.Command()
        pre_command.handle()
        command = demo_data_contact.Command()
        command.handle()

    def test_init_app(self):
        """ Test the management command """
        command = init_app_contact.Command()
        command.handle()
