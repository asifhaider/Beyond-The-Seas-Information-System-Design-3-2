from django.shortcuts import render
from django.http import HttpResponse

from homepage.models import University, Location, Feedback, Student, Professor
# Create your views here.
def show_homepage(request):

    # name = University.objects.all()[0].university_name
    # print(name)
    return render(request, 'homepage.html')