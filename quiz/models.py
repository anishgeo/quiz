
from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
	name = models.CharField(max_length=1000)
	questions_count = models.IntegerField(default=0)
	description = models.CharField(max_length=70)
	created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	slug = models.CharField(max_length=100)
	
	class Meta:
		verbose_name_plural = "quiz"
	
	def __str__(self):
		return self.name

class Question(models.Model):
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	question_label = models.CharField(max_length=1000)

	def __str__(self):
		return self.question_label

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer = models.CharField(max_length=1000)
	is_correct = models.BooleanField(default=False)

	def __str__(self):
		return self.answer

class QuizAttendee(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	correct_answers = models.IntegerField(default=0)

	def __str__(self):
		return self.user
