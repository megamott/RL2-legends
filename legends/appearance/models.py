from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.shortcuts import get_object_or_404


class Category(models.Model):
    """ Categories of questions """

    category_name = models.CharField(
        max_length=50,
        verbose_name='name of category, like Преподаватели'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name='parent category, to achieve nesting of categories'
    )

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'Categories'

    @classmethod
    def get_default_pk(cls):
        """ Default value of Category model for .SET_DEFAULT behavior in models with FK """
        obj, created = cls.objects.get_or_create(category_name='Без категории')
        return obj.pk


class QuestionManager(models.Manager):
    """ Manager for question model """

    def get_queryset(self):
        """ Override get_queryset method from BaseManager """
        return super().get_queryset()

    def find_by_id(self, pk):
        """ Retrieve one question by id """
        return get_object_or_404(self.get_queryset(), pk=pk)

    def find_by_complexity(self, complexity_level):
        """ Find all questions by complexity: H, M, E """
        return self.get_queryset().filter(complexity=complexity_level)

    def find_by_group(self, group_name):
        """
        Find all questions by group
        Example: find_by_group('Общие знания')
        """
        return self.get_queryset().filter(group=group_name)


class Question(models.Model):
    """ Question for the quiz """

    COMPLEXITY_TYPES = (
        ('H', 'hard'),
        ('M', 'medium'),
        ('E', 'easy'),
    )

    question_name = models.CharField(
        max_length=200,
        verbose_name='question name, describing its essence'
    )
    question_text = models.CharField(
        max_length=200
    )
    question_answers = ArrayField(
        models.CharField(max_length=100),
        size=4,
        verbose_name='list of four answers for the question'
    )
    complexity = models.CharField(
        max_length=1,
        choices=COMPLEXITY_TYPES
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_DEFAULT,
        default=Category.get_default_pk,
        blank=True,
        verbose_name='which category the question belongs to'
    )
    hint = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='a hint to a question to help answer it'
    )
    objects = QuestionManager()

    def __str__(self):
        return f'{self.question_text}, ({self.category})'

    class Meta:
        verbose_name = 'question'
        verbose_name_plural = 'Questions'
        ordering = ['-complexity']
