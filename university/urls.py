from django.urls import path
from university import views

urlpatterns = [
    path('university/<university_id>', views.university_page, name='university_page'),
    # path('book/<isbn>/add_review', views.add_review, name='add_review'),
]