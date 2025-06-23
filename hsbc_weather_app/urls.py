from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('get_details/',views.get_details,name='get_details'),
    path('',views.input_form_view),
]