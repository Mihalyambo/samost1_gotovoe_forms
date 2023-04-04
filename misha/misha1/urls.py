from django.urls import path

from . import views

urlpatterns = [
    path('index/product/', views.product),
    path('index/detail/', views.detail),
    path('index/customer/', views.customer),
    path('index/', views.index),
    path('index/forms/', views.forms)
]