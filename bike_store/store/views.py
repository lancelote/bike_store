from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404, render

from .models import SparePart


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


def statistics(request):
    """Статистика по популярным маркам"""
    pass
