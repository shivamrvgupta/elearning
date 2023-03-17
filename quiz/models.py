from django.db import models
from topics.models import Sub_Topic
from django.contrib.auth.models import User
# Create your models here.

DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)


class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.ForeignKey(Sub_Topic, on_delete=models.CASCADE)
    number_of_question = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")
    required_score = models.IntegerField(help_text="required score in %")
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}-{self.topic}"
    
    def get_question(self):
        return self.question_set.all()
    
    class Meta:
        verbose_name_plural = 'Quizes'


class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)
    
    def get_answers(self):
        return self.answer_set.all()
    
class Answers(models.Model):
  text = models.CharField(max_length=200)
  correct = models.BooleanField(default=False)
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return f"question: {self.question.text}, answer:{self.text}, correct: {self.correct}"
  


class Result(models.Model):
  quiz =  models.ForeignKey(Quiz, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  score = models.FloatField()

  def __str__(self):
      return self.pk