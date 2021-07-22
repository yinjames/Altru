from django.db import models
from multiselectfield import MultiSelectField
#from django.utils.functional import curry
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


    gender = models.IntegerField(choices=GENDER)
    qualification = models.CharField(max_length=50, choices=QUALIFICATION)
    #income_range = models.DecimalField(max_digits=6, decimal_places=2)
    marital_status = models.IntegerField(choices=MARITAL_STATUS)
    date_completed = models.DateField(auto_now_add=True)
    #knowledge about organ donation
    q1 = models.BooleanField(choices=YES_NO)
    q2 = MultiSelectField(choices=INFO_SOURCE)
    q3 = models.BooleanField(choices=YES_NO)
    q4 = models.BooleanField(choices=YES_NO)
    q5 = models.BooleanField(choices=YES_NO)
    q6 = models.BooleanField(choices=YES_NO)
    q7 = models.BooleanField(choices=YES_NO)
    q8 = models.BooleanField(choices=YES_NO)
    q9 = models.BooleanField(choices=YES_NO)
    q10 = models.BooleanField(choices=YES_NO)


    def _get_help_text(self, field_name):
        """Given a field name, return it's help text."""
        for field in self._meta.fields:
            if field.name == field_name:
                return field.help_text

    def __init__(self, *args, **kwargs):
        # Call the superclass first; it'll create all of the field objects.
        super(DonorKnowledge, self).__init__(*args, **kwargs)

        # Again, iterate over all of our field objects.
        for field in self._meta.fields:
            # Create a string, get_FIELDNAME_help text
            method_name = "get_{0}_help_text".format(field.name)

            # We can use curry to create the method with a pre-defined argument
            curried_method = curry(self._get_help_text, field_name=field.name)

            # And we add this method to the instance of the class.
            setattr(self, method_name, curried_method)


class DonorAttitude(models.Model):
   
  
    #Attitude about organ donation
    date_completed = models.DateField(auto_now_add=True)
    q1 = models.BooleanField(choices=YES_NO)  #Are you willing to donate an organ? 
    q2 = models.CharField(max_length=100) #If no, why? 
    q3 = models.BooleanField(choices=YES_NO) #If the answer to question 1 is yes, when (Living or after death):
    q4 = models.CharField(max_length=100) #If the answer is yes, why? 
    q5 = MultiSelectField(choices=ORGANS) #What organs will you donate during life? 
    q6 = models.CharField(max_length=100) #If the answer is (after death), why? 
    q7 = MultiSelectField(choices=ORGANS) #What organs will you donate after death? 
    q8 = models.CharField(max_length=100) #Who are you willing to donate for? 
    q9 = models.CharField(max_length=100) #In your opinion, what causes people not to donate organs? 
    q10 = models.CharField(max_length=100) #What do you think of the methods to increase consent for donation? 
    q11 = models.BooleanField(choices=YES_NO) #Do you know someone who has given consent to donate after death?   
    q12 = models.BooleanField(choices=YES_NO) #Are you willing to give consent to donate after death? 
    q13 = models.CharField(max_length=20) #If no, why? 
    q14 = models.BooleanField(choices=YES_NO) #If you have a family member who is a brain-dead, would you consent to donate his/her organs? 