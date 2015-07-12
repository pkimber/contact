# -*- encoding: utf-8 -*-
from django.conf.urls import (
    patterns,
    url,
)

from .views import (
    ContactCreateView,
    ContactDetailView,
    ContactListView,
    ContactUpdateView,
)


urlpatterns = patterns(
    '',
    url(regex=r'^contact/create/$',
        view=ContactCreateView.as_view(),
        name='contact.create'
        ),
    url(regex=r'^contact/(?P<slug>[-\w\d]+)/$',
        view=ContactDetailView.as_view(),
        name='contact.detail'
        ),
    url(regex=r'^contact/$',
        view=ContactListView.as_view(),
        name='contact.list'
        ),
    url(regex=r'^contact/(?P<slug>[-\w\d]+)/edit/$',
        view=ContactUpdateView.as_view(),
        name='contact.update'
        ),
)
