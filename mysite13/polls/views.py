from django.shortcuts import get_object_or_404, render
from django.http  import HttpResponseRedirect
# from django.http  import HttpResponse, Http404
# from django.template import loader
# from django.utils import timezone
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

#------------------------------------------------------------------
#def index(request):
    # timezone テスト
    # now = timezone.now()
    # return HttpResponse(timezone.localtime(now))

#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
    # ページのデザインと癒着する書き方
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    
    # latest_question_list ... model Question object 最新５件
#    context = {
#        'latest_question_list': latest_question_list,
#    }

    # ショートカットを使わない書き方
    # get_template -> ./templates/polls/index.html
    # template = loader.get_template('polls/index.html')

    # 'latest_question_list' ... html内でオブジェクトとして呼び出す変数名
    # return HttpResponse(template.render(context, request))

    # shortcuts.renderを使う書き方
 #   return render(request, 'polls/index.html', context)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

#------------------------------------------------------------------
#def detail(request, question_id):
    # ショートカットを使わない書き方
    # try:
    #    question = Question.objects.get(pk=question_id)
                                # primary key = <int:question_id>
    # except Question.DoesNotExist:
    #    raise Http404("Question does not exist. question_id is %s" % question_id)
    
    # shortcuts.get_object_or_404を使う書き方
#    question = get_object_or_404(Question, pk=question_id)

#    return render(request, 'polls/detail.html', {'question': question})

    # shortcuts.render()を使わない例
    # %s <= % object
    # return HttpResponse("You're looking at question %s." % question_id)

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
# "pk" という名前で URL からプライマリキーをキャプチャ -> path('<int:pk>/', , )

#------------------------------------------------------------------
#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/results.html', {'question': question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

#------------------------------------------------------------------

def vote(request, question_id):
    # question_id ... detail.html formからPOSTされたchoice=#が来る
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice,DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 東京数+1して保存
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
