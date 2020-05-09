from django.contrib import admin
import nested_admin
from .models import Poll, Question, Choice


class ChoiceInline(nested_admin.NestedStackedInline):
    model = Choice


class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    inlines = [ChoiceInline]


class PollAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        QuestionInline,
    ]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['start_at', ]
        return []


admin.site.register(Poll, PollAdmin)
