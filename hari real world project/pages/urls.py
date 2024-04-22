from django.urls import path
from . import views

urlpatterns=[
    path('home',views.home_page),
path('service',views.service_page, name="service"),
path('about',views.about_page, name="about"),
]