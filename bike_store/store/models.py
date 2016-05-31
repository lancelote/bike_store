from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Brand(models.Model):
    """Марка запасной части"""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SparePart(models.Model):
    """Запасная часть"""

    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True,
                                validators=[MinValueValidator(Decimal('0.01'))])
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.name
