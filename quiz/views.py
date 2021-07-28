from django.shortcuts import render, get_object_or_404
from .models import Question, Quiz
from django.http import JsonResponse
import uuid

def quiz_list(request):

    quiz_list = Quiz.objects.all()

    return render(request, 'quiz/quiz_list.html', {"quiz_list":quiz_list})


def quiz(request,id):

    quiz = get_object_or_404(Quiz, pk=id)
    question_list = quiz.get_questions()

    return render(request, "quiz/quiz.html", {"quiz":quiz, "question_list": question_list})


def quiz_data(request, id):
    quiz = Quiz.objects.get(pk=id)

    question_list = []
    for q in quiz.get_questions():
        choices = []

        for c in q.get_choices():
            choices.append(c.choice_text + ':{0}'.format(c.correct) )

        question_list.append({str(q.question_text):choices})
    
    return JsonResponse({
        'data': question_list
    })