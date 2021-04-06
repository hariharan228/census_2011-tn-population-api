from django.db import models

class Population(models.Model):
    dist_name = models.CharField(max_length=50)
    total = models.BigIntegerField()
    males = models.BigIntegerField()
    females = models.BigIntegerField()
