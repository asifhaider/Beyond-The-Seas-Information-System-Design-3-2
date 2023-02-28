from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_homepage(request):
    return render(request, 'homepage.html')