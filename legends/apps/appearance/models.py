from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class QuestionCategoryManager(models.Manager):
    """ Manager for QuestionCategory model """

    def get_queryset(self):
        """ Override get_queryset method from BaseManager """
        return super().get_queryset()

    def find_by_category(self, category):
        """ Retrieve one question by id """
        return get_object_or_404(self.get_queryset(), pk=category.id)


class QuestionCategory(models.Model):
    """ Categories of questions """

    slug = models.SlugField(
        db_index=True,
        max_length=255,
        unique=True
    )
    category_name = models.CharField(
        db_index=True,
        max_length=64,
        unique=True,
        verbose_name='name of category, like Преподаватели'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name='parent category, to achieve nesting of categories'
    )

    objects = QuestionCategoryManager()

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'Categories'

    @classmethod
    def get_default_pk(cls):
        """ Default value of QuestionCategory model for .SET_DEFAULT behavior in models with FK """
        obj, created = cls.objects.get_or_create(category_name='Без категории')
        return obj.pk


class UserManager(models.Manager):
    """ Manager for User model """

    ADMIN_ID = 1  # PK of my user

    @classmethod
    def get_default_user(cls):
        """ Get first user 'megamot' """
        return User.objects.filter(pk=cls.ADMIN_ID)[0].pk


class QuestionManager(models.Manager):
    """ Manager for Question model """

    def get_queryset(self):
        """ Override get_queryset method from BaseManager """
        return super().get_queryset()

    def find_by_id(self, pk):
        """ Retrieve one question by id """
        return get_object_or_404(self.get_queryset(), pk=pk)

    def find_by_complexity(self, complexity_level):
        """ Find all questions by complexity: H, M, E """
        return self.get_queryset().filter(complexity=complexity_level)

    def find_by_category(self, category):
        """
        Find all questions by category
        Example: find_by_category('Общие знания')
        """
        return self.get_queryset().filter(category=category)


class Question(models.Model):
    """ Question for the quiz """

    COMPLEXITY_TYPES = (
        ('H', 'hard'),
        ('M', 'medium'),
        ('E', 'easy'),
    )

    slug = models.SlugField(
        db_index=True,
        max_length=255,
        unique=True
    )
    question_name = models.CharField(
        db_index=True,
        max_length=255,
        unique=True,
        verbose_name='question name, describing its essence'
    )
    question_text = models.CharField(
        max_length=255
    )
    question_answers = ArrayField(
        models.CharField(max_length=128),
        size=4,
        verbose_name='list of four answers for the question'
    )
    true_answer = models.CharField(
        max_length=128,
        verbose_name='true answer to a question, "question answers" contains it'
    )
    complexity = models.CharField(
        max_length=1,
        choices=COMPLEXITY_TYPES
    )
    question_author = models.ForeignKey(
        User,
        related_name='questions',
        db_index=True,
        on_delete=models.SET_DEFAULT,
        default=UserManager.get_default_user,
        blank=True,
        verbose_name='which user the question belongs to'
    )
    category = models.ForeignKey(
        QuestionCategory,
        related_name='questions',
        db_index=True,
        on_delete=models.SET_DEFAULT,
        default=QuestionCategory.get_default_pk,
        blank=True,
        verbose_name='which category the question belongs to'
    )
    hint = models.CharField(
        max_length=255,
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
