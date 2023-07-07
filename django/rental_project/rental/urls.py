from django.urls import path
from . import views

app_name = 'rental'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('filter/', views.explore_listings, name='filter'),
    path('explore/', views.explore_page_view, name='explore'),
    path('host/', views.host_page_view, name='host'),
    path('product/<int:apartment_id>', views.product_page_view, name='apartment_details'),
]
