from django.contrib import admin
from django.urls import path
from djangoprj.views import index

urlpatterns = [
    path('index', index)
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),  # Оставили только allauth
    path("products/", include("simpleapp.urls")),
]