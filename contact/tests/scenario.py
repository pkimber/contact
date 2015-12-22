# -*- encoding: utf-8 -*-
from decimal import Decimal

from contact.models import (
    Contact,
    UserContact,
)
from login.tests.scenario import (
    get_user_fred,
    get_user_mike,
    get_user_sara,
    get_user_staff,
)


def default_scenario_contact():
    """Default scenario.

    fred has a farm...
    the orchard needs fencing,
    but we forgot to order the fence posts!

    sara has a smallholding

    mike owns the local agricultural merchants

    TODO Would be nice to remove this scenario.

    """
    staff = get_user_staff()
    fred = get_user_fred()
    mike = get_user_mike()
    staff = get_user_staff()
    farm = Contact.objects.create_contact(
        fred,
        company_name="Fred's Farm",
        slug='fred',
    )
    UserContact.objects.create_user_contact(fred, farm)
    # sara has a smallholding
    sara = get_user_sara()
    smallholding = Contact.objects.create_contact(
        sara,
        company_name="Sara's Smallholding",
        slug='sara',
    )
    UserContact.objects.create_user_contact(sara, smallholding)
    merchant = Contact.objects.create_contact(
        mike,
        company_name="Mike's Agricultural Merchants",
        slug='mike',
    )
    UserContact.objects.create_user_contact(mike, merchant)


def get_contact_farm():
    return Contact.objects.get(user=get_user_fred())


def get_contact_merchant():
    return Contact.objects.get(user=get_user_mike())


def get_contact_smallholding():
    return Contact.objects.get(user=get_user_sara())


def get_note_fence_forgot():
    fence = get_ticket_fence_for_farm()
    staff = get_user_staff()
    return Note.objects.get(ticket=fence, user=staff)


def get_priority_unassigned():
    return Priority.objects.get(level=0)


def get_ticket_fence_for_farm():
    fred = get_user_fred()
    farm = get_contact_farm()
    return Ticket.objects.get(contact=farm, user=fred)


def get_ticket_fix_roof_for_farm():
    staff = get_user_staff()
    farm = get_contact_farm()
    priority=get_priority_unassigned()
    return Ticket.objects.get(contact=farm, user=staff, priority=priority)


def get_ticket_paperwork_for_smallholding():
    sara = get_user_sara()
    smallholding = get_contact_smallholding()
    return Ticket.objects.get(contact=smallholding, user=sara)
