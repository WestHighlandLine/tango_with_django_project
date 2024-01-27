from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page

import random

def index(request):
    category_list = Category.objects.order_by('-likes')[:5] # the minus sign mean descending order
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = Page.objects.order_by('-views')[:5]
    return render(request, 'rango/index.html', context=context_dict)


def about(request):


    J = '/static/images/test_images/cat.jpg'
    context_dict = {'imageName': J,'name':'Matthew Cole'}
    
    return render(request, 'rango/about.html', context=context_dict)
#    return HttpResponse("Rango says here is the about page.<a href='/rango/'>Index</a><br>")
    
def  show_category(request, category_name_slug):
    context_dict = {}
   # Basically, If the given slug category does not exist, give it blank fields when passing stuff into the tmeplate 
   # so that teh error messages will display
    try:
        category = Category.objects.get(slug=category_name_slug)  
        pages = Page.objects.filter(category=category) 
        context_dict['pages'] = pages
        context_dict['category'] = category
        
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)

#def show_page(request, page_name_slug):
#    context_dict = {}
#   # Basically, If the given slug category does not exist, give it blank fields when passing stuff into the tmeplate 
#   # so that teh error messages will display
#    try:
#        page = Page.objects.get(slug=page_name_slug)  
#        pages = Page.objects.filter(page=page) 
#        
#        
#        
#        context_dict['title'] = title
#        context_dict['category'] = category
#        context_dict['url'] = url
#        context_dict['views'] = views
#
#        
#    except Page.DoesNotExist:
#        context_dict['title'] = None
#        context_dict['category'] = None
#        context_dict['url'] = None
#        context_dict['views'] = None
#
#    return render(request, 'rango/category.html', context=context_dict)
