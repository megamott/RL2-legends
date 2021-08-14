from django.urls import path
from .views import QuestionList

urlpatterns = [
    path('question/', QuestionList.as_view()),
]
