from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page_view, name='rental'),
    path('explore/', views.explore_page_view),
    path('host/', views.host_page_view),
    path('product/<int:apartment_id>', views.product_page_view, name='apartment_details'),
]
