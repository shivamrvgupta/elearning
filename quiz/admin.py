from django.contrib import admin  
from .models import Result, Quiz, Question, Answers
# Register your models here.

class AnswerInline(admin.TabularInline):
    model = Answers

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Quiz)
admin.site.register(Result)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answers)


