from rest_framework import serializers
from ..models import (
    Question,
    QuestionCategory
)


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionCategory
        fields = '__all__'


class QuestionCategoryDetailsSerializer(serializers.ModelSerializer):

    questions = serializers.SerializerMethodField()

    class Meta:
        model = QuestionCategory
        fields = '__all__'

    @staticmethod
    def get_questions(obj):
        return QuestionSerializer(Question.objects.find_by_category(obj), many=True).data
