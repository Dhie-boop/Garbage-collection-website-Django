from django.urls import path 
from .import views
#from waste_management import views
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('aboutpage/', views.aboutpage, name='aboutpage'),
    path('team/', views.team, name='team'),
    path('faq', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
]

