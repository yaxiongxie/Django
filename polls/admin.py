from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
