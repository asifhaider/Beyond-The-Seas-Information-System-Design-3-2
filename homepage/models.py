from django.db import models
# from django.forms import UUIDField


# Create your models here.
class University(models.Model):
	# primary key
	university_id = models.UUIDField(primary_key=True, help_text='Unique ID for university')

	university_name = models.CharField(max_length=1000)
	university_type = models.CharField(max_length=200)
	university_rank = models.IntegerField()
	university_location = models.CharField(max_length=200)

	class Meta:
		ordering = ['university_name', 'university_type', 'university_rank', 'university_location']

	def __str__(self):
		"""String for representing the Model object."""
		return self.university_name
	

class Location(models.Model):
    	# primary key
	location_id = models.UUIDField(primary_key=True, help_text='Unique ID for location')

	location_name = models.CharField(max_length=1000)
	living_cost = models.IntegerField()
	weather = models.CharField(max_length=200)

	class Meta:
		ordering = ['location_name', 'living_cost', 'weather']

	def __str__(self):
		"""String for representing the Model object."""
		return self.location_name
	

class Feedback(models.Model):
        	# primary key
	feedback_id = models.UUIDField(primary_key=True, help_text='Unique ID for feedback')

	person_name = models.CharField(max_length=1000)
	feedback_post = models.CharField(max_length=200)

	class Meta:
		ordering = ['person_name', 'feedback_post']

	def __str__(self):
		"""String for representing the Model object."""
		return self.person_name