from django.shortcuts import render


# Create your views here.
def home(request): 
  return render (request, 'home.html', {})


def dashboard(request):
  return render (request, 'dashboard.html', {})

def aboutpage(request):
  return render (request, 'aboutpage.html')

def team(request):
  return render (request, 'team.html')

def faq(request):
  return render (request, 'faq.html')

def contact(request):
  return render (request, 'contact.html')

def services(request):
  return render (request, 'services.html')