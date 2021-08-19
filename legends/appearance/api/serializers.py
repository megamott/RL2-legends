from rest_framework import serializers
from ..models import (
    Question,
    QuestionCategory
)


class QuestionSerializer(serializers.ModelSerializer):
    """ Simple question serializer """
    class Meta:
        model = Question
        fields = '__all__'


class QuestionCategorySerializer(serializers.ModelSerializer):
    """ Simple question category serializer """
    class Meta:
        model = QuestionCategory
        fields = '__all__'


class QuestionCategoryDetailsSerializer(serializers.ModelSerializer):
    """ Question category serializer with questions belonging to categories """

    questions = serializers.SerializerMethodField()

    class Meta:
        model = QuestionCategory
        fields = '__all__'

    @staticmethod
    def get_questions(obj):
        """ List of questions belonging to the category """
        return QuestionSerializer(Question.objects.find_by_category(obj), many=True).data
