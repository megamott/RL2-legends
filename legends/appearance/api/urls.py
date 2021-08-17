from django.urls import path

from rest_framework import routers
from .views import QuestionViewSet

router = routers.SimpleRouter()
router.register('questions', QuestionViewSet, 'questions')

urlpatterns = []
urlpatterns += router.urls
