from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def get_cons(request: HttpRequest) -> HttpResponse:
    return render(request, 'services/cons.html')
