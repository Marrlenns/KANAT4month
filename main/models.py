from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    rating = models.IntegerField(default=0, blank=True, null=True)
    duration = models.FloatField(default=0)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL,
                                 related_name='films', null=True)

    def __str__(self):
        return f"{self.title} - {self.director.name}"