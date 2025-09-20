from django.contrib import admin
from django.urls import path
from sihapp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('registration/', views.registration, name="registration"),
    path('features/', views.features, name="features"),
    path('contact/', views.contact, name="contact"),
    path('internship/', views.internship, name="internship"),
    path('quicklinks/', views.quicklinks, name="quicklinks"),
    path('great/',views.great, name="great"),
    path("matches/", views.show_matches, name="matches"),
]

