from django.conf.urls.defaults import patterns, include, url
from settings import MEDIA_ROOT, STATIC_ROOT

from mediguest_admin.site import mediguest_admin_site
from django.contrib import admin
admin.site = mediguest_admin_site
admin.autodiscover()

urlpatterns = patterns('',
    # third-party stuff
    url(r'^foreignkeysearch/', include('foreignkeysearch.urls')),

    # static/uploaded files
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': MEDIA_ROOT
    }),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': STATIC_ROOT
    }),

    # custom stuff
    url(r'^mediguest_client_reports/',    include('mediguest_reports.urls')),
    url(r'^$',                     'mediguest_admin.views.front_page', name="frontpage"),

    # admin
    url(r'^admin/doc/',             include('django.contrib.admindocs.urls')),
    url(r'^admin/',                 include(mediguest_admin_site.urls)),
)

