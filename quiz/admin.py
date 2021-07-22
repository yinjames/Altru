from django.contrib import admin
from .models import Quiz, Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice


class QuizAdmin(admin.ModelAdmin):
    exclude = ('slug',)

class QuestionAdmin(admin.ModelAdmin):
    
    inlines = [ChoiceInline]



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Quiz, QuizAdmin)