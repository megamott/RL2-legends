from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_name', 'question_text', 'question_answers', 'complexity', 'hint')
    list_display_links = ('id', 'question_name')
    search_fields = ('title', 'question_name', 'complexity')


admin.site.register(Question, QuestionAdmin)
