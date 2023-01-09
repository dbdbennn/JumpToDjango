from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Question


def index(request):
    # - 기호가 붙어 있으면 역방향, 없으면 순방향 정렬을 의미한다.
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)