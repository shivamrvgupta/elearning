from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse

# Create your views here.


class QuizListView(ListView):
    model= Quiz
    template_name = 'quizes/main.html'


def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    context = {
        'quiz' : quiz
    }
    return render(request, 'quizes/quiz.html', context=context)


def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_question():
        answers = []
        for a in q.get_answer():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data' : questions,
        'time' : quiz.time,
    })