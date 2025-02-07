
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about, name='about'),  # About page
    path('fruit/', views.fruit, name='fruit'),  # Our Fruit page route (fruit.html)
    path('contact/', views.contact, name='contact'),  # Contact page route (contact.html)
    path('testimonial/', views.testimonial, name='testimonial'),  # Testimonial page route (testimonial.html)
    path('auth/', views.auth_page, name='auth_page'),  # Single auth page
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]

