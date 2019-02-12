from django.db import models

# Create your models here.
class Decade(models.Model):
    start_year = models.IntegerField()

    def __str__(self):
        return self.start_year

class Fads(models.Model):
    name = models.TextField()
    image_url = models.TextField()
    description = models.TextField()
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fads')

    def __str__ (self):
        return self.name
