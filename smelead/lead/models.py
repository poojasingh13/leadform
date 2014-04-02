from django.db import models

# Create your models here.

class leadform(models.Model):
	name= models.CharField(max_length=200)
	organisation= models.CharField(max_length=200)
	city= models.CharField(max_length=200)
	emailId= models.EmailField()
	contactno= models.CharField(max_length=200)

	def __unicode__(self):
		return self.name
