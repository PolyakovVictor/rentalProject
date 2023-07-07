from django.shortcuts import render
from .utils import get_apartment_data, get_apartment_data_by_id, get_filter_apartment
from django.core.paginator import Paginator


def home_page_view(request):
    return render(request, 'rental/home.html')


def host_page_view(request):
    return render(request, 'rental/host.html')


def product_page_view(request, apartment_id):
    apartment_data = get_apartment_data_by_id(apartment_id)
    context = {'apartment_data': apartment_data}
    return render(request, 'rental/product.html', context)


def explore_page_view(request):
    max_price = request.GET.get("max_price")
    title = request.GET.get("title")
    country = request.GET.get("country")
    city = request.GET.get("city")
    property_type = request.GET.get("type")
    room_count = request.GET.get("room_count")
    variables = [
        max_price,
        title,
        country,
        city,
        property_type,
        room_count
    ]
    if any(variables):
        apartments = get_filter_apartment(max_price, title, country, city, property_type, room_count)
    else:
        apartments = get_apartment_data()
    paginator = Paginator(apartments, 9)
    page_number = request.GET.get('page')
    apartment_data = paginator.get_page(page_number)
    context = {'apartment_data': apartment_data}
    return render(request, 'rental/explore.html', context)
