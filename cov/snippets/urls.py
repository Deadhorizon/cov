from django.urls import path
from snippets import views

urlpatterns = [
    path('covid', views.covid_list),
]