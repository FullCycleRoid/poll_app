from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Poll, Question
from .serializers import ListPollSerializer, DetailPollSerializer, QuestionSerializer


class ListPollView(APIView):

    def get(self, request, format=None):
        poll = Poll.objects.all()
        serializer = ListPollSerializer(poll, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class DetailPollView(APIView):

    def get(self, request, format=None, **kwargs):
        poll = Poll.objects.get(pk=kwargs['pk'])
        print(poll)
        serializer = DetailPollSerializer(poll, context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)


class DetailQuestionView(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.get(pk=kwargs['pk'])
        serializer = QuestionSerializer(question, context={'request': request})
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def vote(request, pk):
    user = request.user
    print(user)
    question = Question.objects.get(pk=pk)