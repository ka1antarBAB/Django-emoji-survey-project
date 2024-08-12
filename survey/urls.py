from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'survey'

urlpatterns = [
    path('', views.emoji_survey_view, name='emoji_survey'),
]
