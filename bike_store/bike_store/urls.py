from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^store/', include('store.urls', namespace='store', app_name='store')),
    url(r'^api/', include('api.urls', namespace='api')),
]
