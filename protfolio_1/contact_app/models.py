from django.db import models

# Create your models here.
class studentContact(models.Model):
    name=models.CharField(max_length=15)
    fname=models.CharField(max_length=12)
    mobile=models.IntegerField()
    village=models.CharField(max_length=25)