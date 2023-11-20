from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'site_app/home.html')

def research(request):
    return render(request, 'site_app/research.html')

def publications(request):
    return render(request, 'site_app/publications.html')

def team(request):
    return render(request, 'site_app/team.html')