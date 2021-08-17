from rest_framework.routers import SimpleRouter
from .views import QuestionViewSet

router = SimpleRouter()
router.register('questions', QuestionViewSet, basename='list_questions')

urlpatterns = []
urlpatterns += router.urls
