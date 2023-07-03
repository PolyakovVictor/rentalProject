from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('explore', include('rental.urls')),
    path('host', include('rental.urls')),
    path('product', include('rental.urls')),
    path('', include('rental.urls')),
    path('admin/', admin.site.urls),
]
