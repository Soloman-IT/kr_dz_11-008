from django.db import models
class Record(models.Model):
    name = models.CharField(max_length=300)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    gender = models.CharField(max_length=10, default='man')
    result = models.CharField(max_length=30, default='No')
    imt = models.FloatField(default='0.0')
