from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import Quiz, QuizScore, Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice


class QuizScoreAdmin(admin.ModelAdmin):
    model = QuizScore

   
    list_display  = ('visitor_id', 'quiz', 'score')

class QuizAdmin(admin.ModelAdmin):
    exclude = ('slug',)

class QuestionAdmin(admin.ModelAdmin):
    
    inlines = [ChoiceInline]



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizScore, QuizScoreAdmin)