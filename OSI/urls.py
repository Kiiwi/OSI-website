from django.conf.urls import include, url
from django.contrib import admin
from solid_i18n.urls import solid_i18n_patterns

import data.views as view


urlpatterns = [
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        view.home_files, name='home-files'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += solid_i18n_patterns('',


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
