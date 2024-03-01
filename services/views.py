from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Service
from menu.models import Category


def get_serv(request: HttpRequest) -> HttpResponse:
    service_serv = Service.objects.filter(category__parent__title='Услуги')
    return render(request, 'services/serv.html', context={'service_serv': service_serv})


def get_cons(request: HttpRequest) -> HttpResponse:
    services_consulting = Service.objects.filter(category__title="Консалтинг")
    return render(request, 'services/cons.html', context={'services_consulting': services_consulting})


def get_design(request: HttpRequest) -> HttpResponse:
    service_design = Service.objects.filter(category__title='Дизайн')
    return render(request, 'services/design.html', context={'service_design': service_design})


def get_mobile(request: HttpRequest) -> HttpResponse:
    service_mobile = Service.objects.filter(category__title='Мобильные приложения')
    return render(request, 'services/mobile.html', context={'service_mobile': service_mobile})


def get_soft(request: HttpRequest) -> HttpResponse:
    service_soft = Category.objects.filter(parent__title='Разработка ПО')
    return render(request, 'services/softs.html', context={'service_soft': service_soft})


def get_web(request: HttpRequest) -> HttpResponse:
    service_web = Service.objects.filter(category__title='Веб-приложения')
    return render(request, 'services/web.html', context={'service_web': service_web})