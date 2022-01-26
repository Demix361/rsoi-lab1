from django.db import models


class Person(models.Model):
	name = models.CharField(max_length=256)
	age = models.IntegerField()
	address = models.CharField(max_length=256)
	work = models.CharField(max_length=256)
