from django.db import models

class Recommend(models.Model):
    totalCount = models.IntegerField(null=True)

