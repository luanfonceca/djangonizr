# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponse
from core.forms import *


def index(request):
    return render_to_response('public/index.html', locals(),
            context_instance=RequestContext(request))
            
def contact(request):
    contact_form = ContactForm(request.POST or None)
    if request.method is 'POST':
        import pdb;pdb.set_trace()
    return render_to_response('public/contact.html', locals(),
            context_instance=RequestContext(request))