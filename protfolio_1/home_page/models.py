from django.db import models

class stunetInfo(models.Model):
    ids=models.IntegerField()
    Name=models.CharField(max_length=40)
    Roll=models.IntegerField()
    Dep=models.CharField(max_length=3)
    Code=models.IntegerField()
    Commnet=models.CharField(max_length=50)