from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile


class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'url','views') # these are the column names that are shown on the admin site
#    prepopulated_fields = {'slug':('title',)}
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)} # this bit related to automatically filling out fields when entering new data into the DB

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)

admin.site.register(UserProfile)
    
    
    
#    Finally, register the PageAdmin class with Django’s admin interface.
#You should modify the line admin.site.register(Page). Change it to
#admin.site.register(Page, PageAdmin) in Rango’s admin.py file.


