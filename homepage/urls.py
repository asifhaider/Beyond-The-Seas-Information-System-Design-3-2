from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_homepage, name='homepage'),
    path('/', views.search, name='search'),
    path('/sort', views.sort, name='sort'),
]