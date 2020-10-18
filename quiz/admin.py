from django.contrib import admin
from .models import Quiz, Question, Answer, QuizAttendee
from django.apps import apps

class AnswerInline(admin.TabularInline):
	model = Answer
	extra = 4
	max_num = 4

class QuestionInline(admin.TabularInline):
	model = Question
	inlines = [AnswerInline,]
	extra = 19

class QuizAdmin(admin.TabularInline):
	inlines = [QuestionInline,]

models = apps.get_models()
for model in models:
	try:
		admin.site.register(model)
	except:
		continue
