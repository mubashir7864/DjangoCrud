from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
    latest_question = Question.objects.order_by('pub_date')[:5]
    context = {'latest_question':latest_question}
    return render(request, 'index.html' , context)

def detail(request,question_id):
    return HttpResponse("Your a looking at question %s" % question_id)


def results(request, question_id):
    response = "Your are looking at result page %s"
    return HttpResponse(response % question_id)

def vote (request, question_id):
    return HttpResponse ("You're voting on question %s" %question_id)

