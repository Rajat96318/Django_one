from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),  # / after about works also without / also works
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
]