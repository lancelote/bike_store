from rest_framework.serializers import ModelSerializer, SerializerMethodField

from store.models import Brand, SparePart


class BrandSerializer(ModelSerializer):

    class Meta:
        model = Brand
        fields = [
            'name'
        ]


class BrandTopSerializer(ModelSerializer):

    spare_part_num = SerializerMethodField()

    def get_spare_part_num(self, obj):
        return SparePart.objects.filter(brand=obj).count()

    class Meta:
        model = Brand
        fields = [
            'name',
            'spare_part_num',
        ]


class SparePartCreateSerializer(ModelSerializer):

    class Meta:
        model = SparePart
        fields = [
            'name',
            'brand',
            'price',
            'contact',
        ]


class SparePartListSerializer(SparePartCreateSerializer):

    brand = SerializerMethodField()

    def get_brand(self, obj):
        brand = obj.brand
        return BrandSerializer(brand).data
