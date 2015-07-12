# -*- encoding: utf-8 -*-
from django.core.management.base import BaseCommand

from contact.tests.scenario import default_scenario_contact


class Command(BaseCommand):

    help = "Create demo data for 'contact'"

    def handle(self, *args, **options):
        default_scenario_contact()
        print("Created 'contact' demo data...")
