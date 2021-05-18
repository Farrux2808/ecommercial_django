from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=100)

class Measurement(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=100)

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    voluem = models.FloatField()
    measurement_id = models.ForeignKey(Measurement, on_delete=models.CASCADE)
    info = models.TextField()


