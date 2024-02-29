from django.db import models

# Create your models here.
class Portfolio(models.Model):
	url = models.URLField(blank=True)
	title = models.CharField(max_length=200)
	description  = models.CharField(max_length=400)
	image = models.ImageField(upload_to='Portfolio/images/')
	
	def __str__(self):
		return self.title


