from django.shortcuts import render, redirect
from django.http import HttpResponse, response
from .forms import DonorAttitudeForm, DonorKnowledgeForm
import uuid
from .models import DonorAttitude, DonorKnowledge, Champion, Team
from django.contrib.auth.decorators import login_required
from quiz.models import Quiz


def home(request, *args, **kwargs):
    sponsor = str(kwargs.get('sponsor'))
    #request.session.get('has_taken_survey', False)
       
    if sponsor:
        request.session['sponsor']  = sponsor
        print("Sponsor: {0}".format(sponsor))

    num_visits = request.session.get('num_visits', 0)
    visitor_id = get_visitor_id(request)
    print(request.session.keys())
    print("Visitor ID: {0}".format(visitor_id))
    request.session['num_visits'] = num_visits + 1
    

  
    taken_survey = request.session.get('has_taken_survey')
    given_consent = request.session.get('has_given_consent')
    
    return render(request, "home.html", {'has_taken_survey':taken_survey, 'has_given_consent':given_consent})


def donor_stats(request):

    champ_list = Champion.objects.all().order_by('-points')
    return render(request, 'donor/donor.html',{'champ_list':champ_list})



def team_stats(request):

    team_list = Team.objects.all()

    return render(request, 'donor/team.html',{'team_list':team_list})


@login_required
def create_team(request):
    if request.method == 'POST':
        pass

    return render(request, 'donor/create_team.html',{})


@login_required
def profile(request):
    has_team = False
    quiz_list = Quiz.objects.all()

    if not Champion.objects.filter(user=request.user).exists():
        

        champ = Champion.objects.create(user=request.user)
        sponsor = request.session.get('sponor')
        if sponsor:
            champ.sponsor = sponsor
        champ.save()

    if Team.objects.filter(user=request.user).exists():
        has_team = True

    return render(request, 'donor/profile.html', {'has_team':has_team, 'quiz_list':quiz_list})

def enrollment(request):

    return render(request, "donor/enroll.html", {})


def donor_attitude(request):
    visitor_id = get_visitor_id(request)
    
    print(visitor_id)
    if request.method == "POST":
        form = DonorAttitudeForm(request.POST)
        if form.is_valid():
            print('form is valid')
            survey = form.save(commit=False)
            if visitor_id:
                survey.visitor_id = visitor_id

            survey.save()
            request.session['has_taken_survey'] = True
            if survey.q12:
                request.session['has_given_consent'] = True
                print("Willing to give consent")
            return redirect('/')
        else:
            for er in form.errors:
                print(er)
            return render(request, "donor/donor_attitude.html", {'form':form})

    else:
        form = DonorAttitudeForm()
        #request.session['survey'] = False

    
    return render(request, "donor/donor_attitude.html", {'form':form})


def donor_knowledge(request):
    
    visitor_id = get_visitor_id(request)
    survey = None
    if DonorKnowledge.objects.filter(visitor_id=visitor_id).count():
                survey = DonorKnowledge.objects.get(visitor_id=uuid.UUID(visitor_id))

    print(survey)
    if request.method == 'POST':

        form = DonorKnowledgeForm(request.POST, instance=survey)
        if form.is_valid():
            survey = form.save(commit=False)
            if visitor_id and survey:
                survey.visitor_id = uuid.UUID(visitor_id)

            survey.save()

            return redirect('donor:survey_attitude')
        else:
            return render(request, "donor/donor_knowledge.html", {'form':form})

    else:
        if visitor_id:
            if survey:
                form = DonorKnowledgeForm(instance=survey)

                return render(request, "donor/donor_knowledge.html", {'form':form})
            else:
                form = DonorKnowledgeForm()
                return render(request, "donor/donor_knowledge.html", {'form':form})
        else:
            form = DonorKnowledgeForm()
       
            return render(request, "donor/donor_knowledge.html", {'form':form})


def get_visitor_id(request):
    #visitor_id =  None 
    if not request.session.get('visitor_id'):
        request.session['visitor_id'] = str(uuid.uuid4())
        visitor_id = request.session.get('visitor_id', )
        #request.session.modified = True
        return visitor_id
    else:
        visitor_id = request.session.get('visitor_id')
        return visitor_id