from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class school(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	username = models.CharField(max_length = 50)
	school = models.CharField(max_length= 200)

	def __str__(self):
		return self.username

class course(models.Model):
	subject_choices = (('Maths','Maths'),
					   ('Computer','Computer'),
					   ('Chemistry','Chemistry'),
					   ('Physics','Physics'))
	grade_choices = (('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'))
	name = models.CharField(max_length=200)
	price = models.IntegerField()
	teacher = models.CharField(max_length=50)
	duration = models.CharField(max_length = 20)
	subject = models.CharField(max_length=15, choices = subject_choices, default = 1)
	grade = models.CharField(max_length=2, choices = grade_choices)

	def __str__(self):
		return self.name

class subscription_plan(models.Model):
	user = models.ForeignKey(school, on_delete = models.CASCADE)
	amount = models.IntegerField()

	def __str__(self):
		return self.user

class subscription_course(models.Model):
	subscription_plan = models.ForeignKey(subscription_plan, on_delete = models.CASCADE)
	parent_course = models.ForeignKey(course, on_delete = models.CASCADE)

	def __str__(self):
		return self.parent_course

class cart(models.Model):
	user = models.ForeignKey(school, on_delete = models.CASCADE)
	courses_id = []
	open = models.BooleanField(default = True)

	def __str__(self):
		return self.user

