from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class blogs(models.Model):
		title = models.CharField(max_length=200)
		description = models.TextField()
		slug = models.SlugField(max_length=100, unique=True)
		published = models.DateTimeField(auto_now_add=True)
		author = models.ForeignKey(User, on_delete=models.CASCADE) #a one to many relationship model


		def __str__(self):
			return self.title