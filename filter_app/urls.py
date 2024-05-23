from django.urls import path
from filter_app import views

urlpatterns = [
    path('about/', views.about),
    path('contact/', views.contact),
    path('methods/', views.methods),
]