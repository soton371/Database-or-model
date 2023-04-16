from django.db import models

# Create your models here.
class CollectModel(models.Model):
    name = models.CharField(max_length=40)
    age = models.CharField(max_length=3)
    team = models.CharField(max_length=20,default='Australia')

    def __str__(self):
        return self.name