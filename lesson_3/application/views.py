from django.shortcuts import render
from application.models import Ad
from django.http import HttpRequest, HttpResponse

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    message = "Список реклам:\n\n\n"
    for ad in Ad.objects.all():
        message += str(ad.name) + '\n' + str(ad.description) + '\n' + str(ad.published)
    return HttpResponse(message, content_type="text/plain; charset=utf-8")
