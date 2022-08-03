from django import views
from django.contrib import admin
from django.urls import path
from fuelapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('petrol/', views.Petrol_Prices),
    path('diesel/', views.Diesel_Prices),
    path('lpg/', views.LPG_Prices),
    path('cng/', views.CNG_Prices),
]
