from django.db import models


# Create your models here.
class Customer(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')
    gender = models.CharField(max_length=100, blank=True, default='')
    company = models.CharField(max_length=100, blank=True, default='')
    city = models.CharField(max_length=100, blank=True, default='')
    title = models.CharField(max_length=100, blank=True, default='')
    latitude = models.CharField(max_length=100, blank=True, default='')
    longitude = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        managed: False
        db_table: 'Customer'
