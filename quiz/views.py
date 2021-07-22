from django.shortcuts import render, get_object_or_404
from .models import Question, Quiz

def quiz_list(request):

    quiz_list = Quiz.objects.all()

    return render(request, 'quiz/quiz_list.html', {"quiz_list":quiz_list})


def quiz(request,id):

    quiz = get_object_or_404(Quiz, pk=id)
    question_list = quiz.get_questions()

    return render(request, "quiz/quiz.html", {"quiz":quiz, "question_list": question_list})