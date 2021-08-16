from django.db import models
from django.db.models.fields.related import ForeignKey
from multiselectfield import MultiSelectField
import uuid
from django.db.models.signals import post_delete, pre_save, post_save, pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

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





class Team(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)

    def get_team_points(self):
        
        champs = self.champion_set.all()

        points = 0
        for c in champs:
            points += c.points
        return points


    def __str__(self):
       return self.name
class Champion(models.Model):
 
    id = models.UUIDField(editable=False, unique=True,default=uuid.uuid4, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sponsor = models.ForeignKey('self', null=True, blank=True,on_delete=models.SET_NULL)
    level = models.IntegerField(default=0)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)
    date_created = models.DateField(auto_now_add=True)
    points = models.IntegerField(default=0)
    def __str__(self):
        return str(self.id)



@receiver(pre_delete, sender=Champion)
def auto_reassign_sponsored_on_champion_delete(sender, instance, **kwargs):
        sponsor = instance.sponsor

        sponsored =sender.objects.filter(sponsor=instance)



        if sponsored:
            if Team.objects.get(user=instance.user):
                my_team = Team.objects.get(user=instance.user)
                new_team_lead = sponsored.order_by('-date_created')[0]
                my_team.user = new_team_lead
                my_team.save()
            if sponsor:
                for sp in sponsored:
                    sp.sponsor = sponsor
                    sp.level = sponsor.level + 1
                    sp.save()
            else:
                for sp in sponsored:
                    sp.sponsor = None
                    sp.level = 1
                    sp.save()



@receiver(post_save, sender=Champion)
def auto_reassign_sponsor(sender, instance, created, **kwargs):
        
        sponsor = instance.sponsor

        sponsored =sender.objects.filter(sponsor=instance)
        if sponsored:
            if sponsor:
                for sp in sponsored:
                    sp.sponsor = sponsor
                    sp.level  = sponsor.level + 1
                    sp.save()
            else:
                for sp in sponsored:
                    sp.sponsor = None
                    sp.level = 0
                    sp.save()



@receiver(post_save, sender=Champion)
def auto_reassign_sponsor(sender, instance, created,  **kwargs):
        if created:
            sponsor = instance.sponsor
            if sponsor:
                instance.level  = sponsor.level + 1
                instance.save()



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