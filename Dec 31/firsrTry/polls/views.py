from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from . models import Choise, Question
from django.views import generic


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
    response = f"You're looking at the result of question {question_id}"
    return HttpResponse(response)

def vote(request, quesiton_id):
    return HttpResponse(f"You're voting at the question {quesiton_id}")


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """ return the last file published quesiton """
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/details.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choise = question.choise_set.get(pk=request.port['choises'])
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
