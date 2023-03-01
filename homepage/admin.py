from django.contrib import admin
from .models import University, Location, Feedback, Student, Professor

# Register your models here.
admin.site.register(University)
admin.site.register(Location)
admin.site.register(Feedback)
admin.site.register(Student)
admin.site.register(Professor)