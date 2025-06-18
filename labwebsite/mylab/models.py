from django.db import models
from django.template.defaultfilters import first


# Create your models here.

class user_signup(models.Model):
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email_id= models.EmailField()
    password= models.CharField(max_length=50)
    reg_date= models.DateField(null=True)

    def __str__(self):
        return (self.first_name)

