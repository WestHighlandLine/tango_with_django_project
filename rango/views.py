from django.shortcuts import render


from django.http import HttpResponse
def index(request):
                        # these return html code
    return HttpResponse("Rango says hey there partner! <br> To go to the about page, click <a href='http://127.0.0.1:8000/rango/about'>here</a>")
    
def about(request):
    return HttpResponse("Rango says here is the about page. <br> To go to the index page, click <a href='http://127.0.0.1:8000/rango/'>here</a>")
    