from django.template import RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponsePermanentRedirect
import random
import json
import string
from django import shortcuts
from django.views.decorators.csrf import csrf_exempt

def index(request):
	#t=loader.get_template('url/index.html')
	return render_to_response('index2.html')


