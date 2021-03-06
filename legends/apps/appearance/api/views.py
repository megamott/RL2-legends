from rest_framework.viewsets import ModelViewSet

from legends.apps.core.class_utils import BaseView

from .serializers import (
    QuestionWithCategoryNameSerializer,
    QuestionCategoryWithQuestionsSerializer,
    QuestionCategoryDetailSerializer
)

from ..models import (
    Question,
    QuestionCategory
)


class QuestionViewSet(BaseView, ModelViewSet):
    """ ViewSet that for listing or retrieving Question """

    lookup_field = 'slug'
    queryset = Question.objects.all()
    serializer_class = QuestionWithCategoryNameSerializer


class QuestionCategoryViewSet(BaseView, ModelViewSet):
    """ ViewSet that for listing or retrieving QuestionCategory """

    lookup_field = 'slug'
    queryset = QuestionCategory.objects.all()
    serializer_class = QuestionCategoryWithQuestionsSerializer

    action_to_serializer = {
        'retrieve': QuestionCategoryDetailSerializer
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )
