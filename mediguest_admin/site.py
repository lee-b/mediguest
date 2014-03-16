from django.contrib.admin import AdminSite
from django.shortcuts import render
from datetime import datetime

class MediGuestAdminSite(AdminSite):
    def index(self, req):
        return index_view(req)

    def get_urls(self):
        from django.conf.urls.defaults import patterns, url
        url_patterns = super(MediGuestAdminSite, self).get_urls()
        url_patterns += patterns('mediguest_admin.views',
            url(r'^advanced_index$',          self.advanced_index_view),
        )
        return url_patterns

    def index(self, req, *args, **kwargs):
        now = datetime.now()

        last_year = now.year - 1
        this_year = now.year

        context_dict = {
            "title":                    "Administration Area",
            "user":                     req.user,
            'this_year':                this_year,
            'last_year':                last_year,
        }

        return render(req, 'mediguest_admin/index.html', context_dict)

    def advanced_index_view(self, req):
        return super(MediGuestAdminSite, self).index(req)

mediguest_admin_site = MediGuestAdminSite()

