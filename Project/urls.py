
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('salon/', views.salon, name='salon'),
    path('contact/', views.contact, name='contact'),
    path('temp/', views.temp, name='temp'),
    path('profile/', views.profile, name='profile'),
    path('loginaction/', views.loginaction, name='loginaction'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path('updateDetails/', views.updateDetails, name='updateDetails'),
    path('delete_user/', views.delete_user, name='delete_user'), 
    path('contact_form/', views.contact_form, name='contact_form'),
    ]

