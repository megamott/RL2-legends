from rest_framework import serializers
from ..models import (
    Question,
    QuestionCategory
)


class QuestionWithCategoryNameSerializer(serializers.ModelSerializer):
    """ Simple question serializer """

    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = '__all__'

    @staticmethod
    def get_category_name(obj):
        """ Name of category to which the question belongs"""
        return QuestionCategorySerializer(QuestionCategory.objects.find_by_category(obj.category)).data['category_name']


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


class QuestionCategoryWithQuestionsSerializer(serializers.ModelSerializer):
    """ Simple question category serializer """

    questions = serializers.StringRelatedField(many=True)

    class Meta:
        model = QuestionCategory
        fields = ['id', 'category_name', 'parent', 'questions', 'slug']


class QuestionCategoryDetailSerializer(serializers.ModelSerializer):
    """ Question category serializer with all questions details belonging to categories """

    question_details = serializers.SerializerMethodField()

    class Meta:
        model = QuestionCategory
        fields = '__all__'

    @staticmethod
    def get_question_details(obj):
        """ List of questions belonging to the category """
        return QuestionSerializer(Question.objects.find_by_category(obj), many=True).data
