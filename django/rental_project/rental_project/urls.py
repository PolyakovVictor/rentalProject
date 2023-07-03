from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('rental.urls')),
    path('admin/', admin.site.urls),
    path("account/", include("account.urls")),
]
