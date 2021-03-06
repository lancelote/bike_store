from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.spare_part_list, name='spare_part_list'),
    url(r'^(?P<spare_part>\d+)/$', views.spare_part_detail, name='spare_part_detail'),
    url(r'^stats/$', views.statistics, name='statistics'),
    url(r'^new/$', views.add_new, name='new'),
]
