#from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
#from django.template import RequestContext, loader
from polls.models import Question,Choice
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    content =  {'latest_question_list':latest_question_list}
    #output = ', '.join([p.question_text for p in last_question_list])
    #return HttpResponse(template.render(content))
    return render(request,'polls/index.html',content)

def detail(request,question_id):
    #try:
    #question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
     #   raise Http404('Question does not exist')
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/detail.html',{'question':question})
    #return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)