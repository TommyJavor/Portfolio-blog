from django.db import models


class Blog(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	date = models.DateField(auto_now=True)
	
# Create your models here.
	def __str__(self):
		return self.title
