from rest_framework.viewsets import ModelViewSet

from ..core.class_utils import BaseView

from .serializers import (
    QuestionSerializer,
    QuestionCategorySerializer,
    QuestionCategoryDetailsSerializer
)

from ..models import (
    Question,
    QuestionCategory
)


class QuestionViewSet(BaseView, ModelViewSet):
    """ ViewSet that for listing or retrieving Question """

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionCategoryViewSet(BaseView, ModelViewSet):
    """ ViewSet that for listing or retrieving QuestionCategory """

    queryset = QuestionCategory.objects.all()
    serializer_class = QuestionCategorySerializer

    action_to_serializer = {
        'retrieve': QuestionCategoryDetailsSerializer
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )
