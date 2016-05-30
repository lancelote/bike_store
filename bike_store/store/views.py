from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .forms import SparePartForm
from .models import Brand, SparePart


def spare_part_list(request):
    """Список выставленных запчастей"""
    object_list = SparePart.objects.all()

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')
    try:
        spare_parts = paginator.page(page)
    except PageNotAnInteger:
        spare_parts = paginator.page(1)
    except EmptyPage:
        spare_parts = paginator.page(paginator.num_pages)

    return render(request, 'store/list.html', {
        'page': page,
        'spare_parts': spare_parts
    })


def spare_part_detail(request, spare_part):
    """Информация о детали, добавление новой"""
    spare_part = get_object_or_404(SparePart, id=spare_part)
    return render(request, 'store/detail.html', {
        'spare_part': spare_part
    })


def add_new(request):
    if request.method == 'POST':
        spare_part_form = SparePartForm(data=request.POST)
        if spare_part_form.is_valid():
            spare_part = spare_part_form.save()
            return HttpResponseRedirect('/store/%s/' % spare_part.id)
    else:
        spare_part_form = SparePartForm()

    return render(request, 'store/new.html', {
        'spare_part_form': spare_part_form
    })


def statistics(request):
    """Статистика по популярным маркам"""
    brands = Brand.objects.select_related() \
                          .annotate(parts_num=Count('sparepart')) \
                          .filter(parts_num__gte=5) \
                          .order_by('-parts_num')
    return render(request, 'store/stats.html', {
        'brands': brands
    })
