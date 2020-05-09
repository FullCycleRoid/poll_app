from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Poll
from .serializers import ListPollSerializer


class ListPollView(APIView):

    def get(self, request, format=None):
        poll = Poll.objects.all()
        serializer = ListPollSerializer(poll, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#
# @api_view(['GET'])
# def polls_complete_by_user(request):
#     polls = Poll.objects.filter(user=request.query_params.get['id'])
#     serializer = PollDetailSerializer(polls, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)