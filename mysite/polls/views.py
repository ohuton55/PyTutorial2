from django.shortcuts import render
from django.http  import HttpResponse
from django.template import loader
from django.utils import timezone 
from .models import Question

# Create your views here.
def index(request):
    # timezone テスト
    # now = timezone.now()
    # return HttpResponse(timezone.localtime(now))

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
    # ページのデザインと癒着する書き方
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    
    # get_template -> ./templates/polls/index.html
    template = loader.get_template('polls/index.html')

    # 'latest_question_list' ... html内でオブジェクトとして呼び出す変数名
    # latest_question_list ... model Question object 最新５件
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
