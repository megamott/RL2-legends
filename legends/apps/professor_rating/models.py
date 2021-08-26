from django.contrib.auth.models import User
from django.db import models


class Professor(models.Model):
    """ Professor at the RL2 department """

    professor_name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name='full name of the professor'
    )

    professor_description = models.TextField(
        verbose_name='short dossier of the professor'
    )

    professor_rating = models.FloatField(
        verbose_name='rating of professor'
    )

    professor_email = models.EmailField(
        max_length=64,
        verbose_name='personal professor\'s email '
    )

    # professor_photo = models.IntegerField()

    def __str__(self):
        return self.professor_name


class Review(models.Model):
    """ Feedback on professor behavior"""

    reviewed_professor = models.ForeignKey(
        Professor,
        db_index=True,
        on_delete=models.CASCADE,
        verbose_name='the professor to whom the review is written'
    )

    reviewer = models.ForeignKey(
        User,
        db_index=True,
        on_delete=models.CASCADE,
        verbose_name='review author'
    )

    review_text = models.TextField(
        verbose_name='reviews on professors'
    )

    def __str__(self):
        return f'Professor: {self.reviewed_professor}, Reviewer: {self.reviewer}'


# class Subject(models.Model):
#     """ Subject at the department RL2 """
#     pass



