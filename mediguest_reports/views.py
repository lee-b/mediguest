from django import http
import cgi
from booking.models import RoomType
from drug_db.models import Drug
from html_to_pdf import PISA_PDFRenderer as PDFRenderer
from django.shortcuts import get_object_or_404, render
from datetime import datetime, timedelta
from servicecharges.models import ServiceChargePayment
from django.template import Template, Context, loader

def _day_iter(start_date, end_date, step=1):
    dt = start_date
    counter = 1
    while dt <= end_date:
        yield dt, counter
        counter += 1
        dt += timedelta(days=step)

def _iso_week_start(dt):
    year, weeknum, weekday = dt.isocalendar()
    if year != dt.year:
        # this year starts mid-week, so we need to account for the year before
        starting_month = 12
        starting_day = (dt - timedelta(days=weekday-1)).day
    else:
        starting_month = 1
        starting_day = 1

    year_start = datetime(year, starting_month, starting_day)

    return year_start

def _week_start_end(year, week_num):
    year_start = datetime(year, 1, 1)
    iso_year_start = _iso_week_start(year_start)

    week_start = iso_year_start + timedelta(weeks=week_num-1)
    week_end = week_start + timedelta(days=6, hours=23, minutes=59)

    return week_start, week_end

def pdf_report(req, tpl, extra_args={}):
    from clients.models import Client

    br = "<br>"

    report_title = "Client Pack"
    org_name = "Your Organisation"

    street1 = "1 YourOrg Street"
    town = "YourTown"
    postcode = "P057 C0D3"

    phone = "+44 2342 3435"
    fax = "+44 2324 2235"

    addr_html = br.join(street1, town, post_code)
    addr_inline = ", ".join(street1, town, post_code)

    pdf_renderer = PDFRenderer()

    args = {
        'pagesize':             "A4",

        'title':                report_title,
        'org_name':             org_name,
        'org_address_html':     addr_html,
        'org_address_inline':   addr_inline,
        'org_phone':            phone,
        'org_fax':              fax,
        'parent_org':           parent_org,
        'is_print':             True,
    }
    args.update(extra_args)

    pdf_buf = pdf_renderer(req, tpl, args)

    return http.HttpResponse(
        pdf_buf,
        mimetype='application/pdf'
    )

def client_report(request, report_fname, client_id, extra_args={}):
    from clients.models import Client

    client = get_object_or_404(Client, pk=client_id)
    deposit = 10.00

    my_args = {
        'deposit':              deposit,
        'client':               client,
        'room_types':           RoomType.objects.all().filter(is_client_room=True),
    }
    my_args.update(extra_args)

    return pdf_report(request, report_fname, extra_args=my_args)

def client_pack(request, client_id):
    report_fname = 'mediguest_reports/client_pack/client_pack.html'
    return client_report(request, report_fname, client_id)

def client_pack_dynonly(request, client_id):
    extra_args = { 'page_offset': '13' }
    report_fname = 'mediguest_reports/client_pack_dynonly.html'
    return client_report(request, report_fname, client_id, extra_args=extra_args)

def validity_report(request):
    from validity_checks import DoseValidityCheck
    from django.template.loader import get_template
    from django.template import RequestContext

    template_src = "mediguest_reports/validity_report.html";
    template = get_template(template_src)

    validity_checks = [ DoseValidityCheck ]
    validity_results = []
    for chk in validity_checks:
        inst = chk()
        res = inst()
        validity_results.append(res)

    args = {
        'validity_results':  validity_results,
    }

    context = RequestContext(request, args)
    html  = template.render(context)

    return http.HttpResponse(html)

def service_charge_control_sheet(request, year, week_num):
    from servicecharges.models import ServiceCharge

    template = "mediguest_reports/service_charge_control_sheet.html"
    start, end = _week_start_end(int(year), int(week_num))

    service_charges = ServiceCharge.objects.filter(date_charged__range=(start, end), type__include_on_control_sheet=True)

    args = {
        'year':             year,
        'week_num':         week_num,
        'service_charges':  service_charges,
        'start':            start,
        'end':              end,
    }

    return pdf_report(request, template, extra_args=args)

def csv_report(req, tpl, extra_args={}):
    t = loader.get_template(tpl)

    args = {}
    args.update(extra_args)

    context = Context(args)
    csv_buf = t.render(context)

    return http.HttpResponse(
        csv_buf,
        mimetype='text/csv'
    )

def service_charge_control_sheet_csv(request, year, week_num):
    from servicecharges.models import ServiceCharge

    template = "mediguest_reports/service_charge_control_sheet.csv"
    start, end = _week_start_end(int(year), int(week_num))

    service_charges = ServiceCharge.objects.filter(date_charged__range=(start, end), type__include_on_control_sheet=True)

    args = {
        'year':             year,
        'week_num':         week_num,
        'service_charges':  service_charges,
        'start':            start,
        'end':              end,
    }

    return csv_report(request, template, extra_args=args)

def service_charge_week(req, year):
    tpl = "mediguest_reports/service_charge_week.html"

    weeks = {}
    jan_1st = datetime(int(year), 1, 1)
    year_start = _iso_week_start(jan_1st)
    year_end = year_start+timedelta(days=365, minutes=-1)
    for start, week_num in _day_iter(year_start, year_end, step=7):
        end = start + timedelta(days=6, hours=23, minutes=59, seconds=59)
        weeks[week_num] = { 'start': start, 'end': end }

    args = {
        'year':         year,
        'weeks':        weeks,
    }

    return render(req, tpl, args)

def service_charge_payment_receipt(req, payment_id):
    tpl = "mediguest_reports/service_charge_payment_receipt.html"

    payment = get_object_or_404(ServiceChargePayment, id=payment_id)
    extra_args = {
        'payment':              payment,
    }

    return pdf_report(req, tpl, extra_args=extra_args)

