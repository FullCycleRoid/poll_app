from django.urls import path

from .views import ListPollView, DetailPollView, DetailQuestionView

urlpatterns = [
    path('polls/', ListPollView.as_view()),
    path('polls/<int:pk>', DetailPollView.as_view(), name='poll-detail'),
    path('question/<int:pk>', DetailQuestionView.as_view(), name='question-detail')

]