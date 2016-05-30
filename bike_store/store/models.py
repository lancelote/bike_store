from django.db import models


class Brand(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SparePart(models.Model):

    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.name
