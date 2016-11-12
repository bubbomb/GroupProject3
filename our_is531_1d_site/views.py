from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    #return HttpResponse("Hello from django, try out <a href='/admin/'>/admin/</a>\n")
    return render_to_response('home/index.html', context_instance=RequestContext(request))
