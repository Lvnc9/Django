from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hallo this is a test")


def detail(request, question_id):
    return HttpResponse(f"You're looking at the question {question_id}")

def result(request, question_id):
    reponse = f"You're looking at the result of question {question_id}"
    return HttpResponse(reponse)

def vote(request, quesiton_id):
    return HttpResponse(f"You're voting at the question {quesiton_id}")
