from django.contrib import admin
from rango.models import Category, Page


admin.site.register(Category) # add more of these to add new classes
admin.site.register(Page)
