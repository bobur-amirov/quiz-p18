from random import sample

from django.db.models import Q
from django.core.cache import cache
from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from .filters import ResultFilter
from .models import Category, Question, Result
from .services import check_answer


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        cd = super().get_context_data(**kwargs)
        cd['categories'] = Category.objects.all()
        return cd


def question_list(request, slug):
    category = Category.objects.get(slug=slug)
    questions = Question.objects.filter(category=category)
    questions = sample(list(questions), 3)
    if cache.get('questions'):
        questions = cache.get('questions')
    else:
        cache.set('questions', questions, 300)
    if request.method == 'POST':
        context = check_answer(request, questions, category)
        cache.delete('questions')
        return render(request, 'app/result.html', context)

    context = {
        'questions': questions,
        'category': category,
    }

    return render(request, 'app/question_list.html', context)



def result_list(request):
    filter = ResultFilter(request.GET, queryset=Result.objects.all())

    context = {
        'filter': filter
    }
    return render(request, 'app/result_list.html', context)