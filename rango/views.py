from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

import random

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
 #   return HttpResponse("Rango says hey there partner!<br><a href='/rango/about/'>About</a><br />")
    return render(request, 'rango/index.html', context=context_dict)

def about(request):


    J = '/static/images/test_images/cat.jpg'
    context_dict = {'imageName': J,'name':'Matthew Cole'}
    
    return render(request, 'rango/about.html', context=context_dict)
#    return HttpResponse("Rango says here is the about page.<a href='/rango/'>Index</a><br>")
    
    