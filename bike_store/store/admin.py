from django.contrib import admin

from .models import Brand, SparePart


class BrandAdmin(admin.ModelAdmin):

    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Brand, BrandAdmin)


class SparePartAdmin(admin.ModelAdmin):

    list_display = ('name', 'brand', 'price', 'contact')
    search_fields = ('name', 'brand')

admin.site.register(SparePart, SparePartAdmin)
