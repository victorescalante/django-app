from django.db import models


class Question(models.Model):
    questions_text = models.CharField(max_length=200)
    pub_date = models.DateField()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)