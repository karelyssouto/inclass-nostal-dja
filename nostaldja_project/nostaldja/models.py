from django.db import models

# Create your models here.


class Decade(models.Model):
    start_year = models.CharField(max_length=5)

    def __str__(self):
        return self.start_year


class Fads(models.Model):
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fads')
    image_url = models.CharField(max_length=500, default='')
    name = models.CharField(max_length=500, default='')
    description = models.TextField()

    def __str__(self):
        return self.name
