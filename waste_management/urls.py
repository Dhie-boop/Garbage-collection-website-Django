from django.urls import path 
from .import views
#from garbage import views
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('dashboard/<int:pk>/', views.dashboard, name='dashboard'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard' ),
    path('driver_dashboard/', views.driver_dashboard, name='driver_dashboard'),
    
]
