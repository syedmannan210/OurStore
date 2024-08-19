from django.urls import path
from . import views
urlpatterns = [
    path('shop/', views.index, name='ShopHome'),
    path('shop/about/', views.about, name='AboutUs'),
    path('shop/contact/', views.contact, name='ContactUs'),
    path('shop/tracker/', views.tracker, name='TrackingStatus'),
    path('shop/search/', views.search, name='Search'),
    path("shop/products/<int:myid>", views.productView, name='ProdView'),
    path('shop/checkout/', views.checkout, name='Checkout')
]