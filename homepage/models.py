from django.db import models
# from django.forms import UUIDField
import uuid


# Create your models here.
class University(models.Model):
	# primary key
	university_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for university')
	university_name = models.CharField(max_length=1000)
	university_type = models.CharField(max_length=200)
	university_rank = models.IntegerField()
	
    # foreign key location id    
	
	university_location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
	university_link = models.CharField(max_length=1000, default='http://csrankings.com')

	class Meta:
		ordering = ['university_name', 'university_type', 'university_rank', 'university_location', 'university_link']

	def __str__(self):
		"""String for representing the Model object."""
		return self.university_name
	

class Location(models.Model):
    	# primary key
	location_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for location')

	location_name = models.CharField(max_length=1000)
	living_cost = models.FloatField()
	weather = models.CharField(max_length=200)

	class Meta:
		ordering = ['location_name', 'living_cost', 'weather']

	def __str__(self):
		"""String for representing the Model object."""
		return self.location_name


class Student(models.Model):
	# primary key
    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for student')

    student_name = models.CharField(max_length=1000)
    student_gpa = models.FloatField()

    class Meta:
        ordering = ['student_name', 'student_gpa']

    def __str__(self):
        """String for representing the Model object."""
        return self.student_name


# with name and email, university id as foreigner key
class Professor(models.Model):
	# primary key
    professor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for professor')

    professor_name = models.CharField(max_length=1000)
    professor_email = models.CharField(max_length=200)
    university_id = models.ForeignKey('University', on_delete=models.SET_NULL, null=True)


    class Meta:
        ordering = ['professor_name', 'professor_email']

    def __str__(self):
        """String for representing the Model object."""
        return self.professor_name



class Feedback(models.Model):
        	# primary key
	feedback_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for feedback')
	
    # foreign key student id and university id

    
	university_id = models.ForeignKey('University', on_delete=models.SET_NULL, null=True)
	student_id = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True)
	feedback_post = models.CharField(max_length=200)

	class Meta:
		ordering = ['feedback_post']

	def __str__(self):
		"""String for representing the Model object."""
		return self.feedback_post