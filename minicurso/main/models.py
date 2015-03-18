from django.db import models

# Create your models here.
class Course(models.Model):

	name = models.CharField(max_length=50)
	slug = models.SlugField(null=True, blank=True)
	description = models.TextField(max_length=200)
	image = models.ImageField(upload_to = 'course')

	def __unicode__(self):
		return self.name

class Inscription(models.Model):

	course = models.ForeignKey(Course)
	full_name = models.CharField(max_length=100)
	email = models.EmailField()

	def __unicode__(self):
		return self.full_name