from django.shortcuts import render
from django.http import HttpResponse, response
from .forms import DonorAttitudeForm, DonorKnowledgeForm

def home(request):

    #request.session.get('has_taken_survey', False)
       
      
    
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    request.session.set_test_cookie()
    print('Test Cookie worked: ',request.session.test_cookie_worked())
    request.session.delete_test_cookie()

  
    taken_survey = request.session.get('has_taken_survey')
   
    #print(request.)

    return render(request, "home.html", {'has_taken_survey':taken_survey})


def enrollment(request):

    return render(request, "donor/enroll.html", {})


def donor_attitude(request):
    request.session['has_taken_survey'] = False
    if request.method == "GET":
        form = DonorAttitudeForm()
    else:
        request.session['survey'] = False

    
    return render(request, "donor/donor_attitude.html", {'form':form})


def donor_knowledge(request):
    request.session['has_taken_survey'] = True

    if request.session.test_cookie_worked():
            print('Cookies Worked!')
            request.session.delete_test_cookie()
            return HttpResponse("You're logged in.")
    
    if request.method == 'POST':
        form = DonorKnowledgeForm(request.POST)
    
        if form.is_valid():
            print('form valid')
        else:
            #print(form)
            print('form is not valid')
            for err in form.errors:
                print(err, '\n')
            return render(request, "donor/donor_knowledge.html", {'form':form})
    else:
        form = DonorKnowledgeForm()
        #print(form)
        return render(request, "donor/donor_knowledge.html", {'form':form})