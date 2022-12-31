#!/usr/bin/python3\
# Start
# Modules
from django.shortcuts import render

from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name="index")
]


# End