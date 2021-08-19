from rest_framework.viewsets import ModelViewSet

from .serializers import QuestionSerializer
from ..core.class_utils import BaseView
from ..models import Question


class QuestionViewSet(BaseView, ModelViewSet):
    """ ViewSet that for listing or retrieving Question """

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
