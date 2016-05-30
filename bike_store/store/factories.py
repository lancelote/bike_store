from decimal import Decimal

import factory

from store import models


class BrandFactory(factory.DjangoModelFactory):

    name = factory.Sequence(lambda n: 'Test Brand %s' % n)

    class Meta:
        model = models.Brand


class SparePartFactory(factory.DjangoModelFactory):

    name = factory.Sequence(lambda n: 'Test Spare Part %s' % n)
    brand = factory.SubFactory(BrandFactory)
    price = Decimal('100.00')
    contact = factory.Sequence(lambda n: 'Test Contacts %s' % n)

    class Meta:
        model = models.SparePart
