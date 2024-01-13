from django.urls import path
from tango_app2 import views

app_name = 'tango_app2'
urlpatterns = [
    path('', views.index, name='index'),
]