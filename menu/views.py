from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from services.models import Service
from services.models import Category


def get_portfolio(request: HttpRequest) -> HttpResponse:
    service_portfolio = Service.objects.filter(category__title='Портфолио')
    all_category = Category.objects.all()
    print(all_category)
    return render(request, 'menu/portfolio.html', context={'service_portfolio': service_portfolio})


def get_main(request: HttpRequest) -> HttpResponse:
    return render(request, 'menu/main.html')


def get_about(request: HttpRequest) -> HttpResponse:
    return render(request, 'menu/about.html')


def get_contacts(request: HttpRequest) -> HttpResponse:
    return render(request, 'menu/contacts.html')


def get_history(request: HttpRequest) -> HttpResponse:
    return render(request, 'menu/history.html')


def get_team(request: HttpRequest) -> HttpResponse:
    return render(request, 'menu/team.html')
