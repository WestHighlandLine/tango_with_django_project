from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page # the database models (tables)
from rango.forms import CategoryForm, PageForm # which forms are there?
from django.shortcuts import redirect
from django.urls import reverse
from rango.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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

@login_required
def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid(): # vailidating the received data
            form.save(commit=True) # addingf to the database
            return redirect('/rango/') # redirect to given page
    else:
        print(form.errors)
    
    return render(request, 'rango/add_category.html', {'form': form})
    
@login_required
def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None
    # You cannot add a page to a Category that does not exist...
    if category is None:
        return redirect('/rango/')
    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
    if form.is_valid():
        if category:
            page = form.save(commit=False)
            page.category = category
            page.views = 0
            page.save()
            return redirect(reverse('rango:show_category', kwargs={'category_name_slug': category_name_slug}))  ## E R R O R   H E R E
    else:
        print(form.errors)
    
    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context=context_dict)
      
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            user.set_password(user.password) # hashing the password
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'rango/register.html', context = {'user_form': user_form,'profile_form': profile_form,'registered': registered})
           
def user_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
    
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('rango:index'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'rango/login.html')
    
@login_required   # put this line to ensure that the view can only be seen by a logged in user  ?
def restricted(request):
    return render(request, 'rango/restricted.html')
    
    
    
@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('rango:index'))

    
    