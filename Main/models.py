from django.db import models

# Create your models here.


class ReportList(models.Model):
	reportname = models.CharField(max_length=20)

class ReportDetail(models.Model):
	name = models.CharField(max_length = 20, default = "")
	positionX = models.DecimalField(max_digits = 8, decimal_places = 3)
	positionY = models.DecimalField(max_digits = 8, decimal_places = 3)
	time = models.CharField(max_length = 20)
	listptr = models.DecimalField(max_digits = 3, decimal_places = 0)
