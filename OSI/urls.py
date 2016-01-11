from django.conf.urls import patterns, include, url
from django.contrib import admin

import data.views as view

urlpatterns = patterns('',

    # Admin URL
    url(r'^admin/', include(admin.site.urls)),

    # Home URL
    url(
        regex=r'^$',
        view=view.home,
        name='home'
    ),

    # Team URLs
    url(
        regex=r'^d1/$',
        view=view.D1.as_view(),
        name='D1'
    ),

    url(
        regex=r'^d2/$',
        view=view.D2.as_view(),
        name='D2'
    ),

    url(
        regex=r'^h1/$',
        view=view.H1.as_view(),
        name='H1'
    ),

    url(
        regex=r'^h2/$',
        view=view.H2.as_view(),
        name='H2'
    ),
)
