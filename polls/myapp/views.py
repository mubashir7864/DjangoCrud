from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.db.models import F
from django.urls import reverse
# Create your views here.

def index(request):
    latest_question = Question.objects.order_by('pub_date')[:5]
    context = {'latest_question':latest_question}
    return render(request, 'index.html' , context)


def detail(request,question_id):
    question = get_object_or_404(Question,id=question_id)
    return render(request, 'detail.html',{'question':question})



def results(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'results.html',{'question':question} )



def vote (request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_Choice = question.choices.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'detail.html', {'question': question, 'error' : "you didn't Select a choice"})
    
    else:
        selected_Choice.votes = F("votes") + 1
        selected_Choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))




