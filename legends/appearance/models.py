from django.db import models
from django.contrib.postgres.fields import ArrayField


class Question(models.Model):
    """ Question for the quiz """

    COMPLEXITY_TYPES = (
        ('H', 'hard'),
        ('M', 'medium'),
        ('E', 'easy'),
    )

    question_name = models.CharField(
        verbose_name='question name, describing its essence',
        max_length=200
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
    hint = models.CharField(
        verbose_name='a hint to a question to help answer it',
        max_length=200,
        null=True,
    )

    def __repr__(self):
        return self.question_text

    class Meta:
        verbose_name = 'question'
        verbose_name_plural = 'Questions'
        ordering = ['-complexity']
