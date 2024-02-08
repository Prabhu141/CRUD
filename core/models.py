from django.db import models

class company(models.Model):
    employee_id = models.CharField(max_length=250)
    employee_name = models.TextField()
    employee_phone = models.IntegerField()
