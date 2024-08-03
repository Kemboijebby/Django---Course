from django.urls import path
from . import views

urlpatterns = [

    path('register/',views.registerpage, name = 'register'),
    path('login/',views.loginpage, name = 'login'),
     path('logout/',views.logoutuser, name = 'logout'),

    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name='customer'),
    
    path('create_order/<str:pk>/',views.create_order,name='create_order'),
    path('updateorder/<str:pk>/',views.updateorder,name='updateorder'),
    path('deleteorder/<str:pk>/',views.deleteorder,name='deleteorder'),
]

