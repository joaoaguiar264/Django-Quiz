from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search-survey/', views.search_survey, name='search_survey'),
    path('add-survey/', views.add_survey, name='add_survey'),
    path('my-surveys/', views.my_surveys, name='my_surveys'),
    path('survey-details/<int:id>', views.survey_details, name='survey_details'),
    path('answer-survey/<int:id>', views.answer_survey, name='answer_survey'),
    path('close-survey/<int:id>', views.close_survey, name='close_survey')
]