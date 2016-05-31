# pylint: disable=unused-argument

from django.db.models import Count

from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView

from store.models import Brand, SparePart
from .pagination import SparePartPageNumberPagination
from .serializers import BrandTopSerializer, SparePartListSerializer, SparePartCreateSerializer


class SparePartListAPIView(ListAPIView):

    queryset = SparePart.objects.all()
    serializer_class = SparePartListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'brand__name']
    pagination_class = SparePartPageNumberPagination


class SparePartCreateAPIView(CreateAPIView):

    queryset = SparePart.objects.all()
    serializer_class = SparePartCreateSerializer


class BrandTopListAPIView(ListAPIView):

    serializer_class = BrandTopSerializer

    def get_queryset(self, *args, **kwargs):
        return Brand.objects.select_related() \
                            .annotate(parts_num=Count('sparepart')) \
                            .filter(parts_num__gte=5) \
                            .order_by('-parts_num')
