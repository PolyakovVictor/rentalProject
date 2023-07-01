from django.shortcuts import render
from .utils import get_apartment_data


def explore_page_view(request):
    apartment_data = get_apartment_data()
    context = {'apartment_data': apartment_data}
    return render(request, 'rental/explore.html', context)


def home_page_view(request):
    return render(request, 'rental/home.html')


def host_page_view(request):
    return render(request, 'rental/host.html')
