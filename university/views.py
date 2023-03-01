from django.shortcuts import render
from homepage.models import University, Location, Student, Professor
# Create your views here.

# get university model attributes
def university_page(request, university_id):
    university = University.objects.get(pk=university_id)
    university_name = university.university_name
    university_type = university.university_type
    university_rank = university.university_rank
    university_location = university.university_location
    university_link = university.university_link

    # find location id based on university location from location model
    location = Location.objects.get(location_name=university_location)

    # get location model attributes
    location_name = location.location_name
    living_cost = location.living_cost
    weather = location.weather

    context = {
        'university_id': university_id,
        'university_name': university_name,
        'university_type': university_type,
        'university_rank': university_rank,
        'university_location': university_location,
        'university_link': university_link,
        'location_name': location_name,
        'living_cost': living_cost,
        'weather': weather,
    }
    return render(request, 'university_page.html', context=context)
