from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=4)
    hasWine = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' ' + self.position+' '+ self.hasWine