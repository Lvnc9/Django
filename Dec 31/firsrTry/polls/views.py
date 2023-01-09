from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from . models import Question


# return questions date from Question date saved
def index(request):
    latest_question_list = Question.objects.order_by("-pub-date")[:5]
    template = loader.get_template('index.html')
    context = {
        "latest_question_list" : latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    

# first style
#def detail(request, question_id):
#    return HttpResponse(f"You're looking at the question {question_id}")

# Second style
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {'quesiton': question})

def result(request, question_id):
    reponse = f"You're looking at the result of question {question_id}"
    return HttpResponse(reponse)

def vote(request, quesiton_id):
    return HttpResponse(f"You're voting at the question {quesiton_id}")
