from rest_framework.routers import SimpleRouter
from .views import (
    QuestionViewSet,
    QuestionCategoryViewSet
)

router = SimpleRouter()
router.register('questions', QuestionViewSet, basename='list_questions')
router.register('categories', QuestionCategoryViewSet, basename='list_categories')

urlpatterns = []
urlpatterns += router.urls
