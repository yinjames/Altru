from django.db.models.query_utils import Q
from django.shortcuts import redirect, render, get_object_or_404
from .models import Question, Quiz, QuizScore
from django.http import JsonResponse
from donor.models import DonorAttitude
import uuid
import random
from utils import get_visitor_id
from django.urls import reverse


def quiz_list(request):

    quiz_list = Quiz.objects.all()

    return render(request, 'quiz/quiz_list.html', {"quiz_list":quiz_list})


def educate_donor(request):

    quiz = Quiz.objects.all()[0]
    question_list = quiz.get_questions()

    return redirect('quiz:quiz', id=quiz.id)
    #return render(request, "quiz/quiz.html", {"quiz":quiz, "question_list": question_list})



def quiz(request,id):

    quiz = get_object_or_404(Quiz, pk=id)
    question_list = quiz.get_questions()

    return render(request, "quiz/quiz.html", {"quiz":quiz, "question_list": question_list})


def quiz_data(request, id):
    quiz = Quiz.objects.get(pk=id)
    url = reverse("donor:consent_after_quiz")
    print(url)

    question_list = []
    for q in quiz.get_questions():
        choices = []

        for c in q.get_choices():
            choices.append(c.choice_text + ':{0}'.format(c.correct) )

        choices.append(q.long_text)
        question_list.append({str(q.question_text):choices})
    
    return JsonResponse({
        'data': question_list,
        'url': url
    })


def add_score(request, quiz_id, score):
    
    quiz_id = int(quiz_id)
    try:
        visitor_id  = get_visitor_id(request)
        survey = DonorAttitude.objects.get(visitor_id=visitor_id)
        survey.quiz_score = int(score)
        survey.save()
        print(survey)
        quiz = Quiz.objects.get(id=quiz_id)
        QuizScore.objects.create(visitor_id=visitor_id,quiz=quiz, score=score)
        #survey = DonorAttitude.objects.get(visitor_id=visitor_id)
        
        return JsonResponse({
        'data': True
        })

    except:
         return JsonResponse({
        'data': False
    })



   
    