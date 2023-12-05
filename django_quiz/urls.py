from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search-survey/', views.search_survey, name='search_survey'),
    path('add-survey/', views.add_survey, name='add_survey'),
]