from django.contrib.gis.db import models


class Culture(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Farmer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Plot(models.Model):
    status = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4')
    )

    contour = models.PointField()
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)
    seasons = models.CharField(max_length=100, choices=status)

    def __str__(self):
        return self.farmer.name


class Season(models.Model):
    name = models.IntegerField()

    def __int__(self):
        return self.name







