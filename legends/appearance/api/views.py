from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import QuestionSerializer

from ..models import Question
from ..core.class_utils import BaseView


class QuestionViewSet(BaseView, ViewSet):
    """ ViewSet that for listing or retrieving Question """

    def list(self, request):
        queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Question.objects.find_by_id(pk)
        serializer = QuestionSerializer(queryset)
        return Response(serializer.data)
