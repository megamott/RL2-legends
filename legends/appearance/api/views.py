from rest_framework.viewsets import ModelViewSet
from .serializers import QuestionSerializer

from ..models import Question
from ..core.class_utils import BaseView


class QuestionViewSet(BaseView, ModelViewSet):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
