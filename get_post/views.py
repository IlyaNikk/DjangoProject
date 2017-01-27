
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



import urlparse

@csrf_exempt
def application(request):

	method = request.method
 
        data = 'Hello world\n'

        if method  == 'POST':
		data = data + '<p>Post data</p>'
        	for key in request.POST:
			data = data + '<p>' + key + '=' + request.POST.get(key)+'</p>' 
			
        if method  == 'GET':
               data = data + 'Get data\n'
               for key in request.GET:
                       data = data + '<p>' + key + '=' + request.GET.get(key) + '</p>'

        return HttpResponse(data)

