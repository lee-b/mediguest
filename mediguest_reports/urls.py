from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('mediguest_reports.views',
    url(r'^client/(\d+)/pack$', 'client_pack', name="client_pack"),
    url(r'^client/(\d+)/pack_dynonly$', 'client_pack_dynonly', name="client_pack_dynonly"),
    url(r'^reports/validity/$', 'validity_report', name="validity_report"),
    url(r'^reports/service_charge_control_sheet/(?P<year>\d+)/(?P<week_num>\d+)/$', 'service_charge_control_sheet', name="service_charge_control_sheet"),
    url(r'^reports/service_charge_control_sheet_csv/(?P<year>\d+)/(?P<week_num>\d+)/$', 'service_charge_control_sheet_csv', name="service_charge_control_sheet_csv"),
    url(r'^service_charge_week/(?P<year>\d+)/$',    'service_charge_week',    name='service_charge_week'),
    url(r'^service_charge_payment_receipt/(?P<payment_id>\d+)/$',    'service_charge_payment_receipt',    name='service_charge_payment_receipt'),
)

