from django.db.models.base import Model
from django.forms import ModelForm
from django import forms
#from django.forms.models import model_to_dict
from . models import DonorAttitude, DonorKnowledge, Team, Story


YES_NO = (
    (0, 'No'),
    (1, 'Yes')
)

DEAD_ALIVE = (
    (0, 'Living'),
    (1, 'After death')
)

ORGANS = (
        ('kidney', 'Kidney'),
        ('heart', 'Heart'),
        ('lungs', 'Lungs'),
        ('liver', 'Liver'),
        
    )

MALE = 1
FEMALE = 2

GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )

AGE_RANGE = (
    ('18-64', '18-64 years'),
    ('65', '65 years or older')
)

INFO_SOURCE = (
    ('Radio/TV', 'Radio/TV'),
    ('Social Media', 'Social Media'),
    ('News Papers', 'News Papers')
)

QUALIFICATION =(
    ('Basic', 'Basic Level'),
    ('Secondary', 'Secondary Level'),
    ('Tertiary', 'Tertiary Level')
)


MARITAL_STATUS = (
    (1, 'Single'),
    (2, 'Married'),
    (3, 'Divorced')
)


class StoryForm(ModelForm):
    class Meta:
        model = Story
        exclude = ('champion',)

class TeamForm(ModelForm):

    class Meta:
        model = Team
        fields = ('team_name',)

class DonorKnowledgeForm(ModelForm):

    gender = forms.IntegerField(label='Sex:', widget=forms.RadioSelect(choices=GENDER))
    qualification = forms.CharField(label='Academic qualification:', widget=forms.RadioSelect(choices=QUALIFICATION))
    marital_status = forms.IntegerField(label='Marital status:', widget=forms.RadioSelect(choices=MARITAL_STATUS))
  
    #knowledge about organ donation
    q1 = forms.IntegerField(label='1. Have you heard about organ donation?', widget=forms.RadioSelect(choices=YES_NO))
    q2 = forms.MultipleChoiceField(label='2. Sources of information about organ donation ', widget=forms.CheckboxSelectMultiple, choices=INFO_SOURCE)
    q3 = forms.IntegerField(label='3. Do you know someone who is a recipient of organ transplant?',widget=forms.RadioSelect(choices=YES_NO))
    q4 = forms.IntegerField(label='4. Do you know someone who’s relative is a recipient of organ transplant?', widget=forms.RadioSelect(choices=YES_NO))
    q5 = forms.IntegerField(label='5. Does organ donation has effect on the recipient’s health?', widget=forms.RadioSelect(choices=YES_NO))
    q6 = forms.IntegerField(label='6. Is organ donation legal?', widget=forms.RadioSelect(choices=YES_NO))
    q7 = forms.IntegerField(label='7. Will someone who is brain-dead react (grimace, move away, or blink) if someone touches their eyeball?', widget=forms.RadioSelect(choices=YES_NO))
    q8 = forms.IntegerField(label='8. Can a person be brain-dead even if the heart is still beating? ', widget=forms.RadioSelect(choices=YES_NO))
    q9 = forms.IntegerField(label='9. Is brain death different from coma? ', widget=forms.RadioSelect(choices=YES_NO))
    q10 = forms.IntegerField(label='10. Is brain death different from a vegetative state? ', widget=forms.RadioSelect(choices=YES_NO,))


    class Meta:
        model = DonorKnowledge
    
        fields = ('gender','qualification', 'marital_status', 'q1', 'q2', 'q3', 'q4','q5','q6','q7', 'q8', 'q9', 'q10' )
        
        def __init__(self, *args, **kwargs):
            super(DonorKnowledgeForm, self).__init__(*args, **kwargs)


class DonorAttitudeForm(ModelForm):

    q1 = forms.IntegerField(label='Are you willing to donate an organ?', widget=forms.RadioSelect(choices=YES_NO)) 
    #q2 = forms.CharField(label='If no, why?', max_length=100, widget=forms.Textarea, required=False )  
    q3 = forms.IntegerField(label='If yes, when (Living or after death)', widget=forms.RadioSelect(choices=DEAD_ALIVE), required=False) 
    #q4 = forms.CharField(label="If the answer is yes, why?",widget=forms.Textarea, max_length=100, required=False) 

    q5 = forms.MultipleChoiceField(
        label='What organs will you donate during life?',
    widget=forms.CheckboxSelectMultiple, 
    choices=ORGANS,required=False ) 

    #q6 = forms.CharField(label='If the answer is (after death), why? ', max_length=100, widget=forms.Textarea, required=False)
    q7 = forms.MultipleChoiceField(label='What organs will you donate after death? ', widget=forms.CheckboxSelectMultiple, choices=ORGANS, required=False)

    #q8 = forms.CharField(label='Who are you willing to donate for?', max_length=100, widget=forms.Textarea, required=False) 
    #q9 = forms.CharField(label='In your opinion, what causes people not to donate organs?', max_length=100, widget=forms.Textarea, required=False) 
    #q10 = forms.CharField(label='What do you think of the methods to increase consent for donation? ', max_length=100, widget=forms.Textarea, required=False) 
    q11 = forms.IntegerField(label='Do you know someone who has given consent to donate after death?', widget=forms.RadioSelect(choices=YES_NO))   
    q12 = forms.IntegerField(label='Are you willing to give consent to donate your organs after death?', widget=forms.RadioSelect(choices=YES_NO), required=False)  
    #q13 = forms.CharField(label='If no, why? ', max_length=100, widget=forms.Textarea, required=False) 
    q14 = forms.IntegerField(label='If you have a family member who is a brain-dead, would you consent to donate his/her organs?', widget=forms.RadioSelect(choices=YES_NO)) 
    
    class Meta:

        model = DonorAttitude
        exclude = ('date_completed', )

        def __init__(self, *args, **kwargs):
            super(DonorAttitudeForm, self).__init__(*args, **kwargs)