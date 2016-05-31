from django.conf.urls import url

from .views import BrandTopListAPIView, SparePartListAPIView, SparePartCreateAPIView

urlpatterns = [
    url(r'^list/$', SparePartListAPIView.as_view(), name='spare_part_list'),
    url(r'^create/$', SparePartCreateAPIView.as_view(), name='new'),
    url(r'^stats/$', BrandTopListAPIView.as_view(), name='statistics'),
]
