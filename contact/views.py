# -*- encoding: utf-8 -*-
from django.contrib import messages
from django.core.exceptions import PermissionDenied
# TODO PJK Is this the correct import for 'RelatedObjectDoesNotExist'
# from django.db.models.fields.related import RelatedObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)

from base.view_utils import BaseMixin
from .forms import ContactForm
from .models import (
    Contact,
    ContactError,
    UserContact,
)


def _check_user_contact(user, contact):
    try:
        if user.usercontact.contact == contact:
            return True
        else:
            return False
    except UserContact.DoesNotExist as e:
        raise ContactError(
            "user '{}' does not have a contact".format(user.username)
        ) from e


def _check_perm(user, contact):
    if user.is_staff:
        pass
    elif _check_user_contact(user, contact):
        pass
    else:
        # the user is NOT linked to the contact
        raise PermissionDenied()


class CheckPermMixin(object):

    def _check_perm(self, contact):
        _check_perm(self.request.user, contact)


class ContactCreateView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, CreateView):

    form_class = ContactForm
    model = Contact


class ContactDetailView(
        LoginRequiredMixin, CheckPermMixin, BaseMixin, DetailView):

    model = Contact

    def get_object(self, *args, **kwargs):
        obj = super(ContactDetailView, self).get_object(*args, **kwargs)
        self._check_perm(obj)
        return obj


class ContactListView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, ListView):

    paginate_by = 20

    model = Contact


class ContactUpdateView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, UpdateView):

    form_class = ContactForm
    model = Contact
