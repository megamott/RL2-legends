# Generated by Django 3.2.6 on 2021-08-19 17:56

import appearance.models
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, verbose_name='name of category, like Преподаватели')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='appearance.questioncategory', verbose_name='parent category, to achieve nesting of categories')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_name', models.CharField(max_length=200, verbose_name='question name, describing its essence')),
                ('question_text', models.CharField(max_length=200)),
                ('question_answers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=4, verbose_name='list of four answers for the question')),
                ('complexity', models.CharField(choices=[('H', 'hard'), ('M', 'medium'), ('E', 'easy')], max_length=1)),
                ('hint', models.CharField(blank=True, max_length=200, null=True, verbose_name='a hint to a question to help answer it')),
                ('category', models.ForeignKey(blank=True, default=appearance.models.QuestionCategory.get_default_pk, on_delete=django.db.models.deletion.SET_DEFAULT, to='appearance.questioncategory', verbose_name='which category the question belongs to')),
                ('question_author', models.ForeignKey(blank=True, default=appearance.models.UserManager.get_default_user, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='which user the question belongs to')),
            ],
            options={
                'verbose_name': 'question',
                'verbose_name_plural': 'Questions',
                'ordering': ['-complexity'],
            },
        ),
    ]
