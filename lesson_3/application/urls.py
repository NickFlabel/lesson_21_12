from django.urls import path
from application.views import index

urlpatterns = [
    path('ads/', index)
]
