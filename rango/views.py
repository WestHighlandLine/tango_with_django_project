from django.shortcuts import render
from django.http import HttpResponse

import random

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def about(request):

    names = ["elephant1","frog1","girraf1","goat1","hippo1","lion1","lion2","monkey1","panda1","parrot1","pig1"]

       
    V = random.choice(names)
    J = '/static/images/test_images/' + V + ".jpg"
    context_dict = {'imageName': J,'boldmessage':"Displaying "+V+".jpg"}
    return render(request, 'rango/about.html', context=context_dict)
    
    
    