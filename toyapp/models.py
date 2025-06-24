from django.db import models

# Create your models here.
class Reg_tbl(models.Model):
    email=models.EmailField()
    psw=models.CharField(max_length=16)
    rpsw=models.CharField(max_length=16)
    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    gender=models.CharField(max_length=7)

class Products_tbl(models.Model):
    tname = models.CharField(max_length=25)
    timg = models.FileField(upload_to="pic")
    tprc = models.IntegerField()
    tdes = models.TextField()

class cart_tbl(models.Model):
    product = models.ForeignKey(Products_tbl,on_delete=models.CASCADE)
    customer = models.ForeignKey(Reg_tbl,on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)