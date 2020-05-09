from rest_framework import serializers
from core.models import Poll, Choice, Question


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('choice_text',)


class QuestionSerializer(serializers.ModelSerializer):
    choice = ChoiceSerializer()

    class Meta:
        model = Question
        fields = ('question_text', 'question_type', 'choice')


class ListPollSerializer(serializers.ModelSerializer):


    class Meta:
        model = Poll
        fields = ('title', 'start_at', 'end_at', 'question_set', 'question__choice_set')
