from django.contrib import admin

from .models import Category, Question, Answer, Result

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = ['name', 'is_correct']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['name', 'category']
    list_display = ['name', 'category', ]
    inlines = [AnswerInlineModel]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_correct', 'question']

admin.site.register(Result)
