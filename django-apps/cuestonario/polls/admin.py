from django.contrib import admin

from .models import Choice, Question, Users


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Score', {'fields': ['score'], 'classes': ['collapse']}),
        ('Answer', {'fields': ['answer']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'score')
    list_filter = ['score']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Users)
