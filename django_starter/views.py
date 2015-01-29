from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

def home(request):
    data = {}
    return render_to_response('base.html',
                              data,
                              context_instance=RequestContext(request))
