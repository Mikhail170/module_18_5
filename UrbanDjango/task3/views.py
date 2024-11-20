from django.shortcuts import render
from django.views.generic import TemplateView


def task3_func_view(request):
    return render(request, 'third_task/platform.html')


def task3_shop_view(request):
    return render(request, 'third_task/scates.html')


def task3_description_view(request):
    return render(request, 'third_task/description.html')


def skate_list(request):
    VAPOR = 'Коньки Vapor'
    SUPREME = 'Коньки Supreme'
    NEXUS = 'Коньки Nexus'

    context = {
        'VAPOR': VAPOR,
        'SUPREME': SUPREME,
        'NEXUS': NEXUS,
    }
    return render(request, 'third_task/scates.html', context)
