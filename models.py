from django.db import models


# Create your models here.

class List(models.Model):
    item_name = models.CharField(max_length=1000)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name