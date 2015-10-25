from django.db import models
from decimal import Decimal
# Create your models here.


class ReportList(models.Model):
	reportname = models.CharField(max_length=20)

class ReportDetail(models.Model):
	listptr = models.DecimalField(max_digits = 8,decimal_places=0)
	latitude = models.DecimalField(max_digits = 20, decimal_places = 7)
	longitude = models.DecimalField(max_digits = 20, decimal_places = 7)
	bornyear = models.DecimalField(max_digits = 4, decimal_places = 0)
	time = models.DateTimeField()

