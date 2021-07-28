from django.db import models
from multiselectfield import MultiSelectField
import uuid

from functools import partial as curry
YES_NO = (
    (0, 'No'),
    (1, 'Yes')
)

MALE = 1
FEMALE = 2

GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
ORGANS = (
        ('kidney', 'Kidney'),
        ('heart', 'Heart'),
        ('lungs', 'Lungs'),
        ('liver', 'Liver'),
        
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



class DonorKnowledge(models.Model):

    visitor_id = models.UUIDField(blank=True, null=True, editable=False, unique=True)
    gender = models.IntegerField(choices=GENDER)
    qualification = models.CharField(max_length=50, choices=QUALIFICATION)
    #income_range = models.DecimalField(max_digits=6, decimal_places=2)
    marital_status = models.IntegerField(choices=MARITAL_STATUS)
    date_completed = models.DateField(auto_now_add=True)
    #knowledge about organ donation
    q1 = models.SmallIntegerField(choices=YES_NO)
    q2 = MultiSelectField(choices=INFO_SOURCE,)
    q3 = models.SmallIntegerField(choices=YES_NO)
    q4 = models.SmallIntegerField(choices=YES_NO)
    q5 = models.SmallIntegerField(choices=YES_NO)
    q6 = models.SmallIntegerField(choices=YES_NO)
    q7 = models.SmallIntegerField(choices=YES_NO)
    q8 = models.SmallIntegerField(choices=YES_NO)
    q9 = models.SmallIntegerField(choices=YES_NO)
    q10 = models.SmallIntegerField(choices=YES_NO)

    def __str__(self):
        return str(self.visitor_id)
      

class DonorAttitude(models.Model):
   
  
    #Attitude about organ donation
    visitor_id = models.UUIDField(blank=True, null=True, editable=False, unique=True)

    date_completed = models.DateField(auto_now_add=True)
    q1 = models.SmallIntegerField(choices=YES_NO)  #Are you willing to donate an organ? 
    q2 = models.CharField(max_length=500) #If no, why? 
    q3 = models.SmallIntegerField(choices=YES_NO, blank=True, null=True) #If the answer to question 1 is yes, when (Living or after death):
    q4 = models.CharField(max_length=500, blank=True, null=True) #If the answer is yes, why? 
    q5 = MultiSelectField(choices=ORGANS, blank=True, null=True) #What organs will you donate during life? 
    q6 = models.CharField(max_length=500, blank=True, null=True) #If the answer is (after death), why? 
    q7 = MultiSelectField(choices=ORGANS, blank=True, null=True) #What organs will you donate after death? 
    q8 = models.CharField(max_length=100, blank=True, null=True) #Who are you willing to donate for? 
    q9 = models.CharField(max_length=500, blank=True, null=True) #In your opinion, what causes people not to donate organs? 
    q10 = models.CharField(max_length=500, blank=True, null=True) #What do you think of the methods to increase consent for donation? 
    q11 = models.SmallIntegerField(choices=YES_NO) #Do you know someone who has given consent to donate after death?   
    q12 = models.SmallIntegerField(choices=YES_NO) #Are you willing to give consent to donate after death? 
    q13 = models.CharField(max_length=200, blank=True, null=True) #If no, why? 
    q14 = models.SmallIntegerField(choices=YES_NO) #If you have a family member who is a brain-dead, would you consent to donate his/her organs? 

    def __str__(self):
        return str(self.visitor_id)