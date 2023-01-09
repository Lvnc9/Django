from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from . models import Choise, Question


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

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choise = question.choise_set.get(pk=request.port['chosise'])
    except (KeyError, Choise.DoesNotExist):
        # redisplay the question voting form.
        return render(request, "polls/detail.html", {
            "question" : question,
            "error_message" : "You didn't select a choise.",
        })
    else:
        selected_choise += 1
        selected_choise.save()
        # Always retunr an HttpRepsonseRedirect after successfully dealing
        # with post data. this prevents data from being posted twice if a 
        # hits the back button
        return HttpResponseRedirect(reverse('polls.results', 
            args=(question.id,)))
