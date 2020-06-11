from rest_framework import serializers
from core.models import Poll, Choice, Question


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ('id', 'choice_text',)


class QuestionSerializer(serializers.ModelSerializer):
    choice_set = ChoiceSerializer(many=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='question-detail',
        lookup_field='pk'
    )

    class Meta:
        model = Question
        fields = ('question_text', 'question_type', 'choice_set', 'url')


class ListPollSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='poll-detail',
        lookup_field='pk'
    )

    class Meta:
        model = Poll
        fields = ('title', 'start_at', 'end_at', 'url')


class DetailPollSerializer(serializers.ModelSerializer):
    question_set = QuestionSerializer(many=True)

    class Meta:
        model = Poll
        fields = ('title', 'start_at', 'end_at', 'question_set')

