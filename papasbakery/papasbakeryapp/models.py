from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=500)
    quest_date = models.DateTimeField("date the question was asked")


class Allergies(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)