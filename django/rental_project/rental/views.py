from django.shortcuts import render


# Create your views here.
def explore_page_view(request):
    return render(request, 'rental/explore.html')


def home_page_view(request):
    return render(request, 'rental/home.html')


def host_page_view(request):
    return render(request, 'rental/host.html')
