from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
# class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3   # extra ... 余分スロット数

class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "question_text"]
    fieldsets = [
            (None, {"fields":["question_text"]}),
            ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
            #classes = ["collapse"] 境界を重ねて並べる
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)

