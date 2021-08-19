from django.contrib import admin
from .models import (
    Question,
    Category
)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_name', 'question_text', 'question_answers', 'category', 'complexity', 'hint')
    list_display_links = ('id', 'question_name', 'category')
    search_fields = ('title', 'question_name', 'complexity', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'parent')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Category, CategoryAdmin)
