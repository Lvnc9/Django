#!/usr/bin/python3\
# Start
# Modules
from django.shortcuts import render

from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name="index"),                     # path -> polls/
    path("<int:question_id>/", views.detail, name="detail"), # path -> polls/5
    path("<int:question_id>/results/", views.result, name="results"),# path -> polls/5/results
    path("<int:question_id>/vote", views.vote, name="votes")     # path -> polls/5/vote
    ]


# End