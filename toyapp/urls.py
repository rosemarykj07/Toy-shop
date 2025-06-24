from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('register',views.reg),
    path('login',views.login),
    path('users',views.users),
    path('edit/<int:pk>',views.edit,name="edit"),
    path('delete/<int:pk>',views.delete,name="delete"),
    path('products',views.products),
    path('toys',views.toy),
    path('cart/<int:idn>',views.cart,name="cart"),
    path('viewcart',views.viewcart),
    path('cartdelete/<int:pid>',views.cartdelete,name="cartdelete"),
    path('email',views.email),
    path('formview',views.formview),
]
