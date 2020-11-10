from django.db import models
from django.utils import timezone


# Create your models here.
class Items(models.Model):
    item = models.CharField(max_length=100)

    def __str__(self):
        return self.item

class Prices(models.Model):
    item = models.ForeignKey(to=Items, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(default=00)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.item) + " _ "+ str(self.date.date())