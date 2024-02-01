from django.shortcuts import render
from django.http import HttpResponse
from .models import create_bin

# Create your views here.
def dashboard(request):
  dustbin = create_bin.objects.all()
  dustb = create_bin.objects.get(id=pk)
  
  context = {'dustbin': dustbin, 'dustb': dustb}
  return render (request, 'dashboard.html', context)

def user_dashboard(request): 
  return render (request, 'user_dashboard.html')


def driver_dashboard(request):
  return render (request, 'driver_dashboard.html')


