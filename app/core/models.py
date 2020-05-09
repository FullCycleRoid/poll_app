from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    start_at = models.DateField()
    end_at = models.DateField(blank=True, null=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Question(models.Model):
    type_of_question = (
        ('1', 'Text answer'),
        ('2', 'One choice option'),
        ('3', 'Multiple choice option')
    )
    question = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question_type = models.CharField(max_length=1, choices=type_of_question, default=1)
    question_text = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
