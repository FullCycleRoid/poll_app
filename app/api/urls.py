from django.urls import path

from .views import ListPollView

urlpatterns = [
    # path('user/', polls_complete_by_user),
    path('polls/', ListPollView.as_view()),

]