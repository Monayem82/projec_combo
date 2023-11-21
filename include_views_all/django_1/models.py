from django.db import models

class DjangoTable(models.Model):
    ids=models.IntegerField()
    names=models.CharField(max_length=40)
    balance=models.IntegerField()

class studentPublic(models.Model):
    s_id=models.IntegerField()
    s_name=models.CharField(max_length=20)
    s_roll=models.IntegerField()
    s_dep=models.CharField(max_length=3)
