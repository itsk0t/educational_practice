from django.shortcuts import render
from django.views.generic import ListView


def main_view(request):
    return render(request, 'main/main.html')
