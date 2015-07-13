# -*- encoding: utf-8 -*-
from django import forms

from base.form_utils import RequiredFieldForm

from .models import Contact


class ContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        names = (
            'address_1',
            'address_2',
            'address_3',
            'website',
        )
        for name in names:
            self.fields[name].widget.attrs.update({'class': 'pure-input-2-3'})

    class Meta:
        model = Contact
        fields = (
            'address_1',
            'address_2',
            'address_3',
            'town',
            'county',
            'postcode',
            'country',
            'phone',
            'mobile',
            'website',
        )
