from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=45, blank=False, default='')
    last_name= models.CharField(max_length=45,blank=False, default='')
    email_id = models.EmailField(unique=True, default='')
    mobile_no= models.CharField(max_length=12,blank=False, default='')
    role = models.CharField(max_length=10,blank=False, default='')
    password= models.CharField(max_length=45,blank=False, default='')

class Property(models.Model):
    property_name = models.CharField(max_length=45,blank=False, default='')
    description =  models.CharField(max_length=200,blank=False, default='')
    address= models.CharField(max_length=200,blank=False, default='')
    state= models.CharField(max_length=45,blank=False, default='')
    city= models.CharField(max_length=45,blank=False, default='')
    area_sq_feet = models.CharField(max_length=12,blank=False, default='')
    num_bedrooms = models.IntegerField(blank=False)
    num_bathrooms = models.IntegerField(blank=False)
    hospitals_nearby = models.TextField()
    colleges_nearby = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    seller_name = models.CharField(max_length=45, blank=False, default='')
    image= models.ImageField(upload_to='static/',default="")
    email_id = models.EmailField(unique=True, default="")
    mobile_no= models.CharField(max_length=12,blank=False, default='')
    likes = models.IntegerField(default=0)
class States(models.Model):
    stateid = models.IntegerField(blank=False)
    statename= models.CharField(max_length=45,blank=False, default='')


class Cities(models.Model):
    stateid = models.IntegerField(blank=False)
    cityid=  models.IntegerField(blank=False)
    cityname= models.CharField(max_length=45,blank=False, default='')
