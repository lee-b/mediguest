# Create your views here.
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect

def front_page(req):
    return HttpResponseRedirect('/admin/')

