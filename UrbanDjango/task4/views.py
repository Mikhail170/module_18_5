from django.shortcuts import render
from django.views.generic import TemplateView


def task3_func_view(request):
    return render(request, 'fourth_task/platform4.html')


def task3_shop_view(request):
    return render(request, 'fourth_task/scates.html')


def task3_description_view(request):
    return render(request, 'fourth_task/cart.html')


def skate_list(request):
    scates = ['Коньки Vapor', 'Коньки Supreme', 'Коньки Nexus']

    context = {
        'scates': scates
    }
    return render(request, 'fourth_task/scates.html', context)