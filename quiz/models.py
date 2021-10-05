from django.db import models
from django.contrib.auth.models import User
#from django.template.defaultfilters import slugify
from django.utils.text import slugify
import uuid
class Quiz(models.Model):
    name = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True)
    number_of_questions = models.IntegerField(default=5)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)


    def get_questions(self):
        return self.question_set.all()[:self.number_of_questions]

    class Meta:
        ordering=('-name',)
        verbose_name_plural = "Quizes"
    
    def __str__(self):
        return f"{self.topic}-{self.name}"

class Question(models.Model):
    question_text = models.CharField(max_length=1000)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    long_text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.question_text

    def get_choices(self):
        
        return self.choice_set.all()



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.choice_text


class QuizScore(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    #user = models.ForeignKey(User,  on_delete=models.CASCADE)
    visitor_id = models.UUIDField(blank=True, null=True, editable=False, unique=True)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.visitor_id} - {self.score}"