from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name

class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	pub_year = models.DateField('date published')
	edition = models.PositiveSmallIntegerField('Edition')
	user = models.ForeignKey(User, blank=True, null=True)
	def __unicode__(self):
		return self.title