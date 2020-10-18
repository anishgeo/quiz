from django.shortcuts import render
from .models import Quiz, Question, Answer, QuizAttendee

def quiz_view(request):
	if request.method == "GET":
		quiz_list = Quiz.objects.all()

		return render(request, 'quiz/quiz.html', {"context":quiz_list})

def quiz_list(request, slug):
	if request.method == "GET":
		try:
			quiz = Quiz.objects.get(slug=slug)
		except Exception as e:
			return render(request, 'quiz/quiz_list.html', {"context":None})

		questions = quiz.question_set.all()

		return render(request, 'quiz/quiz_list.html', {"context":questions})
	if request.method == "POST":
		pass
